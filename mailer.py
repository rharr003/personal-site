from smtplib import SMTP


class Mailer:

    def __init__(self, receiver):
        self.email = "pythontest1226@gmail.com"
        self.password = "Dissidia1!"
        self.receiver = receiver


    def sendmail(self, message):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.receiver,
                msg=f"Subject:New Message on Your Personal Website!\n\n{message}"
            )