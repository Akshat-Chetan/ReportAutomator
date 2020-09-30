import shutil

import os
mypath = 'D:/Mailer'
dest = 'D:/Moved'
fpaths = [file for file in os.listdir(mypath)]
for f in fpaths:
    print(f)
    shutil.move(mypath + '/' + f,dest)
