# Documento Lista de User Stories

[Link para o documento](https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing)

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 22/06/2020 | 0.0.1   | Template e descrição do documento  | Taciano |
| 05/12/2023 | 1.0.0   | Documento completo com o detalhamento de todos os User Stories | Anderson, Cleomar, Ericleison, Marlon, Rafael, Thomas |
| 01/03/2023 | 2.0.0   | Adaptação do documento so modelo proposto para a disciplina ESII | Thomas |
| 18/03/2024 | 2.0.1   | Alteração de user stories (Manter Recurso) | Anderson 
| 18/03/2024 | 2.0.2   | Alteração de user stories (Manter Laboratório) | Marlon 
| 19/03/2024 | 2.0.3   | Alteração de user stories (Manter Auditório) | Rafael 
| 19/03/2024 | 2.0.4   | Alteração de user stories (Autenticação do Usuário) | Cleomar 
| 20/03/2024 | 2.0.5   | Alteração de user stories (Manter Servidor e Bolsista) | Ericleison 
| 20/03/2024 | 2.1.0   | Alterações em todos os user stories | Thomas 


### User Story US00 - Estrutura inicial do projeto    

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Construção da estrutura da aplicação Django, com a página inicial e os arquivos envolvendo rotas e banco de dados. |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 2h                                  | 
| **Tempo Gasto (real):**   | 2h                                  | 
| **Analista**              | Tgomas                              | 
| **Desenvolvedor**         | Ericleison                          | 
| **Revisor**               | Thomas                              | 
| **Testador**              | Anderson                            | 

### User Story US01 - Autenticação de Usuário    

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir que o usuário tenha acesso via login e senha. Um usuário tem os atributos matrícula, nome, email, senha e tipo de perfil. |

| **Requisitos envolvidos** | **Descrição**                                                  |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastro de usuário |
| RF02          | Login de usuário  |
| RF03          | Logout de usuário       |
| RF04          | Remoção de conta de usuário |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 10h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 13 PF                               | 
| **Analista**              | Cleomar                             | 
| **Desenvolvedor**         | Rafael                              | 
| **Revisor**               | Thomas                              | 
| **Testador**              | Anderson                            | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| **Código**  | **Descrição** |
| **TA01.01** | O usuário informa, na tela Cadastro, todos os dados para registrar-se corretamente, ao clicar em **Salvar** ele é encaminhado para a tela principal do sistema e notificado com uma mensagem de sucesso. Mensagem: *Cadastro realizado com sucesso*. |
| **TA01.02** | O usuário informa, na tela Cadastro, os dados para registrar-se faltando alguma informação, ao clicar em **Salvar** ele é notificado com uma mensagem de erro. Mensagem: *Cadastro não realizado, o campo “xxxx” não foi informado corretamente.* |
| **TA01.03** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em **Entrar** ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: *Login realizado com sucesso.* |
| **TA01.04** | O usuário informa, na tela Login, os dados para logar incorretamente, ao clicar em **Entrar** ele é notificado com uma mensagem de erro. Mensagem: *Login e/ou senha incorreta*. |
| **TA01.05** | O usuário, ao clicar no botao **Logout** é exibida uma mensagem de confirmação de logout, após confirmar o usuário é deslogado de sua conta. Mensagem: *Deseja sair da sua conta?* .|
| **TA01.06** | O usuário navega até a área de configurações do perfil, e clica em **Excluir conta.** Ele deve então digitar sua senha para confirmar a decisão, recebendo uma mensagem de confirmação. Mensagem: *Conta removida com sucesso.* |

### User Story US02 - Manter Locais

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de locais por usuário. Uma sala pode ter várias reservas e tem os atributos identificação, e reservas. Cada sala possui um histórico de reservas, que poderá ser acessado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF19          | Cadastrar Local |
| RF20          | Alterar Local  |
| RF21          | Excluir Local        |
| RF22          | Listar Locais |
| RF23          | Visualizar Local |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                          | 
| *Estimativa*            | 8h                                  | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 10 PF                               | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Anderson                            | 
| *Revisor*               | Cleomar                             | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA02.01* | O usuário preenche a identificação do local no formulário de cadastro de Local e depois clica em *Salvar. O sistema exibe a MSG001: *Local {id} cadastrado com sucesso. |
| *TA02.02* | Tentar cadastrar com erro, exibir uma das mensagens de erro: MSG001: O campo {id} é obrigatório. MSG002: O local {id} já existe. |
| *TA02.03* | O usuário preenche as novas informações da Local no formulário para Editar Local, e clica em *Salvar. MSG001: *Local alterado com sucesso. |
| *TA02.04* | O usuário tenta excluir o Local desejado, e obtém sucesso. MSG001:  Local excluído com sucesso.. Caso o usuário não tenha essa permissão, o botão para a funcionalidade não é renderizado. |
| *TA02.05* | Pesquisar com sucesso. Exibição com sucesso ou exibição vazia. (MSG001: Nenhum resultado encontrado.) |

