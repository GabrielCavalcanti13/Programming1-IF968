'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Gabriel Cavalcati (gcm2)
Email:	gcm2@cin.ufpe.br
Data:	13/11/2017

Copyright(c) 2017 Gabriel Cavalcanti de Melo
Projeto de programacao 1. 2017.2 prof: Fernando Neto
'''
from tkinter import *
from tkinter import messagebox
import funcoes
from datetime import datetime
from functools import partial
#_________________________________JANELA LOGIN_________________________________
def janelaLogin():
    janela=Tk()
    janela.title("Login")
    janela["bg"]="gray6"
    
    lb1=Label(janela, text="Login:",bg="gray6", fg="white")
    lb2=Label(janela, text="Senha:",bg="gray6", fg="white")
    ed1=Entry(janela)
    ed2=Entry(janela, show="*")
    bt=Button(janela, text="Confirmar")
    bt["command"] = partial(confirmarLogin, listaComando, janela, ed1, ed2)
    photo=PhotoImage(file="images/login.png")
    tigre=Label(janela, image=photo, bg="gray6")
    
    lb1.place(x=10, y=15)
    lb2.place(x=10, y=75)
    ed1.place(x=10, y=45)
    ed2.place(x=10, y=105)
    bt.place(x=10, y=135)
    tigre.place(x=100, y=0)
    
    janela.geometry("420x360+300+200")
    janela.mainloop()
#-------------------------------------------------
def confirmarLogin(lista, window, entry1, entry2):
    '''Verifica se o login digitado esta presente no dicionario de usuarios
