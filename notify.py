#https://realpython.com/python-send-email/
#https://developers.upwork.com/?lang=python#introduction




# import smtplib, ssl
#
# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "WebCrawler1996@gmail.com"  # Enter your address
# receiver_email = "12145491447@txt.att.net"  # Enter receiver address
# password = "jhUjhUjhU$"
# #input("Type your password and press enter: ")
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)


# 12145491447@txt.att.net

#2142286829@txt.att.net






import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "WebCrawler1996@gmail.com"
receiver_email = "12145491447@txt.att.net"
password = "jhUjhUjhU$"
#input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
