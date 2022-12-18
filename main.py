import customtkinter
from program import app, writeData

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")


# ! Funções


def calcule(value1, value2, value3):
    result = app(value1, value2, value3)
    loadResult(result[0], result[1], True, value1, value2, value3)
    closeMenu()


def callback():
    value1 = menuEntry1.get()
    value2 = menuEntry2.get()
    value3 = menuEntry3.get()
    calcule(value1, value2, value3)


def salvar():
    

    RessemQuebra = tempProbabilidade.replace("\n", "")
    DescricaoQuebra = tempDescricao.replace("\n", "")
    # Salva no banco de dados
    writeData(DescricaoQuebra, tempUmidade,
              tempTemperatura, tempVentos, RessemQuebra)
    # Fecha a janela de resultado
    closeResult()
    # Abre a janela de menu
    loadMenu()

def newEntry():
    global tempDescricao
    tempDescricao = entry4E.get()
    global tempProbabilidade
    tempProbabilidade = entry5E.get()
    closeNewEntry()
    salvar()


# ! Itens da interface
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)


# ! Itens da interface de Menu
menuLabel = customtkinter.CTkLabel(
    master=frame, text="Sistema de Previsão do tempo", font=("Roboto", 30))
labelUmid = customtkinter.CTkLabel(
    master=frame, text="Umidade", font=("Roboto", 15))
labelTemp = customtkinter.CTkLabel(
    master=frame, text="Temperatura", font=("Roboto", 15))
labelVentos = customtkinter.CTkLabel(
    master=frame, text="Ventos", font=("Roboto", 15))
menuEntry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Umidade")
menuEntry2 = customtkinter.CTkEntry(
    master=frame, placeholder_text="Temperatura")

menuEntry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Ventos")
menuButton = customtkinter.CTkButton(
    master=frame, text="Enviar", command=callback)


def loadMenu():

    menuLabel.pack(pady=10, padx=10, fill="both", expand=True)

    labelUmid.pack(pady=10, padx=10, fill="both", expand=True)
    menuEntry1.pack(pady=10, padx=10, fill="both", expand=True)

    labelTemp.pack(pady=10, padx=10, fill="both", expand=True)
    menuEntry2.pack(pady=10, padx=10, fill="both", expand=True)
    
    labelVentos.pack(pady=10, padx=10, fill="both", expand=True)
    menuEntry3.pack(pady=10, padx=10, fill="both", expand=True)
    
    
    menuButton.pack(pady=10, padx=10, fill="both", expand=True)
    #Limpa os valores do input
    menuEntry1.delete(0, "end")
    menuEntry2.delete(0, "end")
    menuEntry3.delete(0, "end")


def closeMenu():
    menuLabel.pack_forget()
    menuEntry1.pack_forget()
    menuEntry2.pack_forget()
    menuEntry3.pack_forget()
    menuButton.pack_forget()
    labelUmid.pack_forget()
    labelTemp.pack_forget()
    labelVentos.pack_forget()

def backMenu():
    closeNewEntry()
    loadMenu()

# ! Itens da interface de nova entrada
titleE = customtkinter.CTkLabel(
    master=frame, text="Sistema de Previsão do tempo", font=("Roboto", 30))
subtitleE = customtkinter.CTkLabel(
    master=frame, text="Caso deseje informar o resultado \n esperado preencha os dados abaixo", font=("Roboto", 15))
label2E = customtkinter.CTkLabel(
    master=frame, text="Por favor, digite a descrição do tempo", font=("Roboto", 15))
entry4E = customtkinter.CTkEntry(master=frame, placeholder_text="Descrição")
label3E = customtkinter.CTkLabel(
    master=frame, text="Por favor, digite a probabilidade do tempo", font=("Roboto", 15))
entry5E = customtkinter.CTkEntry(
    master=frame, placeholder_text="Probabilidade")
button3E = customtkinter.CTkButton(
    master=frame, text="Salvar", command=newEntry)
button4E = customtkinter.CTkButton(
    master=frame, text="Não informar", command=backMenu)



def loadNewEntry():
    tempU = tempUmidade
    tempT = tempTemperatura
    tempV = tempVentos  
    closeResult()

    titleE.pack(pady=10, padx=10, fill="both", expand=True)
    subtitleE.pack(pady=10, padx=10, fill="both", expand=True)
    label2E.pack(pady=10, padx=10, fill="both", expand=True)
    entry4E.pack(pady=10, padx=10, fill="both", expand=True)
    label3E.pack(pady=10, padx=10, fill="both", expand=True)
    entry5E.pack(pady=10, padx=10, fill="both", expand=True)
    button3E.pack(pady=10, padx=10, fill="both", expand=True)
    button4E.pack(pady=10, padx=10, fill="both", expand=True)

def closeNewEntry():
    titleE.pack_forget()
    subtitleE.pack_forget()
    label2E.pack_forget()
    entry4E.pack_forget()
    label3E.pack_forget()
    entry5E.pack_forget()
    button3E.pack_forget()
    button4E.pack_forget()

def loadResult(desc, res, fopen, u, t, v):
    global labelResult
    labelResult = customtkinter.CTkLabel(
        master=frame, text="Descrição: "+desc, font=("Roboto", 25))
    global labelResult2
    labelResult2 = customtkinter.CTkLabel(
        master=frame, text="Probabilidade: "+res, font=("Roboto", 25))

    # ! Itens da interface de resultado
    # Botões para verificar satifação do usuário
    global labelSatisfacao
    labelSatisfacao = customtkinter.CTkLabel(
        master=frame, text="Você está satisfeito com o resultado?", font=("Roboto", 20))

    global button1
    button1 = customtkinter.CTkButton(
        master=frame, text="Sim", command=salvar)
    global button2
    button2 = customtkinter.CTkButton(
        master=frame, text="Não", command=loadNewEntry)

    labelResult.pack(pady=10, padx=10, fill="both", expand=True)
    labelResult2.pack(pady=10, padx=10, fill="both", expand=True)
    labelSatisfacao.pack(pady=10, padx=10, fill="both", expand=True)
    button1.pack(pady=10, padx=10, fill="both", expand=True)
    button2.pack(pady=10, padx=10, fill="both", expand=True)
    #  Salva os dados temporariamente
    global tempUmidade
    global tempTemperatura
    global tempVentos
    tempUmidade = u
    tempTemperatura = t
    tempVentos = v
    global tempDescricao
    global tempProbabilidade
    tempDescricao = desc
    tempProbabilidade = res


def closeResult():
    labelResult.pack_forget()
    labelResult2.pack_forget()
    labelSatisfacao.pack_forget()
    button1.pack_forget()
    button2.pack_forget()


loadMenu()
root.mainloop()
