import ssl
from smtplib import SMTP
from ssl import SSLContext
from typing import Text


class Login:
    _server: SMTP

    def __init__(self, email: str, password: str):
        """
        :param email: Your Email Address
        :param password: Yor Email Password
        """
        # Attributes
        self.email: Text = email
        self.__password: Text = password
        self.status: bool = bool()
        self.login: bool = bool()
        self.multi: bool = bool()
        self._sleep: int = int()
        self._repeat: int = 1
        self.count_rec: int = 1
        self.count_cc: int = int()
        self.count_bcc: int = int()
        self.count_msg: int = self._repeat * self.count_rec
        self.__port: int = 587
        self.GMAIL: Text = 'smtp.gmail.com'
        # self.YAHOO: Text = 'smtp.mail.yahoo.com' # Unsupported Now
        self.MICROSOFT: Text = 'smtp.office365.com'
        self.provider: Text = self.GMAIL

    # Login Method
    def _login(self) -> bool:
        context: SSLContext = ssl.create_default_context()

        self._server = SMTP(host=self.provider,
                            port=self.__port)
        self._server.ehlo()
        self._server.starttls(context=context)
        self._server.ehlo()

        try:
            self._server.login(user=self.email,
                               password=self.__password)
            self.login = True
            return True
        except Exception as e:
            if self.provider == self.GMAIL:
                problem = """
Error: Email And Password Not Accepted.

Note:
    Make sure you Allowed less secure apps,
    if you didn't, visit this link:
    ==> https://myaccount.google.com/lesssecureapps

    For More information visit this link:
    ==> https://support.google.com/mail/?p=BadCredentials
                    """
            else:
                problem = e
            print(problem)
            self.login = False
            return False
