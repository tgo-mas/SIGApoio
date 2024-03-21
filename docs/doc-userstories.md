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


### User Story US02 - Manter Servidor

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de servidor que tem acesso ao sistema via login e senha. Um servidor tem os atributos matrícula, nome, endereço, email, telefone e senha. A matrícula será o login e ele pode registrar-se diretamente no sistema. Ele pode realizar alterações de endereço, e-mail e telefone, senha, além de poder visualizar todos os outros servidores cadastrados no próprio sistema. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF06          | Alterar Servidor      |
| RF07          | Listar Servidor       |
| RF08          | Visualizar Servidor   |
| RF09          | Excluir Servidor      |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Essencial                           | 
| *Estimativa*            | 10h                                 | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 13 PF                               | 
| *Analista*              | Ericleison                          | 
| *Desenvolvedor*         | Thomas                              | 
| *Revisor*               | Marlon                              | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| **Código**  | **Descrição** |
| **TA01.01** | O servidor informa seus dados na tela de registro, caso os dados estejam corretamente dispotos, ao clicar em **Cadastrar-se** ele é redirecionado para a tela principal do sistema (home screen) e notificado com uma mensagem de sucesso. Mensagem: **O Cadastro foi realizado com sucesso.** |
| **TA01.02** | O servidor informa, na tela Registrar, os dados para registrar-se incorretamente, ao clicar em **Salvar** ele é notificado com uma mensagem de erro e o cadastro não é efetuado. Mensagem: **Cadastro não realizado, o campo “xxxx” não foi informado corretamente.** |
| **TA01.03** | O servidor informa, na tela de Login, os dados para logar de forma correta, ao clicar em **Entrar** ele é redirecionado para a tela de gestão(?) do sistema. É exibida a Mensagem: **Login efetuado com sucesso.** |
| **TA01.04** | O servidor informa, na tela Login, os dados para logar incorretamente, ao clicar em **Entrar** ele é notificado com uma mensagem de erro. Mensagem: **Não foi possível efetuar o login, verifique seus dados**. |
| **TA01.05** | O servidor navega até a área de configurações do perfil, e clica em **Excluir conta.** Ele deve confirmar seus dados para concluir a sua decisão, recebendo uma mensagem de confirmação. Mensagem: **Conta removida com sucesso.** |
| **TA01.06** | O servidor não preenche um ou mais dos campos obrigatórios (marcados com " * "), ao clicar para avançar, ele é notificado com uma mensagem de erro. Mensagem : **O campo "xxxx" não foi preenchido.** |
| **TA01.07** | O Usuário foi alterar seus dados cadastrais e informou algum dado inválido, uma mensagem de erro aparecerá. Mensagem: **Você informou dados incorretos**.|
| **TA01.08** | O usuário foi alterar seus dados cadastrais, ao efetuar as alterações, aparece a mensagem : **Dados atualizados com sucesso.**| 

| Protótipo de telas |
| ------------------ |
Imagem a ser inserida futuramente.

