from typing import Text, Union


def file_reader(filename: str) -> Union[bytes, bool]:
    try:
        with open(filename, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return False


# Example Function
def example() -> Text:
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
          cc='someone1@example.com',
          bcc='someone2@example.com',
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
    return ex
