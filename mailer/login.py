import ssl as _ssl
from smtplib import SMTP as _SMTP


class Login:
    def __init__(self, email: str, password: str):
        """
        :param email: Your Email Address
        :param password: Yor Email Password
        """
        # Variables
        self.email = email
        self.__password = password
        self._server = None
        self.status = bool()
        self.login = bool()
        self.multi = bool()
        self._sleep = int()
        self._repeat = 1
        self.count_rec = 1
        self.count_cc = int()
        self.count_bcc = int()
        self.count_msg = self._repeat * self.count_rec
        self.__port = 587
        self.GMAIL = 'smtp.gmail.com'
        # self.YAHOO = 'smtp.mail.yahoo.com' # Unsupported Now
        self.MICROSOFT = 'smtp.office365.com'
        self.provider = self.GMAIL

    # Login Method
    def _login(self) -> bool:
        context = _ssl.create_default_context()

        self._server = _SMTP(host=self.provider,
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
