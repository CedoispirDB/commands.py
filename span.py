import smtplib

server = smtplib.SMTP("smtp.gmail.com", 467)
server.ehlo()
server.starttls()
server.ehlo()

server.login("marcodato03@gmail.com", "recabuca123")

subject = "Test"
body = "Python.com"

msg = f"Subject: {subject}\n\n{body}"

server.sendmail(
    "marcodato03@gmail.com",
    "tamassia@gmail.com",
    msg
)

print("it worked")

server.quit
