from logging import root
from platform import node

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
  
      dic_1= {'Aluno Graduação': 1,'Aluno Pós': 2, 'Professor': 3, 'Coordenação': 4, 'Reitoria': 5}
      
      NoDic_1 = Node(dic_1) #criação do primeiro nó
      rootNode.setfilhos(NoDic_1) #Primeiro nó se torna filho da raiz
      NoDic_1.setpai(rootNode) # raiz se torna pai do primeiro nó
      #endregion

      #region 2º Nivel, Set filhos e pais, Tree Blocks

      #bloco linkando 1.1 a 1
      dic_1_1= {'Matricula': 1,'Disciplinas': 2, 'Estágio': 3, 'Secretaría': 4, 'Financeiro': 5}
      NoDic_1_1 = Node(dic_1_1)
      NoDic_1.setfilhos(NoDic_1_1)
      NoDic_1_1.setpai(NoDic_1)
      
      #bloco linkando 1.2 a 1
      dic_1_2= {'Mestrado': 1,'Doutorado': 2, 'Católica Business School': 3, 'Especialização': 4}
      NoDic_1_2 = Node(dic_1_2)
      NoDic_1.setfilhos(NoDic_1_2)
      NoDic_1_2.setpai(NoDic_1)

      #bloco linkando 1.3 a 1
      dic_1_3= {'Burocracia': 1,'Caderneta': 2, 'Calendario letivo': 3}
      NoDic_1_3 = Node(dic_1_3)
      NoDic_1.setfilhos(NoDic_1_3)
      NoDic_1_3.setpai(NoDic_1)

      #bloco linkando 1.4 a 1
      dic_1_4= {'Coordenação Geral de Pesquisa': 1,'Coordenação Geral dos Cursos de MBA': 2, 'Coordenação Geral de Estágio – COGEST': 3, 'Coordenadores de Cursos': 4}
      NoDic_1_4 = Node(dic_1_4)
      NoDic_1.setfilhos(NoDic_1_4)
      NoDic_1_4.setpai(NoDic_1)

      #bloco linkando 1.5 a 1
      dic_1_5= {'Reitoria': 1,'Pró-Reitoria Administrativa': 2, 'Pró-Reitoria Comunitária e de Extensão': 3, 'Pró-Reitoria de Graduação': 4, 'Pró-Reitoriade Pesquisa, Pós-graduação e Inovação': 5}
      NoDic_1_5 = Node(dic_1_5)
      NoDic_1.setfilhos(NoDic_1_5)
      NoDic_1_5.setpai(NoDic_1)
      
      #endregion
      
      #region 3º Nivel, Set filhos e pais, Tree Blocks
      #faltam nós de matricula, disciplinas, secretaria e financeiro
     
      dic_1_1_3= {'Não Estágiando': 1,'Estágio': 2, 'Concedente de Estagio': 3, 'Agentes de integração': 4}
      NoDic_1_1_3 = Node(dic_1_1_3)
      NoDic_1_1.setfilhos(NoDic_1_1_3)
      NoDic_1_1_3.setpai(NoDic_1_1)
     
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
      rootNode.ShowOptions()    
      #falta fazer NextOp ser funcional
      Next = t.NextOp(0)
      print(Next)
      
      
   
      
