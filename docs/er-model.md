# Modelo ER (Entidade Relacionamento v0.1)


flowchart TD
{
    Usuario["Usuário"] --> Docente["Docente"] & Servidor["Servidor"] & Bolsista["Bolsista"] & Chefia["Chefia"]
    Docente -- Abre --> Chamado["Chamado"]
    Servidor -- Aprova --> Reserva_de_salas["Reserva de Salas"]


    Reserva_de_salas -- reserva --> Sala["Sala"]
    Sala --> |acompanha| Bolsa[Bolsa fa:fa-car]
    
    Bolsista --> |empresta| Chave --> Possui
    Possui --> autorizacao[fa:fa-car Autorização]

    Chefia --> |solicita| Reserva_de_salas 

    Usuario --> |reserva| Recurso
    Recurso --> Notebook
    Recurso --> Caixadesom["Caixa de som"]
    Recurso --> Projetor
    Recurso --> 
    
## Componentes e funcionalidades de um diagrama ER
Diagramas ER são compostos de entidades, relacionamentos e atributos. Eles também descrevem a cardinalidade, que define as relações em termos de números. 

## Entidade

Algo que pode ser definido e que pode ter dados armazenados sobre ele — como uma pessoa, um objeto, conceito ou evento. Pense em entidades como substantivos. Exemplos: um cliente, estudante, carro ou produto. 

## Tipos de entidade
Tipo de entidade: um grupo de coisas definíveis, como estudantes ou atletas, ao passo que a entidade seria um estudante ou atleta específico. Outros exemplos: clientes, carros ou produtos.




## Listando entidades

|Entidades normais|Entidades fracas |Entidade associativa|
|------|-----|------|
|Docente|Bolsa|Abre|
|Servidor|Autorização|Aprova|
|Chefia|             |Solicita|
|Bolsista|           |Empresta|
|Recurso|            |Acompanha|