se estiver, salva numa variavel para ser usado tanto no log quando para ver
qual o nivel de acesso do usuario. ex:(Fernandoneto123, true)'''
    acessoLiberado=False
    usuarioLogado=entry1.get()
    if entry1.get() in funcoes.bancoUsuarios:
        if funcoes.bancoUsuarios[entry1.get()][0]==entry2.get():
            acessoLiberado=True
    lista.append((usuarioLogado,acessoLiberado))
    window.destroy()
#_____________________________________JANELA PRINCIPAL___________________________________________
def janelaSuper():
    global mainJanela
    mainJanela=Tk()
    mainJanela.title("MainJanela")
    mainJanela["bg"]="Green4"
    
    btRemoverUsuario=Button(mainJanela, text="      Remover Usuario     ", command=removerUser)
    btCadastroUsuario=Button(mainJanela, text="     Cadastrar Usuario     ", command=cadastroUsuario)
    btAlterarNivel=Button(mainJanela, text="Alterar nivel do usuario", command=alterarNivel)
    btCadastroEle=Button(mainJanela, text="    Cadastrar Animais     ", command=cadastroElemento)
    btRemocao=Button(mainJanela, text="     Remover Animal      ", command=removerElemento)
    btBusca=Button(mainJanela, text="     Buscar Animal          ", command=searchAnimal)
    btAtualizar=Button(mainJanela, text="     Atualizar Dados        ", command=updateAnimal)
    btOrdenar=Button(mainJanela, text="    Ordenar Animais       ",command=ordenacao)
    photo=PhotoImage(file="images/orangotando.gif")
    photo4=PhotoImage(file="images/tigre2.png")
    tigre=Label(mainJanela, image=photo4, bg="Green4")
    orangotango=Label(mainJanela, image=photo, bg="Green4")
    btLogout=Button(mainJanela, text=" Logout ", command=logout)
    title=Label(mainJanela, text="Sherikan's Wildlife\n Foundation",font=("fixedsys", "38"), bg="Green4", fg="white")
    
    
    btCadastroUsuario["bg"]="green yellow"
    btAlterarNivel["bg"]="green yellow"
    btCadastroEle["bg"]="green yellow"
    btRemocao["bg"]="green yellow"
    btBusca["bg"]="green yellow"
    btAtualizar["bg"]="green yellow"
    btOrdenar["bg"]="green yellow"
    btLogout["bg"]="green yellow"
    btRemoverUsuario["bg"]="green yellow"

    tigre.place(x=50, y=190)            
    btCadastroUsuario.place(x=380, y=215)
    btAlterarNivel.place(x=380, y=245)
    btCadastroEle.place(x=380, y=275)
    btRemocao.place(x=380, y=305)
    btBusca.place(x=380, y=335)
    btAtualizar.place(x=380, y=365)
    btOrdenar.place(x=380, y=395)
    btRemoverUsuario.place(x=380, y=425)
    orangotango.place(x=630, y=0)
    btLogout.place(x=820, y=530)
    title.place(x=45, y=30)
    
         
    mainJanela.geometry("900x600+100+70")
    mainJanela.mainloop()
#---------------------------------------------------------------------------------------
def janelaGerente():
    global mainJanela
    mainJanela=Tk()
    mainJanela.title("MainJanela")
    mainJanela["bg"]="Green4"
    
    btRemoverUsuario=Button(mainJanela, text="      Remover Usuario     ", command=removerUser)
    btCadastroUsuario=Button(mainJanela, text="     Cadastrar Usuario     ", command=cadastroUsuario)
    btCadastroEle=Button(mainJanela, text="    Cadastrar Animais     ", command=cadastroElemento)
    btRemocao=Button(mainJanela, text="     Remover Animal      ", command=removerElemento)
    btBusca=Button(mainJanela, text="     Buscar Animal          ", command=searchAnimal)
    btAtualizar=Button(mainJanela, text="     Atualizar Dados        ", command=updateAnimal)
    btOrdenar=Button(mainJanela, text="    Ordenar Animais       ",command=ordenacao)
    photo=PhotoImage(file="images/orangotando.gif")
    photo4=PhotoImage(file="images/tigre2.png")
    tigre=Label(mainJanela, image=photo4, bg="Green4")
    orangotango=Label(mainJanela, image=photo, bg="Green4")
    btLogout=Button(mainJanela, text=" Logout ", command=logout)
    title=Label(mainJanela, text="Sherikan's Wildlife\n Foundation",font=("fixedsys", "38"), bg="Green4", fg="white")
    
    
    btCadastroUsuario["bg"]="green yellow"
    btCadastroEle["bg"]="green yellow"
    btRemocao["bg"]="green yellow"
    btBusca["bg"]="green yellow"
    btAtualizar["bg"]="green yellow"
    btOrdenar["bg"]="green yellow"
    btLogout["bg"]="green yellow"
    btRemoverUsuario["bg"]="green yellow"

    tigre.place(x=50, y=190)            
    btCadastroUsuario.place(x=380, y=215)
    btCadastroEle.place(x=380, y=245)
    btRemocao.place(x=380, y=275)
    btBusca.place(x=380, y=305)
    btAtualizar.place(x=380, y=335)
    btOrdenar.place(x=380, y=365)
    btRemoverUsuario.place(x=380, y=395)
    orangotango.place(x=630, y=0)
    btLogout.place(x=820, y=530)
    title.place(x=45, y=30)
    
         
    mainJanela.geometry("900x600+100+70")
    mainJanela.mainloop()
#---------------------------------------------------------------------------------------
def janelaTecnico():
    global mainJanela
    mainJanela=Tk()
    mainJanela.title("MainJanela")
    mainJanela["bg"]="Green4"
    
    
    btCadastroEle=Button(mainJanela, text="    Cadastrar Animais     ", command=cadastroElemento)
    btBusca=Button(mainJanela, text="     Buscar Animal          ", command=searchAnimal)
    photo=PhotoImage(file="images/orangotando.gif")
    photo4=PhotoImage(file="images/tigre2.png")
    tigre=Label(mainJanela, image=photo4, bg="Green4")
    orangotango=Label(mainJanela, image=photo, bg="Green4")
    btLogout=Button(mainJanela, text=" Logout ", command=logout)
    title=Label(mainJanela, text="Sherikan's Wildlife\n Foundation",font=("fixedsys", "38"), bg="Green4", fg="white")
    
    btCadastroEle["bg"]="green yellow"
    btBusca["bg"]="green yellow"
    btLogout["bg"]="green yellow"

    tigre.place(x=50, y=190)            
    btCadastroEle.place(x=380, y=275)
    btBusca.place(x=380, y=305)
    orangotango.place(x=630, y=0)
    btLogout.place(x=820, y=530)
    title.place(x=45, y=30)
    
         
    mainJanela.geometry("900x600+100+70")
    mainJanela.mainloop()
#--------------------------------------------------------------------------------------
def janelaEstagiario():
    global mainJanela
    mainJanela=Tk()
    mainJanela.title("MainJanela")
    mainJanela["bg"]="Green4"
    
    
    btBusca=Button(mainJanela, text="     Buscar Animal          ", command=searchAnimal)
    photo=PhotoImage(file="images/orangotando.gif")
    photo4=PhotoImage(file="images/tigre2.png")
    tigre=Label(mainJanela, image=photo4, bg="Green4")
    orangotango=Label(mainJanela, image=photo, bg="Green4")
    btLogout=Button(mainJanela, text=" Logout ", command=logout)
    title=Label(mainJanela, text="Sherikan's Wildlife\n Foundation",font=("fixedsys", "38"), bg="Green4", fg="white")
    
    btBusca["bg"]="green yellow"
    btLogout["bg"]="green yellow"

    tigre.place(x=50, y=190)            
    btBusca.place(x=380, y=305)
    orangotango.place(x=630, y=0)
    btLogout.place(x=820, y=530)
    title.place(x=45, y=30)
    
         
    mainJanela.geometry("900x600+100+70")
    mainJanela.mainloop()
#______________________________________CADASTRAR USUARIO________________________________
def cadastroUsuario():
    global edLogin
    global edSenha
    global janelaCadastro
    janelaCadastro=Tk()
    lbLogin=Label(janelaCadastro, text="Digite o Login")
    lbSenha=Label(janelaCadastro, text="Digite a Senha")
    edLogin=Entry(janelaCadastro)
    edSenha=Entry(janelaCadastro, show="*")
    btCadastrar=Button(janelaCadastro, text="Cadastrar",command=confirmarCadastro)
    lbLogin.grid(row=0, column=0)
    lbSenha.grid(row=1, column=0)
    edLogin.grid(row=0, column=1)
    edSenha.grid(row=1, column=1)
    btCadastrar.grid(row=2, column=1)
    janelaCadastro.geometry("200x100+500+500")
    janelaCadastro.mainloop()
#---------------------------------------------------------------------------------------
def confirmarCadastro():
    '''Cadastra o usuario e senha mais o nivel de acesso 4(estagiario) no
