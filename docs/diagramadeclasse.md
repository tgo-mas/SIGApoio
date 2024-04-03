~~~mermaid 
classDiagram

    Local <|-- Sala
    Local <|-- Auditório
    Local <|-- Laboratório

    %% Reserva <|-- Usuário
    %% Usuário <|-- Bolsista
    %% Usuário <|-- Docente
    %% Usuário <|-- Chefia
    %% Usuário <|-- Servidor




    Local --> Reserva
    Horario --> Reserva

    Chamado --> Reserva
    Horario --> Usuário

    Recurso *-- TipoRecurso
    Usuário *-- TipoUsuario


    Recurso --> Empréstimo
    Usuário --> Empréstimo


    class Local{
        -int id
        -Chave chave
        +criarLocal():Local;
        +editarLocal();
        +removerLocal();
        +listarLocais();
        +getLocal();
    }
    class Horario{
        -string id
        -string cod
        -Date dia
        -Datetime hora
        +criarLocal():Local;
        +editarLocal();
        +removerLocal();
        +listarLocais();
    }
    class Reserva{
        -Horario horarios
        -int id
        -int idLocal
        -string matResponsavel
        -string matSolicitante
        +isAprovada():bool
        +novaReserva():Reserva
    }
    class Sala{
        -char bloco
        -int codigo
    }
    class Auditório{
        -String nome
    }
    class Laboratório{
        -string nome
    }
    class Recurso{
        -int codigo
        -bool status
        -bool funcionando
        +alterarRecurso();
    }
    class TipoRecurso{
        -string tipo
    }
    class Usuário{
        -string email
        -string matricula
        -string nome
        -string tipo
        -Horario escala

    }
    class TipoUsuario{
        -string tipo
    }
    class Empréstimo{
        -Datetime horaSaida
        -Datetime horaEntrada
        -int id
        -int idRecurso
        -string matBolsista
        -string matUsuario
    }
    class Chamado{
        -Reserva reserva
        -string descricao
        -Datetime hora
        -bool status
        -int id
    }
~~~