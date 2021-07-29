# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:20:06 2018

@author: acvats
"""

import smtplib
import config


def send_email(msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        #server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS2, config.PASSWORD)
        #message = "Subject: {}\n\n{}", format(subject,msg)
        print("1")
        server.sendmail(config.EMAIL_ADDRESS2,"achalvats17@gmail.com" , msg)
        print("2")
        server.quit()
        print("Email sent!!!")
    except:
        print("Email sending failed!!!")


msg1 =open("data7.txt","r")
msg=msg1.read()
#msg="hello vamsi, how are you. from achal"
send_email(msg)