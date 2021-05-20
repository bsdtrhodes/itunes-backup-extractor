This is my first python program, please be nice with any feedback.

I put this together when I needed to download the images from a broken iPhone
that, thankfully, had a very recent backup. And luckily for me, the backup
wasn't encrypted so I didn't need to deal with that - but if you do, check
out iOSbackup (https://pypi.org/project/iOSbackup/) it looks pretty cool.

To use this, install python (I used 3.7), on a virtual machine.
Copy the iTunes backup directory (it's a directory with a hashname) to the VM.
Edit this script to fix the path to the backup directory and Manifest.db file.
Run "chmod 755" on this file and run: ./itunes-img-extractor.py


Read the license, don't blame me for anything, change this all you want. Have
fun with this, I hope it's as useful for someone else as it was for me.