### User Story US03 - Manter Bolsista

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de bolsisa, ele tem acesso ao sistema via login e senha. Um bolsista tem os atributos **matrícula**, nome, endereço, email, telefone e escala de horários. </p>O email será o login e ele deve ser registrado no sistema por um **servidor**. O bolsista pode alterar os seus dados cadastrais (email, endereço e telefone), além de poder visualizar os demais bolsistas cadastrados no sistema. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF10          | Incluir Bolsista    |
| RF11          | Alterar Bolsista    |
| RF12          | Listar Bolsista     |
| RF13          | Visualizar Bolsista |
| RF14          | Excluir Bolsista    |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Essencial                           | 
| *Estimativa*            | 5h                                  | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 12 PF                               | 
| *Analista*              | Thomas                              | 
| *Desenvolvedor*         | Ericleison                          | 
| *Revisor*               | Cleomar                             | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| **Código**  | **Descrição** |
| **TA02.01** | O servidor informa, na tela de Registro, todos os dados para registrar um bolsista corretamente, ao clicar em **Salvar** ele é notificado com uma mensagem de sucesso. Mensagem: *Cadastro realizado com sucesso.* |
| **TA02.02** | O servidor informa, na tela de Registro, os dados para registrar um bolsista incorretamente, ao clicar em **Salvar** ele é notificado com uma mensagem de erro. Mensagem: *Cadastro não realizado, o campo “xxxxx” não foi informado corretamente.* |
| **TA02.03** | O bolsista informa, na tela Login, os dados para logar corretamente, ao clicar em **Entrar** ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: *O Login foi realizado com sucesso.* |
| **TA02.04** | O bolsista informa, na tela Login, os dados para logar incorretamente, ao clicar em **Entrar** ele é notificado com uma mensagem de erro. Mensagem: *Login e/ou senha incorreta(s)*. |
| **TA02.05** | O servidor navega até a área de configurações do perfil do bolsista, e clica em **Excluir conta.** Ele deve então digitar sua senha para confirmar a decisão da exclusão, ao digitar a senha corretamente, o sistema responde retornando uma mensagem de confirmação. Mensagem: *Essa conta foi removida com sucesso.* |
| **TA02.06** | O servidor navega até a área de configurações do perfil do bolsista, e clica em **Excluir conta.** Ele deve então digitar sua senha para confirmar a decisão da exclusão, caso a senha digitada seja incorreta, o sistema responde retornando uma mensagem de alerta. Mensagem: *Erro, senha incorreta.* |
| **TA02.07** | O bolsista navega até a área de configurações do perfil, atualiza seus dados, informando de maneira correta e  clica em Salvar, Ele deve então digitar sua senha para confirmar a decisão, caso a senha digitada corretamente, o sistema responde retornando uma mensagem de confirmação. Mensagem: *Seus dados foram atualizados com sucesso.* |
| **TA02.08** | O bolsista navega até a área de configurações do perfil, atualiza seus dados, mas informa algum dado incorreto, ao clicar em **Salvar** Ele deve então digitar sua senha para confirmar a decisão da exclusão, caso tenha digitado a senha corretamente, o sistema responde retornando uma mensagem de alerta. Mensagem: *Erro, os dados do campo "xxxxx" não foram preenchidos corretamente.* |
| **TA02.09** | O bolsista navega até a área de configurações do perfil, atualiza seus dados corretamente, ao clicar em **Salvar** Ele deve então digitar sua senha para confirmar a decisão da exclusão, caso tenha digitado a senha incorretamente, o sistema responde retornando uma mensagem de alerta. Mensagem: *Erro, senha digitada não corresponde.* |

### User Story US04 - Manter salas

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de salas por usuário. Uma sala pode ter várias reservas e tem os atributos identificação, e reservas. Cada sala possui um histórico de reservas, que poderá ser acessado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF19          | Cadastrar Sala |
| RF20          | Alterar Sala  |
| RF21          | Excluir Sala        |
| RF22          | Listar Salas |
| RF23          | Visualizar Sala |

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
| *TA03.01* | O usuário preenche a identificação da sala no formulário de cadastro de Sala e depois clica em *Salvar. O sistema exibe a mensage: *Sala {id} cadastrada com sucesso. |
| *TA03.02* | Tentar cadastrar com erro, exibir uma das mensagens de erro: MSG001: O campo {id} é obrigatório. MSG002: A sala {id} já existe. |
| *TA03.03* | O usuário preenche as novas informações da sala no formulário para Editar Sala, e clica em *Salvar. Mensagem: *Sala alterada com sucesso. |
| *TA03.04* | O usuário tenta excluir a sala desejada, e obtém sucesso. Mensagem:  Sala excluída com sucesso.. Caso o usuário não tenha essa permissão, o botão para a funcionalidade não é renderizado. |
| *TA03.05* | Pesquisar com sucesso. Exibição com sucesso ou exibição vazia (Mensagem: Nenhum resultado encontrado.). Testar exibição com paginação. |

