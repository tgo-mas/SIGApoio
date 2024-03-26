# Comandos e descrição de como utilizar o projeto em Django

> [!IMPORTANT]
> Necessário ter o python instalado na máquina, de preferência, a versão mais recente.\
> Crie uma pasta para o projeto. 

## Instalando o sistema
## Ambiente Virtual
### Criando o ambiente virtual

Antes é necessário baixar a biblioteca do python, responsável por criar o ambiente virtual.

> [!NOTE]
> Um ambiente virtual é um espaço isolado no seu sistema operacional que contém as bibliotecas e configurações específicas para um determinado projeto Django. Ele oferece diversos benefícios, como: Isolamento de dependências, Gerenciamento de bibliotecas, Organização e Reprodutibilidade.
```
pip install virtualenv
```

Criando o ambiente virtual
```
python -m venv <nome do ambiente virtual>
```

### Iniciando o ambiente virtual
É preciso estar na raiz do projeto.

* bash: 
```
$ source <venv>/bin/activate
```
* cmd:
```
C:\Projeto> <venv>\Scripts\activate
```

## Instalando o Django no projeto
```
pip install django
```

## Instalando dependências
```
pip install -r requirements.txt
```

## Criando um projeto
> [!IMPORTANT]
> É importante o ponto final ``(.)`` logo em seguida do nome do seu projeto, pois a criação do ``manage.py`` ficará na raiz do projeto, facilitando a localização e execução.
```
django-admin startproject <nome do projeto> .
```

## Criando o app
Esteja na raiz do projeto ou no mesmo diretório que o projeto 

```
python manage.py startapp <nome do app>
```

