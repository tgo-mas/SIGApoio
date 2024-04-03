~~~mermaid

graph TD;

subgraph Render
    http[HTTP Cliente]
    style http fill: darkred
end

subgraph Aplicação Django
    urls[urls.py]
    views[views.py]
    templates[templates]
    models[models.py]
    style urls fill: purple
    style views fill: purple
    style templates fill: purple
    style models fill: purple
end

subgraph Banco de Dados
    db[(Banco de Dados)]
    style db fill: darkblue
end

http --> urls
urls --> models
urls --> templates
templates --> views
views --> models
models --> db



~~~