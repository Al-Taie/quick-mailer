## Google Security

We will be sending e-mail with [Gmail](https://en.wikipedia.org/wiki/Gmail). So the first thing we need to do is setup
Google security.

On May 30th, 2022 Gmail removed the [setting](https://support.google.com/accounts/answer/6010255?hl=en) to allow "less
secure" applications to access an account with just username and password.

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843af0d21c47c6725e7a_f53bbe91-e9b9-4aa6-b1ae-d65b1f2c55d5.png" width=540px height=640px alt="Less secure apps & your Google Account">

What this means is that you have to enable some other means of account security.

One way to do it is to use [API Authentication](https://www.abstractapi.com/api-glossary/api-authentication)
with [OAuth2](https://oauth.net/2/) which
Google [documents here](https://developers.google.com/gmail/api/quickstart/python).

Another way, which I will describe here, is to turn on two-factor authentication.

#### Two-factor Authentication

In order to allow our Python client script to access Gmail accounts we will enable two-factor authentication (2FA) which
Google calls " [2-step verification](https://support.google.com/accounts/answer/185839)".

With 2FA you add an extra layer of security to your account in case your password is stolen. After you set it up, you’ll
sign in to your account in two steps using:

* something you know, like your **password** and
* something you have, like your **phone**.

To enable 2FA:

1. Open your [Google Account](https://myaccount.google.com/).
2. In the navigation panel, select **Security**.
3. Under “Signing in to Google,” select **2-Step Verification**

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843b4047dd2402e79fd7_d69f34fd-1a23-4a05-8e4d-9164bdf94c09.png" width=540px height=790px alt="Signing in to Google: 2-step Verification">

<br>

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843ad408f849b8aabe76_f25cbc8f-2f56-456b-882c-08ede9efd82d.png" width=540px height=360px alt="Signing in to Google: 2-step Verification (close-up)">


Click the blue GET STARTED button:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843ca5036f513c3b1907_5d596f55-8c5f-428e-a2c9-8b77f6aa171d.png" width=540px height=590px alt="3">

Login using your password. Make sure you are using the right account.

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843cf148f40e2a89e678_896736ac-9905-467f-9dfe-e7933f985e31.png" width=540px height=590px alt="Google login">

Enter your phone number and click SEND:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843b6ae4cf132a436289_22775b96-87b3-46fc-bb11-20f20dc40246.png" width=540px height=640px alt="Phone number">

Wait for the confirmation code to arrive and enter it in:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843b43e049c80cd49151_81330437-5053-4408-8f5f-10dd485c5d16.png" width=540px height=640px alt="Confirmation code">

Click the TURN ON button:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843d43e0495b73d492c5_b52ea86f-f1cf-4dd2-8884-a0c9ad9f2d4e.png" width=540px height=640px alt="Turn on">

2FA should now be enabled:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843cd408f86b92aabe8a_83c75904-6438-470f-83ed-6e2fd56fe883.png" width=540px height=640px alt="2FA on">

#### App Passwords

Now we will generate a special password that our app can use as the 2-step verification.

Back in the Signing in to Google panel select "App passwords" to add a new password:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843bb81a327f903af954_e55dadf8-7e54-460e-907e-0a1d3891c275.png" width=540px height=640px alt="App passwords: none">

Under the "Select app" drop-down select " Other":

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843bf2d8b74704fe2464_033b19ec-f8bd-4831-a8d8-27d82757c042.png" width=540px height=640px alt="App passwords: other">

Give your app a name and click GENERATE:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843c67fd2c708467fab1_ae0f2735-5c52-4fe6-82ed-fa4509dd6207.png" width=540px height=640px alt="App passwords: generate">

Write down (copy to clipboard) your generated password to use in the app:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843cf2d8b74e89fe248d_1d42dbed-1271-471e-a495-ae40c4e345de.png" width=540px height=640px alt="App password: generated">

We should now have our generated app password:

<img src="https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/6299843c538a79da96a43532_7370adc1-0996-4065-9134-a7846094f9c7.png" width=540px height=590px alt="App password: list">

> **Note:**
>
> **Use App password instead of your account password.**

[Article Source](https://www.abstractapi.com/guides/sending-email-with-python)
