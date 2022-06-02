from logging import root
from platform import node
import json
from sqlalchemy import null

class Node:

   def __init__(self,Dicionario):
       self.Dicionario = Dicionario
       self.filhos = []
       self.pai = None 

   def getpai(self):
      return self.pai

   def setpai(self,Refpai):
      self.pai = Refpai

   def getfilhos(self):
      return self.filhos

   def setfilhos(self,Reffilho):
      self.filhos.append(Reffilho) 

   def getDicionario(self):
      return self.Dicionario

   def setDicionario(self,RefDicionario):
      self.Dicionario = RefDicionario

   def ShowOptions(self):
       print(self.Dicionario)

   def ShowFilho(self,pos):
      a = self.getfilhos()
      a = a[pos]
      print(a.getDicionario())
           
       
class Tree:

   def __init__(self):
      #region 1º nivel, Raiz e primeiro nó
      self.root =  {'Olá sou o UnicapBot, em quais das categorias a seguir eu poderia lhe auxiliar?'}
      
      global rootNode
      global NoDic_1
      global NoDic_1_1
      global NoDic_1_2
      global NoDic_1_3
      global NoDic_1_4
      global NoDic_1_5
      global NoDic_1_1_3
      


      rootNode = Node(self.root) #criação do nó raiz
  
      dic_1= {'Coordenação': 1,'Estágio': 2, 'Pesquisa': 3, 'Extensão': 4}
      
      NoDic_1 = Node(dic_1) #criação do primeiro nó
      rootNode.setfilhos(NoDic_1) #Primeiro nó se torna filho da raiz
      NoDic_1.setpai(rootNode) # raiz se torna pai do primeiro nó
      #endregion

      #region 2º Nivel, Set filhos e pais, Tree Blocks

      #bloco linkando 1.1 a 1
      dic_1_1= {'Coordenação Geral de Pesquisa': 1,'Coordenação Geral dos Cursos de MBA': 2, 'Coordenação Geral de Estágio – COGEST': 3, 'Coordenadores de Cursos': 4}
      NoDic_1_1 = Node(dic_1_1)
      NoDic_1.setfilhos(NoDic_1_1)
      NoDic_1_1.setpai(NoDic_1)
      
      #bloco linkando 1.2 a 1
      dic_1_2= {'Ainda não estou estagiando': 1,'Já estou estagiando': 2}
      NoDic_1_2 = Node(dic_1_2)
      NoDic_1.setfilhos(NoDic_1_2)
      NoDic_1_2.setpai(NoDic_1)

      #bloco linkando 1.3 a 1
      dic_1_3= {'Contato': 1,'Informações': 2, 'Formularios e Documentos': 3}
      NoDic_1_3 = Node(dic_1_3)
      NoDic_1.setfilhos(NoDic_1_3)
      NoDic_1_3.setpai(NoDic_1)

      #bloco linkando 1.4 a 1
      dic_1_4= {'Cursos': 1,'Programas e Projetos': 2, 'Como se inscrever num curso': 3, 'Quer ministrar um curso?': 4, 'Fluxograma do processo para criação de cursos': 5}
      NoDic_1_4 = Node(dic_1_4)
      NoDic_1.setfilhos(NoDic_1_4)
      NoDic_1_4.setpai(NoDic_1)

      
      #endregion
      
      #region 3º Nivel, Set filhos e pais, Tree Blocks
      #faltam nós de matricula, disciplinas, secretaria e financeiro
     
      dic_1_2_1= {'Informações iniciais': 1,'Agencia experimental': 2, 'Agentes de integração': 3, 'Entidades concedentes/oportunidades': 4, 'Regime CLT':5}
      NoDic_1_2_1 = Node(dic_1_2_1)
      NoDic_1_1.setfilhos(NoDic_1_2_1)
      NoDic_1_2_1.setpai(NoDic_1_1)
     
      #endregion
     
      #region 4º Nivel, Set filhos e pais, Tree Blocks, Question blocks
     
      dic_1_1_3_1= {'Não Estágiando': 1,'Estágio Não Obrigatório': 2, 'Estágio Obrigatório ': 3, 'Voluntariado': 4, 'Concedente de Estagio': 5}
      dic_1_1_3_2= {'Não Estágiando': 1,'Estágio Não Obrigatório': 2, 'Estágio Obrigatório ': 3, 'Voluntariado': 4, 'Concedente de Estagio': 5}
      dic_1_1_3_3= {'Não Estágiando': 1,'Estágio Não Obrigatório': 2, 'Estágio Obrigatório ': 3, 'Voluntariado': 4, 'Concedente de Estagio': 5}
      dic_1_1_3_4= {'Não Estágiando': 1,'Estágio Não Obrigatório': 2, 'Estágio Obrigatório ': 3, 'Voluntariado': 4, 'Concedente de Estagio': 5}
      dic_1_1_3_5= {'Não Estágiando': 1,'Estágio Não Obrigatório': 2, 'Estágio Obrigatório ': 3, 'Voluntariado': 4, 'Concedente de Estagio': 5}
      #endregion

      #region 5º Nivel, Set filhos e pais, Tree Blocks, Answer blocks
      
      
      #endregion
      
      

   def getroot(self):
      return rootNode

   #def NextOp(self,No,entrada):
      #refazer metodo, não funcional
    #  a = Node(No)
    #  b = a.getfilhos()
    #  i =0 
      #não entra no for????? retorna None 
    #  for i in b:  
    #     if(dict(b[i]).values() == entrada):       
    #        return Node(b[i])
   def BackOp(self,No):
      a = Node(No)
      b = a.getpai
      return b

   def FirstNode(self):   
      a = rootNode   
      b = Node(a).getfilhos()
      x = b[0]
      return x


if __name__ == "__main__":
      #teste
      t = Tree()
      #rootNode.ShowOptions()    
      #falta fazer NextOp ser funcional
      #Next = t.NextOp(0)
      #print(Next)

      print()      
   
      
