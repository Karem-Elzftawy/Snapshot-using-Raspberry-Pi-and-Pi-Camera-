HOST='192.168.1.2:2121'
USER='Kareem'
PASS='123'
TARGETFOLDER='/home/pi/Desktop/Snapshoot/Data'
SOURCEFOLDER='ftp://192.168.1.2:2121/Data/'
lftp -f "
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
mirror --reverse --delete --verbose $SOURCEFOLDER $TARGETFOLDER
"