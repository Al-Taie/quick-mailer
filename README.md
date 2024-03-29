![image](https://raw.githubusercontent.com/Al-Taie/quick-mailer/master/images/bsmala.png)

<a href="#"><img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=E4415F" alt="Star Badge"/></a>
![GitHub last commit](https://img.shields.io/github/last-commit/Al-Taie/quick-mailer)
![Lines of code](https://img.shields.io/tokei/lines/github/Al-Taie/quick-mailer?color=red&style=flat)
[![Downloads](https://pepy.tech/badge/quick-mailer)](https://pepy.tech/project/quick-mailer)
[![Downloads](https://pepy.tech/badge/quick-mailer/month)](https://pepy.tech/project/quick-mailer/month)
[![Downloads](https://pepy.tech/badge/quick-mailer/week)](https://pepy.tech/project/quick-mailer/week)
<a href="https://www.instagram.com/9_Tay"><img src="https://img.shields.io/badge/instagram-%23E4415F?style=flat&logo=instagram&logoColor=white"/></a>
[![Rate this package](https://badges.openbase.com/python/rating/quick-mailer.svg?token=dOXQlHZtUTrsmrkIt5r6f6j37pA19DqmuXrXasI5+e8=)](https://openbase.com/python/quick-mailer?utm_source=embedded&amp;utm_medium=badge&amp;utm_campaign=rate-badge)
[![Verified on Openbase](https://badges.openbase.com/python/verified/quick-mailer.svg?token=dOXQlHZtUTrsmrkIt5r6f6j37pA19DqmuXrXasI5+e8=)](https://openbase.com/python/quick-mailer?utm_source=embedded&amp;utm_medium=badge&amp;utm_campaign=rate-badge)

# Description

This Module help you to send **fast Email. 🌸**

And you can attach **image, audio, and other files easily.**

The Module support **Gmail And Microsoft** right now, but in the nearly future will support other mail services.

# Auth

see this: [How to login after disable less secure apps?](GoogleAuth.md)

# Installation:

```cmd
pip install quick-mailer
```

**[-->> pypi Link](https://pypi.org/project/quick-mailer)**

[//]: # (**[-->> GitHub Link]&#40;https://github.com/Al-Taie/quick-mailer&#41;**)

# Usage:

**Send Message**

```py
from mailer import Mailer

mail = Mailer(email='someone@gmail.com',
              password='your_password')

mail.send(receiver='someone@example.com',  # Email From Any service Provider
          no_reply='noreplay@example.com', # Redirect receiver to another email when try to reply.
          subject='TEST',
          message='HI, This Message From Python :)')
```

**Parameters**
```py
receiver: Email Address as String or List.                [Required]
cc: Email Address as String or List.  (Carbon Copy)       [Optional]
bcc: Email Address as String or List. (Blind Carbon Copy) [Optional]
sender_name: Set Sender name.                             [Optional]
receiver_name: Set receiver name.                         [Optional]
no_reply: Set Another Email To Reply                      [Optional]
subject: Message Title.                                   [Optional]
message: Your Message.                                    [Optional]
image: Image File Name.               (Image Path)        [Optional]
audio: Audio File Name.               (Audio Path)        [Optional]
file: File Name.                      (Any File Path)     [Optional]
```

**Check Send Status**
```py
# Using (status) Attribute 
print(mail.status)

# Example For One Receiver:
if mail.status:
  pass
else:
  pass
  
 # Note:
 # IF You Put List Emails Receivers
 # Variable Will Return Dictionary Results.
 
 # IF You Allowed Repeat
 # The Attribute Will provide Results List.
```

**Send Multi Files**
```py
mail.send(receiver='someone@example.com',  # Email From Any service Provider
          subject='TEST',
          message='HI, This Message From Python :)',
          image='img.jpg',      # Image File Path
          audio='sound.mp3',    # Audio File Path
          file='file.zip')      # Any File Path
```

**Settings Method**
```py
mail.settings(repeat=1,             # To Repeat Sending
              sleep=0,              # To Sleep After Send Each Message
              provider=mail.GMAIL,  # Set Maill Service
              multi=False)          # Default False, If You Set True
                                    # Message Will Sent 4 Each Email Alone
                                    # Else Will Sent To All Together
```

**Send Multi Emails**
```py
# One By One:
mail.settings(multi=False)

# In Same Message:
mail.settings(multi=True)

mail.send(receiver=['someone@example.com', 'someone1@example.com'],
          subject='TEST',
          message='HI, This Message From Python :)')
```

**Counter Variables**
```py
# CC Receivers Count
print('CC count:', mail.count_cc)

# BCC Receivers Count
print('BCC count:', mail.count_bcc)

# Receivers Count
print('Receivers count:', mail.count_rec)

# Messages Count
print('Messages count:', mail.count_msg)
```

**Example Function**
```py
from mailer import example

example()
```

**About Method**

```py
# You Can Use (mail.about) Method for more info.
mail.about()
```

#### Changelogs

> > 2022.2.22 update:
> - Add (sender name & receiver name) feature.

<br>

> > 2022.2.10 update:
> - Fix issue #3 TypeError on python < 3.10

<br>

> > 2022.2.2 update:
> - Support Html Message
> - Fix issue #1 TypeError on python < 3.10

**Follow Me on Instagram: [@9_Tay](https://www.instagram.com/9_tay). 🌸**

# Thank You :) 🌸
