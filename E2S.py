#! Python 3.9.4/E2S.py
# email to sms #
# secured with tls

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

	# make this reprogrammable based on email service provider (smtp server, port)
	with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(EMAIL_ADDR, EMAIL_PASS)
		login_log = smtp.login(EMAIL_ADDR, EMAIL_PASS)

		# make this reprogrammable based on product and values
		subject = SUBJECT
		body = BODY

		# email message packer
		msg = ("From: %s\r\n" % EMAIL_ADDR
             + "To: %s\r\n" % RECV_ADDR
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)

		# email send function
		smtp.sendmail(EMAIL_ADDR, RECV_ADDR, msg)


# function executioner
notify_user(EMAIL_ADDR, EMAIL_PASS, RECV_ADDR, SUBJECT, BODY)



