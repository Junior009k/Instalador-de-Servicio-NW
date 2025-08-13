from FrontEnd.VariableDeterminadas import *
from tkinter import simpledialog
#Frame 11 Mail
varMail=IntVar()
R1Mail = Radiobutton(frame11,text="Sin SSL", variable=varMail,width=5 ,value=0, bg=colorframe1)
R2Mail = Radiobutton(frame11, text="Con SSL", variable=varMail,width=5, value=1,bg=colorframe1)
labelMailsrv = tk.Label(frame11,text="Servidor",bg=colorframe3)
TextboxMailsrv = tk.Entry(frame11)
labelMailPort = tk.Label(frame11,text="Puerto",bg=colorframe3)
TextboxMailPort = tk.Entry(frame11)
labelMailSenderAccount = tk.Label(frame11,text="Correo",bg=colorframe3)
TextboxMailSenderAccount = tk.Entry(frame11)
labelMailPassword= tk.Label(frame11,text="Password",bg=colorframe3)
TextboxMailPassword = tk.Entry(frame11)
button4 = tk.Button(frame11,width=16,height=1, text="Diagnosticar", command=lambda: diagnoseMailServer()).place(x="280",y="180")
#place
R1Mail.place(x=342,y=80)
R2Mail.place(x=342,y=100)
TextboxMailsrv.place(x=110,y=120)
TextboxMailPort.place(x=110,y=150)
TextboxMailSenderAccount.place(x=110,y=180)
TextboxMailPassword.place(x=110,y=210)
labelMailsrv.place(x=40,y=120)
labelMailPort.place(x=40,y=150)
labelMailSenderAccount.place(x=40,y=180)
labelMailPassword.place(x=40,y=210)

#esta funcion se encarga de modificar el correo
def modifyMail():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar el MailServer')
  bandera=validateLabel(label11,logging,MessageBox,"el MailServer","la ruta",datetime)
  if(bandera!=False):
    logging.info(f' {datetime.datetime.now() }: Se comienza a modificar el mailserver')
    configurarMail(label11.cget("text"),varMail.get(),TextboxMailsrv.get(),TextboxMailPort.get(),TextboxMailSenderAccount.get(),TextboxMailPassword.get(),logging, datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El correo se configuro  correctamente")   
  
#esta funcion se encarga de modificar el correo
def diagnoseMailServer():
  logging.info(f' {datetime.datetime.now() }: Se comienza a diagnosticar el MailServer')
  destinatario = simpledialog.askstring("Input", "Ingrese el correo del destinatario", parent=frame)
  bandera=validateField(TextboxMailsrv,logging,MessageBox,"MailServer","del servidor",datetime)
  bandera=bandera*validateField(TextboxMailPort,logging,MessageBox,"MailServer","del puerto",datetime)
  bandera=bandera*validateField(TextboxMailSenderAccount,logging,MessageBox,"MailServer","del correo",datetime)
  bandera=bandera*validateField(TextboxMailPassword,logging,MessageBox,"MailServer","del sitio de e-Flow",datetime)
  if(bandera!=False):
    logging.info(f' {datetime.datetime.now() }: Se comienza a Diagnosticar el mail server')
    resultTNC=TNC(TextboxMailsrv.get(),TextboxMailPort.get(),logging, datetime)
    if(re.findall("False",resultTNC)==[]):
      sendEmail(TextboxMailsrv.get(),TextboxMailPort.get(),TextboxMailSenderAccount.get(),TextboxMailPassword.get(),destinatario,logging, datetime)
      tk.messagebox.showinfo(title="Felicidades", message="El correo se configuro  correctamente")   
    else:
      tk.messagebox.showerror("Error",f"No se puede conectar al server {TextboxMailsrv.get()} por el puerto {TextboxMailPort.get()}")
        
   