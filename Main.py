from DictTree import Tree
#from BotManipulator import BotManipulator
#from selenium import webdriver

if __name__ == "__main__":
    T = Tree()
    #BM = BotManipulator()
    Ciclo = 0
    #while(Ciclo == 0):

    RecentNode = T.getroot() 
    print(RecentNode.getDicionario()) #mensagem de introdução

    RecentNode = T.NextNode(RecentNode,1)
    print(RecentNode.getDicionario()) #Apresentação das primeira categorias

    


        #RecentNode = T.NextNode(RecentNode,2)
        #RecentNode = T.BackOp(RecentNode)
        #print(RecentNode.getDicionario())