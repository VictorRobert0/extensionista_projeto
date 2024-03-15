import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
import bcrypt

#Inicio do projeto Extensionista de reconhecimento facial 14/3/2024

root = ctk.CTk()
root.title('Action Prol - System')
root.geometry('700x500')
root.resizable(False,False)
root.config(bg='#DCDCDC')

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    





#----------------------------------------------------------------------------------------------------------------
# BANCO DE DADOS | TABELA DE USUÁRIOS
#----------------------------------------------------------------------------------------------------------------
conn = sqlite3.connect('./DB/bancodedados.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS users (
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   rg TEXT NOT NULL,
                   password TEXT NOT NULL )''')
#----------------------------------------------------------------------------------------------------------------
# VALIDANDO O FORMULÁRIO DE CADASTRO | TELA DE CADASTRO
#----------------------------------------------------------------------------------------------------------------
def validar_formulario():
    username = username_cadastro.get()
    email = email_cadastro.get()
    rg = rg_cadastro.get()
    password = password_cadastro.get()

    if username != '' and email != '' and password != '' and rg != '':
        cursor.execute(
            'SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('ERRO', 'Usuário já existe.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?,?,?,?)',[username, email, rg, hashed_password])
            conn.commit()
            messagebox.showinfo('SUCESSO', 'Cadastro realizado com sucesso.')
    else:
        messagebox.showerror('ERRO', 'Por favor, insira todos os dados.')
#----------------------------------------------------------------------------------------------------------------       
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
# TELA DE CADASTRO | TODOS OS ELEMENTOS DA TELA DE CADASTRO
#----------------------------------------------------------------------------------------------------------------
def tela_cadastro():
    global username_cadastro
    global email_cadastro
    global rg_cadastro
    global password_cadastro
    
    root.destroy()
    
    screen_register = ctk.CTk()
    screen_register.geometry('1200x630')
    screen_register.title('Action Prol - System | Register')
    screen_register.resizable(False, False)
    
    # ------------------------------------------------------------------------
    
    canvas = Canvas(screen_register,  bd=0, highlightthickness=0)
    canvas.pack()
    image_register = PhotoImage(file='./img/20230228_migracao_saopaulo.png')
    image_label1 = Label(screen_register, image=image_register, width=1200, height=630,)
    image_label1.place(relx=0.0, rely=0.0)
    root.image_register = image_register
    
    #------------------------------------------------------------------------
    
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

    
    
    #----------------------------------------------------------------------------------------------------------------
    #BOTÃO REGISTRO | FUNÇÃO DE CADASTRO ESTÁ AQUI
    #----------------------------------------------------------------------------------------------------------------
    validar_cadastro = ctk.CTkButton(screen_register,command=validar_formulario,text_color='#fff', text='CADASTRAR-SE',
                                     fg_color='#778899', hover_color='#005180', bg_color='#fff', cursor='hand2', corner_radius=5, width=120, anchor=CENTER)
    validar_cadastro.place(relx=0.35, rely=0.70)
    
    
    
    
    screen_register.mainloop()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#LOGIN IMAGE (recursos do TkInter) 
#----------------------------------------------------------------------------------------------------------------
canvas = Canvas(root,  bd=0, highlightthickness=0)
canvas.pack()
image_login = PhotoImage(file='./img/vidadeimigrante.png')
image_label = Label(root, image=image_login, width=500, height=500,bg="#DCDCDC")
image_label.place(relx=0.15, rely=0.0)
root.image_login = image_login
#----------------------------------------------------------------------------------------------------------------
#INPUTS LOGIN | APENAS ELEMENTOS DA TELA DE LOGIN
#----------------------------------------------------------------------------------------------------------------
input_login = ctk.CTkEntry(master=root,placeholder_text="Digite seu usuário", width=200)
input_password = ctk.CTkEntry(master=root, placeholder_text="Digite sua senha", width=200)

#----------------------------------------------------------------------------------------------------------------
#INPUTS LOGIN POSIÇÃO
#----------------------------------------------------------------------------------------------------------------
input_login.place(relx=0.32, rely=0.4)
input_password.place(relx= 0.32, rely= 0.5)
#----------------------------------------------------------------------------------------------------------------
#BOTÕES
#----------------------------------------------------------------------------------------------------------------
login_button = ctk.CTkButton(master=root, text="Acessar", width=200)
to_register = ctk.CTkButton(master=root, text="REGISTRAR-SE", width=200, command=tela_cadastro)
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#BOTÕES POSIÇÃO | ELEMENTOS DA TELA DE LOGIN
#----------------------------------------------------------------------------------------------------------------
to_register.place(relx= 0.32, rely=0.75)
login_button.place(relx=0.32, rely= 0.6)
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

root.mainloop()

