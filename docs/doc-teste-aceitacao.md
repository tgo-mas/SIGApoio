**US001 – Autenticação de Usuário**

| Teste | Descrição | Especificação | Resultado |
| :---- | :---- | :---- | :---- |
| Teste 01 Cadastrar Usuário | TA01 \- Cadastrar Usuário 	<br> A1.1 \- O ator preenche os dados de cadastro; 			  <br> A1.2 - O ator seleciona a opção Cadastrar; 			 <br>A1.3 \- O sistema salva os dados; 			<br> A1.4 \- O sistema exibe uma mensagem de: Cadastro realizado com sucesso. ; <br> A1.5 \- Fim do fluxo. | Especificação OK. 		 | OK	 |
| Teste 02 Login de usuário | TA03 \- Excluir Produto 	 A3.1 \- O ator preenche os dados de login			 <br> A3.2 \- O ator seleciona a opção login ; <br> A3.3 \- O sistema confirma o login baseado nas informações 	 <br> A3.4 \- O ator é redirecionado para a tela principal do sistema; <br> A3.5 \- O Sistema exibe uma mensagem de Login realizado com sucesso.| A função implementada não segue o passo 3.4. A implementação não segue o User Story. 	 | O login é efetuado, contudo a mensagem de login efetuado não foi exibida. |
| Teste 03 Logout de usuário | TA05 \- Logout de usuário 			 A5.1 \- O ator autenticado seleciona a opção logout; <br> A5.2 \- O sistema apresenta uma mensagem de confirmação de logout; <br> A5.3 \- O ator seleciona a confirmação do logout; 			 <br> A5.4 \- O ator é deslogado do sistema.        | Requisição OK. | OK. |
| Teste 04 Excluir conta | TA06 \- Excluir conta            A6.1 O ator navega até a área de configurações de perfil  <br> 6.2 \- O ator seleciona a opção Excluir conta  <br> 6.3 \- O ator preenche as informações para confirmação     <br>6.4 \- O ator confirma seleciona a confirmação de exclusão   <br>6.5 \- O sistema exclui aconta <br> 6.6 \- O sistema exibe uma mensagem [MSG005] de conta removida com sucesso | A função implementada não segue os passos TA 6.6. | A mensagem [MSG005] não é exibida, contudo a conta é excluída do sistema.

**Relatório de Bugs e Providências**  
Responsabilidade do Gerente

| Teste | Providência | Tarefas/Tipo |
| :---- | :---- | :---- |
| Teste 02 – Logout de Usuário| Corrigir a implementação do fluxo do user story.	 | Tarefa: Bug de Implementação. |
| Teste 04 – Excluir conta | Corrigir a especificação do fluxo do US e sua implementação. | Tarefa:  Tarefa: Bug de Implementação. |


**US03 – Manter Recursos**

| Teste | Descrição | Especificação | Resultado |
| :---- | :---- | :---- | :---- |
| Teste 01: Incluir Recurso com sucesso | TA01 \- Incluir Recurso com sucesso		 TA01.1. O usuário preenche os dados; 			 TA01.2. O usuário seleciona a opção Cadastrar; 			 TA01.3. O sistema salva os dados; 			 TA01.4. O sistema exibe uma mensagem de acordo com a \[MSG001\]; TA01.5. Fim do fluxo. | A função implementada não segue os passos TA01.4.  		 | O recurso é inserido, contudo a mensagem \[MSG001\] não foi exibida, após o cadastro do recurso, é retornado à página de cadastro. 		 |
| Teste 02: Incluir Recurso com erro | TA02 \- Incluir Recurso com erro		 TA02.1. O usuário preenche os dados; 			 TA02.2. O usuário seleciona a opção Cadastrar; 			 TA02.3. O sistema exibe uma mensagem de acordo com a \[MSG002.1\] ou \[MSG002.2\] ; 			 TA02.4.  Fim do fluxo. | Implementação OK.  		 | OK. 		 |
| Teste 03: Emprestar Recurso com sucesso | TA07 \- Emprestar Recurso com sucesso		 TA07.1. O usuário preenche os dados; 			 TA07.2. O usuário seleciona a opção Confirmar Empréstimo; 			 TA07.3. O sistema exibe uma mensagem de acordo com a \[MSG007\]; 	T107.8. Os dados são salvos.		 TA07.5.  Fim do fluxo. | A função implementada não segue os passos TA07.3.  		 | O empréstimo é realizado, contudo a mensagem \[MSG007\] não foi exibida. 		 |
| Teste 04: Emprestar Recurso com erro | TA08 \- Emprestar Recurso com erro		 TA08.1. O usuário preenche os dados; 			 TA08.2. O usuário seleciona a opção Confirmar Empréstimo; 			 TA08.3. O sistema exibe uma mensagem de acordo com a \[MSG008\]; 			 TA08.4.  Fim do fluxo. | A função implementada não segue os passos TA08.3.  		 | A mensagem \[MSG008\] não foi exibida, não é possível saber se o recurso está disponível. Também, aparece para emprestar os tipos de recursos e não os recursos.		 |