dicionario de ususarios'''
    if edLogin.get() in funcoes.bancoUsuarios:
        messagebox.showerror("ERROR","Nome de login já existente")
    else:
        lbUsuarioCadastrado=Label(janelaCadastro, text="Usuario Cadastrado")
        lbUsuarioCadastrado.place(x=5,y=50)
        funcoes.bancoUsuarios[edLogin.get()]=(edSenha.get(),"4")
        edLogin.delete(0,END)
        edSenha.delete(0, END)
    funcoes.salvarLog(usuarioLogado, "cadastrou usuario", log)
#__________________________________REMOVER USUARIO_____________________________________
def removerUser():
    global edRemoverUser
    janelaRemoveUser=Tk()
    janelaRemoveUser.title("Remover usuario")
    lbPergunta=Label(janelaRemoveUser, text="Digite o login")
    edRemoverUser=Entry(janelaRemoveUser)
    btRemoverUser=Button(janelaRemoveUser, text="Remover", command=confirmRemoveUser)

    lbPergunta.grid(row=0, column=0)
    edRemoverUser.grid(row=0, column=1)
    btRemoverUser.place(x=40, y=30)

    janelaRemoveUser.geometry("200x60+500+300")
    janelaRemoveUser.mainloop()
#--------------------------------------------------------------------------------------
def confirmRemoveUser():
    if edRemoverUser.get() in funcoes.bancoUsuarios:
        funcoes.bancoUsuarios.pop(edRemoverUser.get())
        messagebox.showinfo("Remocao", "Usuario removido com sucesso!")
        edRemoverUser.delete(0,END)
        funcoes.salvarLog(usuarioLogado, "Removeu usuario", log)
    else:
        messagebox.showerror("Remocao", "Usuario nao existenteno banco de dados")
        edRemoverUser.delete(0,END)
#__________________________________ALTERAR NIVEL________________________________________
def alterarNivel():
    global changeUser
    global changeLevel
    janelaNivel=Tk()
    lbUser=Label(janelaNivel, text="Digite o Usuario")
    lbLevel=Label(janelaNivel, text="Novo Nivel de acesso")
    changeUser=Entry(janelaNivel)
    changeLevel=Entry(janelaNivel)
    btConfirmar=Button(janelaNivel,text="Confirmar",command=confirmarAlteracao)
    lbUser.place(x=0,y=0)
    changeUser.place(x=0,y=20)
    lbLevel.place(x=0, y=40)
    changeLevel.place(x=0, y=60)
    btConfirmar.place(x=20,y=85)
    janelaNivel.geometry("150x110+500+500")
    janelaNivel.mainloop()
#---------------------------------------------------------------------------------------
def confirmarAlteracao():
    '''Se existir o ussuario no banco de da dados o nivel de acesso mudara. 1 para super
