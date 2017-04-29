import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
me = "info3180projectkjjs@gmail.com"

def sendMail(you, you_name, subject, message):

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = me
	msg['To'] = you

	html = message


	# Record the MIME types of both parts - text/plain and text/html.
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part2)
	# Send the message via local SMTP server.
	mail = smtplib.SMTP('smtp.gmail.com', 587)

	mail.ehlo()

	mail.starttls()

	mail.login('info3180project2kjjs@gmail.com', 'bdmzbbvkddrhpjlc')
	mail.sendmail(me, you, msg.as_string())
	mail.quit()