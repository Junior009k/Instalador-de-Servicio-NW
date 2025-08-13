from FrontEnd.VariableDeterminadas import *


#esta funcion se encarga de abrir el directorio y validar que el archivo seleccionado sea el servicio
def Examine(p):
  logging.info(f' {datetime.datetime.now() }: Se esta examinando el archivo')
  path = tkinter.filedialog.askopenfilename()
  if(p==1 and validateService(path.lower(),"sidesys.services.applicationservice.exe","middleware","bin")):label1.config(text=path) 
  #nodo xml
  if(p==2 and validateService(path.lower(),".xml","FrontEnd","view_configuration")):
    label16.config(text=path) 
    TextboxNodeFont.delete(0, tk.END)
    TextboxNodeVoice.delete(0, tk.END)
    TextboxNodeHeaderColor.delete(0, tk.END)
    TextboxNodeFooterColor.delete(0, tk.END)
    TextboxNodeNumberSize.delete(0, tk.END)
    TextboxNodeLang.delete(0, tk.END)
    TextboxNodeW.delete(0, tk.END)
    TextboxNodeUW.delete(0, tk.END)
    TextboxNodeNumberTableHeaderColor.delete(0, tk.END)
    TextboxNodeNumberTableHeaderSize.delete(0, tk.END)
    TextboxNodeNumberTableHeaderfontColor.delete(0, tk.END)
    TextboxNodeBannerBackgroundColor.delete(0, tk.END)
    TextboxNodeBannerFontColor.delete(0, tk.END)
    
    TextboxNodeFont.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','fontFamily":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeVoice.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','voice":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeHeaderColor.insert(0, IdentifyJSON(path,'"header":{[\S|\s]+"logo"','backgroundColor":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeFooterColor.insert(0, IdentifyJSON(path,'"footer":{[\S|\s]+"alignContent"','backgroundColor":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberSize.insert(0, IdentifyJSON(path,'"numbersTableBody":{[\S|\s]+"columnTask"','fontSize":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeLang.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','lang":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeW.insert(0, IdentifyJSON(path,'"header":{[\S|\s]+"text"','width":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeUW.insert(0, IdentifyJSON(path,'"header":{[\S|\s]+"text"','unitWidth":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberTableHeaderColor.insert(0, IdentifyJSON(path,'"numbersTableHeclader":{[\S|\s]+"columnTask"','backgroundColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberTableHeaderSize.insert(0, IdentifyJSON(path,'"numbersTableHeader":{[\S|\s]+"columnTask"','fontSize":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberTableHeaderfontColor.insert(0, IdentifyJSON(path,'"numbersTableHeader":{[\S|\s]+"columnTask"','fontColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeBannerBackgroundColor.insert(0, IdentifyJSON(path,'"banner":{[\S|\s]+"fontColor"','backgroundColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeBannerFontColor.insert(0, IdentifyJSON(path,'"banner":{[\S|\s]+}','fontColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))

#esta funcion se encarga de modificar el nodo xml
def modifyNode():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar el nodo')
  if( validateDirectory(label16.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label16.cget("text"),"FrontEnd",logging,datetime)):label16.config(text="") 
  bandera=validateLabel(label16,logging,MessageBox,"el Web sevice de citas","tiene que estar en la carpeta del aplicativo",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Web sevice de citas')
    configurarNodo(label16.cget("text"),TextboxNodeFont.get(),TextboxNodeVoice.get(),TextboxNodeHeaderColor.get(),TextboxNodeFooterColor.get(), TextboxNodeNumberSize.get(),TextboxNodeLang.get(),TextboxNodeW.get(),TextboxNodeUW.get(),TextboxNodeNumberTableHeaderColor.get(),TextboxNodeNumberTableHeaderSize.get(),TextboxNodeNumberTableHeaderfontColor.get(),TextboxNodeBannerBackgroundColor.get(),TextboxNodeBannerFontColor.get(),logging,datetime)    