usuario, 2 para gerente. 3 tecnico e 4 para estagiario. sera escrita outra tupla'''
    if changeUser.get() in funcoes.bancoUsuarios:
        senha=funcoes.bancoUsuarios[changeUser.get()][0]
        if changeLevel.get()=="estagiaro" or changeLevel=="Estagiario":
            funcoes.bancoUsuarios[changeUser.get()]=(senha,"4")
        elif changeLevel.get()=="tecnico" or changeLevel=="Tecnico":
            funcoes.bancoUsuarios[changeUser.get()]=(senha,"3")
        elif changeLevel.get()=="gerente" or changeLevel=="Gerente":
            funcoes.bancoUsuarios[changeUser.get()]=(senha,"2")
        elif changeLevel.get()=="super" or changeLevel=="Super":
            funcoes.bancoUsuarios[changeUser.get()]=(senha,"1")
        funcoes.salvarLog(usuarioLogado, "alterou nivel de acesso", log)
        changeUser.delete(0, END)
        changeLevel.delete(0, END)
        messagebox.showinfo("Nivel alterado", "Nivel alterado com sucesso")
    else:
        messagebox.showerror("ERROR","Usuario nao encontrado")
#_____________________CADASTRAR ELEMENTO___________________
def cadastroElemento():
    global especie
    global idade
    global peso
    global sexo
    global janelaElementos
    mainJanela.destroy()
    janelaElementos=Tk()
    janelaElementos["bg"]="Green4"
    
    lbLinha=Label(janelaElementos, text="____________________________", bg="green4", fg="white")
    lbTitulo=Label(janelaElementos, text="Digite os dados do animal", bg="green4", fg="white")
    photoM=PhotoImage(file="images/1057a616f01ac7e4de3ea8e706ec08bc.png")
    macaco=Label(janelaElementos, image=photoM, bg="green4")
    lbEspecie=Label(janelaElementos, text="Especie", bg="green4", fg="white")
    lbIdade=Label(janelaElementos, text="Idade(Anos)", bg="green4", fg="white")
    lbPeso=Label(janelaElementos, text="Peso/Kg", bg="green4", fg="white")
    lbSexo=Label(janelaElementos, text="Sexo(M/F)", bg="green4", fg="white")
    especie=Entry(janelaElementos)
    idade=Entry(janelaElementos)
    peso=Entry(janelaElementos)
    sexo=Entry(janelaElementos)
    btConfirmarElemento=Button(janelaElementos,text="Cadastrar", command=confirmarAnimal)
    btBack=Button(janelaElementos, text="voltar", command=backToMain)
    title=Label(janelaElementos, text="Cadastro de\nAnimais",font=("fixedsys", "32"), bg="Green4", fg="white")

    title.place(x=15, y=30)
    macaco.place(x=250, y=20)
    lbLinha.place(x=35, y=170)
    lbTitulo.place(x=35, y=165)
    lbEspecie.place(x=35, y=200)
    lbIdade.place(x=35, y=225)
    lbPeso.place(x=35, y=250)
    lbSexo.place(x=35, y=275)
    especie.place(x=105, y=200)
    idade.place(x=105, y=225)
    peso.place(x=105, y=250)
    sexo.place(x=105, y=275)
    btConfirmarElemento.place(x=150, y=305)
    btBack.place(x=500, y=15)
    
    janelaElementos.geometry("590x380+100+70")
    janelaElementos.mainloop()

#-------------------------------------------------------------------------------
def backToMain():
    janelaElementos.destroy()
    if funcoes.bancoUsuarios[listaComando[0][0]][1]=="1":
        janelaSuper()
    elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="2":
        janelaGerente()
    elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="3":
        janelaTecnico()
    elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="4":
        janelaEstagiario()
#_--------------------------------------------------------------
def backToMain2():
    janelaBusca.destroy()
    if funcoes.bancoUsuarios[listaComando[0][0]][1]=="1":
        janelaSuper()
    elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="2":
        janelaGerente()
    elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="3":
        janelaTecnico()
    elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="4":
        janelaEstagiario()
    
    
#-----------------------------------------------------------
def confirmarAnimal():
    '''Se a especie for diferente de string vazia eh adicionado no dicionario de elementos com chave