### User Story US05 - Manter Recurso

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
| *TA04.01* | O usuário preenche tipo e código do recurso no formulário de cadastro do Recurso e depois clica em *Salvar. O sistema exibe a mensagem: *Recurso {tipo + codigo} cadastrado com sucesso. |
| *TA04.02* | Tentar cadastrar com erro, exibir uma das mensagens de erro: MSG001: O campo {codigo} é obrigatório. MSG002: O recurso {codigo} já existe. |
| *TA04.03* | O usuário preenche o novo status do funcionamento do recurso no formulário para Editar Recurso, e clica em *Salvar. Mensagem: *Recurso alterada com sucesso. |
| *TA04.04* | O usuário tenta excluir o recurso desejado, e obtém sucesso. Mensagem:  Recurso excluído com sucesso.. Caso o usuário não tenha essa permissão, o botão para a funcionalidade não é renderizado. |
| *TA04.05* | Pesquisar com sucesso. Exibição com sucesso e exibição vazio. Testar exibição com paginação. |
| *TA04.06* | Ao realizar uma devolução, aparece a seguinte mensagem: Devolução realizada com sucesso. |
| *TA04.07* | Emprestar um recurso, aparece a mensagem: Empréstimo do recurso com sucesso. |
| *TA04.08* | Tentar emprestar, recebe mensagem de erro: O recurso escolhido já está emprestado no momento. |

### User Story US06 - Manter reservas de salas

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de reservas para cada sala. Uma reserva deve ter os atributos responsável, sala e período de permanência(horário de início e fim). Cada sala possui um histórico de reservas, que poderá ser acessado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF24          | Cadastrar Reserva de Sala |
| RF25          | Excluir Reserva de Sala  |

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
| *TA05.01* | O usuário preenche o nome do responsável, a sala e o período de permanência na sala e depois clica em *Salvar. O sistema exibe a mensagem: *Sala reservada com sucesso. |
| *TA05.02* | Tentar reservar com erro, exibir a mensagem de erro: MSG001: O campo {nome} é obrigatório. MSG002: A sala {id\_sala} está reservada no período escolhido. |
| *TA05.03* | O usuário seleciona a reserva que deseja excluir e clica no botão *Excluir reserva. Mensagem: *Reserva excluída com sucesso. |

| Protótipo de telas |
| ------------------ |
| <p><img src="https://lh3.googleusercontent.com/fife/ALs6j_FV2e9-2iiyDpmf132vXZau8ch8TsxgJ_FTLprSz15fNKBGFiohYcaKIWGWVLlhNA0O1Pr0UrfrQBK3mFHhtS2us3KcyF0_JErfJ5GqDLYkSMh_6qOJWLkb9hJeFEQSBBkQR-ZRlYZR-9iq01p_rVLVm6ir05THbx2VZQbmjvByHVX8x6EDFx9cZag_kHW8Cx2eH2SoF6YxrMLIHBz082xR0NUciini60hzuhl9juZ0hnLio3Tn7aRWjCQKUnh17iG6FX3L89ldvHtla4V18OfxPS6CFN47an3a4hSRS3GHFavk5dP3mpJy6h-jm80K4pW0o5rguQ1OshW49u07s58yu3HkR7uPyGtBIarGFpGuSiRcfwrY7HkmLBpHGP1-shVq6Gf2tBX81V-c38KA0FJ1f_VRNltVZBpDFk0XLAQxTtLWj3UY-zAWzv76MWx9loinTNfDvuHUsqOD7sX6NPNOFLVQm_VKpGb-7HOBHcvKBF5KXcx1lPNUPYLLfYmeNrAfjCgWZgKoQpavTQ51ME5ywPsLFfO1httZUKUuKmzafjuOVegi1j3l6MfA2TE8TPZNj8o7TuIKkh6kYFKRfDmsvSy5VPgpR1947o1pg9iSN0v2Y_AzWJbIknBI5LyyxtGoTNx-OKhL9UQ290cDPq7ZjohB6CaCwCKHBvG-xAzavyPr5eCfFp1I-52zJaHQ4Fe6sWYAP265dfb1bPduS0dpCe2p9EIEdNL4sN41yfGMifawZOjTqwk-OEXR3XCDbEpNsxcUdnZ8XRcymefthRmUgxCaLAG_hOaEg9K0-ZMKzbrD7_IBqgULnENF1pLsn_0F_3xQFUkWKZn07Saz0HpAlB7_i2NODyiFyvG76YGVN2CHEP6XxnieuunEive3Hzmd6TFhzJUUZral5BW_mYw-EYSZRNss1cEjFjTbXOyxK_LQy0hB5tzXT8dP1Bs8ZbmCGYssqLQ7SRThP-KI3H1A_dgqS9MOfquCbFKo88BmKunuA5ABYgz-kee3rUcPfQ7zEc7hD4GI1UnxbKhT9IVoW9jJS4gR2G3QFqA8OxeFJfxTeB_Bd0DJy0DvNfYXeRjkKalfgW676OAaogBfvFVPegd3gkbmg1glwCp-jg_j9hzRyjm85r8yuXmTXh6R8IWHr-gjpM8E0z3mxm2VxuF90E6KxNhZXzEy64-enMRTp9nTDkNS4N3hLvKWdk4dmtMx0RwykvdWlAr-ToKVTe7fby4BamabzI9c3sbqTAW_Viw02URb-FNjYIZY26-66dnv5cTO9_tEWUJeEKUxwbeilT_RkHQFOKDJNps4HyYY_5jF3wutxitRSecVPtgGydVbCbyccnRPV9c3RWHQnsv7_0GTazVUiNDws9ofOYgH4S1Me4bIiNsjs-u-In0eTfqFFssO01mWuoFJSJnyghr2620YTrxGxjC8Ugtnq0SLMTZ8WCiOw4NyI3SGS-CDfusi2n9jGEmJ0TfWT2iLleJD_VcEf38YnW-3Gp6XPKG5XhpV7dir9fNJCQsHQfB3oUbPB5p-qkC4_hqw-xdufXcZJxLRvlyqLZTpMiesBFnFPAisXLxNxGZMGC7G2q6EpWj4Y_ge7QOtLnx7DQ=w1863-h882" ></p><p>Figura 2 - Página de Salas</p> |

