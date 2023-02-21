from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'ArnalIman.shoes.com registration code', # title
        f'http://localhost:8000/api/v1/account/activate/{code}', # body
        'bananad196@gmail.com', # from
        [email] # to
    )
