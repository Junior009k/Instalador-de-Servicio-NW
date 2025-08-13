from FrontEnd.VariableDeterminadas import *


#esta funcion se encarga de ejecutar el script
def executeScript():
  logging.info(f' {datetime.datetime.now() }: Se esta ejecutando la instalacion del servicio')
  if(label1.cget("text")!="" and Textbox.get()!="" and var.get()!=0): 
    if(installService(Textbox.get(),label1.cget("text"),var.get(),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="El servicio se instalo correctamente")
    else: MessageBox.showerror("Error","El servicio no se ha instalado, valide que se este ejecutando como administrador")
  if(label1.cget("text")==""): MessageBox.showerror("Error","Debe de haber seleccionado El servicio a instalar")
  if(Textbox.get()==""): MessageBox.showerror("Error","Debe de ingresar un nombre para su servicio a crear")
  if(var.get()==0):MessageBox.showerror("Error","Debe seleccionar si el servicio iniciara en automatico o manual")