### User Story US07 - Manter reservas de itens

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de reservas para cada item. Uma reserva pode ter os atributos responsável e item. Cada item possui um histórico de reservas, que poderá ser acessado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF26          | Cadastrar Reserva de Item |
| RF27          | Excluir Reserva de Item |

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
| *TA06.01* | O usuário preenche o nome do responsável, o item e depois clica em *Salvar. O sistema exibe a mensagem: *Reserva cadastrada com sucesso. |
| *TA06.02* | Tentar reservar com erro, exibir a mensagem de erro: MSG001: O campo {responsável} é obrigatório. MSG002: O item {id\_item} está reservado no período escolhido para {responsável}. |
| *TA06.03* | O usuário seleciona a reserva que deseja excluir e clica no botão *Excluir reserva. Mensagem: *Reserva excluída com sucesso. |

| Protótipo de telas |
| ------------------ |
| <p><img src="https://lh3.googleusercontent.com/fife/ALs6j_HTbeALc-DHj6t6ya2NKgv-v_hlYcHf2PjRCAyRCSv_ZbOPuRlaYMlb56_2OVx4dznoB1tD_9R1_TN4lZhY6SEcCb49CQgnjp4FWbg2gd-0KOebbqr-kX4U6FoGrkXx7DdIuoo050n4-7wWq2uV_z5W0duqoqrR8dCdslEi5LVsxpwp8Qyy7T9QfKtD1cvqB0pGtzMAcBpFy2yQCTHfJOqj3PTzaFUfV_wJtGoPtQdfKo_ba3OLN-XMwKDdP6DfLRyyLrLk4HzRhfGLywFsIq96z4uGn_zPQ1tUOS6eMYX7uoP8k8tIY2W5BkPei-BztV8iUV1OUWoQ-MJKPaSJEH_CWzNpZMh9fbFFncWOvdq-nhu9zWYAjc2k_5ogv-86V27bauBbPVPFv8znxWpOK5CJyHyy2baknCC2NG4EZZuqsnE1QFZ8SAAhJjgFg7sgYuUh1hw6rg4chwe8Wn6UvFMNVZa0lfap9faDIuENBO9t2WPrk6KRf90D6IM_a-j2i2GzVFe9nrNP1hbNDdKJ3xlpBbU69UxLlWjxrBxE8Z0j-41Hx5H7NS-ikl9ioFdNDObIb32Yd0wPXdSrAOsKhs5LtjN0dOUxc1SesPrgczxEVjamGr8Vcli-MYtKJOMe5UVsygxDzewwQ1yVf59s4Bh__IDYMi7tfdG8Sjck_9VZRUShHYmHKNBSF_6G0ClTfiyUIEd4OTYeBXqjB4opPlfuUVD8k-TkqLYMCn4muQaF5lGJTEWaErJPflRV3WEcnrrR3K3drM7KSCyJUa56orIR_5BFwVPzCvfYoeGR63ObAsGfKmhwpsYoWw-tZ7HzLCLE1uUAxstwvPQ5jtwdfCn24bwA2z7FTMdXTsaICdNDlP2owuiLktKwpSWBC0NqXO0SS_bqk4KQOm9lZVch5bEd4WN2rnKHhegQwNanJTRRg9HlTzFlCbAs-phSKc9HLr8ixIYwy1TeJP_9-D2WqSGOvW-yxUpLhlKLiByH5L_hGzjNmmoR_5-4Tkw4C5CWl4QfHI1qsBXdcdEJ1Z5m4OgSO5WK7L6yX1g3UDI6HLqTiys6LS5a2Tr59lIoyRdTQjulDBjzpI-IxvaqcQd-qNZ6qrRAzWVrQpcQb_T7HGbhtiyMWeDQQv9tu3aRtNnfLAVyeHPTBCcNr18MT-Dw-ZZWd26w1pSv3b8Vj8ejOBHBkNddi1QLznfTFBGa0xrYpYgUIGtDcdDA86yaV4yWPdaduXBXMdKUaPScIoTL6V2MVoJH1TLACESMCPAEVDbH8_ewcmiqOBZ3VAeKptgKCV2GIAR4ki-ShfFRL0lxNJ8KtizwgrqaK5GLaSWp8minFNrQaagC0Hb_g_biV31dGass-kRakhdIOwSZg2o0swAWun4D7lmezvBRPrZ5lIfFI24GP2bI6eNTfGS80hz0hWCXwgHq7bD4DsDUKfYaGH4G91lU65HoH2pZJzjeuQgy_-jNV1erRHmEUZEDOnzyChKaVhXO6SRxFBSzyc9bI2opUfks3qhJvHjF1UyosYiYoSUoIYQ8LifKASe6Ky_SthM4rSaMRrOEH9ZfTf-oO_v-V6ZjvYY81S2XgBQnBncl8eDWmmOizjXfX9oyNWM=w1295-h882" ></p><p>Figura 3 - Página de Itens (Estoque)</p> |

