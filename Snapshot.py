from picamera import PiCamera
from gpiozero import Button
import datetime
from ftplib import FTP
import sys

########### MODIFY ########################

USER = 'ftp-user'
PASS = '123'

########### MODIFY IF YOU WANT ############

SERVER = '192.168.1.4'
PORT = 21
BINARY_STORE = True # if False then line store (not valid for binary files (videos, music, photos...))

###########################################

Start_button = Button(17)
Stop_button = Button(27)
Camera = PiCamera()


def print_line(result):
    print(result)

def connect_ftp():
    #Connect to the server
    ftp = FTP()
    ftp.connect(SERVER, PORT)
    ftp.login(USER, PASS)
    return ftp

def upload_file(ftp_connetion, upload_file_path):

    #Open the file
    try:
        upload_file = open(upload_file_path, 'rb')
        
        #get the name
        path_split = upload_file_path.split('/')
        final_file_name = path_split[len(path_split)-1]
    
        #transfer the file
        print('Uploading ' + final_file_name + '...')
        
        if BINARY_STORE:
            ftp_connetion.storbinary('STOR '+ final_file_name, upload_file)
        else:
            #ftp_connetion.storlines('STOR ' + final_file_name, upload_file, print_line)
            ftp_connetion.storlines('STOR '+ final_file_name, upload_file)
            
        print('Upload finished.')
        
    except IOError:
        print ("No such file or directory... passing to next file")


#Take all the files and upload all
ftp_conn = connect_ftp()

Camera.start_preview()

while True:
    if Start_button.is_pressed:
        utc_datetime = datetime.datetime.utcnow()
        filename = utc_datetime.strftime('/home/pi/Desktop/%d_%m_%Y_%H-%M-%S.jpg') #this is our filename string
        Camera.capture(filename)
        upload_file(ftp_conn, filename)

    if Stop_button.is_pressed:
        Camera.stop_preview()
        break
        
        
        


     
