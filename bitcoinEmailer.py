#request a website to pull API data
#import time to set durations
#email.mime & smtplib to send emails 
#import getpass to mask emails when entered
import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

#create a function that sends an email notification

def send_email():
  # create message object instance
  msg = MIMEMultipart()

  #set message parameters
  password = yourPassword
  msg['From'] = yourEmail
  msg['To'] = sendEmailTo
  msg['Subject'] = "Bitcoin Price Low, BUY!"

  #email body
  message = "Hey" + " " + yourName + ",""\r\nBitcoin price is now" + " "+ "$" + str(price) + ". Better buy quick! \r\nRegards,\n" + "Team a3j"
  
  #adds in the message from the above variable
  msg.attach(MIMEText(message, 'plain'))
  
  #create the gmail server
  server = smtplib.SMTP('smtp.gmail.com: 587')

  #call our server
  server.starttls()

  #Login Creds for sending the email
  server.login(msg['From'], password)

  #sends the message
  server.sendmail(msg['From'], msg['To'], message)
  #quit server
  server.quit()

  #prints to your console
  print("our email has been sent to %s:" % (msg['To']))
  print("Price of bitcoin was at " + "$" + str(price))

#user inputs
yourName = input('Enter your name: ')
yourEmail = input('Enter email address (Gmail ONLY): ')
yourPassword = getpass.getpass()
sendEmailTo = input('Enter address to send notifiction to: ')
alertAmount = input('Alert if Bitcoin drops below: ')

'''
This loop will continuousy call our JSON and retrieve information for our Bitcoin price as long as it remains true. Once the price hits the alertAmount the email function is called and an email is sent to designated email.
'''
while True:
  r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
  #is our page a working site? Show: 200 if valid
  r.status_code
  if r.status_code != 200:
    print('coin desk website down')
    break
  #define variable "price" rounded to two decimals
  price = round(float(r.json()["bpi"]["USD"]["rate_float"]), 2)
  #send email if price is below our alert
  if price < float(alertAmount):
    send_email()
    break
  else:
    print('Will check again in 30 seconds. Ctrl + C to quit.')
    time.sleep(30)

'''
resources used:

https://stackoverflow.com/a/8940627

https://mkaz.blog/code/python-string-format-cookbook/

https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

https://travis.media/create-bitcoin-price-alert-app-in-python-tutorial
'''
