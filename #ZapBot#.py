#ZapBot#
from selenium import webdriver
import time


class Whatsappbot:
    def _init_(self):
        self.menssagem = "Bom dia pessoal"
        self.grupos = ["Base da seleção"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

def EnviarMensagens(self):
    
