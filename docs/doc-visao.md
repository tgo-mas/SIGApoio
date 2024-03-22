# Documento de Visão

Documento construído a partido do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no
link: https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing

## Equipe e Definição de Papéis

|Membro|Papel|E-mail|
|------|-----|------|
|Anderson|Cliente, Desenvolvedor|andersonsilva14.2017@gmail.com|
|Cleomar|Desenvolvedor|cl\_jr@outlook.com|
|Ericleison|Cliente, Desenvolvedor|ericleisonrn@gmail.com|
|Marlon|Gerente|marlonsilva840@gmail.com|
|Rafael|Desenvolvedor|garciarafael.2298@gmail.com|
|Thomas|Tech Lead|talmeidasf@gmail.com|

### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
|Anderson  |Python, Django, JavaScript, Next, C.|
|Cleomar   |Excel, Python, C.                 |
|Ericleison|Python, c, JavaScript, UML, Canva.|
|Marlon    |Python, C, C++, JavaScript, SQL.  |
|Rafael    |Pytest, Postman, Excel, Jest, Mocha JS.|
|Thomas    |JavaScript, Node, React, Express, Figma, Canva, UML, C, Java, Python.|

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função.
Servidor | Este usuário utiliza o sistema para cadastrar novos usuários (bolsistas e outros servidores), gerenciamento do estoque do sistema, reservas de salas cadastradas (assim como cadastrá-las e controle do fluxo de entrada e saída de itens.)
Bolsista | O bolsista tem um acesso mais limitado ao sistema, utilizando apenas para realizar gerenciamento de estoque, juntamente com entrada e saída de itens, podendo também efetuar reservas de salas caso seja requerido por um servidor. Caso a reserva seja de algum auditório ou anfiteatro, o papel do bolsista é apenas verificar se está disponível no horário em que foi determinado, caso esteja, é repassado para o servidor do setor, e ele por sua vez, efetuará a reserva no sistema.
Chefia  | Este usuário é o Coordenador de curso ou chefe de departamento. Ele pode solicitar horários do semestre ou reservar recursos e locais.
Docente | Este usuário tem permissão para visualizar os horários e as reservas de salas. Além disso, ele pode abrir chamados e solicitar a reserva de itens antecipadamente.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | -----|
RF01 - Cadastro de usuário |Descrição: O sistema deve permitir que novos usuários se cadastrem fornecendo as seguintes informações: matrícula, nome, e-mail, senha e tipo de perfil. |Ator: Chefia/Servidor/Bolsista/Docente
RF02 - Login de usuário |Descrição: Os usuários devem ser capazes de fazer login no sistema usando suas credenciais. |Ator: Chefia/Servidor/Bolsista/Docente
RF03 - Logout de usuário |Descrição: O sistema deve fornecer uma funcionalidade para que os usuários façam logout de suas contas. |Ator: Chefia/Servidor/Bolsista/Docente
RF04 - Remoção de conta de usuário |Descrição: Os usuários devem ter a opção de remover suas contas do sistema. |Ator: Chefia/Servidor/Bolsista/Docente
RF05 - Incluir Servidor|Descrição: Um servidor tem os atributos matricula, nome, endereço, email, telefone.|Ator: Servidor
RF06 - Alterar Servidor|Descrição: A alteração permite a mudança do endereço, e-mail e telefone..|Ator: Servidor
RF07 - Listar Servidor|Descrição: Mostrar todos os servidores cadastrados no sistema em uma lista.|Ator: Servidor/Bolsista
RF08 - Visualizar Servidor|Descrição: Mostra detalhadamente os atributos do servidor selecionado. |Ator: Servidor/Bolsista
RF09 - Excluir Servidor|Descrição: Remover o servidor selecionado do sistema. |Ator: Servidor
RF10 - Incluir Bolsista|Descrição: Um bolsista tem os atributos matricula, nome, endereço, email, telefone e escala.|Ator: Servidor
RF11 - Alterar Bolsista|Descrição: Pode alterar o email, endereço e telefone. |Ator: Servidor/Bolsista
RF12 - Listar Bolsista|Descrição: Mostrar todos os bolsistas cadastrados no sistema em uma lista. |Ator: Servidor/Bolsista
RF13 - Visualizar Bolsista|Descrição: Mostrar detalhadamente os atributos do bolsista selecionado. |Ator: Servidor/Bolsista
RF14 - Excluir Bolsista|Descrição: Remover um bolsista selecionado do sistema. |Ator: Servidor
RF15 - Visualizar histórico|Descrição: Exibir o histórico dos empréstimos e reservas, aplicando filtragens e ordenações se necessário.|Ator: Servidor/Bolsista
RF16 - Incluir Recurso|Descrição: Realiza o cadastro de Adaptador HDMI, Notebook, Projetor e Caixa de Som.|Ator: Servidor
RF17 - Alterar Recurso|Descrição: Atualiza as informações de determinado recurso que há no estoque. |Ator: Servidor
RF18 - Excluir Recurso|Descrição: Exclui um recurso ou mais recursos do cadastro do sistema. |Ator: Servidor
RF19 - Exibir Estoque|Descrição: Exibe o estoque de itens que há disponível, podendo filtrar para itens que não estão disponíveis.|Ator: Servidor/Bolsista
RF20 - Visualizar Recurso|Descrição: Detalha um determinado recurso do estoque. |Ator: Servidor/Bolsista
RF21 - Registrar Saída|Descrição: O indivíduo, informa o nome do servidor ou bolsista e o pedido de itens. |Ator: Servidor/Bolsista
RF22 - Registrar Entrada|Descrição: O indivíduo devolve os itens pegos. |Ator: Servidor/Bolsista
RF23 - Cadastrar Sala|Descrição: A sala tem os atributos bloco e número. Criar uma sala também cria uma bolsa com itens predefinidos e editáveis. |Ator: Servidor
RF24 - Alterar Sala|Descrição: Pode alterar o bloco e número. |Ator: Servidor
RF25 - Excluir Sala|Descrição: Pode remover uma sala do sistema. |Ator: Servidor
RF26 - Listar Salas|Descrição: Exibe em lista todas as salas cadastradas indicando quais estão reservadas e disponíveis.|Ator: Servidor/Bolsista
RF27 - Visualizar Sala|Descrição: Exibe o horário de reserva de uma sala.|Ator: Servidor/Bolsista
RF28 - Cadastrar Laboratório|Descrição: O Laboratório tem os atributos bloco e número. Criar um Laboratório também cria uma chave com lista de autorizados editável. |Ator: Servidor
RF29 - Alterar Laboratório|Descrição: Pode alterar o bloco e número. |Ator: Servidor
RF30 - Excluir Laboratório|Descrição: Pode remover um Laboratório do sistema. |Ator: Servidor
RF31 - Listar Laboratórios|Descrição: Exibe em lista todos os Laboratórios cadastrados indicando quais estão reservados e/ou disponíveis.|Ator: Servidor/Bolsista
RF32 - Visualizar Laboratório|Descrição: Exibe os horários de reserva de um Laboratório.|Ator: Servidor/Bolsista
RF33 - Cadastrar Auditório|Descrição: O Auditório tem os atributos nome e ID. Criar um Auditório também cria uma chave com lista de autorizados editável. |Ator: Servidor
RF34 - Alterar Auditório|Descrição: Pode alterar o nome. |Ator: Servidor
RF35 - Excluir Auditório|Descrição: Pode remover um Auditório do sistema. |Ator: Servidor
RF36 - Listar Auditórios|Descrição: Exibe em lista todos os Auditórios cadastrados indicando quais estão reservados e/ou disponíveis.|Ator: Servidor/Bolsista
RF37 - Visualizar Auditório|Descrição: Exibe os horários de reserva de um Auditório.|Ator: Servidor/Bolsista
RF38 - Cadastrar Reserva de local|Descrição: Efetua a reserva de um local caso esteja disponível |Ator: Servidor
RF39 - Excluir Reserva de local|Descrição: Remoção do local da lista de reservas |Ator: Servidor
RF40 - Cadastrar Reserva de Recurso|Descrição: Efetua a reserva de um recurso caso esteja disponível |Ator: Servidor/Bolsista
RF41 - Excluir Reserva de Recurso |Descrição: Faz a exclusão de uma reserva|Ator: Servidor/Bolsista
RF42 - Relatório de reserva de locais no mês|Descrição: Exibe um relatório de todas os locais e suas reservas. |Ator: Servidor/Bolsista
RF43 - Relatório de reserva de itens no mês|Descrição: Exibe um relatório de determinados itens e suas reservas. |Ator: Servidor/Bolsista|
RF44 - Adicionar solicitação de horário| Descrição: Pode realizar a solicitação de horário.| Ator: Chefia
RF45 - Editar solicitação de horário| Descrição: Realiza a edição de solicitação em aberto.| Ator: Chefia
RF46 - Listar solicitação de horário| Descrição: Efetua a listagem de todas as solicitações cadastradas, filtrando por pendentes, canceladas, concluídas.| Ator: Chefia
RF47 - Detalhar solicitação de horário| Descrição: Exibe as informações de uma solicitação, como hora e data, horários solicitados, pessoa que solicitou.| Ator: Chefia
RF48 - Excluir solicitação de horário| Descrição: Realiza a exclusão de uma solicitação.| Ator: Chefia
RF49 - Aprovar solicitação de horário| Descrição: Efetua o deferimento ou indeferimento do horário solicitado.| Ator: Servidor
RF50 - Visualizar horários| Descrição: Permite que o docente visualize os horários disponíveis das salas de aula.| Ator: Docente.
RF51 - Abrir chamado| Descrição: Permite abrir um chamado no sistema para relatar problemas relacionados à infraestrutura, equipamentos ou outros assuntos pertinentes.| Ator: Docente.
RF52 - Solicitar reserva de itens| Descrição: Solicita a reserva antecipada de itens específicos, como equipamentos de laboratório, materiais didáticos ou outros recursos.| Ator: Docente.
RF53 - Solicitar horários do semestre| Descrição: Permite solicitar os horários do semestre ao sistema para planejamento acadêmico.| Ator:Chefia.

