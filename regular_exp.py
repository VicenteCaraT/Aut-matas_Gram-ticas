import re

#Numero real con dos decimales y separador de miles
def verificar_numero(numero:str):
    patron = r'^\d{1,3}(\.\d{3})*(,\d{2})?$'
    
    if re.match(patron, str(numero)):
        return f"El numero ingresado <{numero}> es valido."
    else:
        return f"El numero ingresado <{numero}> no es valido."

print("< Verificación de Número >")
print(verificar_numero("2.32"))         
print(verificar_numero("2"))            
print(verificar_numero("123.431.312"))  
print(verificar_numero("234,123"))     
print(verificar_numero("234123"))       
print(verificar_numero("230.234,23"))   

#Cuenta de Email de alumno de la Universidad de Mendoza
def emailUM(email:str):
    patron = r'^\w+(\.\w+)*@alumno\.um\.edu\.ar$'
    if re.match(patron, str(email)):
        return f"El email ingresado <{email}> es valido."
    else:
        return f"El email ingresado <{email}> no es valido."
    
print("< Mail UM >")
print(emailUM("vit.cara@alumno.um.edu.ar"))
print(emailUM("juan@gmail.com"))

#Número de teléfono móvil de Argentina, que incluya código de país, de
#provincia, y el 15.
def numeroArg(telefono:str):
    patron = r'^\+54(15)(\d{3})(\d{7})$'
    
    if re.match(patron, str(telefono)):
        return f"El número ingresado <{telefono}> es valido."
    else:
        return f"El número ingresado <{telefono}> no es valido."

print("< Numero Telefono >")
print(numeroArg("+54152991566946"))
print(numeroArg("+542996563936"))

#CUIL.
def cuil(dni:str):
    patron = r'^\d{2}-\d{8}-\d{1}$'
    
    if re.match(patron, str(dni)):
        return f"El CUIL ingresado <{dni}> es valido."
    else:
        return f"El CUIL ingresado <{dni}> no es valido."

print("< CUIL >")
print(cuil("20-44909938-2"))
print(cuil("44909938"))
    
#Fecha con formato dd/mm/yyyy o dd-mm-yyyy
def fecha(fecha:str):
    patron = r'^\d{2}[-/]\d{2}[-/]\d{4}$'
    
    if re.match(patron, str(fecha)):
        return f"La fecha ingresada <{fecha}> es valida."
    else:
        return f"La fecha ingresada <{fecha}> no es valida."

print("< Fecha >")
print(fecha("10-03-2024"))
print(fecha("23/10/2024"))
print(fecha("2024/02/13"))

#ID de un vídeo de Youtube
def youTubeid(id):
    patron = r'^\w{11}$'

    if re.match(patron, str(id)):
        return f"La id ingresada <{id}> es valida."
    else:
        return f"La id ingresada <{id}> no es valida."

print("< IDYoutube >")
print(youTubeid("dQw4w9WgXcQ"))  
print(youTubeid("123456789010"))

#Seguridad de una contraseña
def contraseña(password):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){10,16}$'
    
    if re.match(patron, str(password)):
        return f"La contraseña <{password}> cumple con las condiciones."
    else:
        return f"La constraseña <{password}> no cumple con las condiciones."
    
print("< Contraseña >")
print(contraseña("Vicente123@"))
print(contraseña("JuanVCrack135")) 
print(contraseña("CONtraseñ@123"))  
print(contraseña("C0ntraseñ@Super-secret@123")) 