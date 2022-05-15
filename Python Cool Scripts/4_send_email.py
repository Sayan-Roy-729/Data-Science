import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = "ikhowpython14@gmail.com"
to_addr = ["rsayan553@gmail.com", "sayanroy729@outlook.com"]
msg = MIMEMultipart()
msg["From"] = from_addr
msg["To"] = " ,".join(to_addr)
msg["subject"] = "just to check"

body = "hello world"

msg.attach(MIMEText(body, "plain"))

# sender's email id and password
email = ""
password = ""

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(email, password)
text = msg.as_string()
mail.sendmail(from_addr, to_addr, text)
mail.quit()
