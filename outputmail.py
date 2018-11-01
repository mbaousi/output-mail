import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os

os.system('clear')
os.system('rm /home/output')
os.system('IBSngCC --no-usb')
cn = raw_input('Please Enter Customer Name : ') 
num = raw_input('\nPlease Enter Ticket Number : ') 



y = raw_input('\n1)New install\n2)Update Service\n3)change Hardware Lock To Software\n4)Change online User Count\n5)Change Expire Time\n6)Migrate IBSng Server\nPlease Enter a number :')
if y == '1':
    cause = "New install"
if y == '2':
    cause = "Update Service"
if y == '3':
    cause = "change Hardware Lock To Software"
if y == '4':
    cause = "Change online User Count"
if y == '5':
    cause = "Change Expire Time"
if y == '6':
    cause = "Migrate IBSng Server"
else:
    print 'Please Select 1 To 6 - Try Again'

x = raw_input('\n1)IT\n2)Sales \nMail Send TO : ')
if x == '1':
    toaddr = "m@gmail.com" # to address
elif x == '2':
    toaddr = "m@gmail.com" # another to address
else:
    print 'Please Select 1 OR 2 - Try Again'
fromaddr = "yourmail@gmail.com" # your gmail address
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'license ' + cn + ' ticket num ' + num
 
body = 'Hi\n\n Please add this output to license server\n Cause change :' + cause + '\nTicket number : ' + num + '\n\nRegards,\nSupport Team'
 
msg.attach(MIMEText(body, 'plain'))
 
filename = cn + "_output"
attachment = open("/home/output", "rb") # attach this file 
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "password") #your gmail password
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print 'Send Succsessfully!!!'
time.sleep(5)