sendo o contador de Id e o valor sendo uma tupla com especie, idade, peso e sexo'''
    if especie.get()!="":
        funcoes.bancoElementos[str(funcoes.contadorId)]=(especie.get(),idade.get(),peso.get(),sexo.get())
        confirmacaoCadastro=Label(janelaElementos, text="Animal Cadastrado", bg="green4", fg="white")
        confirmacaoCadastro.place(x=20, y=330)
        especie.delete(0, END)
        idade.delete(0, END)
        peso.delete(0, END)
        sexo.delete(0, END)
        funcoes.contadorId+=1
        funcoes.salvarLog(usuarioLogado, "cadastrou elemento", log)
#______________________REMOVER ELEMENTO_____________________
def removerElemento():
    global edRemover
    global janelaRemover
    janelaRemover=Tk()
    lbLinha=Label(janelaRemover, text="________________________________________________")
    lbTitulo=Label(janelaRemover, text="DIGITE O ID DO ANIMAL Q DESEJA REMOVER")
    lbId=Label(janelaRemover, text="ID Animal")
    edRemover=Entry(janelaRemover)
    btConfirmar=Button(janelaRemover, text="Remover",command=askRemocao)
    lbLinha.place(x=3,y=10)
    lbTitulo.place(x=5, y=5)
    lbId.place(x=15, y=30)
    edRemover.place(x=85, y=30)
    btConfirmar.place(x=150, y=57)
    janelaRemover.geometry("250x85+500+300")
    janelaRemover.mainloop()
#-----------------------------------------------------------
def askRemocao():
    global janelaPergunta
    if edRemover.get() in funcoes.bancoElementos:
        janelaPergunta=Tk()
        lbLinha=Label(janelaPergunta, text="____________________________________")
        lbPergunta=Label(janelaPergunta, text="Deseja Remover:")
        lbId=Label(janelaPergunta, text="ID:           "+edRemover.get())
        lbEspecie=Label(janelaPergunta, text="Especie: "+funcoes.bancoElementos[edRemover.get()][0])
        lbIdade=Label(janelaPergunta, text="Idade:    "+funcoes.bancoElementos[edRemover.get()][1]+" anos")
        lbPeso=Label(janelaPergunta, text="Peso:     "+funcoes.bancoElementos[edRemover.get()][2]+" Kg")
        lbSexo=Label(janelaPergunta, text="Sexo:      "+funcoes.bancoElementos[edRemover.get()][3])
        btConfirmarYes=Button(janelaPergunta, text="     SIM     ", command=confirmRemove)
        btCOnfirmarNo=Button(janelaPergunta, text="    NAO    ", command=notConfirmRemove)
        lbLinha.place(x=5, y=15)
        lbPergunta.place(x=5, y=5)
        lbId.place(x=5, y=35)
        lbEspecie.place(x=5, y=50)
        lbIdade.place(x=5, y=65)
        lbPeso.place(x=5, y=80)
        lbSexo.place(x=5, y=95)
        btConfirmarYes.place(x=70, y=115)
        btCOnfirmarNo.place(x=5, y=115)
        janelaPergunta.geometry("150x150+500+300")
        janelaPergunta.mainloop()
    else:
        messagebox.showinfo("ERROR","Animal nao encontrado!")
#-------------------------------------------------------------
def confirmRemove():
    '''se confirmar o dejeso de remover. o item eh deletado do dicionario. a janela de pergunta eh
