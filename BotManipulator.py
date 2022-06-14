from selenium import webdriver
import time

class BotManipulator:
    global driver

    def OpenDriver(self):
        self.driver = webdriver.Chrome("C:\\Users\\Aluno\\Desktop\\Whats bot\\chromedriver.exe")
    
    def FindContact(self, name):
        Search_box = self.driver.find_element_by_class_name('_13NKt copyable-text selectable-text')
        time.sleep(3)
        Search_box.click()
        Search_box.send_keys(name)

    def RespPendente(self):
        NotReadMsg = self.driver.find_element_by_xpath("//span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")
        time.sleep(3)
        NotReadMsg.click()

    def Texting(self, mensagem):
        chat_box = self.driver.find_element_by_class_name('p3_M1')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(mensagem)
        time.sleep(3)

    def Enviar(self):
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon = 'send']")
        time.sleep(3)
        botao_enviar.click()

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
        #self.ReceiveMsg= "Ola Sou o UnicapBot, estou aqui para ajudar em que precisar!"
        NotReadMsg = self.driver.find_element_by_xpath("//span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")
        time.sleep(3)
        NotReadMsg.click() 

    def CapturarResposta(self):
        #fazer baseado no video https://www.youtube.com/watch?v=_ge6QcYY34I

        #<div class="_1Gy50"> 
        a
    def lerArquivo(self,rota: str):

        Arquivo = open(rota, mode ='r', encoding='utf-8')
        chat_box = self.driver.find_element_by_class_name('p3_M1')

        for linha in Arquivo.readlines():
            chat_box.send_keys(linha)

        Arquivo.close()