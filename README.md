![image](images/bsmala.png)

# Installation:
```cmd
pip install altaie-mailer
```

[pypi Link]()

# Usage:
```py
from altai-mailer import Mailer

mail = Mailer(email='someone@gamil.com'
              password='your_password')

mail.send(receiver='someone2@gmail.com',
          subject='First Message',
          message='Hello This Message From Python')
```