### User Story US03 - Manter Recurso

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de recursos disponíveis para empréstimo no Apoio Pedagógico. Um recurso pode ter os atributos codigo, status, funcionando e tipo. Haverá uma tela de estoque para listar os recursos disponíveis. Os tipos de recursos são adaptador HDMI, projetor, notebook, caixa de som e mouse. Bem como, uma tela que mostra os recursos disponíveis e os reservados. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF16          | Incluir Recurso    |
| RF17          | Alterar Recurso    |
| RF18          | Excluir Recurso    |
| RF19          | Exibir Recurso     |
| RF20          | Visualizar Recurso | 
| RF21          | Registrar Saída    |
| RF22          | Registrar Entrada  |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                          | 
| *Estimativa*            | 8h                                  | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 10 PF                               | 
| *Analista*              | Anderson                            | 
| *Desenvolvedor*         | Marlon              | 
| *Revisor*               | Ericleison              | 
| *Testador*              | Cleomar              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA03.01* | O usuário preenche tipo e código do recurso no formulário de cadastro do Recurso e depois clica em *Salvar. O sistema exibe a mensagem: *Recurso {tipo + codigo} cadastrado com sucesso. |
| *TA03.02* | Tentar cadastrar com erro, exibir uma das mensagens de erro: MSG001: O campo {codigo} é obrigatório. MSG002: O recurso {codigo} já existe. |
| *TA03.03* | O usuário preenche o novo status do funcionamento do recurso no formulário para Editar Recurso, e clica em *Salvar. Mensagem: *Recurso alterada com sucesso. |
| *TA03.04* | O usuário tenta excluir o recurso desejado, e obtém sucesso. Mensagem:  Recurso excluído com sucesso.. Caso o usuário não tenha essa permissão, o botão para a funcionalidade não é renderizado. |
| *TA03.05* | Pesquisar com sucesso. Exibição com sucesso e exibição vazio. Testar exibição com paginação. |
| *TA03.06* | Ao realizar uma devolução, aparece a seguinte mensagem: Devolução realizada com sucesso. |
| *TA03.07* | Emprestar um recurso, aparece a mensagem: Empréstimo do recurso com sucesso. |
| *TA03.08* | Tentar emprestar, recebe mensagem de erro: O recurso escolhido já está emprestado no momento. |

| Protótipo de telas |
| ------------------ |
| <p><img src="./images/tela_cadastro_recurso.png" ></p><p>Figura 01 - Página de Cadastro de Recurso</p> |

### User Story US04 - Manter reservas de locais

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de reservas para cada local. Uma reserva deve ter os atributos responsável, local e período de permanência(horário de início e fim). Cada local possui um histórico de reservas, que poderá ser acessado pelos servidores e bolsistas. As reservas poderão ser porsonalizadas ou semanais (baseadas nos horários cadastrados) |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF24          | Cadastrar Reserva de Local |
| RF25          | Excluir Reserva de Local  |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Essencial                           | 
| *Estimativa*            | 14h                                 | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 14 PF                               | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Thomas                              | 
| *Revisor*               | Cleomar                             | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA04.01* | O usuário seleciona o tipo Personalizada, e abre o formulário. Depois, preenche a descrição, data e hora de entrada e data e hora de saída, quantidade de pessoas, bloco, o responável e o local e depois clica em Salvar. O sistema exibe a mensagem: MSG001: Local reservado com sucesso. |
| *TA04.02* | O usuário seleciona o tipo Semanal, e abre o formulário. Depois, preenche a descrição, seleciona os dias e horários que irá ocupar, quantidade de pessoas, bloco, o responável e o local e depois clica em Salvar. O sistema exibe a mensagem: MSG001: Local reservado com sucesso. |
| *TA04.03* | Tentar reservar com erro, exibir a mensagem de erro: MSG001: O campo {campo} é obrigatório. MSG002: O local {id\_local} está reservado no período escolhido. |
| *TA04.04* | O usuário seleciona a reserva que deseja excluir e clica no botão *Excluir reserva. Mensagem: *Reserva excluída com sucesso. |

