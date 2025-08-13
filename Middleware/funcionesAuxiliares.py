import re

def show_frame(frame1,frame2):
    frame1.pack_forget()
    frame2.pack()
def show_Configuration(component,frameC):
    for components  in component:components[0].pack_forget()
    frameC.pack()

def fixWord(word):
    p="'"
    if("('" in word):
        print(f"arreglamos la palabra {word.split(p,2)[1]}")
        return word.split(p,2)[1]
    return word

#Esta funcion se encargara de reemplazar la cadena de texto
def replaceCadena(path,patron, service,loggin,datetime):
    #Loggin para capturar la ruta del archivo a reemplazar
    loggin.info(f' {datetime.datetime.now() }: Se comienza a modificar el  archivo {path}')
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())
        print(path)
        #abre el archivo solo para lectura, indicandolo con la "r"
        content=open(path,"r").read()

        #Almacena ese valor en la variable, old, para saber el valor antiguo
        old = re.findall(patron, content)

        #redefinimos el nuevo contenido del archivo, reemplazando el antiguo valor por el nuevo
        content=content.replace(old[0],service)
        print(f' {datetime.datetime.now() }: Se cambio la cadena de texto {old[0]}')
        print(f' {datetime.datetime.now() }: por la cadena de texto {service}')
        #Se vuelve abrir el archivo pero esta vez con permiso de escritura
        #tener cuidado ya que esto sobreescribe el documento seleccionado.
        open(path,"w").write(content)

        loggin.info(f' {datetime.datetime.now() }: Ha sido modificado el  archivo {path} de forma exitosa')
        loggin.info(f' {datetime.datetime.now() }: Se cambio la cadena de texto {old[0]}')
        loggin.info(f' {datetime.datetime.now() }: por la cadena de texto {service}')
    except:
        print(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')

        loggin.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')


#Esta funcion se encarga de remplazar un patron de un nombre con un nombre especifico en una seccion especifica
def replaceCadenaInSection(path,patron,SecondPatron, service,loggin,datetime):
    #Loggin para capturar la ruta del archivo a reemplazar
    loggin.info(f' {datetime.datetime.now() }: Se comienza a modificar el  archivo {path}')

    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:

        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #Abre el documento, especificado en la ruta(path)
        content=open(path,"r").read()

        #Almacena ese valor en la variable, old, para saber el valor antiguo
        old = re.findall(patron, content)

        #Realmacenar  el valor de la segunda busquedad del patron, pero esta vez buscara no en el archivo sino en la seccion anteriormente almacenada
        old=re.findall(SecondPatron, old[0])

        #redefinimos el nuevo contenido del archivo, reemplazando el antiguo valor por el nuevo
        content=content.replace(old[0],service)

        #Se vuelve abrir el archivo pero esta vez con permiso de escritura
        #tener cuidado ya que esto sobreescribe el documento seleccionado.
        open(path,"w").write(content)
        
        #Si el proceso sale exitoso, se imprime "exitoso" y captura la ruta, nombre del antiguo y nuevo texto reemplazarlo  
        print("Exitoso")
        loggin.info(f' {datetime.datetime.now() }: Ha sido modificado el  archivo {path} de forma exitosa')
        loggin.info(f' {datetime.datetime.now() }: Se cambio la cadena de texto {old[0]}')
        loggin.info(f' {datetime.datetime.now() }: por la cadena de texto {service}')
        
    except Exception as e:
        #si ocurre una excepcion, se imprimira esto_
        print(f"Espacio en blanco detectado {e}")
        loggin.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')

def Identify(path,patron,secondPatron, logging, datetime):
    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #Imprime la ruta del archivo
        #print(path)

        #abre el archivo solo como lectura
        content=open(f"{path}","r").read()

        #asigna el patron encontrado a la variable patron 
        patron=re.findall(f'{patron}' , content)

        #Una vez idemtificado el patron, este lo divide en tres string 
        #[String1>][PATRON][<String2]
        patron=re.findall(f"{secondPatron}",patron[0])[0].split(">",3)[1].split("<",2)[0]
        #patron=re.findall(f"{secondPatron}",patron[0])[0].split('"',3)[1].split('"',2)[0]
        print(patron)
        return patron
    except Exception as e:
        logging.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')
def IdentifyJSON(path,patron,secondPatron, logging, datetime):
    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #Imprime la ruta del archivo
        #print(path)

        #abre el archivo solo como lectura
        content=open(f"{path}","r").read()
        
        #asigna el patron encontrado a la variable patron 
        patron=re.findall(f'{patron}' , content)
        #Una vez idemtificado el patron, este lo divide en tres string 
        #[String1:][PATRON][,String2]
        patron=re.findall(f"{secondPatron}",patron[0])[0].split(":",2)[1].split(",",2)[0].strip()
        
        #Retorna el patron
        return patron
    except Exception as e:
        print(f"Espacio en blanco detectado: {e}")
        logging.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')
def identifyBaseURL(path,patron,secondPatron, logging, datetime):
    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #Imprime la ruta del archivo
        #print(path)

        #abre el archivo solo como lectura
        content=open(f"{path}","r").read()

        #asigna el patron encontrado a la variable patron 
        patron=re.findall(f'{patron}' , content)

        #Una vez idemtificado el patron, este lo divide en tres string 
        #[String1>][PATRON][<String2]
        #patron=re.findall(f"{secondPatron}",patron[0])[0].split(">",3)[1].split("<",2)[0]
        patron=re.findall(f"{secondPatron}",patron[0])[0].split('"',3)[1].split('"',2)[0]
        print(patron)
        return patron
    except Exception as e:
        print(f"Espacio en blanco detectado: {e}")
        logging.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')
def loadImagen(img,PI,loggin, datetime):
    try:
        return PI(file=img)
    except Exception as e:
        loggin.info(f' {datetime.datetime.now() }: No se ha encontrado la img {img}')
        loggin.info(f' {datetime.datetime.now() }: {e}')

def Insert(tb,function,loggin,datetime):
    try:
        tb.insert(0,function)
    except Exception as e:
        loggin.error(f' {datetime.datetime.now() }: No se ha cargado el dato')
        loggin.error(f' {datetime.datetime.now() }: {e}')

def validateField(textbox,loggin, mb, name,second_name,datetime):
    if(textbox.get()==""):
        loggin.error(f' {datetime.datetime.now() }: No se puede modificar {name} sin especificar el nombre {second_name}')
        mb.showerror("Error",f"No se puede modificar {name} sin especificar el nombre {second_name}")
        return False
    else:
        return True
def validateLabel(textbox,loggin, mb, name,second_name,datetime):
    if(textbox.cget("text")==""):
        loggin.error(f' {datetime.datetime.now() }: No se puede modificar {name} sin especificar el nombre {second_name}')
        mb.showerror("Error",f"No se puede modificar {name} sin especificar el nombre {second_name}")
        return False
    else:
        return True