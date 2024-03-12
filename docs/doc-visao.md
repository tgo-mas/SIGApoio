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
|Anderson  |Desenvolvedor JavaScript, Next, C.|
|Cleomar   |Excel, Postman.                   |
|Ericleison|Python, c, JavaScript, UML, Canva.|
|Marlon    |Python, C, C++, JavaScript, SQL.  |
|Rafael    |Pytest, Postman, Excel, Jest, Mocha JS.|
|Thomas    |JavaScript, Node, React, Express, Figma, Canva, UML, C, Java.|

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função.
Servidor | Este usuário utiliza o sistema para cadastrar novos usuários (bolsistas e outros servidores), gerenciamento do estoque do sistema, reservas de salas cadastradas (assim como cadastrá-las e controle do fluxo de entrada e saída de itens.)
Bolsista | O bolsista tem um acesso mais limitado ao sistema, utilizando apenas para realizar gerenciamento de estoque, juntamente com entrada e saída de itens, podendo também efetuar reservas de salas caso seja requerido por um servidor. Caso a reserva seja de algum auditório ou anfiteatro, o papel do bolsista é apenas verificar se está disponível no horário em que foi determinado, caso esteja, é repassado para o servidor do setor, e ele por sua vez, efetuará a reserva no sistema.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | -----|
RF01 - Incluir Servidor|Descrição: Um servidor tem os atributos matricula, nome, endereço, email, telefone.|Ator: Servidor
RF02 - Alterar Servidor|Descrição: A alteração permite a mudança do endereço, e-mail e telefone..|Ator: Servidor
RF03 - Listar Servidor|Descrição: Mostrar todos os servidores cadastrados no sistema em uma lista.|Ator: Servidor/Bolsista
RF04 - Visualizar Servidor|Descrição: Mostra detalhadamente os atributos do servidor selecionado. |Ator: Servidor/Bolsista
RF05 - Excluir Servidor|Descrição: Remover o servidor selecionado do sistema. |Ator: Servidor
RF06 - Incluir Bolsista|Descrição: Um bolsista tem os atributos matricula, nome, endereço, email, telefone e escala.|Ator: Servidor
RF07 - Alterar Bolsista|Descrição: Pode alterar o email, endereço e telefone. |Ator: Servidor/Bolsista
RF08 - Listar Bolsista|Descrição: Mostrar todos os bolsistas cadastrados no sistema em uma lista. |Ator: Servidor/Bolsista
RF09 - Visualizar Bolsista|Descrição: Mostrar detalhadamente os atributos do bolsista selecionado. |Ator: Servidor/Bolsista
RF10 - Excluir Bolsista|Descrição: Remover um bolsista selecionado do sistema. |Ator: Servidor
RF11 - Visualizar histórico|Descrição: Exibir o histórico dos empréstimos e reservas, aplicando filtragens e ordenações se necessário.|Ator: Servidor/Bolsista
RF12 - Incluir Recurso|Descrição: Realiza o cadastro de Adaptador HDMI, Notebook, Projetor e Caixa de Som.|Ator: Servidor
RF13 - Alterar Recurso|Descrição: Atualiza as informações de determinado recurso que há no estoque. |Ator: Servidor
RF14 - Excluir Recurso|Descrição: Exclui um recurso ou mais recursos do cadastro do sistema. |Ator: Servidor
RF15 - Exibir Estoque|Descrição: Exibe o estoque de itens que há disponível, podendo filtrar para itens que não estão disponíveis.|Ator: Servidor/Bolsista
RF16 - Visualizar Recurso|Descrição: Detalha um determinado recurso do estoque. |Ator: Servidor/Bolsista
RF17 - Registrar Saída|Descrição: O indivíduo, informa o nome do servidor ou bolsista e o pedido de itens. |Ator: Servidor/Bolsista
RF18 - Registrar Entrada|Descrição: O indivíduo devolve os itens pegos. |Ator: Servidor/Bolsista
RF19 - Cadastrar Sala|Descrição: A sala tem os atributos bloco e número. Criar uma sala também cria uma bolsa com itens predefinidos e editáveis. |Ator: Servidor
RF20 - Alterar Sala|Descrição: Pode alterar o bloco e número. |Ator: Servidor
RF21 - Excluir Sala|Descrição: Pode remover uma sala do sistema. |Ator: Servidor
RF22 - Listar Salas|Descrição: Exibe em lista todas as salas cadastradas indicando quais estão reservadas e disponíveis.|Ator: Servidor/Bolsista
RF23 - Visualizar Sala|Descrição: Exibe o horário de reserva de uma sala.|Ator: Servidor/Bolsista
RF24 - Cadastrar Reserva de Sala|Descrição: Efetua a reserva de uma sala caso esteja disponível |Ator: Servidor
RF25 - Excluir Reserva de Sala|Descrição: Remoção da sala da lista de reservas |Ator: Servidor
RF26 - Cadastrar Reserva de Recurso|Descrição: Efetua a reserva de um recurso caso esteja disponível |Ator: Servidor/Bolsista
RF27 - Excluir Reserva de Recurso |Descrição: Faz a exclusão de uma reserva|Ator: Servidor/Bolsista
RF28 - Relatório de reserva de salas no mês|Descrição: Exibe um relatório de todas as salas e suas reservas. |Ator: Servidor/Bolsista
RF29 - Relatório de reserva de itens no mês|Descrição: Exibe um relatório de determinados itens e suas reservas. |Ator: Servidor/Bolsista|
RF30 - Adicionar solicitação de horário| Descrição: Pode realizar a solicitação de horário.| Ator: Chefia
RF31 - Editar solicitação de horário| Descrição: Realiza a edição de solicitação em aberto.| Ator: Chefia
RF32 - Listar solicitação de horário| Descrição: Efetua a listagem de todas as solicitações cadastradas, filtrando por pendentes, canceladas, concluídas.| Ator: Chefia
RF33 - Detalhar solicitação de horário| Descrição: Exibe as informações de uma solicitação, como hora e data, horários solicitados, pessoa que solicitou.| Ator: Chefia
RF34 - Excluir solicitação de horário| Descrição: Realiza a exclusão de uma solicitação.| Ator: Chefia
RF35 - Aprovar solicitação de horário| Descrição: Efetua o deferimento ou indeferimento do horário solicitado.| Ator: Servidor
RF36 - Alterar bolsa|Descrição: Permite alterar a lista de itens da bolsa referente. |Ator: Servidor/Bolsista|
RF37 - Listar bolsas|Descrição: Visualizar brevemente cada bolsa, seu status e itens. |Ator: Servidor/Bolsista|
RF38 - Detalhar bolsa|Descrição: Permite visualizar os detalhes da bolsa escolhida, e sua lista de itens, bem como exercer ações sobre a lista. |Ator: Servidor/Bolsista|
RF39 - Adicionar item de bolsa |Descrição: Adiciona um determinado item ao kit de uma bolsa.| Ator: Servidor/Bolsista
RF40 - Listar itens de bolsa |Descrição: Lista os itens do kit de uma bolsa.| Ator: Servidor/Bolsista
RF41 - Remover item de bolsa |Descrição: Remove um determinado item do kit de uma bolsa.| Ator: Servidor/Bolsista
RF42 - Registrar saída de bolsa |Descrição: Registra a saída (empréstimo) de uma bolsa (bolsista, docente, horário de saída, horário de devolução).| Ator: Servidor/Bolsista


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