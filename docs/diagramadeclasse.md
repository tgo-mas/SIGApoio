~~~mermaid 
classDiagram

    Local *-- TipoLocal
    Local --> Reserva
    Horario --> Reserva
    Chamado --> Reserva
    DiaSemana --o Horario

    Usuário --o Reserva
    Usuário <|-- Bolsista
    Usuário <|-- Docente
    Usuário <|-- Chefia
    Usuário <|-- Servidor

    Recurso --o Empréstimo
    Usuário --o Empréstimo
    Recurso *-- TipoRecurso

    class TipoLocal{
        -string tipo
    }
    class Local{
        -int id
        -string bloco
        -string nome
        -TipoLocal tipo
        -bool ocupado
        +setLivre()
        +setOcupado()
    }

    class Horario{
        -string id
        -string cod
        -DiaSemana dia
        -Time hora
    }
    class DiaSemana{
        -int codigo
        -string dia
    }

    class Reserva{
        -int id
        -Horario horarios
        -Local local
        -bool aprovada
        -string matResponsavel
        -string matSolicitante
        -isValida(Horario, Local) bool
        +setAprovada(status) void
    }

    class Recurso{
        -int codigo
        -bool status
        -bool funcionando
        -TipoRecurso tipo
    }
    class TipoRecurso{
        -string tipo
    }

    class Usuário{
        -string email
        -string matricula
        -string nome
    }
    class Servidor{
        -setTipoUsuario(Usuario, tipo)
    }

    class Empréstimo{
        -int id
        -Datetime horaSaida
        -Datetime horaEntrada
        -bool status
        -Recurso Recurso
        -string matBolsista
        -string matUsuario
        +setStatus(status)
    }

    class Chamado{
        -int id
        -Reserva reserva
        -string descricao
        -Datetime hora
        -bool status
        -Bolsista bolsista
        +setAtendido(status)
    }
~~~