**Relatório de Bugs e Providências**  
Responsabilidade do Gerente

| Teste | Providência | Tarefas/Tipo |
| :---- | :---- | :---- |
| Teste 01 – Incluir Recurso com sucesso| Corrigir a implementação do fluxo do user story.	 | Tarefa: Bug de Implementação. |
| Teste 03 – Emprestar Recurso com sucesso | Corrigir a implementação do fluxo do user story.	 | Tarefa: Bug de Implementação. |
| Teste 04 – Emprestar Recurso com erro | Corrigir a especificação do fluxo do US e sua implementação. | Tarefa: Corrigir a análise do US.  Tarefa: Bug de Implementação. |
=====
#

**US04 - Manter Local**

| Teste | Descrição | Especificação | Resultado |
| :---- | :---- | :---- | :---- |
| Teste 01: Incluir Local com sucesso | TA01 \- Incluir Local com sucesso		 TA01.1. O usuário preenche os dados; 			 TA01.2. O usuário seleciona a opção Cadastrar; 			 TA01.3. O sistema salva os dados; 			 TA01.4. O sistema exibe uma mensagem de acordo com a \[MSG001\]; TA01.5. Fim do fluxo. | A função implementada não segue os passos TA01.4.  		 | O local é inserido, contudo a mensagem \[MSG001\] não foi exibida, após o cadastro do recurso, é retornado à página de cadastro. 		 |
| Teste 02: Incluir Local com erro | TA02 \- Incluir Local com erro		 TA02.1. O usuário preenche os dados; 			 TA02.2. O usuário seleciona a opção Cadastrar; 			 TA02.3. O sistema exibe uma mensagem de acordo com a \[MSG002.1\] ou \[MSG002.2\] ; 			 TA02.4.  Fim do fluxo. | Implementação OK.  		 | OK. 		 |
=======



**US07 - Manter Empréstimo**

| Teste | Descrição | Especificação | Resultado |
| :---- | :---- | :---- | :---- |
| Teste 01: Incluir Empréstimo com sucesso | TA06.01 - Incluir Empréstimo com sucesso: <br>TA06.01.1. O usuário preenche o nome do responsável e o item; <br>TA06.01.2. O usuário clica na opção *Salvar*; <br>TA06.01.3. O sistema salva os dados; <br>TA06.01.4. O sistema exibe a mensagem: *Empréstimo cadastrado com sucesso.*; <br>TA06.01.5. Fim do fluxo. | A função implementada não segue os passos TA06.01.4. | O empréstimo é inserido, contudo a mensagem "Empréstimo cadastrado com sucesso." não foi exibida. |
| Teste 02: Incluir Empréstimo com erro | TA06.02 - Incluir Empréstimo com erro: <br>TA06.02.1. O usuário tenta registrar um empréstimo sem preencher o nome do responsável ou com o item já emprestado; <br>TA06.02.2. O sistema exibe a mensagem de erro correspondente: *MSG001: O campo {responsável} é obrigatório* ou *MSG002: O item {id\_item} está emprestado no período escolhido para {responsável}.*; <br>TA06.02.3. Fim do fluxo. | Implementação OK. | OK. |
| Teste 03: Excluir Empréstimo com sucesso | TA06.03 - Excluir Empréstimo com sucesso: <br>TA06.03.1. O usuário seleciona o empréstimo que deseja excluir; <br>TA06.03.2. O usuário clica no botão *Excluir empréstimo*; <br>TA06.03.3. O sistema exclui o empréstimo; <br>TA06.03.4. O sistema exibe a mensagem: *Empréstimo excluído com sucesso.*; <br>TA06.03.5. Fim do fluxo. | A função implementada não segue os passos TA06.03.4. | O empréstimo é excluído, contudo a mensagem "Empréstimo excluído com sucesso." não foi exibida. |

