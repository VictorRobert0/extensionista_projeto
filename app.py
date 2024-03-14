import customtkinter as ctk

#Inicio do projeto Extensionista de reconhecimento facial 14/3/2024

root = ctk.CTk()
root.title('Action Prol - System')
root.geometry('700x500')

#----------------------------------------------------------------------------------------------------------------
#INPUTS LOGIN

input_login = ctk.CTkEntry(master=root,placeholder_text="Digite seu usuário", width=200)
input_password = ctk.CTkEntry(master=root, placeholder_text="Digite sua senha", width=200)
#----------------------------------------------------------------------------------------------------------------

#BOTÕES

login_button = ctk.CTkButton(master=root, text="Acessar", width=200)

to_register = ctk.CTkButton(master=root, text="REGISTRAR-SE", width=210)

#----------------------------------------------------------------------------------------------------------------

#Button position
to_register.place(relx= 0.70, rely=0.8)
login_button.place(relx=0.38, rely= 0.5)


#----------------------------------------------------------------------------------------------------------------
#Inputs position

input_login.place(relx=0.38, rely=0.3)
input_password.place(relx= 0.38, rely= 0.4)

root.mainloop()