fechada.'''
    del funcoes.bancoElementos[edRemover.get()]
    messagebox.showinfo("Remover","Animal removido com sucesso")
    janelaPergunta.destroy()
    edRemover.delete(0, END)
    funcoes.salvarLog(usuarioLogado, "Removeu elemento", log)
#------------------------------------------------------------
def notConfirmRemove():
    janelaPergunta.destroy()
    edRemover.delete(0, END)
#________________________BUSCAR ELEMENTO_______________________###############
def searchAnimal():
    global edBuscar
    global janelaBusca

    mainJanela.destroy()
    janelaBusca=Tk()
    lbLinha=Label(janelaBusca, text="___________________________________", bg="green4", fg="white")
    janelaBusca["bg"]="green4"
    janelaBusca.title("Busca Elementos")

    title=Label(janelaBusca, text="Busca de\nAnimais",font=("fixedsys", "32"), bg="green4", fg="white")
    lbTitulo=Label(janelaBusca, text="DIGITE O ID DO ANIMAL", bg="green4", fg="white")
    lbId=Label(janelaBusca, text="ID", bg="green4", fg="white")
    edBuscar=Entry(janelaBusca)
    btConfirmar=Button(janelaBusca, text="Buscar",command=confirmSearch)
    photo=PhotoImage(file="images/PNG - arara azul.png")
    arara=Label(janelaBusca, image=photo, bg="green4")
    btBack=Button(janelaBusca, text="voltar", command=backToMain2)

    title.place(x=15, y=30)
    lbTitulo.place(x=25, y=173)
    lbId.place(x=30, y=195)
    edBuscar.place(x=60, y=195)
    lbLinha.place(x=20, y=233)
    btConfirmar.place(x=120, y=220)
    arara.place(x=290, y=50)
    btBack.place(x=500, y=15)
    
    janelaBusca.geometry("590x380+100+70")
    janelaBusca.mainloop()
#--------------------------------------------------------------
def confirmSearch():
    '''se estiver no dicionario mostrara os dados do animal. se nao mensagem de erro eh emitida '''
    if edBuscar.get() in funcoes.bancoElementos:
        lbId=Label(janelaBusca, text="ID:           "+edBuscar.get()+"                 ", bg="green4", fg="white")
        lbEspecie=Label(janelaBusca, text="Especie: "+funcoes.bancoElementos[edBuscar.get()][0]+"                  ", bg="green4", fg="white")
        lbIdade=Label(janelaBusca, text="Idade:    "+funcoes.bancoElementos[edBuscar.get()][1]+" anos"+"                   ", bg="green4", fg="white")
        lbPeso=Label(janelaBusca, text="Peso:     "+funcoes.bancoElementos[edBuscar.get()][2]+" Kg"+"                      ", bg="green4", fg="white")
        lbSexo=Label(janelaBusca, text="Sexo:      "+funcoes.bancoElementos[edBuscar.get()][3]+"                        ", bg="green4", fg="white")
        lbId.place(x=25, y=250)
        lbEspecie.place(x=25, y=265)
        lbIdade.place(x=25, y=280)
        lbPeso.place(x=25, y=295)
        lbSexo.place(x=25, y=310)
        edBuscar.delete(0, END)
        funcoes.salvarLog(usuarioLogado, "buscou elemento", log)
    else:
        messagebox.showerror("ERROR", "Animal nao encontrado")
        edBuscar.delete(0, END)
#_______________________ATUALIZAR ANIMAL________________________
def updateAnimal():
    global edAtualizar
    janelaAtualizar=Tk()
    lbTitulo=Label(janelaAtualizar, text="DIGITE O ID DO ANIMAL")
    lbId=Label(janelaAtualizar, text="ID")
    edAtualizar=Entry(janelaAtualizar)
    btConfirmar=Button(janelaAtualizar, text="Buscar",command=confirmUpdate)
    lbTitulo.place(x=0, y=3)
    lbId.place(x=5, y=25)
    edAtualizar.place(x=30, y=25)
    btConfirmar.place(x=50, y=50)
    janelaAtualizar.geometry("200x85+500+300")
    janelaAtualizar.mainloop()
#--------------------------------------------------------------
def confirmUpdate():
    global edNovaIdade
    global edNovoPeso
    global janelaUpdate
    if edAtualizar.get() in funcoes.bancoElementos:
        janelaUpdate=Tk()
        lbLinha=Label(janelaUpdate, text="---------------------------------------")
        lbId=Label(janelaUpdate, text="ID:           "+edAtualizar.get()+"                 ")
        lbEspecie=Label(janelaUpdate, text="Especie: "+funcoes.bancoElementos[edAtualizar.get()][0]+"                  ")
        lbIdade=Label(janelaUpdate, text="Idade:    "+funcoes.bancoElementos[edAtualizar.get()][1]+" anos"+"                   ")
        lbPeso=Label(janelaUpdate, text="Peso:     "+funcoes.bancoElementos[edAtualizar.get()][2]+" Kg"+"                      ")
        lbSexo=Label(janelaUpdate, text="Sexo:      "+funcoes.bancoElementos[edAtualizar.get()][3]+"                        ")
        lbNovoPeso=Label(janelaUpdate, text="Novo Peso")
        lbNovaIdade=Label(janelaUpdate, text="Nova Idade")
        edNovoPeso=Entry(janelaUpdate)
        edNovaIdade=Entry(janelaUpdate)
        btConfirmUp=Button(janelaUpdate, text="Atualizar", command=update)
        lbId.place(x=5, y=0)
        lbEspecie.place(x=5, y=20)
        lbIdade.place(x=5, y=40)
        lbPeso.place(x=5, y=60)
        lbLinha.place(x=0, y=90)
        lbSexo.place(x=5, y=80)
        lbNovoPeso.place(x=5, y=130)
        lbNovaIdade.place(x=5, y=110)
        edNovaIdade.place(x=70, y=110)
        edNovoPeso.place(x=70, y=130)
        btConfirmUp.place(x=50, y=150)
        janelaUpdate.geometry("200x175+500+300")
        janelaUpdate.mainloop()
    else:
        messagebox.showinfo("ERROR","Animal nao encontrado")
        edAtualizar.delete(0, END)
#--------------------------------------------------------------
def update():
    '''salva as informacoes colocadas no Entry e cria uma nova tupla com os novos elementos '''
    especie=funcoes.bancoElementos[edAtualizar.get()][0]
    sexo=funcoes.bancoElementos[edAtualizar.get()][3]
    funcoes.bancoElementos[edAtualizar.get()]=(especie,edNovaIdade.get(),edNovoPeso.get(),sexo)
    edAtualizar.delete(0, END)
    janelaUpdate.destroy()
    messagebox.showinfo("ERROR","Animal Atualizado")
    funcoes.salvarLog(usuarioLogado, "atualizou animal", log)
#_________________________ORDENAR______________________________
def ordenacao():
    janelaOrd=Tk()
    lbLinha=Label(janelaOrd, text="---------------------------------------------")
    lbQuestion=Label(janelaOrd, text="DESEJA ORDENAR APARTIR DE QUE?")
    btIdade=Button(janelaOrd, text="      Idade            ", command=ordenarIdade)
    btPeso=Button(janelaOrd, text="       Peso            ", command=ordenarPeso)
    lbLinha.place(x=0, y=15)
    lbQuestion.place(x=0, y=3)
    btIdade.place(x=5, y=30)
    btPeso.place(x=5, y=55)
    janelaOrd.geometry("200x80+500+300")
    janelaOrd.mainloop()
#-------------------------------------------------------------
def ordenarIdade():
    '''verifica se o segundo item do elemento, que é a idade, de um item da lista eh maior q o do proximo.
    se sim, troca posicao. "sistema de bolhas."'''
    lista=[]
    for x in funcoes.bancoElementos.items():
        lista.append(x)
    achou=True
    while achou:
        achou=False
        cont=0
        while cont<len(lista)-1:
            if float(lista[cont][1][1])>float(lista[cont+1][1][1]):
                achou=True
                aux=lista[cont]
                lista[cont]=lista[cont+1]
                lista[cont+1]=aux
            cont+=1
    for x in lista:
        print("ID: "+x[0]+"\n"+"Especie: "+x[1][0]+"\n"+"Idade: "+x[1][1]+" Anos\n"+
              "Peso: "+x[1][2]+" Kg\n"+"Sexo: "+x[1][3]+"\n"+"---------------------------")
#-------------------------------------------------------------
def ordenarPeso():
    '''verifica se o terceiro item do elemento, que é o peso, de um item da lista eh maior q o do proximo.
    se sim, troca posicao. "sistema de bolhas."'''
    lista=[]
    for x in funcoes.bancoElementos.items():
        lista.append(x)
    achou=True
    while achou:
        achou=False
        cont=0
        while cont<len(lista)-1:
            if float(lista[cont][1][2])>float(lista[cont+1][1][2]):
                achou=True
                aux=lista[cont]
                lista[cont]=lista[cont+1]
                lista[cont+1]=aux
            cont+=1
    for x in lista:
        print("ID: "+x[0]+"\n"+"Especie: "+x[1][0]+"\n"+"Idade: "+x[1][1]+" Anos\n"+
              "Peso: "+x[1][2]+" Kg\n"+"Sexo: "+x[1][3]+"\n"+"---------------------------")
#____________________________________LogOut__________________________________________
def logout():
    '''coloca todos os items do dicionario no txt tanto de usuarios como o de elementos.
