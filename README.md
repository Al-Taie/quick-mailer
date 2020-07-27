![image](images/bsmala.png)

# Description
This Module help you to send **fast Email. 🌸**

And you can attach **image, audio, and other files easily.**

The Module support **Gmail** right now, but in the nearly future will support other mail services.

# Installation:
```cmd
pip install quick-mailer
```

**[-->> pypi Link](https://pypi.org/project/quick-mailer)**

# Usage:
**Send Message**
```py
from mailer import Mailer

mail = Mailer(email='someone@gmail.com',
              password='your_password')

mail.send(receiver='someone2@gmail.com',
          subject='First Message',
          message='Hello This Message From Python')
```

**Check Send Status**
```py
# Using (status) Variable
print(mail.status)

# Example:
if mail.status:
  pass
else:
  pass
```

**Parameters**
```py
receiver: Email Address [Recuired]
subject: Message Title  [Optional]
message: Your Message   [Optional]
image: Image File Name  [Optional]
audio: Audio File Name  [Optional]
file: File Name         [Optional]
```

**Send Multi Files**
```py
mail.send(receiver='someone@gmail.com',
          subject='Test Module',
          message='Hello This Message From Python!',
          image='img.jpg',
          audio='sound.mp3',
          file='file.zip')
```

**About**
```py
# You Can Use (mail.about) Function for more info.
mail.about()
```

**Follow Me on Instagram: [@9_Tay](https://www.instagram.com/9_tay). 🌸**

# Thank You :) 🌸
