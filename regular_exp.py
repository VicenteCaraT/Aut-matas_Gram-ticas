import re

#Numero real con dos decimales y separador de miles
def NumeroReal(numero) -> bool:
    patron = r'^\d\.\d{2}$'
    if re.match(patron, str(numero)):
        return True
    else:
        return False
        
print("< Numeros Reales >")
print(NumeroReal(2.32))
print(NumeroReal(2))

def SeparadordeMiles(numero:str) -> bool :
    patron = r'\b\d{1,3}(,\d{3})*\b'
    
    if re.match(patron, str(numero)):
        return True
    else:
        return False

print("< Separador de Miles >")
print(SeparadordeMiles("123.431.312"))
print(SeparadordeMiles("234123"))

#Cuenta de Email de alumno de la Universidad de Mendoza
def emailUM(email:str) -> bool:
    patron = r'^\w+(\.\w+)*@alumno\.um\.edu\.ar$'
    if re.match(patron, str(email)):
        return True
    else:
        return False
    
print("< Mail UM >")
print(emailUM("vit.cara@alumno.um.edu.ar"))
print(emailUM("juan@gmail.com"))

#Número de teléfono móvil de Argentina, que incluya código de país, de
#provincia, y el 15.
def numeroArg(telefono:str) ->bool :
    patron = r'^\+54(15)(\d{3})(\d{7})$'
    
    if re.match(patron, str(telefono)):
        return True
    else:
        return False

print("< Numero Telefono >")
print(numeroArg("+54152996563936"))
print(numeroArg("+542996563936"))

#CUIL.
def cuil(dni:str)-> bool:
    patron = r'^\d{2}-\d{8}-\d{1}$'
    
    if re.match(patron, str(dni)):
        return True
    else:
        return False

print("< CUIL >")
print(cuil("23-44909938-2"))
print(cuil("44909938"))
    
#Fecha con formato dd/mm/yyyy o dd-mm-yyyy
def fecha(fecha:str) -> bool:
    patron = r'^\d{2}[-/]\d{2}[-/]\d{4}$'
    
    if re.match(patron, fecha):
        return True
    else:
        return False

print("< Fecha >")
print(fecha("10-03-2024"))
print(fecha("23/10/2024"))
print(fecha("2024/02/13"))

#ID de un vídeo de Youtube
def youTubeid(id):
    patron = r'^\w{11}$'

    if re.match(patron, str(id)):
        return True
    else:
        return False

print("< IDYoutube >")
print(youTubeid("dQw4w9WgXcQ"))  
print(youTubeid("123456789010"))

#Seguridad de una contraseña
def contraseña(password):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){10,16}$'
    
    if re.match(patron, str(password)):
        return True
    else:
        return False
    
print("< Contraseña >")
print(contraseña("Vicente123@"))
print(contraseña("JuanVCrack135")) 
print(contraseña("CONtraseñ@123"))  
print(contraseña("C0ntraseñ@Super-secret@123")) 