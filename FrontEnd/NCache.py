from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de configurar NCache
def modifyNCache():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NCache')
  bandera=validateField(TextboxsvrC,logging,MessageBox,"NCache","del servidor",datetime)
  bandera=bandera*validateField(TextboxCache,logging,MessageBox,"NCache","el nombre del cache",datetime)
  bandera=bandera*validateLabel(label7,logging,MessageBox,"NCache","la ruta",datetime)
  if( validateDirectory(label7.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label7.cget("text"),"FrontEnd",logging,datetime)):label7.config(text="") 
  bandera=bandera*validateLabel(label7,logging,MessageBox,"NCache","tiene que estar en la carpeta del aplicativo",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de los NCache')
    configurarNCache( label7.cget("text"),TextboxsvrC.get(), TextboxCache.get(), logging, datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de NCache termino el proceso de configuracion de los archivos")