### User Story US08 - Manter relatório de salas

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve realizar relatórios mensais de salas. Um relatório de sala, exibe um relatório de todas as salas e suas reservas mensalmente. Os relatórios podem ser vistos pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF28          | Relatório de reserva de salas no mês |

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
| *TA07.01* | O usuário informa a sala e o mês e depois clica em *Exibir relatório. O sistema exibe a mensagem: *Relatório gerado com sucesso. Em seguida o relatório é processado e exibido. |
| *TA07.02* | Tentar gerar relatório com erro, exibir a mensagem de erro: MSG001: O campo {sala} é obrigatório. MSG002: O campo {mês} é obrigatório. |
| *TA07.03* | O usuário informa uma sala que nunca foi reservada anteriormente. O sistema exibe um relatório em branco e uma mensagem informando: A sala não foi reservada ainda. |

### User Story US09 - Manter relatório de itens

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve realizar relatórios mensais de itens. Um relatório de itens, exibe um relatório de determinados itens e suas reservas. Os relatórios podem ser vistos pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF29          | Relatório de reserva de itens no mês |

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
| *TA08.01* | O usuário informa o item e o mês e depois clica em *Exibir relatório. O sistema exibe a mensagem: *Relatório gerado com sucesso. Em seguida o relatório é processado e exibido. |
| *TA08.02* | Tentar gerar relatório com erro, exibir a mensagem de erro: MSG001: O campo {item} é obrigatório. MSG002: O campo {mês} é obrigatório. |
| *TA08.03* | O usuário informa um item que nunca foi reservado anteriormente. O sistema exibe um relatório em branco e uma mensagem informando: O item não foi emprestado ainda. |

