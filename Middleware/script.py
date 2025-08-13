from os import system,popen
import psutil
import win32com.client
import subprocess

#Modulo script, se encarga de llevar a cabo la ejecucion de comandos de linea
#V 0.105 usar popen para capturar los eventos 

#esta funcion Se utiliza para establecer el inicio del servicio instalado
def setStart(var,loggin,datetime):
   if(var==1):
    loggin.info(f' {datetime.datetime.now() }: Se establecio el inicio Manual')
    return "demand"    
   if(var==2):
    loggin.info(f' {datetime.datetime.now() }: Se establecio el inicio Automatico')
    return "Auto"
   else: return 0

#See encarga de indentificar el servicio
def identifyService(path,logging,datetime):
    logging.info(f' {datetime.datetime.now() }: Empezando a identificar el servicio de la ruta {path}')
    services = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    service_locator = services.ConnectServer(".", "root\cimv2")
    service_query = "SELECT * FROM Win32_Service"
    service_list = service_locator.ExecQuery(service_query)
    print(path)
    print(path.replace('\\', r"/"))
    path2=path.replace('\\', r"/")
    for service in service_list:
        try:
            if(path==service.PathName or path2==service.PathName):
                print(f"Nombre: {service.Name}")
                print(f"Estado: {service.State}")
                print(f"Tipo de inicio: {service.StartMode}")
                print(f"Descripción: {service.Description}")
                print(f"Ruta del archivo ejecutable: {service.PathName}")
                logging.info(f' {datetime.datetime.now() }: Nombre: {service.Name}')
                logging.info(f' {datetime.datetime.now() }: Estado: {service.State}')
                logging.info(f' {datetime.datetime.now() }: Tipo de inicio: {service.StartMode}')
                logging.info(f' {datetime.datetime.now() }: Descripción: {service.Description}')
                logging.info(f' {datetime.datetime.now() }: Ruta del archivo ejecutable: {service.PathName}')
                return service.Name,service.State, service.StartMode, service.PathName
        except Exception as e:
            logging.info(f' {datetime.datetime.now() }: error al identificar los servicios {e}')
