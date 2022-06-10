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
      
     
      #nó filho de ainda não estou estagiando
      dic_1_2_1= {'Informações iniciais': 1,'Agencia experimental': 2, 'Agentes de integração': 3, 'Entidades concedentes/oportunidades': 4, 'Regime CLT':5}
      NoDic_1_2_1 = Node(dic_1_2_1)
      NoDic_1_1.setfilhos(NoDic_1_2_1)
      NoDic_1_2_1.setpai(NoDic_1_1)
     
      #endregion
     
      #region 4º Nivel, Set filhos e pais, Tree Blocks, Question blocks
      
      #region nó de perguntas de ainda não estou estagiando
      #informações iniciais
      dic_1_2_1_1= {'O que é o estágio?': 1,'Quais são as modalidades de estágio?': 2, 'Quem pode ser estagiário?': 3, 'O estudante estrangeiro pode estagiar?': 4, 'O estágio cria vínculo empregatício?': 5,'Quais são os principais requisitos legais que devem ser observados para a formação da relação de estágio?':6,'As atividades desenvolvidas pelo estudante de extensão, de monitorias e de iniciação científica na educação superior podem ser equiparadas ao estágio?':7,'A estudante gestante pode estagiar?':8,'O estagiário precisa ter Carteira de Trabalho?':9,'Passo a Passo do Estagiário':10}
      NoDic_1_2_1_1 = Node(dic_1_2_1_1)
      NoDic_1_2_1.setfilhos(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setpai(NoDic_1_2_1)
      #agencia experimental
      dic_1_2_1_2= {'O que é a Agência Experimental?': 1,'O que devo fazer para estagiar na Agência experimental?': 2, 'O estágio na Agência Experimental é presencial?': 3, 'O estágio na Agência Experimental é remunerado?': 4, 'Que tipo de trabalho será feito na Agência Experimental?': 5}
      NoDic_1_2_1_2 = Node(dic_1_2_1_2)
      NoDic_1_2_1.setfilhos(NoDic_1_2_1_2)
      NoDic_1_2_1_2.setpai(NoDic_1_2_1)
      #agentes de integração
      dic_1_2_1_3= {'As instituições de ensino e as partes concedentes de estágio podem utilizar-se dos serviços dos agentes de integração?': 1,'Quais são as atribuições definidas na lei para os agentes de integração?': 2, 'Pode ser cobrado do estudante algum valor pelos serviços previstos na lei e prestados pelos agentes de integração?': 3, 'Os agentes de integração podem sofrer penalidades?': 4, 'O agente de integração pode atuar como representante do estagiário, da parte concedente ou da instituição de ensino no Termo de Compromisso de Estágio?': 5}
      NoDic_1_2_1_3 = Node(dic_1_2_1_3)
      NoDic_1_2_1.setfilhos(NoDic_1_2_1_3)
      NoDic_1_2_1_3.setpai(NoDic_1_2_1)
      #entidade concedentes/oportunidades
      dic_1_2_1_4= {'Quem pode contratar estagiário?': 1,'Quais são as principais obrigações da parte concedente na relação de estágio?': 2, 'A celebração de convênio de concessão de estágio entre a instituição de ensino e a parte concedente dispensa a celebração do termo de compromisso de estágio?': 3, 'Qual o prazo máximo de duração do estágio na mesma unidade concedente?': 4, 'Podem, a critério da parte concedente, ser concedidos outros benefícios ao estagiário?': 5, 'As ausências do estagiário podem ser descontadas do valor da bolsa?':6,'O estagiário é segurado obrigatório do Regime Geral da Previdência Social?':7,'O Termo de Compromisso de Estágio pode ser rescindido antes do seu término?':8,'Existe limitação para a contratação de estagiários em relação ao quadro de pessoal das entidades concedentes?':9,'A limitação para a contratação de estagiários em relação ao quadro de pessoal de concedentes se aplica aos estágios de nível superior e de nível médio profissional?':10,'O que se entende por quadro de pessoal para efeitos da lei de estágio?':11,'Qual a consequência prevista para a parte concedente no descumprimento da Lei nº 11.788/2008?':12,'Quais as hipóteses em que a concedente poderá ficar impedida de receber estagiários?':13}
      NoDic_1_2_1_4 = Node(dic_1_2_1_4)
      NoDic_1_2_1.setfilhos(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setpai(NoDic_1_2_1)
      #regime CLT
      dic_1_2_1_5= {'Pendente': 0,'Voltar':1}
      NoDic_1_2_1_5 = Node(dic_1_2_1_5)
      NoDic_1_2_1.setfilhos(NoDic_1_2_1_5)
      NoDic_1_2_1_5.setpai(NoDic_1_2_1)
      #endregion

      #region nó de perguntas de estou estagiando
      dic_1_2_2= {'O que é o estágio?': 1,'Quais são as modalidades de estágio?': 2, 'Quem pode ser estagiário?': 3, 'O estudante estrangeiro pode estagiar?': 4, 'O estágio cria vínculo empregatício?': 5,'Quais são os principais requisitos legais que devem ser observados para a formação da relação de estágio?':6,'As atividades desenvolvidas pelo estudante de extensão, de monitorias e de iniciação científica na educação superior podem ser equiparadas ao estágio?':7,'A estudante gestante pode estagiar?':8,'O estagiário precisa ter Carteira de Trabalho?':9,'Passo a Passo do Estagiário':10}
      NoDic_1_2_2 = Node(dic_1_2_2)
      NoDic_1_2.setfilhos(NoDic_1_2_2)
      NoDic_1_2_1_1.setpai(NoDic_1_2)





      #endregion

      #endregion

      #region 5º Nivel, Set filhos e pais, Tree Blocks, Answer blocks
      
      
      #endregion
      #OBS: nós respostas não possuem filhos
      #campo de respostas do 1_2_1_1
      #1
      dic_1_2_1_1_1= {'Resposta: Estágio é ato educativo escolar supervisionado, desenvolvido no ambiente de trabalho, que visa à preparação para o trabalho produtivo de estudantes. O estágio integra o itinerário formativo do estudante e faz parte do projeto pedagógico do curso (art. 1º).':0,'Voltar':1}
      NoDic_1_2_1_1_1 = Node(dic_1_2_1_1_1)
      NoDic_1_2_1_1_1.setpai(NoDic_1_2_1_1)
      #2
      dic_1_2_1_1_2= {'Resposta: Estágio obrigatório, que é aquele definido como tal no projeto do curso, cuja carga horária é requisito para aprovação e obtenção do diploma, e estágio não obrigatório, que é aquele desenvolvido como atividade opcional, acrescida à carga horária regular e obrigatória (§§ 1º e 2º do art. 2º).':0,'Voltar':1}
      NoDic_1_2_1_1_2 = Node(dic_1_2_1_1_2)
      NoDic_1_2_1_1_2.setpai(NoDic_1_2_1_1)
      #3
      dic_1_2_1_1_3= {'Resposta: estudantes que estejam frequentando o ensino regular em instituições de educação superior, de educação profissional, de ensino médio, da educação especial e dos anos finais do ensino fundamental, na modalidade profissional da educação de jovens e adultos (art. 1º).':0,'Voltar':1}
      NoDic_1_2_1_1_3 = Node(dic_1_2_1_1_3)
      NoDic_1_2_1_1_3.setpai(NoDic_1_2_1_1)
      #4
      dic_1_2_1_1_4= {'Resposta: sim, desde que o estudante estrangeiro esteja regularmente matriculado em curso superior no país autorizado ou reconhecido e seja observado o prazo do visto temporário de estudante, na forma da legislação aplicável (art. 4º).':0,'Voltar':1}
      NoDic_1_2_1_1_4 = Node(dic_1_2_1_1_4)
      NoDic_1_2_1_1_4.setpai(NoDic_1_2_1_1)
      #5
      dic_1_2_1_1_5= {'Resposta: o estágio é regido por legislação própria e, desde que observados os requisitos legais e as obrigações contidas no termo de compromisso de estágio, não estabelece vínculo empregatício de qualquer natureza, para todos os fins da legislação trabalhista e previdenciária (caput e § 2º do art. 3º c/c art. 15).':0,'Voltar':1}
      NoDic_1_2_1_1_5 = Node(dic_1_2_1_1_5)
      NoDic_1_2_1_1_5.setpai(NoDic_1_2_1_1)
      #6
      dic_1_2_1_1_6= {'Resposta: para formação da relação de estágio, devem ser observados os seguintes requisitos: a) matrícula e frequência regular do estudante público-alvo da lei; b) celebração do termo de compromisso entre o estudante, a parte concedente do estágio e a instituição de ensino; e c) compatibilidade entre as atividades desenvolvidas no estágio e as previstas no termo de compromisso. (incisos, I, II, III do art. 3º).':0,'Voltar':1}
      NoDic_1_2_1_1_6 = Node(dic_1_2_1_1_6)
      NoDic_1_2_1_1_6.setpai(NoDic_1_2_1_1)
      #7
      dic_1_2_1_1_7= {'Resposta: sim, desde que previstas no projeto pedagógico do curso (§ 3º do art. 2º).':0,'Voltar':1}
      NoDic_1_2_1_1_7 = Node(dic_1_2_1_1_7)
      NoDic_1_2_1_1_7.setpai(NoDic_1_2_1_1)
      #8
      dic_1_2_1_1_8= {'Resposta: sim. Não há nenhum empecilho da estudante gestante estagiar. Como todo estágio, sujeita-se às regras da Lei 11.788/08.':0,'Voltar':1}
      NoDic_1_2_1_1_8 = Node(dic_1_2_1_1_8)
      NoDic_1_2_1_1_8.setpai(NoDic_1_2_1_1)
      #9
      dic_1_2_1_1_9= {'Resposta: não há obrigatoriedade para a expedição e anotação do estágio na Carteira de Trabalho e Previdência Social, uma vez que estágio não é emprego, sendo definido em legislação própria.':0,'Voltar':1}
      NoDic_1_2_1_1_9 = Node(dic_1_2_1_1_9)
      NoDic_1_2_1_1_9.setpai(NoDic_1_2_1_1)
      #10
      dic_1_2_1_1_10= {'Resposta: Pendente':0,'Voltar':1}
      NoDic_1_2_1_1_10 = Node(dic_1_2_1_1_10)
      NoDic_1_2_1_1_10.setpai(NoDic_1_2_1_1)

      #campo de respostas do 1_2_1_2
      #1
      dic_1_2_1_2_1= {'Resposta: É o setor cujo objetivo é desenvolver as habilidades dos alunos voltadas para suas atuações no mercado de trabalho. A agência experimental tem uma organização semelhante à das agências reais do mercado, com cargos direcionados para atividades específicas, planejamento, projetos e prazos a serem cumpridos.':0,'Voltar':1}
      NoDic_1_2_1_2_1 = Node(dic_1_2_1_2_1)
      NoDic_1_2_1_2_1.setpai(NoDic_1_2_1_2)
      #2
      dic_1_2_1_2_2= {'Resposta: A cada semestre a CGE enviará email para os alunos informando a abertura das vagas para trabalhar na agência experimental, há possibilidade de cumprir as horas de estágio sendo não obrigatório, porém será dada prioridade aos alunos concluintes na categoria estágio obrigatório.':0,'Voltar':1}
      NoDic_1_2_1_2_2 = Node(dic_1_2_1_2_2)
      NoDic_1_2_1_2_2.setpai(NoDic_1_2_1_2)
      #3
      dic_1_2_1_2_3= {'Resposta: Sim, o estágio na agência experimental é presencial, abrindo apenas exceções remotas em casos de calamidade pública.':0,'Voltar':1}
      NoDic_1_2_1_2_3 = Node(dic_1_2_1_2_3)
      NoDic_1_2_1_2_3.setpai(NoDic_1_2_1_2)
      #4
      dic_1_2_1_2_4= {'Resposta: Não':0,'Voltar':1}
      NoDic_1_2_1_2_4 = Node(dic_1_2_1_2_4)
      NoDic_1_2_1_2_4.setpai(NoDic_1_2_1_2)
      #5
      dic_1_2_1_2_5= {'Resposta: Em sua maioria tem funções relacionadas a planejamento e desenvolvimento de projetos contendo prazos a serem cumpridos, é uma experiência que se equivale a adquirida em uma empresa júnior.':0,'Voltar':1}
      NoDic_1_2_1_2_5 = Node(dic_1_2_1_2_5)
      NoDic_1_2_1_2_5.setpai(NoDic_1_2_1_2)



     
      #campo de respostas do 1_2_1_3
      #1
      dic_1_2_1_3_1= {'Resposta: sim. As instituições de ensino e as partes concedentes de estágio podem, mediante condições acordadas em instrumento jurídico apropriado, recorrer aos serviços de agentes de integração públicos e privados. Em caso de contratação com recursos públicos, deverá ser observada a legislação de licitação, Lei no. 8.666/1993 (caput do art. 5º).':0,'Voltar':1}
      NoDic_1_2_1_3_1 = Node(dic_1_2_1_3_1)
      NoDic_1_2_1_3_1.setpai(NoDic_1_2_1_3)
      #2
      dic_1_2_1_3_2= {'Resposta: Cabe ao agente de integração, como auxiliar no processo de aperfeiçoamento do estágio:  a) identificar as oportunidades de estágio;   b) ajustar suas condições de realização;   c) fazer o acompanhamento administrativo;   d) encaminhar negociação de seguros contra acidentes pessoais;  e) Cadastrar os estudantes. (incisos de I a V do § 1º, do art. 5º).  Os agentes de integração podem, ainda, selecionar os locais de estágio e organizar o cadastro dos concedentes das oportunidades de estágio. (art. 6º)':0,'Voltar':1}
      NoDic_1_2_1_3_2 = Node(dic_1_2_1_3_2)
      NoDic_1_2_1_3_2.setpai(NoDic_1_2_1_3)
      #3
      dic_1_2_1_3_3= {'Resposta: Não. É vedada a cobrança de qualquer valor aos estudantes, a título de remuneração pelos serviços dos agentes de integração, previstos na lei (§ 2º do art. 5º).':0,'Voltar':1}
      NoDic_1_2_1_3_3 = Node(dic_1_2_1_3_3)
      NoDic_1_2_1_3_3.setpai(NoDic_1_2_1_3)
      #4
      dic_1_2_1_3_4= {'Resposta: Sim. Os agentes de integração serão responsabilizados civilmente se indicarem estagiários:  a) para atividades não compatíveis com a programação curricular do curso;  b) que estejam frequentando cursos em instituições de ensino para quais não há  previsão de estágio curricular. (§ 3º do art. 5º).':0,'Voltar':1}
      NoDic_1_2_1_3_4 = Node(dic_1_2_1_3_4)
      NoDic_1_2_1_3_4.setpai(NoDic_1_2_1_3)
      #5
      dic_1_2_1_3_5= {'Resposta: Não. O termo de compromisso deve ser firmado pelo estagiário ou com seu representante ou assistente legal e pelos representantes legais da parte concedente e da instituição de ensino, vedada a atuação dos agentes de integração como representante de qualquer das partes (art. 16).':0,'Voltar':1}
      NoDic_1_2_1_3_5 = Node(dic_1_2_1_3_5)
      NoDic_1_2_1_3_5.setpai(NoDic_1_2_1_3)

      #campo de respostas do 1_2_1_4
      #1
      dic_1_2_1_4_1= {'Resposta:  As pessoas jurídicas de direito privado e os órgãos da administração pública direta, autárquica e fundacional de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios e os profissionais liberais de nível superior, devidamente registrados em seus respectivos conselhos de fiscalização profissional (caput do art. 9º).':0,'Voltar':1}
      NoDic_1_2_1_4_1 = Node(dic_1_2_1_4_1)
      NoDic_1_2_1_4_1.setpai(NoDic_1_2_1_4)
      #2
      dic_1_2_1_4_2= {'Resposta: São obrigações da concedente de estágio:  a) celebrar termo de compromisso com a instituição de ensino e com o estudante, zelando por seu cumprimento;  b) ofertar instalações que tenham condições de proporcionar ao estudante atividades de aprendizagem social, profissional e cultural;  c) indicar funcionário de seu quadro de pessoal, com formação ou experiência profissional na área de conhecimento desenvolvida no curso do estagiário, para orientar e supervisionar até 10 (dez) estagiários simultaneamente;  d) contratar em favor do estagiário seguro contra acidentes pessoais, cuja apólice seja compatível com valores de mercado, conforme fique estabelecido no termo de compromisso, podendo, alternativamente, na hipótese de estágio obrigatório, ser assumida pela instituição de ensino;  e) entregar termo de realização do estágio com indicação resumida das atividades desenvolvidas, dos períodos e da avaliação de desempenho por ocasião do desligamento do estagiário;  f) manter à disposição da fiscalização documentos que comprovem a relação de estágio;  g) enviar à instituição de ensino, com periodicidade mínima de 6 (seis) meses, relatório de atividades, com vista obrigatória ao estagiário;   h) implementar a legislação relacionada à saúde e à segurança do trabalho a ser aplicada ao estagiário.(incisos I a VII e parágrafo único do art. 9º e art. 14).':0,'Voltar':1}
      NoDic_1_2_1_4_2 = Node(dic_1_2_1_4_2)
      NoDic_1_2_1_4_2.setpai(NoDic_1_2_1_4)
      #3
      dic_1_2_1_4_3= {'Resposta: Não. A celebração de convênio de concessão de estágio entre a instituição de ensino e a parte concedente não dispensa a celebração do termo de compromisso de estágio (parágrafo único do art. 8º).':0,'Voltar':1}
      NoDic_1_2_1_4_3 = Node(dic_1_2_1_4_3)
      NoDic_1_2_1_4_3.setpai(NoDic_1_2_1_4)
      #4
      dic_1_2_1_4_4= {'Resposta: A duração do estágio, na mesma unidade concedente, não poderá exceder 2 (dois) anos, exceto quando se tratar de estagiário portador de deficiência (art. 11).':0,'Voltar':1}
      NoDic_1_2_1_4_4 = Node(dic_1_2_1_4_4)
      NoDic_1_2_1_4_4.setpai(NoDic_1_2_1_4)
      #5
      dic_1_2_1_4_5= {'Resposta: Sim. A eventual concessão de benefícios relacionados a transporte, alimentação e saúde, entre outros, não caracteriza vínculo empregatício para todos os fins da legislação trabalhista e da previdenciária (§ 1º do art. 12).':0,'Voltar':1}
      NoDic_1_2_1_4_5 = Node(dic_1_2_1_4_5)
      NoDic_1_2_1_4_5.setpai(NoDic_1_2_1_4)
      #6
      dic_1_2_1_4_6= {'Resposta: Sim. A remuneração das atividades de estágio, por meio de bolsa ou outra forma de contraprestação, pressupõe o cumprimento das atividades previstas no termo de compromisso de estágio. Ausências eventuais, devidamente justificadas, poderão ser objetos de entendimento entre as partes, e poderão, na forma acordada, deixar de ser descontadas. (Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_1_4_6 = Node(dic_1_2_1_4_6)
      NoDic_1_2_1_4_6.setpai(NoDic_1_2_1_4)
      #7
      dic_1_2_1_4_7= {'Resposta: Não. O estagiário, porém, pode inscrever-se e contribuir como segurado facultativo da Previdência Social (§ 2º do art. 12).':0,'Voltar':1}
      NoDic_1_2_1_4_7 = Node(dic_1_2_1_4_7)
      NoDic_1_2_1_4_7.setpai(NoDic_1_2_1_4)
      #8
      dic_1_2_1_4_8= {'Resposta: Sim. O Termo de Compromisso de Estágio pode ser rescindido unilateralmente pelas partes e a qualquer momento. (Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_1_4_8 = Node(dic_1_2_1_4_8)
      NoDic_1_2_1_4_8.setpai(NoDic_1_2_1_4)
      #9
      dic_1_2_1_4_9= {'Resposta: Sim. Para os estágios de ensino médio, de educação especial e dos anos finais do ensino fundamental, na modalidade profissional da educação de jovens e adultos. Nesses casos, o número máximo de estagiários deverá atender às seguintes proporções, em relação ao quadro de pessoal de concedente:  a) de 1 (um) a 5 (cinco) empregados: 1 (um) estagiário;  b) de 6 (seis) a 10 (dez) empregados: até 2 (dois) estagiários;  c) de 11 (onze) a 25 (vinte e cinco) empregados: até 5 (cinco) estagiários;   d) acima de 25 (vinte e cinco) empregados, até 20% (vinte por cento) de estagiários (inciso I a IV do art. 17).  Quando esse cálculo resultar em fração, poderá ser arredondado para o número inteiro imediatamente superior (§ 3º do art. 17)':0,'Voltar':1}
      NoDic_1_2_1_4_9 = Node(dic_1_2_1_4_9)
      NoDic_1_2_1_4_9.setpai(NoDic_1_2_1_4)
      #10
      dic_1_2_1_4_10= {'Resposta: Não. Essa limitação não se aplica aos estágios de nível superior e de nível médio profissional.':0,'Voltar':1}
      NoDic_1_2_1_4_10 = Node(dic_1_2_1_4_10)
      NoDic_1_2_1_4_10.setpai(NoDic_1_2_1_4)
      #11
      dic_1_2_1_4_11= {'Resposta: Para efeitos desta lei, considera-se quadro de pessoal o conjunto de trabalhadores empregados existentes no estabelecimento do estágio. Caso a concedente conte com várias filiais ou estabelecimentos, os quantitativos devem ser aplicados a cada um deles (§§1º e 2º, do art. 17).':0,'Voltar':1}
      NoDic_1_2_1_4_11 = Node(dic_1_2_1_4_11)
      NoDic_1_2_1_4_11.setpai(NoDic_1_2_1_4)
      #12
      dic_1_2_1_4_12= {'Resposta: A manutenção de estagiários em desconformidade com esta lei caracteriza vínculo empregatício do educando com a parte concedente do estágio para todos os fins da legislação trabalhista e previdenciária. (caput do art. 15 da Lei nº 11.788/2008)':0,'Voltar':1}
      NoDic_1_2_1_4_12 = Node(dic_1_2_1_4_12)
      NoDic_1_2_1_4_12.setpai(NoDic_1_2_1_4)
      #13
      dic_1_2_1_4_13= {'Resposta: Nas hipóteses em que a concedente reincidir no descumprimento da lei, ficará impedida de receber estagiários por 2 (dois) anos, contados da data da decisão definitiva do processo administrativo correspondente. Essa penalidade limita-se à filial ou agência em que for cometida a irregularidade (§§1º e 2º do art. 15).':0,'Voltar':1}
      NoDic_1_2_1_4_13 = Node(dic_1_2_1_4_13)
      NoDic_1_2_1_4_13.setpai(NoDic_1_2_1_4)


      #campo de respostas do 1_2_1_5



      

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
   
      
