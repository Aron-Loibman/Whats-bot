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

         
       
class Tree:

   def __init__(self):
      #region 1º nivel, Raiz e primeiro nó
      self.root =  {'Olá sou o UnicapBot, em quais das categorias a seguir eu poderia lhe auxiliar?'}
      global rootNode
      rootNode = Node(self.root) #criação do nó raiz
  
      dic_1= {'Coordenação': 1,'Estágio': 2, 'Pesquisa': 3, 'Extensão': 4} 
      NoDic_1 = Node(dic_1) #criação do primeiro nó
      rootNode.setfilhos(NoDic_1) #nó se torna filho da raiz
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
      #OBS: nós respostas não possuem filhos
      
      #region campo de respostas do 1_2_1_1
      #1
      dic_1_2_1_1_1= {'Resposta: Estágio é ato educativo escolar supervisionado, desenvolvido no ambiente de trabalho, que visa à preparação para o trabalho produtivo de estudantes. O estágio integra o itinerário formativo do estudante e faz parte do projeto pedagógico do curso (art. 1º).':0,'Voltar':1}
      NoDic_1_2_1_1_1 = Node(dic_1_2_1_1_1)
      NoDic_1_2_1_1_1.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_1)
      #2
      dic_1_2_1_1_2= {'Resposta: Estágio obrigatório, que é aquele definido como tal no projeto do curso, cuja carga horária é requisito para aprovação e obtenção do diploma, e estágio não obrigatório, que é aquele desenvolvido como atividade opcional, acrescida à carga horária regular e obrigatória (§§ 1º e 2º do art. 2º).':0,'Voltar':1}
      NoDic_1_2_1_1_2 = Node(dic_1_2_1_1_2)
      NoDic_1_2_1_1_2.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_2)
      #3
      dic_1_2_1_1_3= {'Resposta: estudantes que estejam frequentando o ensino regular em instituições de educação superior, de educação profissional, de ensino médio, da educação especial e dos anos finais do ensino fundamental, na modalidade profissional da educação de jovens e adultos (art. 1º).':0,'Voltar':1}
      NoDic_1_2_1_1_3 = Node(dic_1_2_1_1_3)
      NoDic_1_2_1_1_3.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_3)
      #4
      dic_1_2_1_1_4= {'Resposta: sim, desde que o estudante estrangeiro esteja regularmente matriculado em curso superior no país autorizado ou reconhecido e seja observado o prazo do visto temporário de estudante, na forma da legislação aplicável (art. 4º).':0,'Voltar':1}
      NoDic_1_2_1_1_4 = Node(dic_1_2_1_1_4)
      NoDic_1_2_1_1_4.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_4)
      #5
      dic_1_2_1_1_5= {'Resposta: o estágio é regido por legislação própria e, desde que observados os requisitos legais e as obrigações contidas no termo de compromisso de estágio, não estabelece vínculo empregatício de qualquer natureza, para todos os fins da legislação trabalhista e previdenciária (caput e § 2º do art. 3º c/c art. 15).':0,'Voltar':1}
      NoDic_1_2_1_1_5 = Node(dic_1_2_1_1_5)
      NoDic_1_2_1_1_5.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_5)
      #6
      dic_1_2_1_1_6= {'Resposta: para formação da relação de estágio, devem ser observados os seguintes requisitos: a) matrícula e frequência regular do estudante público-alvo da lei; b) celebração do termo de compromisso entre o estudante, a parte concedente do estágio e a instituição de ensino; e c) compatibilidade entre as atividades desenvolvidas no estágio e as previstas no termo de compromisso. (incisos, I, II, III do art. 3º).':0,'Voltar':1}
      NoDic_1_2_1_1_6 = Node(dic_1_2_1_1_6)
      NoDic_1_2_1_1_6.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_6)
      #7
      dic_1_2_1_1_7= {'Resposta: sim, desde que previstas no projeto pedagógico do curso (§ 3º do art. 2º).':0,'Voltar':1}
      NoDic_1_2_1_1_7 = Node(dic_1_2_1_1_7)
      NoDic_1_2_1_1_7.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_7)
      #8
      dic_1_2_1_1_8= {'Resposta: sim. Não há nenhum empecilho da estudante gestante estagiar. Como todo estágio, sujeita-se às regras da Lei 11.788/08.':0,'Voltar':1}
      NoDic_1_2_1_1_8 = Node(dic_1_2_1_1_8)
      NoDic_1_2_1_1_8.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_8)
      #9
      dic_1_2_1_1_9= {'Resposta: não há obrigatoriedade para a expedição e anotação do estágio na Carteira de Trabalho e Previdência Social, uma vez que estágio não é emprego, sendo definido em legislação própria.':0,'Voltar':1}
      NoDic_1_2_1_1_9 = Node(dic_1_2_1_1_9)
      NoDic_1_2_1_1_9.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_9)
      #10
      dic_1_2_1_1_10= {'Resposta: Pendente':0,'Voltar':1}
      NoDic_1_2_1_1_10 = Node(dic_1_2_1_1_10)
      NoDic_1_2_1_1_10.setpai(NoDic_1_2_1_1)
      NoDic_1_2_1_1.setfilhos(NoDic_1_2_1_1_10)
      #endregion
      #region campo de respostas do 1_2_1_2
      #1
      dic_1_2_1_2_1= {'Resposta: É o setor cujo objetivo é desenvolver as habilidades dos alunos voltadas para suas atuações no mercado de trabalho. A agência experimental tem uma organização semelhante à das agências reais do mercado, com cargos direcionados para atividades específicas, planejamento, projetos e prazos a serem cumpridos.':0,'Voltar':1}
      NoDic_1_2_1_2_1 = Node(dic_1_2_1_2_1)
      NoDic_1_2_1_2_1.setpai(NoDic_1_2_1_2)
      NoDic_1_2_1_2.setfilhos(NoDic_1_2_1_2_1)
      #2
      dic_1_2_1_2_2= {'Resposta: A cada semestre a CGE enviará email para os alunos informando a abertura das vagas para trabalhar na agência experimental, há possibilidade de cumprir as horas de estágio sendo não obrigatório, porém será dada prioridade aos alunos concluintes na categoria estágio obrigatório.':0,'Voltar':1}
      NoDic_1_2_1_2_2 = Node(dic_1_2_1_2_2)
      NoDic_1_2_1_2_2.setpai(NoDic_1_2_1_2)
      NoDic_1_2_1_2.setfilhos(NoDic_1_2_1_2_2)
      #3
      dic_1_2_1_2_3= {'Resposta: Sim, o estágio na agência experimental é presencial, abrindo apenas exceções remotas em casos de calamidade pública.':0,'Voltar':1}
      NoDic_1_2_1_2_3 = Node(dic_1_2_1_2_3)
      NoDic_1_2_1_2_3.setpai(NoDic_1_2_1_2)
      NoDic_1_2_1_2.setfilhos(NoDic_1_2_1_2_3)
      #4
      dic_1_2_1_2_4= {'Resposta: Não':0,'Voltar':1}
      NoDic_1_2_1_2_4 = Node(dic_1_2_1_2_4)
      NoDic_1_2_1_2_4.setpai(NoDic_1_2_1_2)
      NoDic_1_2_1_2.setfilhos(NoDic_1_2_1_2_4)
      #5
      dic_1_2_1_2_5= {'Resposta: Em sua maioria tem funções relacionadas a planejamento e desenvolvimento de projetos contendo prazos a serem cumpridos, é uma experiência que se equivale a adquirida em uma empresa júnior.':0,'Voltar':1}
      NoDic_1_2_1_2_5 = Node(dic_1_2_1_2_5)
      NoDic_1_2_1_2_5.setpai(NoDic_1_2_1_2)
      NoDic_1_2_1_2.setfilhos(NoDic_1_2_1_2_5)
      #endregion
      #region campo de respostas do 1_2_1_3
      #1
      dic_1_2_1_3_1= {'Resposta: sim. As instituições de ensino e as partes concedentes de estágio podem, mediante condições acordadas em instrumento jurídico apropriado, recorrer aos serviços de agentes de integração públicos e privados. Em caso de contratação com recursos públicos, deverá ser observada a legislação de licitação, Lei no. 8.666/1993 (caput do art. 5º).':0,'Voltar':1}
      NoDic_1_2_1_3_1 = Node(dic_1_2_1_3_1)
      NoDic_1_2_1_3_1.setpai(NoDic_1_2_1_3)
      NoDic_1_2_1_3.setfilhos(NoDic_1_2_1_3_1)
      #2
      dic_1_2_1_3_2= {'Resposta: Cabe ao agente de integração, como auxiliar no processo de aperfeiçoamento do estágio:  a) identificar as oportunidades de estágio;   b) ajustar suas condições de realização;   c) fazer o acompanhamento administrativo;   d) encaminhar negociação de seguros contra acidentes pessoais;  e) Cadastrar os estudantes. (incisos de I a V do § 1º, do art. 5º).  Os agentes de integração podem, ainda, selecionar os locais de estágio e organizar o cadastro dos concedentes das oportunidades de estágio. (art. 6º)':0,'Voltar':1}
      NoDic_1_2_1_3_2 = Node(dic_1_2_1_3_2)
      NoDic_1_2_1_3_2.setpai(NoDic_1_2_1_3)
      NoDic_1_2_1_3.setfilhos(NoDic_1_2_1_3_2)
      #3
      dic_1_2_1_3_3= {'Resposta: Não. É vedada a cobrança de qualquer valor aos estudantes, a título de remuneração pelos serviços dos agentes de integração, previstos na lei (§ 2º do art. 5º).':0,'Voltar':1}
      NoDic_1_2_1_3_3 = Node(dic_1_2_1_3_3)
      NoDic_1_2_1_3_3.setpai(NoDic_1_2_1_3)
      NoDic_1_2_1_3.setfilhos(NoDic_1_2_1_3_3)
      #4
      dic_1_2_1_3_4= {'Resposta: Sim. Os agentes de integração serão responsabilizados civilmente se indicarem estagiários:  a) para atividades não compatíveis com a programação curricular do curso;  b) que estejam frequentando cursos em instituições de ensino para quais não há  previsão de estágio curricular. (§ 3º do art. 5º).':0,'Voltar':1}
      NoDic_1_2_1_3_4 = Node(dic_1_2_1_3_4)
      NoDic_1_2_1_3_4.setpai(NoDic_1_2_1_3)
      NoDic_1_2_1_3.setfilhos(NoDic_1_2_1_3_4)
      #5
      dic_1_2_1_3_5= {'Resposta: Não. O termo de compromisso deve ser firmado pelo estagiário ou com seu representante ou assistente legal e pelos representantes legais da parte concedente e da instituição de ensino, vedada a atuação dos agentes de integração como representante de qualquer das partes (art. 16).':0,'Voltar':1}
      NoDic_1_2_1_3_5 = Node(dic_1_2_1_3_5)
      NoDic_1_2_1_3_5.setpai(NoDic_1_2_1_3)
      NoDic_1_2_1_3.setfilhos(NoDic_1_2_1_3_5)
      #endregion
      #region campo de respostas do 1_2_1_4
      #1
      dic_1_2_1_4_1= {'Resposta:  As pessoas jurídicas de direito privado e os órgãos da administração pública direta, autárquica e fundacional de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios e os profissionais liberais de nível superior, devidamente registrados em seus respectivos conselhos de fiscalização profissional (caput do art. 9º).':0,'Voltar':1}
      NoDic_1_2_1_4_1 = Node(dic_1_2_1_4_1)
      NoDic_1_2_1_4_1.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_1)
      #2
      dic_1_2_1_4_2= {'Resposta: São obrigações da concedente de estágio:  a) celebrar termo de compromisso com a instituição de ensino e com o estudante, zelando por seu cumprimento;  b) ofertar instalações que tenham condições de proporcionar ao estudante atividades de aprendizagem social, profissional e cultural;  c) indicar funcionário de seu quadro de pessoal, com formação ou experiência profissional na área de conhecimento desenvolvida no curso do estagiário, para orientar e supervisionar até 10 (dez) estagiários simultaneamente;  d) contratar em favor do estagiário seguro contra acidentes pessoais, cuja apólice seja compatível com valores de mercado, conforme fique estabelecido no termo de compromisso, podendo, alternativamente, na hipótese de estágio obrigatório, ser assumida pela instituição de ensino;  e) entregar termo de realização do estágio com indicação resumida das atividades desenvolvidas, dos períodos e da avaliação de desempenho por ocasião do desligamento do estagiário;  f) manter à disposição da fiscalização documentos que comprovem a relação de estágio;  g) enviar à instituição de ensino, com periodicidade mínima de 6 (seis) meses, relatório de atividades, com vista obrigatória ao estagiário;   h) implementar a legislação relacionada à saúde e à segurança do trabalho a ser aplicada ao estagiário.(incisos I a VII e parágrafo único do art. 9º e art. 14).':0,'Voltar':1}
      NoDic_1_2_1_4_2 = Node(dic_1_2_1_4_2)
      NoDic_1_2_1_4_2.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_2)
      #3
      dic_1_2_1_4_3= {'Resposta: Não. A celebração de convênio de concessão de estágio entre a instituição de ensino e a parte concedente não dispensa a celebração do termo de compromisso de estágio (parágrafo único do art. 8º).':0,'Voltar':1}
      NoDic_1_2_1_4_3 = Node(dic_1_2_1_4_3)
      NoDic_1_2_1_4_3.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_3)
      #4
      dic_1_2_1_4_4= {'Resposta: A duração do estágio, na mesma unidade concedente, não poderá exceder 2 (dois) anos, exceto quando se tratar de estagiário portador de deficiência (art. 11).':0,'Voltar':1}
      NoDic_1_2_1_4_4 = Node(dic_1_2_1_4_4)
      NoDic_1_2_1_4_4.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_4)
      #5
      dic_1_2_1_4_5= {'Resposta: Sim. A eventual concessão de benefícios relacionados a transporte, alimentação e saúde, entre outros, não caracteriza vínculo empregatício para todos os fins da legislação trabalhista e da previdenciária (§ 1º do art. 12).':0,'Voltar':1}
      NoDic_1_2_1_4_5 = Node(dic_1_2_1_4_5)
      NoDic_1_2_1_4_5.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_5)
      #6
      dic_1_2_1_4_6= {'Resposta: Sim. A remuneração das atividades de estágio, por meio de bolsa ou outra forma de contraprestação, pressupõe o cumprimento das atividades previstas no termo de compromisso de estágio. Ausências eventuais, devidamente justificadas, poderão ser objetos de entendimento entre as partes, e poderão, na forma acordada, deixar de ser descontadas. (Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_1_4_6 = Node(dic_1_2_1_4_6)
      NoDic_1_2_1_4_6.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_6)
      #7
      dic_1_2_1_4_7= {'Resposta: Não. O estagiário, porém, pode inscrever-se e contribuir como segurado facultativo da Previdência Social (§ 2º do art. 12).':0,'Voltar':1}
      NoDic_1_2_1_4_7 = Node(dic_1_2_1_4_7)
      NoDic_1_2_1_4_7.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_7)
      #8
      dic_1_2_1_4_8= {'Resposta: Sim. O Termo de Compromisso de Estágio pode ser rescindido unilateralmente pelas partes e a qualquer momento. (Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_1_4_8 = Node(dic_1_2_1_4_8)
      NoDic_1_2_1_4_8.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_8)
      #9
      dic_1_2_1_4_9= {'Resposta: Sim. Para os estágios de ensino médio, de educação especial e dos anos finais do ensino fundamental, na modalidade profissional da educação de jovens e adultos. Nesses casos, o número máximo de estagiários deverá atender às seguintes proporções, em relação ao quadro de pessoal de concedente:  a) de 1 (um) a 5 (cinco) empregados: 1 (um) estagiário;  b) de 6 (seis) a 10 (dez) empregados: até 2 (dois) estagiários;  c) de 11 (onze) a 25 (vinte e cinco) empregados: até 5 (cinco) estagiários;   d) acima de 25 (vinte e cinco) empregados, até 20% (vinte por cento) de estagiários (inciso I a IV do art. 17).  Quando esse cálculo resultar em fração, poderá ser arredondado para o número inteiro imediatamente superior (§ 3º do art. 17)':0,'Voltar':1}
      NoDic_1_2_1_4_9 = Node(dic_1_2_1_4_9)
      NoDic_1_2_1_4_9.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_9)
      #10
      dic_1_2_1_4_10= {'Resposta: Não. Essa limitação não se aplica aos estágios de nível superior e de nível médio profissional.':0,'Voltar':1}
      NoDic_1_2_1_4_10 = Node(dic_1_2_1_4_10)
      NoDic_1_2_1_4_10.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_10)
      #11
      dic_1_2_1_4_11= {'Resposta: Para efeitos desta lei, considera-se quadro de pessoal o conjunto de trabalhadores empregados existentes no estabelecimento do estágio. Caso a concedente conte com várias filiais ou estabelecimentos, os quantitativos devem ser aplicados a cada um deles (§§1º e 2º, do art. 17).':0,'Voltar':1}
      NoDic_1_2_1_4_11 = Node(dic_1_2_1_4_11)
      NoDic_1_2_1_4_11.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_11)
      #12
      dic_1_2_1_4_12= {'Resposta: A manutenção de estagiários em desconformidade com esta lei caracteriza vínculo empregatício do educando com a parte concedente do estágio para todos os fins da legislação trabalhista e previdenciária. (caput do art. 15 da Lei nº 11.788/2008)':0,'Voltar':1}
      NoDic_1_2_1_4_12 = Node(dic_1_2_1_4_12)
      NoDic_1_2_1_4_12.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_12)
      #13
      dic_1_2_1_4_13= {'Resposta: Nas hipóteses em que a concedente reincidir no descumprimento da lei, ficará impedida de receber estagiários por 2 (dois) anos, contados da data da decisão definitiva do processo administrativo correspondente. Essa penalidade limita-se à filial ou agência em que for cometida a irregularidade (§§1º e 2º do art. 15).':0,'Voltar':1}
      NoDic_1_2_1_4_13 = Node(dic_1_2_1_4_13)
      NoDic_1_2_1_4_13.setpai(NoDic_1_2_1_4)
      NoDic_1_2_1_4.setfilhos(NoDic_1_2_1_4_13)
      #endregion
      # PENDENTE campo de respostas do 1_2_1_5
      
      #region campo de respostas do 1_2_2
      #1
      dic_1_2_2_1 = {'Resposta: sim. O estágio como ato educativo escolar supervisionado deve ter acompanhamento efetivo pelo professor orientador da instituição de ensino e pelo supervisor da parte concedente, comprovado por vistos nos relatórios de atividades (em prazo não superior a seis meses) e por menção de aprovação final (§ 1º do art. 3º). O supervisor da parte concedente somente pode orientar e supervisionar até 10 (dez) estagiários simultaneamente (inciso III, do art. 9º).':0,'Voltar':1}
      NoDic_1_2_2_1 = Node(dic_1_2_2_1)
      NoDic_1_2_2_1.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_1)
      #2
      dic_1_2_2_2 = {'Resposta: A jornada de atividade em estágio não deve ultrapassar:  a) 4 (quatro) horas diárias e 20 (vinte) horas semanais, no caso de estudantes de educação especial e dos anos finais do ensino fundamental, na modalidade de educação de jovens e adultos;  b) 6 (seis) horas diárias e 30 (trinta) horas semanais, no caso de estudantes do ensino superior, da educação profissional de nível médio e do ensino médio regular;  c) 40 (quarenta) horas semanais, no caso do estágio relativo a cursos que alternam teoria e prática, nos períodos em que não estão programadas aulas presenciais, desde que previsto no projeto pedagógico do curso e da instituição de ensino (incisos I, II e § 1º do art. 10).':0,'Voltar':1}
      NoDic_1_2_2_2 = Node(dic_1_2_2_2)
      NoDic_1_2_2_2.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_2)
      #3
      dic_1_2_2_3 = {'Resposta: A concessão do descanso durante a jornada de estágio deve ser definida de comum acordo entre a instituição de ensino, a parte concedente e o estudante ou seu assistente ou representante legal, devendo constar do termo de compromisso de estágio. Recomenda-se a observância de período suficiente à preservação da saúde física e mental do estagiário e respeito aos padrões de horário de alimentação – lanche, almoço e jantar. O período de intervalo não é computado na jornada de estágio. (Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_2_3 = Node(dic_1_2_2_3)
      NoDic_1_2_2_3.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_3)
      #4
      dic_1_2_2_4 = {'Resposta: sim, caso a instituição de ensino adote verificações de aprendizagem periódicas ou finais nos períodos de avaliação, a carga horária do estágio será reduzida pelo menos à metade, segundo o estipulado no termo de compromisso de estágio. Nesse caso, a instituição de ensino deverá comunicar à parte concedente do estágio, no início do período letivo, as datas de realização de avaliações escolares ou acadêmicas (§ 2º do art. 10 e inciso VII do art. 7º).':0,'Voltar':1}
      NoDic_1_2_2_4 = Node(dic_1_2_2_4)
      NoDic_1_2_2_4.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_4)
      #5
      dic_1_2_2_5 = {'Resposta: No caso do estágio não obrigatório, é compulsória a concessão de bolsa ou outra forma de contraprestação que venha a ser acordada no termo de compromisso do estágio. Somente no caso de estágio obrigatório é que a concessão de bolsa ou outra forma de contraprestação é facultativa. (art. 12).':0,'Voltar':1}
      NoDic_1_2_2_5 = Node(dic_1_2_2_5)
      NoDic_1_2_2_5.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_5)
      #6
      dic_1_2_2_6 = {'Resposta: No caso do estágio não obrigatório, é compulsória a concessão de auxílio-transporte. No caso de estágio obrigatório, a concessão de auxílio transporte é facultativa (art. 12).':0,'Voltar':1}
      NoDic_1_2_2_6 = Node(dic_1_2_2_6)
      NoDic_1_2_2_6.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_6)
      #7
      dic_1_2_2_7 = {'Resposta: sim. É assegurado ao estagiário, sempre que o estágio tenha duração igual ou superior a 1 (um) ano, período de recesso de 30 (trinta) dias. Nos casos de o estágio ter duração inferior a 1 (um) ano, os dias de recesso serão concedidos de maneira proporcional. O recesso deve ser gozado, preferencialmente, durante as férias escolares (caput e § 2º do art. 13).  O recesso poderá ser concedido em período contínuo ou fracionado, conforme estabelecido no termo de compromisso de estágio (Cartilha Esclarecedora sobre a Lei de Estágio/ MTE).':0,'Voltar':1}
      NoDic_1_2_2_7 = Node(dic_1_2_2_7)
      NoDic_1_2_2_7.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_7)
      #8
      dic_1_2_2_8 = {'Resposta: O recesso deve ser remunerado somente quando o estagiário receber bolsa ou outra forma da contraprestação (§1º do art.13).':0,'Voltar':1}
      NoDic_1_2_2_8 = Node(dic_1_2_2_8)
      NoDic_1_2_2_8.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_8)
      #9
      dic_1_2_2_9 = {'Resposta: Sim. Devem ser tomados os cuidados necessários para a promoção da saúde e prevenção de doenças e acidentes, considerando, principalmente, os riscos decorrentes de fatores relacionados aos ambientes, condições e formas de organização do trabalho. Sua implementação é de responsabilidade da parte concedente do estágio. (art. 14º Lei 11.788/2008 e Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_2_9 = Node(dic_1_2_2_9)
      NoDic_1_2_2_9.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_9)
      #10
      dic_1_2_2_10 = {'Resposta: sim. O seguro deve abranger acidentes pessoais ocorridos com o estudante durante o período de vigência do estágio, 24 (vinte e quatro) horas/dia, no território nacional, assim como morte ou invalidez permanente, total ou parcial, provocada por acidente. O valor da indenização deve constar do Certificado Individual de Seguro de Acidentes Pessoais e deve ser compatível com os valores de mercado. (Cartilha Esclarecedora sobre a Lei de Estágio/ MTE).':0,'Voltar':1}
      NoDic_1_2_2_10 = Node(dic_1_2_2_10)
      NoDic_1_2_2_10.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_10)
      #11
      dic_1_2_2_11 = {'Resposta: O termo de compromisso de estágio – TCE – é um acordo tripartite celebrado entre o estudante, a parte concedente do estágio e a instituição de ensino, prevendo as condições de adequação do estágio à proposta pedagógica do curso, à etapa e à modalidade da formação escolar do estudante e ao horário e calendário escolar. (Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_2_11 = Node(dic_1_2_2_11)
      NoDic_1_2_2_11.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_11)
      #12
      dic_1_2_2_12 = {'Resposta: devem constar, no Termo de Compromisso, todas as cláusulas que nortearão o termo de compromisso de estágio, tais como:  a) dados de identificação das partes, inclusive cargo e função do supervisor do estágio da parte concedente e do orientador da instituição de ensino;  b) as responsabilidades de cada uma das partes;  c) objetivo do estágio;  d) definição da área do estágio;  e) plano de atividades do estágio com vigência;  f) a jornada de atividades do estagiário;  g) a definição do intervalo na jornada diária, se for o caso;  h) vigência do termo de compromisso do estágio;  i) período de concessão do recesso, que deve ocorrer na vigência do estágio, destacando sua concessão de forma contínua ou fracionada;  j) valor da bolsa, ou outra forma de contraprestação;  k) valor do auxílio-transporte, ou sua substituição por transporte próprio da empresa;  l) outros benefícios a serem concedidos ao estagiário, quando for o caso;  m) o número da apólice e a companhia de seguros;  n) motivos de rescisão. (Cartilha Esclarecedora sobre a Lei de Estágio/ MTE).':0,'Voltar':1}
      NoDic_1_2_2_12 = Node(dic_1_2_2_12)
      NoDic_1_2_2_12.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_12)
      #13
      dic_1_2_2_13 = {'Resposta: sim. O plano de atividades do estagiário, elaborado de comum acordo entre o estudante, a parte concedente e a instituição de ensino, deve ser incorporado ao termo de compromisso de estágio. E, à medida que for avaliado, progressivamente, o desempenho do estudante, deve ser incorporado ao termo de compromisso por meio de aditivos (parágrafo único do art. 7º).':0,'Voltar':1}
      NoDic_1_2_2_13 = Node(dic_1_2_2_13)
      NoDic_1_2_2_13.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_13)
      #14
      dic_1_2_2_14 = {'Resposta: sim. O Termo de Compromisso de Estágio pode ser rescindido unilateralmente pelas partes e a qualquer momento. (Cartilha Esclarecedora sobre a Lei de Estágio/MTE).':0,'Voltar':1}
      NoDic_1_2_2_14 = Node(dic_1_2_2_14)
      NoDic_1_2_2_14.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_14)
      #15
      dic_1_2_2_15 = {'Resposta: a) o termo de compromisso de estágio, devidamente assinado pela empresa concedente, pela instituição de ensino e pelo estudante;  b) o certificado individual de seguro de acidentes pessoais;  c) comprovação da regularidade da situação escolar do estudante;  d) comprovante de pagamento da bolsa ou equivalente e do auxílio-transporte;  e) verificação da compatibilidade entre as atividades desenvolvidas no estágio e aquelas previstas no termo de compromisso. (Cartilha Esclarecedora sobre a Lei de Estágio / MTE).':0,'Voltar':1}
      NoDic_1_2_2_15 = Node(dic_1_2_2_15)
      NoDic_1_2_2_15.setpai(NoDic_1_2_2)
      NoDic_1_2_2.setfilhos(NoDic_1_2_2_15)
      #endregion
      #endregion

   def getroot(self):
      return rootNode

   def BackOp(self,No):
      a = No
      b = a.getpai()
      return b

   def NextNode(self, NoEntrada, NumFilho):   
      a = NoEntrada  # a contem o nó enviado
      NumFilho = NumFilho - 1 # o numeração da lista começa em 0, o numero recebido vai ser 1 a mais que na lista
      b = a.getfilhos()    # b contem a lista de filhos
      c = b[NumFilho]      # c contem nó filho desejado 
      return c      