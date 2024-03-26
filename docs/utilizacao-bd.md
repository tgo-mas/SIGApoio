# Comandos e descrição de como utilizar o projeto em Django

> [!IMPORTANT]
> Necessário ter o python instalado na sua máquina, de preferência, a versão mais recente.\
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
Usando o terminal e estando na raiz do projeto, ative o ambiente virtual: 

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

## Criando o banco de dados
Automaticamente o Django cria um arquivo com extensão ``sqlite``, com o código: 
~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
~~~
Usar arquivo ``sqlite`` não é o ideal, por isso será usado um banco de dados em ``postgres``.

Antes de tudo, na raiz do seu projeto, crie um arquivo com o nome ``.env``. Nesse arquivo ficarão as credenciais do banco de dados, armazenadas em variáveis de ambiente. Para acessar as mesmas, é necessário instalar a biblioteca ``dotenv``. 
```
pip install python-dotenv
```

Troque o que está entre aspas, pelas credenciais do banco de dados:
~~~python
PGHOST='PGHOST'
PGDATABASE='PGDATABASE'
PGUSER='PGUSER'
PGPASSWORD='PGPASSWORD'
~~~


Import as bibliotecas ``os`` e ``dotenv``. Chame a função ``load_dotenv``, para carregar as variáveis de ambiente.
~~~python
(...)

from os import getenv
from dotenv import load_dotenv

(...)

load_dotenv()

(...)
~~~
 
Em seguida, modifique o ``DATABASES``, usando a função ``getenv``:

~~~python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': getenv('PGDATABASE'),
    'USER': getenv('PGUSER'),
    'PASSWORD': getenv('PGPASSWORD'),
    'HOST': getenv('PGHOST'),
    'PORT': getenv('PGPORT', 5432)
  }
}
~~~

Criando o banco de dados:
~~~
python manage.py makemigrations
~~~

Se existir alterações no banco de dados, utilize o comando:
~~~
python manage.py migrate
~~~


## Executando o projeto 
Com o ambiente virtual ativado, utilize o comando: 
```
python manage.py runserver
```

Abra seu navegador no endereço http://127.0.0.1:8000/ e aproveite seu projeto.