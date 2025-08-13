import re
from tkinter import messagebox as MessageBox
import os
#Valida los servicios
def validateService(path,servicio, carpeta, subCarpeta):
  path=path.lower()
  carpeta=carpeta.lower()
  subCarpeta=subCarpeta.lower()
  servicio=servicio.lower()
  bandera=False
  if(re.findall(carpeta,path) and re.findall(subCarpeta,path) and re.findall(servicio,path)):
    bandera=True
  if(re.findall(carpeta,path)==[] and (re.findall(subCarpeta,path)==[] or re.findall(subCarpeta,path)==[subCarpeta]) and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio])):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {carpeta}") 
    bandera=False
  if(re.findall(carpeta,path)==[carpeta] and re.findall(subCarpeta,path)==[]   and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio])):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {subCarpeta}") 
    bandera=False
  if( re.findall(carpeta,path)==[])and re.findall(subCarpeta,path)==[]   and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio]):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {subCarpeta} ni dentro de la carpeta de {carpeta}") 
    bandera=False
  if(re.findall(carpeta,path)==[carpeta] and re.findall(subCarpeta,path)==[subCarpeta] and re.findall(servicio,path)==[]):
    MessageBox.showerror("Error",f"Usted no esta seleccionando el archivo {servicio}") 
    bandera=False
  return bandera

#Se encarga de validar si un directorio existe o no existe. 
def validateDirectory(path,name,logging,datetime):
    # Verifica si la carpeta existe
    if os.path.exists(f"{path}\{name}") and os.path.isdir(f"{path}\{name}"):
        print(f' {datetime.datetime.now() }: La carpeta {path}\{name} existe')
        logging.info(f' {datetime.datetime.now() }: La carpeta {name}  existe')
        return False     
    else:
        print(f' {datetime.datetime.now() }: La carpeta {path}\{name} no existe')
        logging.error(f' {datetime.datetime.now() }: La carpeta {name} no existe')
        return True    