<!-- RF50 - Alterar bolsa|Descrição: Permite alterar a lista de itens da bolsa referente. |Ator: Servidor/Bolsista|
RF51 - Listar bolsas|Descrição: Visualizar brevemente cada bolsa, seu status e itens. |Ator: Servidor/Bolsista|
RF52 - Detalhar bolsa|Descrição: Permite visualizar os detalhes da bolsa escolhida, e sua lista de itens, bem como exercer ações sobre a lista. |Ator: Servidor/Bolsista|
RF53 - Adicionar item de bolsa |Descrição: Adiciona um determinado item ao kit de uma bolsa.| Ator: Servidor/Bolsista
RF54 - Listar itens de bolsa |Descrição: Lista os itens do kit de uma bolsa.| Ator: Servidor/Bolsista
RF55 - Remover item de bolsa |Descrição: Remove um determinado item do kit de uma bolsa.| Ator: Servidor/Bolsista
RF56 - Registrar saída de bolsa |Descrição: Registra a saída (empréstimo) de uma bolsa (bolsista, docente, horário de saída, horário de devolução).| Ator: Servidor/Bolsista
RF57 - Adicionar chave|Descrição: A chave possui seu número associado a sua sala correspondente, status e uma lista de pessoas autorizadas a pegarem a mesma. |Ator: Servidor/Bolsista
RF58 - Alterar chave|Descrição: Permite a correção de alguma informação referente a chave. |Ator: Servidor/Bolsista
RF59 - Listar chaves|Descrição: Exibe a lista de todas as chaves cadastradas e seus respectivos status. |Ator: Servidor/Bolsista
RF60 - Excluir chave|Descrição: Exclui uma chave |Ator: Servidor/Bolsista
RF50 - Adicionar autorizado|Descrição: Adicionar um usuário à lista de autorizados a pegar determinada chave. |Ator: Servidor/Bolsista
RF51 - Editar autorizado|Descrição: Editar Lista de usuários autorizados a pegar uma chave. |Ator: Servidr/Bolsista
RF52 - Listar autorizados|Descrição: Listar usuários autorizados a pegar determinada chave. |Ator: Servidor/Bolsista
RF53 - Excluir autorizado|Descrição: Excluir um usuário à lista de autorizados a pegar determinada chave. |Ator: Servidor/Bolsista
RF54 - Incluir saída de chave|Descrição: Registra uma saída de chave, alterando o status da mesma. |Ator: Servidor/Bolsista
RF55 - Editar saída de chave|Descrição: Permite corrigir uma saída de chave com algum erro. |Ator: Servidor/Bolsista
RF56 - Listar saída de chave|Descrição: Exibe uma lista das chaves que já foram pegas. |Ator: Servidor/Bolsista
RF57 - Excluir saída de chave|Descrição: Registra uma devolução de chave, alterando seu status. |Ator: Servidor/Bolsista -->

