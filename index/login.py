import bcrypt
from .models import Usuario

def verify(**kwargs):
    input_email = kwargs.get('email')
    input_password = kwargs.get('password')

    usuario = Usuario.objects.filter(email=input_email)
    db_password = usuario.password

    if bcrypt.checkpw(input_password, db_password):
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