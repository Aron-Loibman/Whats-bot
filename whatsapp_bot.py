from lib2to3.pgen2 import driver
from selenium import webdriver
import time
class WhatsappBot:
    global BotOP
    BotOP = 1

    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "ola humanos, eu sou o bot"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos = ["Estágio"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome("C:\\Users\\Aluno\\Desktop\\Whats bot\\chromedriver.exe")
        self.driver.get("https://web.whatsapp.com")
        time.sleep(30)
    

    def ValidaQR(self):
        try:
            self.driver.find_element_by_tag_name("canvas")
        except: 
            return False  
        return True  

    def EnviarMensagens(self):
        grupo = self.driver.find_element_by_xpath("//span[@title='Estágio']")
        time.sleep(3)
        grupo.click()
        chat_box = self.driver.find_element_by_class_name('p3_M1')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon = 'send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(5)     
    
    def ReceberMensagem(self):
        self.ReceiveMsg= "Ola Sou o UnicapBot, estou aqui para ajudar em que precisar!"
        NotReadMsg = self.driver.find_element_by_xpath("//span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")
        time.sleep(3)
        NotReadMsg.click() 
        time.sleep(3)  
        chat_box = self.driver.find_element_by_class_name('p3_M1')
        time.sleep(3)  
        chat_box.click()
        chat_box.send_keys(self.ReceiveMsg)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon = 'send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(5)
    def CapturarResposta(self):
        #fazer baseado no video https://www.youtube.com/watch?v=_ge6QcYY34I
        a
    def lerArquivo(self,rota: str):

        Arquivo = open(rota, mode ='r', encoding='utf-8')
        chat_box = self.driver.find_element_by_class_name('p3_M1')

        for linha in Arquivo.readlines():
            chat_box.send_keys(linha)

        Arquivo.close()
        
bot = WhatsappBot()
while BotOP != 0:
    print("Digite 0 para finalizar, Digite 1 para enviar mensagem, Digite 2 para receber mensagem")
    BotOP = int(input("Que tipo de operação deseja executar?"))
    
    if BotOP == 1:
       bot.EnviarMensagens()
    elif BotOP == 2:
        bot.ReceberMensagem()
    elif BotOP == 0:
        exit()    
    else:
        print("Entrada invalida, selecione um numero de 0 a 2")
        print("Digite 0 para finalizar, Digite 1 para enviar mensagem, Digite 2 para receber mensagem")
        end = int(input("Que tipo de operação deseja executar?"))



