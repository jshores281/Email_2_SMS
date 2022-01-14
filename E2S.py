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
    "MESSAGE = %s" % BODY,'\n')


input()


# email to sms function
def notify_user(EMAIL_ADDR, EMAIL_PASS, RECV_ADDR, EMAIL_SRVR, EMAIL_PORT, SUBJECT, BODY):
	# make this reprogrammable based on email service provider (smtp server, port)
	with smtplib.SMTP(EMAIL_SRVR, EMAIL_PORT) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(EMAIL_ADDR, EMAIL_PASS)
		login_log = smtp.login(EMAIL_ADDR, EMAIL_PASS)
		print(login_log)

		# email message packer
		MSG = ("From: %s\r\n" % EMAIL_ADDR
             + "To: %s\r\n" % RECV_ADDR
             + "Subject: %s\r\n" % SUBJECT
             + "\r\n"
             + BODY)

		# email send function
		smtp.sendmail(EMAIL_ADDR, RECV_ADDR, MSG)


# function executioner
notify_user(EMAIL_ADDR, EMAIL_PASS, RECV_ADDR, EMAIL_SRVR, EMAIL_PORT, SUBJECT, BODY)
print("message sent")




