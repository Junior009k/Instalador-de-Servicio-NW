from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de crear los site en el iis
def createSite():
  logging.info(f' {datetime.datetime.now() }: Se comienza a crear el site')
  bandera=validateField(TextboxNameSite,logging,MessageBox,"No se puede crear el site","nombre del site",datetime)
  bandera=bandera*validateField(TextboxPortHttp,logging,MessageBox,"No se puede crear el site","el puerto del site",datetime)
  bandera=bandera*validateLabel(label6,logging,MessageBox,"No se puede crear el site","la ruta",datetime)
  if(bandera):
    if(createSiteIIS(TextboxNameSite.get(),label6.cget("text"),logging,TextboxPortHttp.get())):tk.messagebox.showinfo(title="Felicidades", message="El site se creo correctamente")
#esta funcion se encarga de crear la aplicacion en el iis
def createAplication():
  logging.info(f' {datetime.datetime.now() }: Se comienza a crear la aplicacion')
  bandera=validateField(TextboxNameApplication,logging,MessageBox,"No se puede crear el aplicacion","nombre del aplicacion",datetime)
  bandera=bandera*validateLabel(label2,logging,MessageBox,"No se puede crear el aplicacion","la ruta",datetime)  
  if(bandera):
    if(createAplicationIIS(TextboxNameApplication.get(),label2.cget("text"),logging)):tk.messagebox.showinfo(title="Felicidades", message="La aplicacion se creo correctamente")