### Modelo Conceitual

[Modelo Entidade-Relacionamento do SIGApoio](./er-model.md)

#### Descrição das Entidades

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF01 - Deve ser acessível via navegador. | Deve funcionar no Chrome e Firefox.
RNF02 - Deve ser multiplataforma. | Deve funcionar no Linux, Windows e Android
RNF03 - Deve ser feito o log de ações dos usuários. | As ações dos usuários serão registradas.
RNF04 - Deve ser responsivo. | Responder corretamente a diferentes tamanhos de tela.
RNF05 - Deve manter o histórico de registros em Banco de Dados. | Será usado o SGBD PostgreSQL para armazenar os dados.
RNF06 - Deve ter diferentes níveis de permissões para cada perfil. | Cada perfil de usuário terá acesso apenas às funcionalidades e dados relevantes às suas responsabilidades e autorizações.

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
29/02/2024 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
|04/12/2023|Não aprendizado da ferramenta pelos servidores e bolsistas do setor|Alta|Servidor|Vigente|Reforçar estudos sobre a ferramenta e workshops para melhor uso desta.|
|04/12/2023|Não devolução integral pelo requerente do recurso emprestado.|Alta|Servidor/ Bolsista|Vigente|Vincular contato do requerente para envio de lembrete do prazo de devolução.|
|04/12/2023|Falta de salas disponíveis para reserva no horário requisitado pelo servidor no horário da reserva..|Baixa|Servidor/ Bolsista|Vigente|Estímulo pelo servidor à reserva de salas ou horários não requisitados.
|05/12/2023|Falta de conectividade à Internet no Campus.|Média|Todos|Vigente|Registro em papel das ocorrências, atualizando o banco de dados posteriormente.|

### Referências

MAXIM, B. R.; PRESSMAN, Roger S. Engenharia de software: uma abordagem profissional. 2021.

[Site oficial do PostgreSQL](https://www.postgresql.org)

[Site oficial do Django Framework](https://www.djangoproject.com)
