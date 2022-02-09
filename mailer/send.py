from email.mime.application import MIMEApplication as MIMEApp
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
from typing import Text, List, Dict, Union

from mailer.exceptions import ImageNotFoundError, AudioNotFoundError, OutboundSpamException
from mailer.login import Login
from mailer.utils import file_reader


class Send(Login):
    def __init__(self, email: str, password: str):
        """
        :param email: Your Email Address
        :param password: Yor Email Password
        """
        # Variables
        super().__init__(email=email, password=password)
        self._msg = MIMEMultipart()

    def __prepare_message(self,
                          receiver,
                          cc=None,
                          bcc=None,
                          no_reply: str = None,
                          subject: str = None,
                          message: str = None) -> None:
        self._msg['Subject'] = subject
        self._msg['From'] = self.email

        if message is not None:
            text = MIMEText(message, 'html')
            self._msg.attach(text)

        if list == type(receiver):
            self.count_rec = len(receiver)
            receiver: Text = ','.join(i for i in receiver)

        if list == type(cc):
            self.count_cc = len(cc)
            cc: Text = ','.join(i for i in cc)

        if list == type(bcc):
            self.count_bcc = len(bcc)
            bcc: Text = ','.join(i for i in bcc)

        self._msg['To'] = receiver
        self._msg['CC'] = cc
        self._msg['BCC'] = bcc
        self._msg['Reply-To'] = no_reply

    def __prepare_attachments(self,
                              image: str = None,
                              audio: str = None,
                              file: str = None) -> None:
        if image is not None:
            image_data: Union[bytes, bool] = file_reader(image)
            # assert image_data, ImageNotFoundError()

            if not image_data:
                raise ImageNotFoundError()

            image = MIMEImage(_imagedata=image_data, name=image)
            self._msg.attach(image)

        if audio is not None:
            audio_data: Union[bytes, bool] = file_reader(audio)

            if not audio_data:
                raise AudioNotFoundError()

            audio = MIMEAudio(_audiodata=audio_data, name=audio, _subtype='')
            self._msg.attach(audio)

        if file is not None:
            file_data: Union[bytes, bool] = file_reader(file)

            if not file_data:
                raise FileNotFoundError("File not exists in a path!")

            file = MIMEApp(_data=file_data, name=file)
            self._msg.attach(file)

    # Send Method
    def send(self,
             receiver,
             cc=None,
             bcc=None,
             no_reply: str = None,
             subject: str = None,
             message: str = None,
             image: str = None,
             audio: str = None,
             file: str = None) -> None:
        """
        :param no_reply: Set no-reply email
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

        send_info: List = []
        multi_info: Dict = {}

        self.__prepare_message(receiver=receiver, cc=cc,
                               bcc=bcc, subject=subject,
                               message=message, no_reply=no_reply)

        self.__prepare_attachments(image=image,
                                   audio=audio,
                                   file=file)
        if self._login():
            if self.multi:
                for _ in range(self._repeat):
                    try:
                        self._server.sendmail(from_addr=self.email,
                                              to_addrs=receiver,
                                              msg=self._msg.as_string())
                    except Exception:
                        if self._repeat == 1 & self.count_rec == 1:
                            self.status = False
                        else:
                            send_info.append(False)

                    else:
                        if self._repeat == 1 & self.count_rec == 1:
                            self.status = True
                        else:
                            send_info.append(True)
                            self.status = send_info

                    finally:
                        sleep(self._sleep)
            else:
                for rec in receiver.split(','):
                    send_info = []
                    for _ in range(self._repeat):
                        try:
                            self._server.sendmail(from_addr=self.email,
                                                  to_addrs=rec,
                                                  msg=self._msg.as_string())
                        except Exception as e:
                            if self._repeat == 1 & self.count_rec == 1:
                                self.status = False
                            else:
                                send_info.append(False)

                            assert OutboundSpamException.__name__ not in str(e), OutboundSpamException()

                        else:
                            if self._repeat == 1 & self.count_rec == 1:
                                self.status = True
                            else:
                                send_info.append(True)
                                self.status = send_info
                                multi_info[rec] = send_info

                        finally:
                            sleep(self._sleep)

                    if self.count_rec != 1:
                        self.status = multi_info

        self._server.close()
