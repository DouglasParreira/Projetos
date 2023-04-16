from tkinter import *
 
def calcular_imc():
    nome = (entry_nome.get())
    apelido = (entry_apelido.get())
    email = (entry_email.get())
    cpf = int(entry_cpf.get())
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())
    time = (entry_time.get())
 
    imc = peso / altura**2
    
    label_resultado['text'] = " Muito obrigado pelos seus dados {} !!  Seu IMC é: %.2f".format(apelido) % imc
 
    if imc < 16:
        label_classificacao['text'] = "Considerado Magreza grave"
    elif imc < 17:
        label_classificacao['text'] = "Considerado Magreza moderada"
    elif imc < 18.5:
        label_classificacao['text'] = "Considerado Magreza leve"
    elif imc < 25:
        label_classificacao['text'] = "Considerado Saudável"
    elif imc < 30:
        label_classificacao['text'] = "Considerado Sobrepeso"
    elif imc < 35:
        label_classificacao['text'] = "Considerado Obesidade Grau I"
    elif imc < 40:
        label_classificacao['text'] = "Considerado Obesidade Grau II (severa)"
    else:
        label_classificacao['text'] = "Considerado Obesidade Grau III (mórbida)"
        
    if time == 'vasco':
        label_time['text'] = "Vamos todos cantar de coração!!!"
    elif time == 'fluminense':
        label_time['text'] = "Sou tricolor de coração!!!" 
    elif time == 'flamengo':   
        label_time['text'] = "Uma vez flamengo, sempre flamengo!!!"
    elif time == 'botafogo':  
        label_time['text'] = "botafogo botafogo campeão desde 1910!!!"
    elif time == 'corinthians':   
        label_time['text'] = "Salve o corinthians, o campeão dos campeões!!!"
    elif time == 'palmeiras':   
        label_time['text'] = "Quando surge o alviverde imponente!!!"
    elif time == 'santos':   
        label_time['text'] = "Agora quem dá a bola é o santos!!!"
    elif time == 'são paulo':   
        label_time['text'] = "Salve o tricolor paulista!!!"
    
 
root = Tk()
root.title("Ficha Cadastro")
 
frame_entrada = Frame(root)
frame_entrada.pack()

label_nome = Label(frame_entrada, text="Digite seu nome:")
label_nome.grid(row=0, column=1)

entry_nome = Entry(frame_entrada)
entry_nome.grid(row=1, column=1)

label_apelido = Label(frame_entrada, text="Como gostaria de ser chamado?")
label_apelido.grid(row=2, column=1)

entry_apelido = Entry(frame_entrada)
entry_apelido.grid(row=3, column=1)

label_email = Label(frame_entrada, text="Digite seu e-mail:")
label_email.grid(row=4, column=1)

entry_email = Entry(frame_entrada)
entry_email.grid(row=5, column=1)
 
label_cpf = Label(frame_entrada, text="Digite seu CPF:")
label_cpf.grid(row=6, column=1)

entry_cpf = Entry(frame_entrada)
entry_cpf.grid(row=7, column=1)
 
label_altura = Label(frame_entrada, text="Digite sua Altura (m):")
label_altura.grid(row=8, column=1)
 
entry_altura = Entry(frame_entrada)
entry_altura.grid(row=9, column=1)
 
label_peso = Label(frame_entrada, text="Digite seu Peso (Kg):")
label_peso.grid(row=10, column=1)
 
entry_peso = Entry(frame_entrada)
entry_peso.grid(row=11, column=1)

label_time = Label(frame_entrada, text="Qual é o seu time de coração?")
label_time.grid(row=12, column=1)

entry_time = Entry(frame_entrada)
entry_time.grid(row=13, column=1)
 
frame_saida = Frame(root)
frame_saida.pack()
 
label_resultado = Label(frame_saida, text="")
label_resultado.pack()
 
label_classificacao = Label(frame_saida, text="")
label_classificacao.pack()
 
botao_enviar = Button(root, text="Enviar", command=calcular_imc)
botao_enviar.pack()
 
root.mainloop()