| Protótipo de telas |
| ------------------ |
| <p><img src="./images/reserva_prot.jpg" ></p><p>Figura 2 - Página de Cadastro de Reserva de Sala</p> |
| <p><img src="./images/tela_efetuar_chamado.png" ></p><p>Figura 3 - Tela de Envio de Chamado</p> |


### User Story US05 - Manter Empréstimo

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de empréstimos para cada recurso. Um empréstimo pode ter os atributos responsável e recurso. Cada recurso possui um histórico de empréstimo, que poderá ser acessado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF26          | Cadastrar Empréstimo |
| RF27          | Excluir Empréstimo |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                          | 
| *Estimativa*            | 10h                                 | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 10 PF                               | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Ericleison                          | 
| *Revisor*               | Cleomar                             | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA05.01* | O usuário preenche o nome do responsável, o recurso e depois clica em *Salvar*. O sistema exibe a MSG001: Empréstimo cadastrada com sucesso. |
| *TA05.02* | Tentar cadastrar empréstimo com erro, exibir a mensagem de erro: MSG001: O campo {responsável} é obrigatório. MSG002: O recurso {id\_recurso} está emprestado no período escolhido para {responsável}. |
| *TA05.03* | O usuário seleciona o empréstimo que deseja excluir e clica no botão *Excluir empréstimo*. MSG001: Empréstimo excluído com sucesso. |

| Protótipo de telas |
| ------------------ |
| <p><img src="https://lh3.googleusercontent.com/fife/ALs6j_HTbeALc-DHj6t6ya2NKgv-v_hlYcHf2PjRCAyRCSv_ZbOPuRlaYMlb56_2OVx4dznoB1tD_9R1_TN4lZhY6SEcCb49CQgnjp4FWbg2gd-0KOebbqr-kX4U6FoGrkXx7DdIuoo050n4-7wWq2uV_z5W0duqoqrR8dCdslEi5LVsxpwp8Qyy7T9QfKtD1cvqB0pGtzMAcBpFy2yQCTHfJOqj3PTzaFUfV_wJtGoPtQdfKo_ba3OLN-XMwKDdP6DfLRyyLrLk4HzRhfGLywFsIq96z4uGn_zPQ1tUOS6eMYX7uoP8k8tIY2W5BkPei-BztV8iUV1OUWoQ-MJKPaSJEH_CWzNpZMh9fbFFncWOvdq-nhu9zWYAjc2k_5ogv-86V27bauBbPVPFv8znxWpOK5CJyHyy2baknCC2NG4EZZuqsnE1QFZ8SAAhJjgFg7sgYuUh1hw6rg4chwe8Wn6UvFMNVZa0lfap9faDIuENBO9t2WPrk6KRf90D6IM_a-j2i2GzVFe9nrNP1hbNDdKJ3xlpBbU69UxLlWjxrBxE8Z0j-41Hx5H7NS-ikl9ioFdNDObIb32Yd0wPXdSrAOsKhs5LtjN0dOUxc1SesPrgczxEVjamGr8Vcli-MYtKJOMe5UVsygxDzewwQ1yVf59s4Bh__IDYMi7tfdG8Sjck_9VZRUShHYmHKNBSF_6G0ClTfiyUIEd4OTYeBXqjB4opPlfuUVD8k-TkqLYMCn4muQaF5lGJTEWaErJPflRV3WEcnrrR3K3drM7KSCyJUa56orIR_5BFwVPzCvfYoeGR63ObAsGfKmhwpsYoWw-tZ7HzLCLE1uUAxstwvPQ5jtwdfCn24bwA2z7FTMdXTsaICdNDlP2owuiLktKwpSWBC0NqXO0SS_bqk4KQOm9lZVch5bEd4WN2rnKHhegQwNanJTRRg9HlTzFlCbAs-phSKc9HLr8ixIYwy1TeJP_9-D2WqSGOvW-yxUpLhlKLiByH5L_hGzjNmmoR_5-4Tkw4C5CWl4QfHI1qsBXdcdEJ1Z5m4OgSO5WK7L6yX1g3UDI6HLqTiys6LS5a2Tr59lIoyRdTQjulDBjzpI-IxvaqcQd-qNZ6qrRAzWVrQpcQb_T7HGbhtiyMWeDQQv9tu3aRtNnfLAVyeHPTBCcNr18MT-Dw-ZZWd26w1pSv3b8Vj8ejOBHBkNddi1QLznfTFBGa0xrYpYgUIGtDcdDA86yaV4yWPdaduXBXMdKUaPScIoTL6V2MVoJH1TLACESMCPAEVDbH8_ewcmiqOBZ3VAeKptgKCV2GIAR4ki-ShfFRL0lxNJ8KtizwgrqaK5GLaSWp8minFNrQaagC0Hb_g_biV31dGass-kRakhdIOwSZg2o0swAWun4D7lmezvBRPrZ5lIfFI24GP2bI6eNTfGS80hz0hWCXwgHq7bD4DsDUKfYaGH4G91lU65HoH2pZJzjeuQgy_-jNV1erRHmEUZEDOnzyChKaVhXO6SRxFBSzyc9bI2opUfks3qhJvHjF1UyosYiYoSUoIYQ8LifKASe6Ky_SthM4rSaMRrOEH9ZfTf-oO_v-V6ZjvYY81S2XgBQnBncl8eDWmmOizjXfX9oyNWM=w1295-h882" ></p><p>Figura 3 - Página de Itens (Estoque)</p> <p><img src="./images/cadastro_local.png"></p><p>Figura 4 - Página de Cadastro de Local</p> |

