import hashlib
from .models import Usuario
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def verify(email):
    find = Usuario.objects.get(email=email)

    if find is not None:
        return True
    else:
        return False

def encrypt(pw):
    hasher = hashlib.sha256()
    hasher.update(pw.encode('utf-8'))
    encrypted = hasher.hexdigest()
    return encrypted

def validate(email, password):
    input_email = email
    user = Usuario.objects.get(email=input_email)

    if user:
        input_password = encrypt(password)
        db_password = user.password

        if db_password == input_password:
            return True
        else:
            return False
    else:
        return None

def validaremail(email):
    validar = EmailValidator()
    try:
        validar(email)
        return True
    except ValidationError:
        return False
    
# ------------------------------------------------------------------------
# Creo que es aplicable sin tener que utilizar todo este código.
#
# def set_session(request):
#     request.session['username'] = 'John'
#     request.session['is_logged_in'] = True
#     return HttpResponse('Session data set.')

# def get_session(request):
#     username = request.session.get('username')
#     is_logged_in = request.session.get('is_logged_in')
#     return HttpResponse(f"Username: {username}, Logged In: {is_logged_in}")