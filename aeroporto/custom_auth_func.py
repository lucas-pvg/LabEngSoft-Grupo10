'''
Funções para criação de usuários de acordo com cada grupo de login
'''
def piloto(user):
    return user.groups.filter(name='piloto').exists()

def companhia(user):
    return user.groups.filter(name='companhia').exists()

def gerente(user):
    return user.groups.filter(name='gerente').exists()

def operador(user):
    return user.groups.filter(name='operador').exists()

def torre(user):
    return user.groups.filter(name='torre').exists()
