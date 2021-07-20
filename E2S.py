#! Python 3.9.4/E2S.py
# email to sms #
# secured with tls

import smtplib



EMAIL_SENDER = input("EMAIL: ")
EMAIL_PASSWORD = input("PASSWORD: ")
EMAIL_SRVR = input("SMTP SERVER: ")
EMAIL_PORT = input("SMTP SERVER PORT: ")
RECV_PHONE = input("CELL PHONE NUMBER: ")
SMS_GATE = input("SMS-GATEWAY: ")
SUBJECT = input("title of sms: ")
BODY = input("type message: ")

EMAIL_ADDR = EMAIL_SENDER
EMAIL_PASS = EMAIL_PASSWORD
RECV_ADDR = RECV_PHONE + SMS_GATE
SUBJECT = SUBJECT
BODY = BODY

print("\n", "PRESS ENTER IF CORRECT OR CTRL+C", "\n"*2,
	"EMAIL = %s" % EMAIL_ADDR,"\n",
	"PASSWORD = %s" % EMAIL_PASS,"\n",
	"SERVER = %s" % EMAIL_SRVR,"\n",
	"PORT = %s" % EMAIL_PORT,"\n",
	"PHONE & SMS-GATEWAY = %s" % RECV_ADDR,"\n"*2,
      	"TITLE = %s" % SUBJECT,'\n',
      	"MESSAGE = %s" % BODY,'\n\)


input()


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



