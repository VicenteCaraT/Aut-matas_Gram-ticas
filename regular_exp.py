import re

#Numero real con dos decimales y separador de miles
def NumeroReal(numero) -> bool:
    patron = r'^\d\.\d{2}$'
    if re.match(patron, str(numero)):
        return True
    else:
        return False
        
        
print(NumeroReal(2.32))
print(NumeroReal(2))

def SeparadordeMiles(numero:str) -> bool :
    patron = r'\b\d{1,3}(,\d{3})*\b'
    
    if re.match(patron, str(numero)):
        return True
    else:
        return False
    
print(SeparadordeMiles("123.431.312"))
print(SeparadordeMiles("234123"))

def emailUM(email:str) -> bool:
    patron = r'^\w+@alumno\.um\.edu\.ar$'
    if re.match(patron, str(email)):
        return True
    else:
        return False
    
print(emailUM("vit.cara@alumno.um.edu.ar"))
print(emailUM("juan@gmail.com"))

def numeroArg(telefono:str) ->bool :
    patron = r'^\+54(15)(\d{4})(\d{3})$'
    
    if re.match(patron, str(telefono)):
        return True
    else:
        return False

print(numeroArg("+54152996563936"))
print(numeroArg("542996563936"))

def cuil(dni:str)-> bool:
    patron = r'^\d{2}-\d{8}-\d{1}$'
    
    if re.match(patron, str(dni)):
        return True
    else:
        return False
    
print(cuil("23-44909938-2"))
print(cuil("44909938"))
    
def fecha(fecha:str) -> bool:
    patron = r'^\d{2}[-/]\d{2}[-/]\d{4}$'
    
    if re.match(patron, fecha):
        return True
    else:
        return False

print(fecha("10-03-2024"))
print(fecha("23/10/2024"))
print(fecha("2024/02/13"))

def youTubeid(id):
    pass
