![image](bsmala.png)

# Installation:
``
pip install altaie-mailer
``

[pypi Link](https://guides.github.com/features/mastering-markdown/)

# Usage:
````
from altai-mailer import Mailer

mail = Mailer(email='someone@gamil.com'
              password='your_password')

mail.send(receiver='someone2@gmail.com',
          subject='First Message',
          message='Hello This Message From Python')
````