#!/usr/bin/env python
#
# (C) BSD License - Tom Rhodes 2021
# Welcome to my first python program. It restores photos and thumbnails
# from an unencrypted backup created with iTunes. Just update the
# basedir (the backup directory) and path to the Manifest.db file.
# For encrypted backups, I think iOSbackup might be an option? I
# haven't tried it because it does not work with unencrypted backups.
#
# Extrated images are sorted similar to Windows explorer, under
# Media/DCIM/nnnApple. This tool will also pull the metadata,
# movie files, thumbnails, and other important information that may
# be useful to someone like a forensics examiner.

import os
import sqlite3
from pathlib import Path
from shutil import copyfile

#
# Location to the Manifest db file and the iPhone backup dir
# The backupdir is normally a directory with a hash as a name
#
manifestDB = "/home/trhodes/tirabkup/Manifest.db"
backupbasedir = "tirabkup/"

try:
	conn = sqlite3.connect(manifestDB)
except Error as e:
	print(e)

# Set up connection
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute("SELECT fileID, relativePath FROM Files WHERE domain = 'CameraRollDomain'")

rows = c.fetchall()
for row in rows:
	localfile = row[0]
	fileloc = row[1]

	# Skip empty entries that we get from Manifest.db
	if not localfile:
		continue

	# File names are hashes, the first two bytes represent the local directory
	# e.g.: 1a/1axxxxxxx so get that for later.
	dirloc = localfile[:2]

	# Get path location of file, create it, ignore if exists
	path = Path(fileloc)
	mkpath = path.parent.absolute()
	targetpath = os.path.join(os.path.join(os.environ.get("HOME"), mkpath))
	if not os.path.exists(targetpath):
		Path(targetpath).mkdir(parents=True, exist_ok=True)

	# Create previous target name, the real filename is from "relativePath" in
	# Manifest.db (I'm new to python, is there an easier way?).
	prevtarget = backupbasedir
	prevtarget += dirloc
	prevtarget += "/"
	prevtarget += localfile

	# Sometimes, it seems, thumbnails and temporary files will leave us without
	# a file to copy but still have a db reference, ignore those "missing" files
	# for now.
	if os.path.isfile(prevtarget):
		print(f"Copying {prevtarget} to {fileloc}.")
		copyfile(prevtarget, fileloc)

c.close()
