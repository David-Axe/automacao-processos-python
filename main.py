import pyautogui
import pandas as pd
import time

# Define um tempo de espera padrão entre cada comando do PyAutoGUI (segurança)
pyautogui.PAUSE = 0.5

# 1. Abrir o navegador e acessar o sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Espera o navegador abrir
time.sleep(2)

# Digita o link do sistema e acessa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Espera a página carregar
time.sleep(3)

# 2. Fazer Login no sistema
# Clica no campo de e-mail (ajuste as coordenadas x e y para a sua tela)
pyautogui.click(x=992, y=376)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # Passa para o campo de senha
pyautogui.write("sua_senha_aqui")
pyautogui.press("tab") # Passa para o botão de logar
pyautogui.press("enter")

time.sleep(3)

# 3. Importar a base de dados de produtos
tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar produto por produto
for linha in tabela.index:
    # Clica no primeiro campo do formulário de cadastro
    pyautogui.click(x=904, y=256)

    # Preenche os campos pegando os dados do arquivo CSV
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Verifica se a informação de 'obs' não está vazia (NaN) antes de preencher
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Envia o formulário
    pyautogui.press("enter")

    # Rola a tela para cima para voltar ao topo do formulário
    pyautogui.scroll(5000)