### User Story US06 - Manter relatório de locais

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve realizar relatórios mensais de locais. Um relatório de local, exibe um relatório de todas as locais e suas reservas mensalmente. Os relatórios podem ser vistos pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF28          | Relatório de reserva de locais no mês |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                          | 
| *Estimativa*            | 4h                                  | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 6 PF                                | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Ericleison                          | 
| *Revisor*               | Anderson                            | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA06.01* | O usuário informa o local e o mês e depois clica em *Exibir relatório*. O sistema exibe a MSG001: Relatório gerado com sucesso. Em seguida o relatório é processado e exibido. |
| *TA06.02* | Tentar gerar relatório com erro, exibir a mensagem de erro: MSG001: O campo {local} é obrigatório. MSG002: O campo {mês} é obrigatório. |
| *TA06.03* | O usuário informa um local que nunca foi reservado anteriormente. O sistema exibe um relatório em branco e uma mensagem informando: O local não foi reservado ainda. (MSG001) |

### User Story US07 - Manter relatório de recursos

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve realizar relatórios mensais de recursos. Um relatório de recursos, exibe um relatório de determinados recursos e suas reservas. Os relatórios podem ser vistos pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF29          | Relatório de reserva de recursos no mês |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                          | 
| *Estimativa*            | 4h                                  | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 6 PF                                | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Ericleison                          | 
| *Revisor*               | Cleomar                             | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA07.01* | O usuário informa o recurso e o mês e depois clica em *Exibir relatório. O sistema exibe a mensagem: *Relatório gerado com sucesso. Em seguida o relatório é processado e exibido. |
| *TA07.02* | Tentar gerar relatório com erro, exibir a mensagem de erro: MSG001: O campo {recurso} é obrigatório. MSG002: O campo {mês} é obrigatório. |
| *TA07.03* | O usuário informa um recurso que nunca foi reservado anteriormente. O sistema exibe um relatório em branco e uma mensagem informando: O recurso não foi emprestado ainda. |


### User Story US08 - Manter chamado

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um registro de chamados para cada reserva. Um chamado deve ter os atributos descrição, reserva e status. Cada chamado estará vinculado a uma reserva, seu status poderá ser alterado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF54          | Efetuar chamado |
| RF55          | Resolver chamado  |
| RF56          | Excluir chamado  |
| RF57          | Listar chamado  |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                           | 
| *Estimativa*            | 10h                                 | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 10 PF                               | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Thomas                              | 
| *Revisor*               | Cleomar                             | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA08.01* | O usuário preenche o campo descrição, seleciona a reserva associada ao chamado e depois clica em *Efetuar chamado*. O sistema exibe a mensagem: *Chamado enviado*. |
| *TA08.02* | Tentar efetuar um chamado com erro(deixando algum dos campos em branco), exibir a mensagem de erro: *O campo {nome_do_camopo} é obrigatório*. |
| *TA08.03* | O usuário seleciona o chamado que deseja resolver e clica no botão *resolver*. O status do chamado deve ser alterado e atualizado na página. |
| *TA08.03* | O usuário seleciona o chamado que deseja remover e clica em *Remover*. O chamado excluido deve ser removido da listagem e a mensagem *chamado excluido!* deverá ser exibida. |

| Protótipo de telas |
| ------------------ |
| <p><img src="./images/tela_efetuar_chamado.png" ></p><p>Figura 3 - Tela de Envio de Chamado</p> |