######################### RAIZ DO SISTEMA BACKEND #########################
import sys
import time
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer,QDateTime, QEventLoop
from tqdm import tqdm
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

import Janela_Loading
import Janela_Principal

class Loading(QtWidgets.QMainWindow, Janela_Loading.Ui_Janela_Loading):
    def __init__(self, parent=None):
        super(Loading, self).__init__(parent)
        self.setupUi(self)
        
        self.Sleep()

        self.segunda_tela = DiagBot()
        self.segunda_tela.show()
        

    def Sleep(self):
        QtCore.QTimer.singleShot(2000, self.progress)
        
    
    
    def progress(self):
        self.completo = 0
        while self.completo < 101:
            self.progressBar.setValue(self.completo)
            self.completo += 1
        #sys.exit(Janela_Loading)
        #self.destroy(Janela_Loading)
        self.segunda_tela = DiagBot()
        self.segunda_tela.show()
        Loading().destroy()
        
            

class DiagBot(QtWidgets.QMainWindow, Janela_Principal.Ui_Janela_Principal):
    def __init__(self, parent=None):
        super(DiagBot, self).__init__(parent)
        self.setupUi(self)
        self.actions()

    def actions(self):
        self.botton_info.clicked.connect(self.clickinfo)
        self.botton_enviar.clicked.connect(self.clickenviar)


    def clickenviar(self):  
        
        #------------------------------------------- Dicionário de falas do robô -----------------------------------------------------------------
        self.falas = {"Robo-Fala-1": "Olá!, como posso ajudar?",
                     "Resposta-Usuario-1":["Oi","Olá", "Eai", "oi", "olá", "oii", "oie", "eai"], 
                     "Resposta-Usuario-2":["O som do meu computador não funciona", "O som não sai", "O som não funciona", "Meu computador ficou sem som do nada", "Meu computador ficou sem som"],
                     "Resposta-Usuario-3":["tudo bem?", "td bem?", "Tudo bem?", "Como vai?", "como vai?", "eai?", "Eai", "eai", "Eai", "tudo bom?", "Tudo bom?", "td bom?", "Td"],
                     "Resposta-Usuario-end":["Adeus", "tchau", "Tchau!", "Tchau"],
                     "Resposta-Usuario-obg":["Obg", "Obrigada", "obrigada", "Obrigado", "obrigado", "valeu", "Valeu", "obg" , "Obrigada!", "obrigada!", "obrigado!", "Obrigado!"],
                     "Resposta-Usuario-4": ["Meu vídeo está travando sem motivos", "video travando sem motivo", "Video travando sem motivo", "vídeo travando sem motivo", "vídeo travando do nada", "Meu vídeo está travando sem motivo", "o vídeo está travando sem motivo"],
                     "Resposta-Usuario-5": ["Meu pc está superaquecendo", "meu pc esta superaquecendo", "meu computador está muito quente", "meu pc está muito quente", "Meu computador está quente"],
                     "Resposta-Usuario-6": ["Meu pc desliga do nada", "meu pc desliga do nada", "meu pc desliga repentinamente", "Meu pc desliga repentinamente", "pc desligando repentinamente", "Pc desligando repentinamente", "Pc desligando do nada", "pc desligando do nada", "Pc desligando sozinho", "pc desligando sozinho", "Computador desligando sozinho", "computador desligando sozinho", "Computador desligando do nada", "computador desligando do nada", "meu pc desliga sozinho", "Computador desliga sozinho", "Meu pc desliga sozinho", "Computador desligando sozinho"],
                     "Resposta-Usuario-7": ["Periféricos não reconhecidos", "meu pc não reconhece perifericos"],
                    "Resposta-Usuario-8": ["Meu hd está com problema", "meu hd esta com problema", "hd com problema", "HD com problema", "Problema no HD", "problema no hd"],
                    "Resposta-Usuario-9": ["Usb não funciona", "porta usb não funciona", "porta usb sem funcionar", "Porta USB não funciona", "Porta USB sem funcionar"],
                    "Resposta-Usuario-10": ["Internet não conecta", "Net n conecta", "internet nao conecta", "minha internet nao conecta"]
                     }


        self.usuario = self.entrada_usuario.text()

   # ------------------------------------------ Treinos ------------------------------------------------------------------------

        for palavras in self.falas["Resposta-Usuario-1"]: #Laço para buscar valores no dicionário de falas do robo e do usuário
             self.resposta_robo.setText(self.falas["Robo-Fala-1"])
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

        for palavras1 in self.falas["Resposta-Usuario-2"]: 
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

            
             
             if palavras1 in self.usuario:
                self.teste1 = "No gerenciador de dispositivos,\nverifique se o driver de som\nestá instalado, caso não,\ninstale-o no site do\nfabricante de seu dispositivo"
                self.resposta_robo.setText(self.teste1)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavras2 in self.falas["Resposta-Usuario-3"]: 

             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras2 in self.usuario:
                self.teste3 = "Tudo bem!"
                self.resposta_robo.setText(self.teste3)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavrasend in self.falas["Resposta-Usuario-end"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavrasend in self.usuario:
                self.testeend = "Tchau!"
                self.resposta_robo.setText(self.testeend)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavrasobg in self.falas["Resposta-Usuario-obg"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavrasobg in self.usuario:
                self.testeobg = "Por nada!"
                self.resposta_robo.setText(self.testeobg)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavras4 in self.falas["Resposta-Usuario-4"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras4 in self.usuario:
                self.print4 = "Seu problema pode ser resultado\nde componentes internos mal\nlimpos ou driver de vídeo\ndesatualizado"
                self.resposta_robo.setText(self.print4)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavras5 in self.falas["Resposta-Usuario-5"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras5 in self.usuario:
                self.print5 = "Seu problema pode ser resultado\nde sobrecarga de processos,\ncooler danificado/sujo ou\nvírus no sistema"
                self.resposta_robo.setText(self.print5)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavras6 in self.falas["Resposta-Usuario-6"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras6 in self.usuario:
                self.print6 = "Algumas das causas de seu\nproblema podem ser:\nsuperaquecimento,processador\ndanificado ou vírus no\nsistema"
                self.resposta_robo.setText(self.print6)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        #for erro in self.falas:
        #    if self.usuario not in self.falas:
         #     self.pergunta_usuario.setText(self.usuario)
          #     self.entrada_usuario.clear() 
          #     self.resposta_robo.setText("Desculpe, não entendi")

        for palavras7 in self.falas["Resposta-Usuario-7"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras7 in self.usuario:
                self.print7 = "Tente reconectá-los no disposi\ntivo; Além disso, verifique se\nos drivers estão atualizados;\nCaso o problema continue,\ntente reiniciar o pc"
                self.resposta_robo.setText(self.print7)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavras8 in self.falas["Resposta-Usuario-8"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras8 in self.usuario:
                self.print8 = "A causa do problema pode ser\ndevido a drivers não atualiza\ndos ou defeito físico, consulte\num técnico para mais\ninformações"
                self.resposta_robo.setText(self.print8)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavras9 in self.falas["Resposta-Usuario-9"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras9 in self.usuario:
                self.print9 = "Verifique o funcionamento das\noutras portas usb caso existam,\nalém da atualização dos\ndrivers e da possível\npresença de vírus no sistema"
                self.resposta_robo.setText(self.print9)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

        for palavras10 in self.falas["Resposta-Usuario-10"]: 
            
             self.pergunta_usuario.setText(self.usuario)
             self.entrada_usuario.clear()

             if palavras10 in self.usuario:
                self.print10 = "Seu problema pode ser devido à\ndrivers de placa de rede e\nadaptador wi-fi não\natualizados, defeito no\nroteador ou incompatibilidade"
                self.resposta_robo.setText(self.print10)
                self.pergunta_usuario.setText(self.usuario)
                self.entrada_usuario.clear()

    
    
# ------------------------------------------------- Treinos ------------------------------------------------------------------------------

      
    def clickinfo(self):
        msgbox = QMessageBox() 
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Informações")
        #definir icone
        msgbox.setWindowIcon(QtGui.QIcon(r"D:\Downloads\Diagbot\Logo.png"))
        msgbox.setText("Em caso de dúvidas ou problemas entre em contato com o seguinte e-mail: diagnosticopcsenai@gmail.com\n  \nSiga-nos no instagram: diag._.bot")
        sair = msgbox.exec_()



def main():
    app = QApplication(sys.argv)
    form = Loading()   
    form.show()
    app.exec_()
    

if __name__ == '__main__':
    main()