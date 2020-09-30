import yagmail
import os
# sender email and password here
yag = yagmail.SMTP('youremail@gmail.com','yourpassword')
#Enter the path here
my_path = "D:/Mailer"

fpaths = [file for file in os.listdir(my_path)]
content = "<h1>Sir,</h1> Please find files attached for todays Scada Report <br> <h2>Regards,</h2><br> <h2>Manish Khare</h2>"

for file in fpaths:
    # enter list of reciever here
    yag.send('receiver1@gmail.com', subject='Todays Scada Report', contents=content, attachments=my_path + '/' + file)
    yag.send('reciever2@gmail.com',subject='Todays Scada Report',contents=content ,attachments= my_path + '/' + file)
