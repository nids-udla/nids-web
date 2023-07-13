import hashlib
from .models import Usuario
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re

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
# funcion para validar email para editar el perfil
def validaremail(email):
    validar = EmailValidator()
    try:
        validar(email)
        return True
    except ValidationError:
        return False

# funcion para validar el numero para editar el perfil
def validar_numero(telefono):
    patron = r'^\d{9}$'
    if re.match(patron, telefono):
        return True
    else:
        return False

# funcion para validar la url de Github

def validar_github(github):
    patron = r'^https:\/\/github\.com\/[a-zA-Z0-9-]+$'
    if re.match(patron, github):
        return True
    else:
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