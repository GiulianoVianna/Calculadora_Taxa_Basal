from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


####### Variaveis com os valores das taxas de atividade #######

#Global

sedentario = 1.2
lev_ativo = 1.375
moderado = 1.55
alt_ativo = 1.725
ext_ativo  = 1.9

###### Funçoes de mensagem ######

def msg_ind_atividade():
    msg1 = QMessageBox()
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor o nível de atividade!')
    x = msg1.exec_()


def msg_peso():
    msg1 = QMessageBox()
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor informar o peso!')
    x = msg1.exec_()


def msg_altura():
    msg1 = QMessageBox()
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor informar a altura!')
    x = msg1.exec_()


def msg_idade():
    msg1 = QMessageBox()
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor informar a idade!')
    x = msg1.exec_()

#######################################################

####### Fução para validar indice de atividade #######

def indice_atividade():
    
    valida_dados = tela.cb_opcao.currentText()

    if valida_dados == 'Sedentário': nivel_atividade = sedentario        

    elif valida_dados == 'Levemente ativo': nivel_atividade = lev_ativo        

    elif valida_dados == 'Moderadamente ativo': nivel_atividade = moderado       

    elif valida_dados == 'Altamente ativo': nivel_atividade = alt_ativo        

    elif valida_dados== 'Extremamente ativo': nivel_atividade = ext_ativo          
        
    return (nivel_atividade) 
        
 
####### Fução que calcula taxa metabólica basal #######
#Fórmula para homens: TMB = fator da taxa de atividade x {66 + [(13,7 x Peso(kg)) + 
# ( 5 x Altura(cm)) – (6,8 x Idade(anos))]}

#Fórmula para mulheres: TMB = fator da taxa de atividade x {655 + [(9,6 x Peso(kg)) + 
# (1,8 x Altura(cm)) – (4,7 x Idade(anos))]}
    
def masc_e_feminino():
    peso = tela.txt_peso.text()    
    altura = tela.txt_altura.text()
    idade = tela.txt_idade.text()    

    if tela.txt_peso.text() == "": msg_peso()        

    elif tela.txt_altura.text() =="": msg_altura()        

    elif tela.txt_idade.text() == "": msg_idade()
      
    elif tela.cb_opcao.currentText() == "": msg_ind_atividade()        
         
    else:
        dados_funcao = indice_atividade() 

        if tela.rd_homem.isChecked():               
            calculo = dados_funcao * (66 + (13.7 * float(peso)) + (5 * float(altura)) - (6.8 * float(idade)))
            tela.txt_resultado.setText(str("%.2f" % calculo))

        else:             
            calculo1 = dados_funcao * (655 + (9.6 * float(peso)) + (1.8 * float(altura)) - (4.7 * float(idade)))
            tela.txt_resultado.setText(str("%.2f" % calculo1))
    
####### Função do botão #######

def botao():
    masc_e_feminino()   


####### Incialização da Janela #######    
    

app = QtWidgets.QApplication([])
tela = uic.loadUi("Maromba_do_Agreste.ui")

lista = ['', 'Sedentário', 'Levemente ativo', 
'Moderadamente ativo', 'Altamente ativo', 'Extremamente ativo'] # Lista para o combobox
tela.cb_opcao.addItems(lista) # Atribui lista ao combobox

tela.bt_calcular.clicked.connect(botao) # Chama a função do botão

tela.show()
app.exec()
