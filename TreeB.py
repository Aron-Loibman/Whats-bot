
from ast import If
from logging import root
from platform import node
#from typing_extensions import Self

from sqlalchemy import null


class Node:
    def __init__(self,str):
        
        self.id = [None,None,None,None,None] # [0,None,none,n...]| [1,None,none,n...]
        self.str = str
        self.filho=[None,None,None,None,None] #[Node_Children,none...]|[None,None,None,None,None]
        self.pai = None #None|No.py

    def getid(self):
        return self.id

    def setid(self,newid):
        self.id = newid

    def getstr(self):
        return self.str

    def setstr(self,newString):
        self.str = newString

    def getpai(self):
        return self.pai

    def setpai(self,Refpai):
        self.pai = Refpai
    
    def getfilho(self, ident):
        for i in self.filho:
            if (self.filho[ident] == None):
                return self.filho

    def setfilho(self,RefFilho):
        for i in self.filho:
          if(self.filho[i] is None):
             self.filho[i]=RefFilho
             break

    def getNextfilho(self, id):
        for i in self.filho:
            if (self.filho[i]==id):
              return self.filho[i+1]  

    def getPrevfilho(self, id):
        for i in self.filho:
            if (self.filho[i]==id):
              return self.filho[i-1]                

    def __repr__(self):
        return "<id_node:{0}>".format(self.id) +": "+"<str_node:{0}>".format(self.str)

class BTree:

    def __init__(self):
       self.root = Node("Olá sou o UnicapBot, em quais das categorias a seguir eu poderia lhe auxiliar?")
       self.root.setid([0,None,None,None,None])
    def percorrer(self,NodeReqID):
       y = self.root  
       x = 1
       z= NodeReqID[x]
       i = 1 
       while i < len(NodeReqID):
            if (self.root.getfilho(i) == None):
             return self.root
            elif(z != None):
             y = y.getfilho(z)
             x = x+1 
             z = NodeReqID[x]
            else: 
             return y    
            return y     

    def inserirFilho(self,NodeID):# to do
        x = self.percorrer(NodeID)
        y=1
        #filho NONE
        # estrutura de loop
        for i in NodeID:
            if (self.x.getfilho(y) == None):
              x.setfilho(NodeID)
              break
            else:  
              x.getNextfilho(y)

    def removerFilho(self, NodeID):# to do
        x = self.percorrer(NodeID)
        y=1
        #filho NONE
        # estrutura de loop
        for i in NodeID:
            if (x.getfilho(y) != None):
              x.setfilho(None)
              break
            else:  
              x.getNextfilho(y)
        


if __name__ == "__main__":
   Arvore = BTree()
   Arvore.inserirFilho([0,1,None,None,None])
