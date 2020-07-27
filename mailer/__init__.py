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


import ssl
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

__all__ = ['Mailer']
VERSION = '0.0.3'


class Mailer:
    def __init__(self, email: str, password: str):
        """
        :param email: Your Email Address
        :param password: Yor Email Password
        """
        self.email = email
        self.password = password

    @staticmethod
    def file_reader(filename):
        with open(filename, 'rb') as f:
            return f.read()

    def send(self,
             receiver: str,
             subject: str = None,
             message: str = None,
             image: str = None,
             audio: str = None,
             file: str = None):
        """
        :param receiver: Email Address
        :param subject: Message Title
        :param message: Your Message
        :param image: Image File Name
        :param audio: Audio File Name
        :param file: File Name
        :return: Boolean
        """

        msg = MIMEMultipart()

        if message is not None:
            text = MIMEText(message)
            msg.attach(text)

        if image is not None:
            image_data = self.file_reader(image)
            image = MIMEImage(_imagedata=image_data, name=image)
            msg.attach(image)

        if audio is not None:
            audio_data = self.file_reader(audio)
            audio = MIMEAudio(_audiodata=audio_data, name=audio, _subtype='')
            msg.attach(audio)

        if file is not None:
            file_data = self.file_reader(file)
            file = MIMEApplication(_data=file_data, name=file)
            msg.attach(file)

        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = receiver

        context = ssl.create_default_context()

        with SMTP_SSL(host='smtp.gmail.com',
                      port=465, context=context) as server:
            try:
                server.login(user=self.email,
                             password=self.password)
            except Exception as e:
                del e
                print('Email And Password Not Accepted, Visit This Link:\n'
                      'https://support.google.com/mail/?p=BadCredentials')
                return False
            else:
                try:
                    server.sendmail(from_addr=self.email,
                                    to_addrs=receiver,
                                    msg=msg.as_string())
                except Exception as e:
                    del e
                    return False
                else:
                    return True

