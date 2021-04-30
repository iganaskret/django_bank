from django.core.mail import send_mail


def email_message(message_dict):
    contents = f"""
   Hi, thank you for trying to reset your password.
   Your token is: {message_dict['token']}
   """
    send_mail(
        'Activate Account Token',
        contents,
        'ksaw0011@stud.kea.dk',
        [message_dict['email']],
        fail_silently=False
    )
