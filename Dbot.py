import re 
import random

class mensageiro(object):
    def probabilidade_mensagen(self, mensagem_usuario):
        self.certeza_mensagem = 0
        self.requerir_mensagens = True
        for word in