quando abre o aquivo de elementos ja salva o contador geral antes de fazer a leitura de
elemento por elementos'''
    usuarios=open("usuarios.txt","w")
    for x in funcoes.bancoUsuarios.items():
        usuarios.write(funcoes.criptografar(x[0]))
        usuarios.write(funcoes.criptografar(x[1][0]))
        usuarios.write(funcoes.criptografar(x[1][1]))
    usuarios.close()
    elementos=open("elementos.txt","w")
    elementos.write(funcoes.criptografar(str(funcoes.contadorId)))
    for x in funcoes.bancoElementos.items():
        elementos.write(funcoes.criptografar(x[0]))
        elementos.write(funcoes.criptografar(x[1][0]))
        elementos.write(funcoes.criptografar(x[1][1]))
        elementos.write(funcoes.criptografar(x[1][2]))
        elementos.write(funcoes.criptografar(x[1][3]))
    elementos.close()
    impressao=open("impressaoelementos.txt","w")
    for x in funcoes.bancoElementos.items():
        impressao.write("Animal: "+x[0]+"\n"+"Especie: "+x[1][0]+"\n"+"Idade: "+x[1][1]+" Anos\n"+
                        "Peso: "+x[1][2]+" Kg\n"+"Sexo: "+x[1][3]+"\n"+"---------------------------\n")
    impressao.close()
    mainJanela.destroy()
#______________________________________PROGRAMA_________________________________
funcoes.loadUsers()
funcoes.loadAnimals()
log=open("log.txt","a")
continua=True
listaComando=[]
while continua:                                    
    janelaLogin()
    if listaComando==[]:
        continua=False
    else:
        if listaComando[0][1]==False:
            messagebox.showinfo("Login","usuario ou senha incorretos")
            del listaComando[0]
        else:
            if funcoes.bancoUsuarios[listaComando[0][0]][1]=="1":
                janelaSuper()
            elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="2":
                janelaGerente()
            elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="3":
                janelaTecnico()
            elif funcoes.bancoUsuarios[listaComando[0][0]][1]=="4":
                janelaEstagiario()
            del listaComando[0]
log.close()

