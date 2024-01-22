#               Passo a passo do projeto

# !pip install pandas numpy openpyxl
# Passo 1 - Entrar no sistema da empresa
    ## https://dlp.hashtagtreinamentos.com/python/intensivao/login

    ## Bibliotecas em Python: RPA - Automacao - pyautogui pip install pyautogui

    #clicar -> pyautogui.click, pyautogui.write, pyautogui.press("win"), pyautogui.hotkey("ctrl","c")
    # a tabela precisa estar na mesma pasta, senao preciso colocar o path dela
  #1#Aperta a tecla do Windows 
  #2#Digita o nome do programa
  #3#Apertar Enter

# Passo 2 - Fazer login
# Passo 3 - Importar a base de dados (pandas)
# passo 4 - Cadastrar um produto
# Passo 5 - Repetir isso ate acabar a base de dados

#Var#
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


#comands#
import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")  #\" contrabarra para incluir as aspas no texto
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(link)
pyautogui.press("enter") #no python tanto aspas duplas "" quanto aspas simples ''
time.sleep(2)
pyautogui.click(x=590, y=398)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

tabela = pandas.read_csv("produtos.csv") # aparentemente tabela e print precisaram ficar juntos
print(tabela)

for linha in tabela.index:

  codigo = tabela.loc[linha, "codigo"]
  marca = tabela.loc[linha, "marca"]
  tipo = tabela.loc[linha, "tipo"]
  categoria = str(tabela.loc[linha, "categoria"])
  preco = str(tabela.loc[linha, "preco_unitario"]) # transformar em texto porque ha numeros nessa coluna
  custo = str(tabela.loc[linha, "custo"])
  
  pyautogui.click(x=489, y=283)
  pyautogui.write(codigo)
  pyautogui.press("tab")
  pyautogui.write(marca)
  pyautogui.press("tab")
  pyautogui.write(tipo)
  pyautogui.press("tab")
  pyautogui.write(categoria) # pyautogui.write("1") ou pyautogui.write(stri(1))
  pyautogui.press("tab")
  pyautogui.write(preco)
  pyautogui.press("tab")
  pyautogui.write(custo) 
  pyautogui.press("tab")

  obs = tabela.loc[linha, "obs"] # atencao! NaN significa not a number no Python
  if not pandas.isna(obs): # if isna verifica se obs esta vazio, if not (senao) ele escreve o valor
    pyautogui.write(obs) # aqui esta o comando de escrever, somente SE

  pyautogui.press("tab")
  pyautogui.press("enter")
  pyautogui.scroll(1000) # ou hotkey pageUp