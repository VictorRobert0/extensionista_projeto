import customtkinter as ctk
from tkinter import *

#Inicio do projeto Extensionista de reconhecimento facial 14/3/2024

root = ctk.CTk()
root.title('Action Prol - System')
root.geometry('700x500')
root.resizable(False,False)
root.config(bg='#DCDCDC')

#----------------------------------------------------------------------------------------------------------------
# TELA DE REGISTRO

def tela_cadastro():
    root.destroy()
    
    screen_register = ctk.CTk()
    screen_register.geometry('700x500')
    screen_register.title('Action Prol - System | Register')
    screen_register.resizable(False, False)
    
    # ------------------------------------------------------------------------

    username_cadastro = ctk.CTkEntry(screen_register, placeholder_text='Usuário', placeholder_text_color='#C0C0C0',
                                     text_color='black', fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    username_cadastro.place(relx=0.35 , rely=0.3)
    username_cadastro.focus()

    # ------------------------------------------------------------------------

    email_cadastro = ctk.CTkEntry(screen_register, placeholder_text='Email', placeholder_text_color='#C0C0C0',
                                  text_color='black', fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    email_cadastro.place(relx=0.35, rely=0.4)

    # ------------------------------------------------------------------------

    rg_cadastro = ctk.CTkEntry(screen_register, placeholder_text='RG', placeholder_text_color='#C0C0C0', text_color='black',
                               fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    rg_cadastro.place(relx=0.35, rely=0.5)

    # ------------------------------------------------------------------------

    password_cadastro = ctk.CTkEntry(screen_register, show='*', placeholder_text='Senha', placeholder_text_color='#C0C0C0',
                                     text_color='black', fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    password_cadastro.place(relx=0.35, rely=0.60)

    # ------------------------------------------------------------------------
    
    #BOTÃO REGISTRO
    validar_cadastro = ctk.CTkButton(screen_register,  text_color='#fff', text='CADASTRAR-SE',
                                     fg_color='#778899', hover_color='#005180', bg_color='#fff', cursor='hand2', corner_radius=5, width=120, anchor=CENTER)
    validar_cadastro.place(relx=0.35, rely=0.70)
    
    
    
    screen_register.mainloop()



#----------------------------------------------------------------------------------------------------------------

#INPUTS LOGIN

input_login = ctk.CTkEntry(master=root,placeholder_text="Digite seu usuário", width=200)
input_password = ctk.CTkEntry(master=root, placeholder_text="Digite sua senha", width=200)
#----------------------------------------------------------------------------------------------------------------

#LOGIN IMAGE (recursos do TkInter)

canvas = Canvas(root,  bd=0, highlightthickness=0)
canvas.pack()
image_login = PhotoImage(file='./img/user-login-icon-29.png')
image_label = Label(root, image=image_login, width=377, height=270,bg="#DCDCDC")
image_label.place(relx=0.23, rely=0.0)
root.image_login = image_login


#----------------------------------------------------------------------------------------------------------------
#BOTÕES

login_button = ctk.CTkButton(master=root, text="Acessar", width=200)

to_register = ctk.CTkButton(master=root, text="REGISTRAR-SE", width=200, command=tela_cadastro)

#----------------------------------------------------------------------------------------------------------------

#Button position
to_register.place(relx= 0.32, rely=0.85)
login_button.place(relx=0.32, rely= 0.75)


#----------------------------------------------------------------------------------------------------------------
#Inputs position

input_login.place(relx=0.32, rely=0.55)
input_password.place(relx= 0.32, rely= 0.65)

root.mainloop()

