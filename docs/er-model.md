# Modelo ER (Entidade Relacionamento v0.1)

```mermaid
erDiagram
Usuario ||--|{ Docente: Tipo
Usuario ||--|{ Servidor: Tipo
Usuario ||--|{ Bolsista: Tipo
Usuario ||--|{ Chefia: Tipo

Docente ||--|{ Chamado : Abre
Servidor ||--|{ Reserva_de_Salas: Aprova 
Reserva_de_Salas ||--|{ Sala : Reserva
Sala ||--||  Bolsa--- :Acompanha
Bolsista ||--|| Chave :Empresta
Chave ||--|{ Autorizado-- :Possui
Chefia  ||--|{Reserva_de_Salas: Solicita

Usuario ||--|{ Recurso : Reserva
Recurso }|--|{ Bolsista : Empresta 
Recurso ||--|| Adaptador : Pode_ser
Recurso ||--|| Caixa_de_som: Pode_ser
Recurso ||--|| Projetor : Pode_ser
Recurso ||--|| Notebook : Pode_ser 
```


## Listando entidades do projeto

|Entidades normais|Entidades fracas |Entidade associativas|
|------|-----|------|
|Docente|Bolsa|Abre|
|Servidor|Autorização|Aprova|
|Chefia|             |Solicita|
|Bolsista|           |Empresta|
|Recurso|            |Acompanha|




[Referências (Lucidchart)](https://www.lucidchart.com/pages/pt/o-que-e-diagrama-entidade-relacionamento)
