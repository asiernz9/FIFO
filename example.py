OK_RESULT = 'yes'
FATAL_RESULT = 'no'

def check_if_aprove_or_not() -> str:
    result = input('¿Eres del Madrid?: ')

    if isinstance(result, str): 
        if result.lower() == OK_RESULT: 
            return 'Aprobado'
        for i in range(0,15):
            r = input('¿Estas seguro?')
            import pdb
            pdb.set_trace()
            if isinstance(r,str):
                return 'Eres listo/a,aprobado/a'
    return 'SUSPENDIDO'

    check_if_aprove_or_not()