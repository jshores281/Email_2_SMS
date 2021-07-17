import smtplib




EMAIL_SENDER = input("enter your email: ")
EMAIL_SENDER_PASSWORD = input("enter your email password: ")
RECV_PHONE = input("enter phone number sms address: ")
EMAIL_ADDR = EMAIL_SENDER
EMAIL_PASS = EMAIL_SENDER_PASSWORD
RECV_ADDR = RECV_PHONE



# email to sms function
def notify_user():
	with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(EMAIL_ADDR, EMAIL_PASS)
		login_log = smtp.login(EMAIL_ADDR, EMAIL_PASS)

		# make this reprogrammable based on product and values
		subject = "PRODUCT ALERT"
		body = "PRODUCT STOCK STATUS: "

		# email message packer
		msg = ("From: %s\r\n" % EMAIL_ADDR
             + "To: %s\r\n" % RECV_ADDR
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)
		
		smtp.sendmail(EMAIL_ADDR, RECV_ADDR, msg)



notify_user()