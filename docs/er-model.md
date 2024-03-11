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
    Recurso --> Adaptador