**US04 – Manter Reservas de Locais**

| Teste | Descrição | Especificação | Resultado |
| :---- | :---- | :---- | :---- |
| Teste 01: Incluir Reserva Personalizada com sucesso | TA01: O usuário seleciona o tipo Personalizada, e abre o formulário. Depois, preenche a descrição, data e hora de entrada e data e hora de saída, quantidade de pessoas, bloco, o responável e o local e depois clica em Salvar. O sistema exibe a mensagem: MSG001: Local reservado com sucesso.| A função está OK, mas a mensagem está diferente: 'Reserva cadastrada com sucesso.' | A reserva foi cadastrada com sucesso. |
| Teste 02: Incluir Reserva Semanal com sucesso | *TA02*: O usuário seleciona o tipo Semanal, e abre o formulário. Depois, preenche a descrição, seleciona os dias e horários que irá ocupar, quantidade de pessoas, bloco, o responável e o local e depois clica em Salvar. O sistema exibe a mensagem: MSG001: Local reservado com sucesso. | A função está OK, mas a mensagem está diferente: 'Reserva cadastrada com sucesso.' | A reserva foi cadastrada com sucesso. |
| Teste 03: Incluir reserva com erro |*TA04.03*: Tentar reservar com erro, exibir a mensagem de erro: MSG001: O campo {campo} é obrigatório. MSG002: O local {id\_local} está reservado no período escolhido. | A mensagem de erro está diferente do esperado, e não informa exatamente qual foi o erro. | Consertar mensagem de erro, para fornecer mais detalhes. |
| Teste 03 – Incluir reserva com erro | Corrigir a mensagem de erro exibida para fornecer mais detalhes.	 | Tarefa: Corrigir mensagem de erro. |



**US12 – Manter Chamado**

| Teste | Descrição | Especificação | Resultado |
| :---- | :---- | :---- | :---- |
| Teste 01: Enviar Chamado com sucesso | TA01 \- Enviar Chamado com sucesso		 TA01.1. O usuário preenche os campos; 			 TA01.2. O usuário clica no botão para efetuar o chamado; 			 TA01.3. O sistema salva os dados; 			 TA01.4. O sistema exibe uma mensagem de acordo com a \[MSG001\]; TA01.5. Fim do fluxo. | A função implementada não segue os passos TA01.4.  		 | O chamado é enviado, contudo a mensagem \[MSG001\] não foi exibida, após o envio do chamado, é retornado à página de cadastro. 		 |
| Teste 02: Enviar Chamado com erro | TA02 \- Enviar Chamado com erro		 TA02.1. O usuário não preenche todos os campos; 			 TA02.2. O usuário clica no botão de efetuar chamado; 			 TA02.3. O sistema exibe uma mensagem de acordo com a \[MSG002.1\]; 			 TA02.4.  Fim do fluxo. | Problema no passo TA02.3.  		 | A mensagem não é exibida contudo o cadastro do chamado também não é realizado. 		 |

**Relatório de Bugs e Providências**  
Responsabilidade do Gerente

| Teste | Providência | Tarefas/Tipo |
| :---- | :---- | :---- |
| Teste 01 – Enviar Chamado com sucesso| Corrigir a implementação do fluxo do user story.	 | Tarefa: Bug de Implementação. |
| Teste 02 – Enviar Chamado com erro | Corrigir a implementação do fluxo do user story.	 | Tarefa: Bug de Implementação. |

