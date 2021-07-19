#! Python 3.9.4/E2S.py
# email to sms #
# secured with tls
###############################################################################
###############################################################################
# FEATURES TO ADD 
# ~ make (smtp server, port) reprogrammable based on user specified email 
# 		service provider
# ~ make msg(FIELDS) reprogrammable based on user input
# ~ make number of emails to send reprogrammable based on /user input
#		/trigger event
###############################################################################
###############################################################################
import smtplib
EMAIL_SENDER = input("enter your email: ")
EMAIL_SENDER_PASSWORD = input("enter your email password: ")
RECV_PHONE = input("enter phone number sms address: ")
SUBJECT = input("enter subject of message: ") 
BODY = input("enter message: ")

EMAIL_ADDR = EMAIL_SENDER
EMAIL_PASS = EMAIL_SENDER_PASSWORD
RECV_ADDR = RECV_PHONE
SUBJECT = SUBJECT
BODY = BODY

# email to sms function
def notify_user(EMAIL_ADDR, EMAIL_PASS, RECV_ADDR, SUBJECT, BODY):

	with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(EMAIL_ADDR, EMAIL_PASS)
		login_log = smtp.login(EMAIL_ADDR, EMAIL_PASS)

		subject = SUBJECT
		body = BODY

		msg = ("From: %s\r\n" % EMAIL_ADDR
             + "To: %s\r\n" % RECV_ADDR
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)
		
		smtp.sendmail(EMAIL_ADDR, RECV_ADDR, msg)

# data stream + trigger condition
def test_func():
	a = 0	
	while a < 100:
		print(a + 1)
		if a == 50:
			input("EMAIL TRIGGER")
			notify_user(EMAIL_ADDR, EMAIL_PASS, RECV_ADDR, SUBJECT, BODY)
		a += 1

test_func()