### User Story US10 - Manter Laboratórios

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de laboratórios por usuário. Um laboratório pode ter várias reservas e tem os atributos de identificação, e reservas, além de uma chave associada ao mesmo. Cada laboratório possui um histórico de reservas, que poderá ser acessado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF28          | Cadastrar Laboratório |
| RF29          | Alterar Laboratório  |
| RF30          | Excluir Laboratório        |
| RF31          | Listar Laboratórios |
| RF32          | Visualizar Laboratório |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                          | 
| *Estimativa*            | 8h                                  | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 10 PF                               | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Anderson                            | 
| *Revisor*               | Ericleison                          | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA09.01* | O usuário preenche a identificação do laboratório no formulário de cadastro e depois clica em *Salvar*. O sistema exibe a mensage: *Laboratório {id} cadastrado com sucesso*. |
| *TA09.02* | Tentar cadastrar mas não preenche alguma informação obrigatória, ou preenche com algum identificador já cadastrado, exibir uma das mensagens de erro: <br>MSG001: *O campo {id} é obrigatório*.<br> MSG002: *A sala {id} já existe*. |
| *TA09.03* | O usuário preenche as novas informações do laboratório no formulário para Editar Laboratório, e clica em *Salvar*. Mensagem: *Sala alterada com sucesso*. |
| *TA09.04* | O usuário tenta excluir a sala desejada, e obtém sucesso. Mensagem:  *Sala excluída com sucesso*. <br>Caso o usuário não tenha essa permissão, o botão para a funcionalidade não é renderizado. |
| *TA09.05* | Pesquisar com sucesso. Exibição com sucesso dos resultados encontrados ou, caso não haja resultados, exibição vazia (Mensagem: *Nenhum resultado encontrado*.). Testar exibição com paginação. |

### User Story US11 - Manter Auditório

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| *Descrição* | O sistema deve manter um cadastro de auditórios por usuário. Um auditório pode ter várias reservas e tem os atributos de identificação, e reservas, além de uma chave associada ao mesmo. Cada auditório possui um histórico de reservas, que poderá ser acessado pelos servidores e bolsistas. |

| *Requisitos envolvidos* | *Descrição*                                                  |
| ------------- | :------------------------------------------------------------- |
| RF33          | Cadastrar Auditório |
| RF34          | Alterar Auditório  |
| RF35          | Excluir Auditório        |
| RF36          | Listar Auditório |
| RF37          | Visualizar Auditório |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| *Prioridade*            | Importante                          | 
| *Estimativa*            | 8h                                  | 
| *Tempo Gasto (real):*   |                                     | 
| *Tamanho Funcional*     | 10 PF                               | 
| *Analista*              | Marlon                              | 
| *Desenvolvedor*         | Anderson                            | 
| *Revisor*               | Ericleison                          | 
| *Testador*              | Rafael                              | 


| Testes de Aceitação (TA) |  |
| ----------- | ------------- |
| *Código*  | *Descrição* |
| *TA10.01* | O usuário preenche a identificação do auditório no formulário de cadastro e depois clica em *Salvar*. O sistema exibe a mensage: *Auditório {id} cadastrado com sucesso*. |
| *TA10.02* | Tentar cadastrar mas não preenche alguma informação obrigatória, ou preenche com algum identificador já cadastrado, exibir uma das mensagens de erro: <br>MSG001: *O campo {id} é obrigatório*.<br> MSG002: *A sala {id} já existe*. |
| *TA10.03* | O usuário preenche as novas informações do Auditório no formulário para Editar Auditório, e clica em *Salvar*. Mensagem: *Sala alterada com sucesso*. |
| *TA10.04* | O usuário tenta excluir a sala desejada, e obtém sucesso. Mensagem:  *Sala excluída com sucesso*. <br>Caso o usuário não tenha essa permissão, o botão para a funcionalidade não é renderizado. |
| *TA10.05* | Pesquisar com sucesso. Exibição com sucesso dos resultados encontrados ou, caso não haja resultados, exibição vazia (Mensagem: *Nenhum resultado encontrado*.). Testar exibição com paginação. |