import re

def code(text, desplazamiento):
    resultado = ""
    for caracter in text:
        if caracter.isalpha():
            codigo = ord(caracter)
            if caracter.islower():
                base = ord('a')
            else:
                base = ord('A')
            codigo = (codigo - base + desplazamiento) % 26 + base
            caracter_cifrado = chr(codigo)
            resultado += caracter_cifrado
        else:
            resultado += caracter
    return resultado


def decode(texto_cifrado, desplazamiento):
    return code(texto_cifrado, -desplazamiento)



def codeSystem():
    content=open("Middleware\Systeminformation.config","r").read()
    content=code(content,3)
    open("Middleware\Systeminformation.config","w").write(content)
    
def decodeSystem():
    content=open("Middleware\Systeminformation.config","r").read()
    content=decode(content,3)
    open("Middleware\Systeminformation.config","w").write(content)
    
def readValueSystem(value):
    content=open("Middleware\Systeminformation.config","r").read()
    #print(re.findall(value, content))
    value=re.findall(value, content)[0].split(">",3)[1].split("<",2)[0]
    #print(value)
    return value

#readValueSystem()
#codeSystem()
#decodeSystem()