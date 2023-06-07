import hashlib
from .models import Usuario

def verify(email):
    find = Usuario.objects.get(email=email)

    print("!!!!!!!!!!! --->".format(find))

    if find is not None:
        return False
    else:
        return True

def encrypt(pw):
    hasher = hashlib.sha256()
    hasher.update(pw.encode('utf-8'))
    encrypted = hasher.hexdigest()
    return encrypted

def validate(email, password):
    input_email = email
    user = Usuario.objects.filter(email=input_email)

    print("!!!!!!!!!!!EMAIL RECIBIDO --->".format(input_email))
    print("!!!!!!!!!!!USUARIO ENCONTRADO --->".format(input_email))

    if user:
        input_password = encrypt(password)
        db_password = user.password

        if db_password == input_password:
            return True
        else:
            return None
    else:
        return None
    
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