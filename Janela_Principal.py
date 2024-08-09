######################### UNIDADE DE GUI #########################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela_Principal(object):
    def setupUi(self, Janela_Principal):
        Janela_Principal.setObjectName("Janela_Principal")
        Janela_Principal.resize(640, 480)
        Janela_Principal.setMinimumSize(QtCore.QSize(640, 480))
        Janela_Principal.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Janela_Principal.setFont(font)
        Janela_Principal.setLayoutDirection(QtCore.Qt.LeftToRight)
        Janela_Principal.setStyleSheet("")
        Janela_Principal.setWindowIcon(QtGui.QIcon(r"D:\Downloads\Diagbot\Logo.png"))
        self.centralwidget = QtWidgets.QWidget(Janela_Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.resposta_robo = QtWidgets.QLabel(self.centralwidget)
        self.resposta_robo.setGeometry(QtCore.QRect(10, 30, 321, 150))
        self.resposta_robo.setStyleSheet("background-color:rgb(12, 158, 255);\n"
        "border-radius : 15px;\n"
        "font: 10pt \"Lucida Console\";\n"
        "padding: 1px;")
        self.resposta_robo.setText("Olá! eu sou o Diagbot, o robô\ndiagnosticador, como posso\najudar?")
        self.resposta_robo.setObjectName("resposta_robo")
        self.pergunta_usuario = QtWidgets.QLabel(self.centralwidget)
        self.pergunta_usuario.setGeometry(QtCore.QRect(300, 190, 321, 111))
        self.pergunta_usuario.setStyleSheet("background-color:rgb(150, 158, 255);\n"
        "border-radius : 15px;\n"
        "font: 10pt \"Lucida Console\";\n"
        "padding: 5px;")
        self.pergunta_usuario.setText("")
        self.pergunta_usuario.setObjectName("pergunta_usuario")
        self.botton_info = QtWidgets.QPushButton(self.centralwidget)
        self.botton_info.setGeometry(QtCore.QRect(30, 410, 40, 40))
        self.botton_info.setStyleSheet("color:rgb(181, 181, 181);\n"
        "border-radius : 20px; \n"
        "border : 2px solid grey;\n"
        "font: 20pt \"Arial Black\";")
        self.botton_info.setObjectName("botton_info")
        self.botton_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.botton_enviar.setGeometry(QtCore.QRect(560, 410, 40, 40))
        self.botton_enviar.setStyleSheet("color:rgb(181, 181, 181);\n"
        "border-radius : 20px;\n"
        "border : 2px solid grey;\n"
        "")
        self.botton_enviar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Downloads/Projeto_Ana/Projeto_Ana\\logo_mensagem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botton_enviar.setIcon(icon)
        self.botton_enviar.setIconSize(QtCore.QSize(36, 36))
        self.botton_enviar.setObjectName("botton_info_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 320, 260))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"D:\Downloads\Diagbot\Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.entrada_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_usuario.setGeometry(QtCore.QRect(90, 415, 451, 30))
        self.entrada_usuario.setStyleSheet("background-color:rgb(181, 181, 181);\n"
        "border-radius : 15px;\n"
        "font: 12pt \"Lucida Console\";\n"
        "padding: 25px;")
        self.entrada_usuario.setObjectName("entrada_usuario")
        self.label_2.raise_()
        self.resposta_robo.raise_()
        self.pergunta_usuario.raise_()
        self.botton_info.raise_()
        self.botton_enviar.raise_()
        self.entrada_usuario.raise_()
        Janela_Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela_Principal)
        QtCore.QMetaObject.connectSlotsByName(Janela_Principal)

    def retranslateUi(self, Janela_Principal):
        _translate = QtCore.QCoreApplication.translate
        Janela_Principal.setWindowTitle(_translate("Janela_Principal", "DiagBot"))
        self.botton_info.setText(_translate("Janela_Principal", "i"))
