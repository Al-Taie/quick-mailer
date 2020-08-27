"""
MIT License

Copyright (c) [2020 Ahmed Al-Taie]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import ssl as _ssl
from email.mime.application import MIMEApplication as _MIMEApp
from email.mime.audio import MIMEAudio as _MIMEAudio
from email.mime.image import MIMEImage as _MIMEImage
from email.mime.multipart import MIMEMultipart as _MIMEMultipart
from email.mime.text import MIMEText as _MIMEText
from smtplib import SMTP as _SMTP
from time import sleep as _sleep

__all__ = ['Mailer', '__VERSION__', 'example']
__VERSION__ = '0.1.0'


# Main Class
class Mailer:
    def __init__(self, email: str, password: str):
        """
        :param email: Your Email Address
        :param password: Yor Email Password
        """
        # Variables
        self.email = email
        self.__password = password
        self.__server = None
        self.status = bool()
        self.login = bool()
        self.multi = bool()
        self.__sleep = int()
        self.__repeat = 1
        self.count_rec = 1
        self.count_cc = int()
        self.count_bcc = int()
        self.count_msg = self.__repeat*self.count_rec
        self.__port = 587
        self.GMAIL = 'smtp.gmail.com'
        # self.YAHOO = 'smtp.mail.yahoo.com' # Unsupported Now
        self.MICROSOFT = 'smtp.office365.com'
        self.provider = self.GMAIL

        # Apply Settings
        self.settings()

    # About Method
    @staticmethod
    def about():
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
        return

    # File Reader Method
    @staticmethod
    def _file_reader(filename: str):
        with open(filename, 'rb') as f:
            return f.read()

    # Settings Method
    def settings(self,
                 repeat: int = 1,
                 sleep=None,
                 provider: str = None,
                 multi=False):
        """
        :param multi:
        :type multi:
        :param repeat: Repeat Number
        :param sleep: Set Sleep Time (In Seconds)
        :param provider: See example Function
        :return: None
        """
        self.__repeat = repeat
        self.multi = multi

        if sleep:
            self.__sleep = sleep

        if provider:
            self.provider = provider

    # Login Method
    def __login(self):
        context = _ssl.create_default_context()

        self.__server = _SMTP(host=self.provider,
                              port=self.__port)
        self.__server.ehlo()
        self.__server.starttls(context=context)
        self.__server.ehlo()

        try:
            self.__server.login(user=self.email,
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

    # Send Method
    def send(self,
             receiver,
             cc=None,
             bcc=None,
             subject: str = None,
             message: str = None,
             image: str = None,
             audio: str = None,
             file: str = None):
        """
        :param cc: Email Address as String or List. (Carbon Copy)
        :param bcc: Email Address as String or List. (Blind Carbon Copy)
        :param receiver: Email Address as String or List
        :param subject: Message Title
        :param message: Your Message
        :param image: Image File Name
        :param audio: Audio File Name
        :param file: File Name
        :return: Boolean
        """

        msg = _MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.email

        try:
            if message is not None:
                text = _MIMEText(message)
                msg.attach(text)

            if image is not None:
                image_data = self._file_reader(image)
                image = _MIMEImage(_imagedata=image_data, name=image)
                msg.attach(image)

            if audio is not None:
                audio_data = self._file_reader(audio)
                audio = _MIMEAudio(_audiodata=audio_data, name=audio, _subtype='')
                msg.attach(audio)

            if file is not None:
                file_data = self._file_reader(file)
                file = _MIMEApp(_data=file_data, name=file)
                msg.attach(file)
        except Exception:
            print('Error: File Not Found!')
            self.status = False
            return False

        send_info = []
        multi_info = {}

        if 'list' in str(type(receiver)):
            self.count_rec = len(receiver)
            receiver = ','.join(i for i in receiver)

        if 'list' in str(type(cc)):
            self.count_cc = len(cc)
            cc = ','.join(i for i in cc)

        if 'list' in str(type(bcc)):
            self.count_bcc = len(bcc)
            bcc = ','.join(i for i in bcc)

        if self.__login():
            msg['To'] = receiver
            msg['CC'] = cc
            msg['BCC'] = bcc

            if self.multi:
                for _ in range(self.__repeat):
                    try:
                        self.__server.sendmail(from_addr=self.email,
                                               to_addrs=receiver,
                                               msg=msg.as_string())
                    except Exception:
                        if self.__repeat == 1 & self.count_rec == 1:
                            self.status = False
                        else:
                            send_info.append(False)

                    else:
                        if self.__repeat == 1 & self.count_rec == 1:
                            self.status = True
                        else:
                            send_info.append(True)
                            self.status = send_info

                    finally:
                        _sleep(self.__sleep)
            else:
                for rec in receiver.split(','):
                    send_info = []
                    for _ in range(self.__repeat):
                        try:
                            self.__server.sendmail(from_addr=self.email,
                                                   to_addrs=rec,
                                                   msg=msg.as_string())
                        except Exception as e:
                            if self.__repeat == 1 & self.count_rec == 1:
                                self.status = False
                            else:
                                send_info.append(False)

                            if 'OutboundSpamException' in str(e):
                                print('Error: Please Login To Your Account And Verify it.')
                                break

                        else:
                            if self.__repeat == 1 & self.count_rec == 1:
                                self.status = True
                            else:
                                send_info.append(True)
                                self.status = send_info
                                multi_info[rec] = send_info

                        finally:
                            _sleep(self.__sleep)

                    if self.count_rec != 1:
                        self.status = multi_info

        self.__server.close()


# Example Function
def example():
    ex = """
####################
# [Copy This Code] #
####################

mail = Mailer(email='someone@gmail.com',
              password='***')

# IF You Want Repeat Sending, Change repeat Value
# And IF You Want Change Mail Service
# Chose One: mail.[GMAIL, MICROSOFT]
mail.settings(repeat=1,
              sleep=0,
              provider=mail.GMAIL,
              multi=False)

# Send Message
mail.send(receiver='someone@example.com',  # Email From Any service Provider
          cc='someone1@example.com'
          bcc='someone2@example.com'
          subject='TEST',
          message='HI, This Message From Python :)',
          image=None,   # Image File Path
          audio=None,   # Audio File Path
          file=None)    # Any File Path

# Login Status Info
print('login:', mail.login)

# Sending Status Info
print('status:', mail.status)

# CC Receivers Count
print('CC count:', mail.count_cc)

# BCC Receivers Count
print('BCC count:', mail.count_bcc)

# Receivers Count
print('Receivers count:', mail.count_rec)

# Messages Count IF You Allowed Repeat
print('Messages count:', mail.count_msg)

# For More Information
mail.about()
        """
    print(ex)
