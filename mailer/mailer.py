from typing import Text

from mailer.send import Send


class Mailer(Send):
    def __init__(self, email: str, password: str):
        """
        :param email: Your Email Address
        :param password: Yor Email Password
        """
        # Attributes
        super().__init__(email=email, password=password)
        # Apply Settings
        self.settings()

    # About Method
    @staticmethod
    def about() -> Text:
        info = """
About Module:
    This Module help you to send fast Email.
    And you can attach [image, audio, and other files] easily.

About Developer:
    Name: Ahmed Al-Taie
    Github: https://github.com/Al-Taie
    Pypi: https://pypi.org/user/Altaie
    Instagram: https://www.instagram.com/9_Tay

    Finally Thanks For Use My Module.
    You Can Join Our Discord For Any Question:
    Discord: https://discord.gg/gWdCNv7
            """
        print(info)
        return info

    # Settings Method
    def settings(self,
                 repeat: int = 1,
                 sleep: int = None,
                 provider: Text = None,
                 multi=False) -> None:
        """
        :param multi:
        :type multi:
        :param repeat: Repeat Number
        :param sleep: Set Sleep Time (In Seconds)
        :param provider: See example Function
        :return: None
        """
        self._repeat = repeat
        self.multi = multi

        if sleep:
            self._sleep = sleep

        if provider:
            self.provider = provider