#identifyService("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\Middleware\\STE\\bin\Sidesys.Services.ApplicationService.exe", logging, datetime)
def installService(name,path,var,loggin,datetime):
    start=setStart(var,loggin,datetime)
    loggin.info(f' {datetime.datetime.now() }: Inicializacion De La instalacion del servicio')
    resp=popen('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    loggin.info(f' {datetime.datetime.now() }: sc create "{name}"  binpath="{path}" obj=localsystem start={str(start)} ')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    print('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    if(validateExistService(name)):
        loggin.info(f' {datetime.datetime.now() }: El servicio {name} se ha instalado exitosamente')
        loggin.info(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return True
    else:
        loggin.error(f' {datetime.datetime.now() }: El servicio {name} no se ha instalado ')
        loggin.error(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return False

#identifyService("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\Middleware\\STE\\bin\Sidesys.Services.ApplicationService.exe", logging, datetime)
def manageService(p,name,path,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del manejador de servicio')
    print(p)
    print(name)
    print(path)
    #Ejecuta el servicio
    if(p==1):
        resp=popen(f'sc start "{name}"')
        loggin.info(f'sc start "{name}"')
        loggin.info(f' {datetime.datetime.now() }: {resp}')
        print(f'sc start "{name}"')   
    if(p==2):
        resp=popen(f'sc stop "{name}"')
        loggin.info(f'sc stop "{name}"')
        loggin.info(f' {datetime.datetime.now() }: {resp}')
        print(f'sc stop "{name}"')  

def instalarCounter(name,path):
    system('')
def installDLL(path,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion el instalador de DLL')
    loggin.info(f' {datetime.datetime.now() }: "{path}\\MultimediaService\\bin\\Sidesys.eFlow.ClientService.exe" install')
    resp=popen(f'{path}\\MultimediaService\\bin\Sidesys.eFlow.ClientService.exe install')
    loggin.info(f' {datetime.datetime.now() }: regsvr32.exe "{path}\e-Flow\SSPrinter\SSPrinter.dll"')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'regsvr32.exe "{path}\e-Flow\SSPrinter\SSPrinter.dll"')
    loggin.info(f' {datetime.datetime.now() }: C:\Windows\Microsoft.NET\Framework\\v4.0.30319\\regasm.exe "{path}\e-Flow\media\queue\SSVoice\Sidesys.SSVoice.dll" /codebase')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'C:\Windows\Microsoft.NET\Framework\\v4.0.30319\\regasm.exe "{path}\e-Flow\media\queue\SSVoice\Sidesys.SSVoice.dll" /codebase')
    loggin.info(f' {datetime.datetime.now() }: Fin de la instalacion de DLL')
    loggin.info(f' {datetime.datetime.now() }: {resp}')

def autologon(name, domainName, password, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del configurador de autologon')
    loggin.info(f' {datetime.datetime.now() }: powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\'-Name \'AutoAdminLogon\' -Value \'1\'')
    resp=popen(f'powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' -Name \'AutoAdminLogon\' -Value \'1\'').read()
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    loggin.info(f' {datetime.datetime.now() }: powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' -Name \'DefaultUserName\' -Value \'{name}\'')
    resp=popen(f'powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' -Name \'DefaultUserName\' -Value \'{name}\'').read()
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    loggin.info(f' {datetime.datetime.now() }: powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' -Name \'DefaultPassword\' -Value \'{password}\'')
    resp=popen(f'powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' -Name \'DefaultPassword\' -Value \'{password}\'').read()
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    loggin.info(f' {datetime.datetime.now() }: powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' -Name \'DefaultDomainName\' -Value \'{domainName}\'')
    resp=popen(f'powershell   Set-ItemProperty -Path \'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\' -Name \'DefaultDomainName\' -Value \'{domainName}\'').read()
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    loggin.info(f' {datetime.datetime.now() }: Finalizacion del configurador de autologon')

def manageInternetOption(url, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del configurador de Internet Option')
    loggin.info(f' {datetime.datetime.now() }: powershell  New-Item -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "https" -Value 2 -Type DWORD -Force ')
    resp=popen(f'powershell  New-Item -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "https" -Value 2 -Type DWORD -Force')
    loggin.info(f' {datetime.datetime.now() }: powershell Set-ItemProperty -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "https" -Value 2 -Type DWORD -Force')        
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell Set-ItemProperty -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "https" -Value 2 -Type DWORD -Force')
    loggin.info(f' {datetime.datetime.now() }: powershell  New-Item -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "http" -Value 2 -Type DWORD -Force ')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell  New-Item -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "http" -Value 2 -Type DWORD -Force')
    loggin.info(f' {datetime.datetime.now() }:powershell Set-ItemProperty -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "http" -Value 2 -Type DWORD -Force')        
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell Set-ItemProperty -Path \'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\{url}\' -Name "http" -Value 2 -Type DWORD -Force')
    loggin.info(f' {datetime.datetime.now() }: powershell Set-ItemProperty -Path \'"HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\2"\' -Name 1201 -Value 0')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell Set-ItemProperty -Path \'"HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\2"\' -Name 1201 -Value 0')
    loggin.info(f' {datetime.datetime.now() }: Finalizacion del configurador de Internet Option')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    
def autoplaylist(url, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del configurador de autoplaylist')
    loggin.info(f' {datetime.datetime.now() }: powershell \'REG	ADD	HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome	/v	AutoplayAllowed /t REG_DWORD /d 1 /f\'')
    resp=popen(f'powershell REG ADD	\'HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome \'	/v	AutoplayAllowed /t REG_DWORD /d 1 /f')
    loggin.info(f' {datetime.datetime.now() }: powershell \'REG ADD	HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoplayAllowlist\ \'	/v	"1"	/t	REG_SZ	/d	{url}	/f')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell REG ADD	\'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoplayAllowlist\ \'	/v	"1"	/t	REG_SZ	/d	{url}	/f')
    loggin.info(f' {datetime.datetime.now() }: powershell \'REG	ADD	HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Edge\'	/v	AutoplayAllowed /t REG_DWORD /d 1 /f')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell REG ADD	\'HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Edge\ \'	/v	AutoplayAllowed /t REG_DWORD /d 1 /f')
    loggin.info(f' {datetime.datetime.now() }: powershell \'REG	ADD HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\AutoplayAllowlist\	/v	"1"	/t	REG_SZ	/d	{url}	/f')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell REG ADD \'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\AutoplayAllowlist\ \'	/v	"1"	/t	REG_SZ	/d	{url}	/f')

    loggin.info(f' {datetime.datetime.now() }: Finalizacion del configurador de autoplaylist')
def cargarResolucion(loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del configurador de ajuste de resolucion')
    loggin.info(f' {datetime.datetime.now() }: assert\QRes.exe /l')
    resp=popen('assert\QRes.exe /l').read()
    resp=resp.split('\n', -1)
    arreglo=[]
    for reps in resp:
        if('x' in reps.split(',', -1)[0] ):
            if(reps.split(',', -1)[0] not in arreglo):arreglo.append(reps.split(',', -1)[0])
    return arreglo
def ajustarResolucion(res, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del configurador de ajuste de resolucion')
    loggin.info(f' {datetime.datetime.now() }:valor x:{res.split("x",-1)[0]} y:{res.split("x",-1)[1]}')
    print(res.split('x',-1)[0])
    print(res.split('x',-1)[1])
    resp=popen(f'assert\QRes.exe /x {res.split("x",-1)[0]} /y {res.split("x",-1)[1]}').read()
    loggin.info(f' {datetime.datetime.now() }: assert\QRes.exe /x {res.split("x",-1)[0]} /y {res.split("x",-1)[1]}')
    loggin.info(f' {datetime.datetime.now() }: {resp}')

    pass
def scriptBotonera(path,script, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Script generado en la ruta {path}')
    loggin.info(f' {datetime.datetime.now() } {script}')
    print(script)
    open(path,"w").write(script)
    pass
def scriptBotoneraExplorer(path, script,fullscreen, x, y, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Script generado en la ruta {path}')
    loggin.info(f' {datetime.datetime.now() } {script}')
    if len(fullscreen)>0:fullscreen=True
    else:fullscreen=False
    print(script)
    print(fullscreen)
    print(x)
    print(y)
    #open(path,"w").write(script)
    pass

def validateExistService(name):
    #Itera los servicios
    for proc in psutil.win_service_iter():
        try:
            # Valida los nombres de lo servicios 
            if name.lower() in proc.name().lower():
                print(proc.name())
                return False;
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return True;

def unLockFolder(url, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del unblockFolder')
    resp=popen(f'powershell "Get-ChildItem -Path \'{url}\' -Recurse | Unblock-File"')
    loggin.info(f' {datetime.datetime.now() }: powershell "Get-ChildItem -Path \'{url}\' -Recurse | Unblock-File"')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    resp=popen(f'powershell "Get-ChildItem -Path \'{url}\' -Recurse -File | % '+"{"+' $_.IsReadOnly=$false '+"}\"")
    loggin.info(f' {datetime.datetime.now() }: powershell "Get-ChildItem -Path \'{url}\' -Recurse -File | % '+"{"+' $_.IsReadOnly=$false '+"}\"")
    loggin.info(f' {datetime.datetime.now() }: {resp}')   
    loggin.info(f' {datetime.datetime.now() }: Finalizacion del unblockFolder')

def TNC(url,port, loggin, datetime):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del tnc')
    resp=consultaPowershell(f'powershell tnc {url} -port {port}',loggin,datetime)
    loggin.info(f' {datetime.datetime.now() }: powershell tnc {url} -port {port}')
    loggin.info(f' {datetime.datetime.now() }: {resp}')
    loggin.info(f' {datetime.datetime.now() }: Finalizacion del tnc')
    return resp
def consultaPowershell(consulta,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }:empezando la consulta en poweshell')
    loggin.info(f' {datetime.datetime.now() }:{consulta}')
    comando_ps =f'''{consulta}'''
    resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
    if(len(resultado.stderr)>0):loggin.error(f' {datetime.datetime.now() }:error al realizar la consulta en powershell {resultado.stderr}')
    return resultado.stdout

#"C:\Users\jaquino\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" main.py script.py Validador.py funcionesAuxiliares.py configuracionCitas.py db.py iis.py NME.py NCache.py code.py Encuesta.py RHI.py mail.py consola.py nodo.py Reporte.py --onefile --name "Instalador servicio"
#"C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" main.py script.py Validador.py funcionesAuxiliares.py configuracionCitas.py db.py iis.py NME.py NCache.py code.py Encuesta.py RHI.py mail.py consola.py --onefile --name "Instalador servicio"
#C:\Users\jaquino\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip