"""email functionality"""
from django.core.mail import send_mail


def email_message(message_dict):
    """email content"""
    contents = f"""
   Welcome to Group4 Bank! A new account was created using this email address.
   For extra safety with your account, we recommend that you set up the Two Factor Authenticator at:
   http://127.0.0.1:8000/account/two_factor/setup/

   using your credentials:
   Your username: {message_dict['username']}
   Your password: {message_dict['password']}

   We are using Two Factor Authenthication, therefore please have the Google Authenticator App installed!
   """
    send_mail(
        'Activate your account',
        contents,
        'codr0040@stud.kea.dk',
        [message_dict['email']],
        fail_silently=False
    )
