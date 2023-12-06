\---

layout: post

title: "Construindo sua Primeira API REST com Flask em Python"

date: 2023-12-08

categories: Tutorial

author: José Santos

\---

## Construindo sua Primeira API REST com Flask em Python

### Introdução

![image](C:\Users\theca\Desktop\new post\image.png)

Você está se interessando pelo back-end, já ouviu geral falar de Python, possívelmente até de Django. API REST então? Você ouve falarem todos os dias em todos os videos e em todas as vagas. De fato é importante possuir conhecimentos sólidos sobre o protocolo HTTP, compreender os princípios da programação orientada a objetos e ter familiaridade com bancos de dados, ORM e padrões arquiteturais, como o MVC para construir aplicações no back-end. No entanto, a verdadeira compreensão desses conceitos surge quando os aplicamos na prática.

Neste tutorial, serei seu guia na construção da sua primeira API utilizando Flask, um microframework para aplicações web em Python. Vamos desenvolver uma aplicação simples seguindo o padrão MVC, introduzindo um serviço para lidar diretamente com a lógica de controle. Bora lá?

![software development GIF](https://media2.giphy.com/media/kwEmwFUWO5Ety/giphy.gif?cid=ecf05e47st1k7dtvoqavyljqa0jnh9bw2u2oz5slnkwyfajo&ep=v1_gifs_search&rid=giphy.gif&ct=g)

## Índice

- [Índice](#índice)
  
  - [Requisitos Iniciais](#requisitos-iniciais)
  
  - [Estrutura do Projeto](#estrutura-do-projeto)
  
  - [Desenvolvendo a Aplicação](#desenvolvendo-a-aplicação)
  
  - [**Preparando nosso ambiente**](#preparando-nosso-ambiente)
  
  - [**Testando a aplicação**](#testando-a-aplicação)
  
  - [**Criando a aplicação Flask**](#criando-a-aplicação-flask)
  
  - [**Primeiro Desafio #1 Testes**](#primeiro-desafio-1-testes)
  
  - [**Segundo Desafio #2 Configurando o Debug**](#segundo-desafio-2-configurando-o-debug)
  
    

---

### Requisitos Iniciais

Antes de começarmos, certifique-se de ter o Python instalado em sua máquina. Para usuários do Windows, faça o download e instale o executável do site oficial. Usuários Linux provavelmente já têm o Python instalado; caso contrário, instale-o via terminal:

```bash
sudo apt install python3 
python3 --version
```

Verifique se a versão do Python é 3.12.0 ou superior.

Site oficial para download 
https://www.python.org/downloads/

### Estrutura do Projeto

A organização de arquivos do projeto é a seguinte:

```bash
├── app
│   ├── controllers
│   │   └── book_controller.py
│   └── models
│       ├── book_model.py
│       └── book_schema.py
├── app.py
└── instance
    └── config.py
```

Breve explicação de cada arquivo:

- **app/controllers/book_controller.py:** Este arquivo contém a lógica de controle para operações relacionadas aos livros na aplicação. Trata as requisições feitas à aplicação.
- **app/models/book_model.py:** Aqui estão as definições das entidades do aplicativo, como a entidade Livro.
- **app/models/book_schema.py:** Este arquivo descreve a estrutura do esquema do livro, responsável pela serialização, garantindo a conformidade dos dados da model para o banco de dados.
- **app/services/book_service.py:** O serviço que encapsula a lógica de negócios para operações CRUD de Livros.

### Desenvolvendo a Aplicação

Agora, partiremos para a criação de uma aplicação de gerenciamento de livros com operações CRUD (Create, Read, Update, Delete).

1. Definindo os Requisitos:
   - Objeto: Livro, com atributos Autor, Título e Prateleira.
   - Operações: Criar, Ler, Editar e Deletar livros.

Preferimos iniciar com a definição clara dos requisitos antes de mergulhar na implementação. Vamos agora para a fase detalhada do tutorial.

### **Preparando nosso ambiente**

Para facilitar a gestão das dependências da aplicação, utilizaremos o pipenv para virtualizar um ambiente contendo as dependências necessárias.

Instale o pipenv utilizando o gerenciador de pacotes do Python, o pip. No bash ou cmd, digite:

```bash
pip install --user pipenv
```

Após a instalação do pipenv, verifique se o comando está disponível no terminal com:

````bash
pipenv --version
pipenv, version 2023.11.15
````

Se configurar o comando no path do seu sistema operacional estiver causando complicações, recomendo buscar informações sobre essa configuração por conta própria. Essa habilidade é valiosa para desenvolvedores.

![Computer GIF](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHEyOThtZXZveTV5cWkyZ2h6cWI0Y3dtOGtmb2ttMGx0cjNlZDZtdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/14wHxi7D45grRK/giphy.gif)



Finalmente, iniciaremos a instalação de todas as dependências do nosso projeto. Crie um novo diretório, acesse-o e instale os pacotes necessários:

```bash
cd api-python
pipenv install flask flask-marshmallow flask-migrate flask-sqlalchemy marshmallow marshmallow-sqlalchemy sqlalchemy pymysql
```

Explicando brevemente o propósito de cada uma dessas dependências:

- **Flask:** Microframework web para servir a aplicação, gerenciando mensagens entre cliente e servidor.
- **SQLAlchemy:** ORM que facilita a interação com o banco de dados, abstraindo a complexidade do SQL.
- **Flask-migrate:** Extensão para realizar migrações em conformidade com Flask e SQLAlchemy.
- **Marshmallow:** Serializador que converte tipos de dados nativos do Python em objetos estruturados para o banco de dados.

Para uma compreensão mais aprofundada, consulte as documentações oficiais desses projetos.

### **Testando a aplicação**

No meio da criação deste post eu acabei lendo um post no Linkedin do Erik Wendel, mencionando várias dicas. O destaque foi a configuração de um ambiente de testes completo.

![image-20231125234250500](C:\Users\theca\AppData\Roaming\Typora\typora-user-images\image-20231125234250500.png)



Embora inicialmente eu utilizasse ferramentas como Postman ou Insomnia para testar os endpoints, Erik sugere começar implementando testes que realizem as requests nos endpoints.

![image-20231125234525477](C:\Users\theca\AppData\Roaming\Typora\typora-user-images\image-20231125234525477.png)



Apesar de não ver frequentemente tutoriais explicando essa configuração completa, aqui estamos em um ambiente controlado. Pode não funcionar diretamente para você, mas ajuste conforme necessário para prosseguir no tutorial.

Seguiremos a sugestão de Erik W. e começaremos implementando testes que realizarão requests em nossos endpoints. Para isso, instale o Pytest.

```bash
pipenv install pytest pytest-flask
```

E finalmente, vamos escrever nossa primeira linha de código, meus amigos. Depois, configuraremos todo o nosso ambiente. Tudo o que vamos precisar para desenvolver nossa aplicação está disponível dentro de um contêiner virtualizado.

Para acessar esse container, basta digitar no terminal `pipenv shell`. Para sair da shell, basta digitar `exit`.

```bash
pipenv shell
```

Lembre-se da regra de ouro: se o comando não retornar "nada", quer dizer que funcionou. Mas pelo menos te avisa que ele está começando a fazer algo hahaha, "Launching subshell in virtual environment..."

### **Criando a aplicação Flask**

###### Vamos codar!

![Video gif. Golden retriever with human hands types away on a laptop. Text, "I have no idea what I'm doing."](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXhianJ0dGpqd2o5YXN3d2J5ajhhNXJza2c2dWVqM3d0bXJ1NHp3NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Dh5q0sShxgp13DwrvG/giphy.gif)

Cara, você está comigo? Conseguiu chegar até aqui, onde finalmente vamos criar o primeiro arquivo Python da nossa aplicação?

Se está comigo, sua pasta deve ter dois arquivos, `Pipfile` e `Pipfile.lock`. São os arquivos criados pelo Pipenv para gerenciar nossas dependências. Se você gosta de Node.js como eu, já deve conhecer o `package.json`. É basicamente a mesma coisa aqui, com esses arquivos.

Você pode aprender um pouco mais sobre Pipenv visitando a documentação oficial.

Crie um arquivo chamado `App.py` e uma pasta `app`. Dentro dessa pasta, crie um arquivo chamado `__init__.py` Este arquivo é usado para indicar que o diretório é um pacote Python.



````bash
# Utilize os seguintes comandos:
touch App.py && mkdir app
cd app && touch __init__.py && cd..
````

Comece a editar o arquivo `__init__.py`. Começamos importando nosso framework web, o Flask, e criando uma função que cria nossa aplicação Flask.

````python
from flask import Flask


def create_app():
   	app = Flask(__name__)
    
    return app
````

Já o arquivo `App.py` é nossa main. Se você vem do Python, este seria seu `static void main`, o arquivo principal que chama toda aplicação. E ele não poderia ser mais simples.

````python
from app import create_app

app = create_app()

if __name__ =='__main__':
    app.run()
````

Se tudo estiver funcionando corretamente, você conseguirá rodar a aplicação utilizando o comando `flask run`.

````bash
flask run
````

Você deve receber uma mensagem informando que tem um servidor rodando no seu localhost. *Running on [http://127.0.0.1:5000](http://127.0.0.1:5000/)*

![Jesse Eisenberg Dev GIF](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3Z5b20wYTNmOXBsZjkyOGwzNmlicnd6aHJ4NTl6MDF6dTNjazlvaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kluzPOxBzGk4U/giphy.gif)

### **Primeiro Desafio #1 Testes**

Dentro da pasta `app`, crie uma pasta chamada `tests`. Dentro da pasta `tests`, crie um arquivo `__init__.py` e outro arquivo `test_api.py`. Lembre-se, bobo, se você estiver executando os comandos do Bash dentro da shell do Pipenv, vai receber um erro. Deixe um terminal aberto. Eu gosto do Git Bash, só para você executar esses comandos de criação de pasta e arquivos e tal. Se não cria e navega na mão.

````bash
cd app && mkdir tests && touch __init__.py test_api.py
````

No arquivo `test_api.py`, vamos criar as configurações iniciais em conformidade com a documentação do Pytest. Não pense que eu criei este código do zero e que você precisa entender exatamente tudo que ele está fazendo. Não é bem assim. Trate essas próximas linhas de código como a configuração, e eu te explico o que realmente você precisa se atentar.

````python
import pytest
from app import create_app

# Primeiro, criamos as configurações iniciais conforme a documentação do pytest:
@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
````

Aqui estamos criando novamente a aplicação Flask e informando para o Pytest qual nosso cliente de testes, no caso, nosso app. Desta forma, quando executarmos métodos como o `get` ou o `post` no client, estaremos executando métodos na nossa aplicação.

Agora, de fato, vamos criar nosso primeiro teste feito para falhar, e vocês vão entender o porquê ele está falhando.



````Python
#continuação do arquivo test_api.py

# Agora, vamos criar nosso primeiro teste, inicialmente configurado para falhar:
def test_server_is_online(client):
    response = client.get('/')
    assert response.status_code == 200
````

Neste teste unitário, estamos realizando uma requisição GET na rota '/' do client (aplicação Flask) e esperamos que a resposta tenha o status code 200. Lembra que disse que você precisaria entender o mínimo de HTTP? Pois bem, toda response HTTP tem um status code. Qualquer status code diferente deste em nosso teste irá falhar.

Vamos rodar?

Em um terminal, digite `flask run` - o servidor já irá rodar com live-reload por padrão.

````bash
flask run
````

No outro terminal, rode o Pytest.

```bash
pytest
```

Se tudo estiver configurado da forma correta, o teste irá falhar.

**FAILED app/test_api.py::test_server_is_online - assert 404 == 200**

![Computer Science Dance GIF by Scaler](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnN0a2l1eHZvanNvZ211bGtybHY4ZGZjMHU1dmJ2YXhwZ2Joc2NpayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ao668huBDpclN0XdrW/giphy.gif)

#### **Passando no Teste**

Sei que você já está morrendo de ansiedade. Mas se acalma, jovem padawan. Tem coisas que são necessárias, e eu juro que um dia você poderá me agradecer. Saber configurar seu ambiente do zero tem seu valor.

Para passar no teste, precisamos que nosso servidor retorne o status code 200 no endpoint  '/'. Como fazemos isso?

Com uma gambiarra, lógico!

 Dentro do arquivo `__init__.py` na pasta `app`, vamos chamar um decorator do Flask para criar nossa primeira rota, e vamos utilizar o método `make_response` do Flask para retornar um objeto vazio com o status code 200 nesta rota.

````python
#atualização do arquivo __init__.py da pasta app

from flask import Flask, make_response

def create_app():
    app = Flask(__name__)
	
    #Quando um get é feito na rota / o servidor executa a função index
    @app.route('/', methods=['GET'])
    def index():
        return make_response([], 200)

    return app
````

Feito isto seu teste já deve passar

![image-20231130210241249](C:\Users\theca\AppData\Roaming\Typora\typora-user-images\image-20231130210241249.png)

Agora você é um cara que entende o básico na pratica é que é TDD, muitos tutoriais ai pela web nem se preocupam em te ensinar isto, é mais simples ensinar a pessoa usar o postman e fazer um get na rota na mão, mas será que isto é produtivo? Erick alugou um triplex na minha cabeça.

Desafio um concluído meus caros amigos!



Explicando de forma bem direta a lógica dos nossos testes. Realizamos uma request em uma rota, e validamos se a response tem que esperamos, um tipo de dado, um status code ou até um tipo de dados espessífico.

Segue o arquivo de testes completo para sua apreciação, se eu fosse você não daria ctrl+C ctrl+V se este for seu primeiro contato com testes unitários.

```python
import pytest
import json

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_create_one_books(client):
    payload = json.dumps({
        "autor": "Paulo Coelho",
        "title": "A espiã",
        "prateleira": "A"
    })

    header = {"Content-Type": "application/json"}

    response = client.post(
        '/books',
        data=payload,
        headers=header
    )

    assert response.status_code == 201


def test_create_a_list_of_books(client):
    header = {"Content-Type": "application/json"}
    payload = json.dumps([{
        "autor": "Paulo Coelho",
        "title": "A espiã",
        "prateleira": "A"
    }, {
        "autor": "Robert C. Martin",
        "title": "Código limpo: habilidades práticas do Agile software",
        "prateleira": "C"
    }, {
        "autor": "George R. R. Martin",
        "title": "A Guerra dos Tronos",
        "prateleira": "A"
    }])

    response = client.post(
        '/books',
        headers=header,
        data=payload

    )

    assert response.status_code == 201

def test_get_all_books(client):
    response = client.get('/books')
    data = json.loads(response.data.decode('utf-8'))
    assert data is list and response.status_code == 200

def test_get_one_book(client):
    response = client.get('/books')
    data = json.loads(response.data.decode('utf-8'))
    assert data is dict
    assert response.status_code == 200

def test_edit_all_book_information(client):
    header = {"Content-Type": "application/json"}
    payload = json.dumps({
        "autor": "Miguel de Cervantes",
        "title": "Dom Quixote",
        "prateleira": "D"
    })
    response = client.post(
        '/books/1',
        headers=header,
        data=payload
    )
    data = json.loads(response.data.decode('uft-8'))
    assert data['autor'] == "Miguel de Cervantes"
    assert data['title'] == "Dom Quixote"
    assert data['prateleira'] == "D"
    assert response.status_code == 201


def test_edit_one_book_information(client):
    header = {"Content-Type": "application/json"}
    payload = json.dumps({
        "prateleira": "M"
    })
    response = client.put(
        '/books/2',
        headers=header,
        data=payload
    )
    data = json.loads(response.data.decode('uft-8'))
    assert data['prateleira'] == "M"
    assert response.status_code == 201

def test_delete_one_book(client):
    response = client.delete('/book/1')
    assert response.status_code == 201
```



### **Preparando o terreno para o MVC**

Até agora podemos dizer que criamos a main do nosso projeto. Uma boa pratica a partir daqui é criar o repositório protejer a brach main e criar as brances conforme as implementações de novas features. Isto garante que apenas alterações testadas sejam integradas à branch main.

````bash
git init
git branch -M main
````

Dentro da pasta app vamos criar as pastas models e controllers dentro de cada uma destas pastas precisamos dos arquivos init

```bash
mkdir app/models/ app/controllers && touch app/models/__init__.py app/controllers/__init__.py
```

[^1]:  Você também não acha lindo que um comando crie duas pastas e dois arquivos distintos em exatamente 0 segundos?

Agora adicione todos estes arquivos ao seu Repo e faça seu commit.

```bash
git add *
git commit -m "main"
```



![image-20231205232024610](C:\Users\theca\AppData\Roaming\Typora\typora-user-images\image-20231205232024610.png)

Você pode e deve colocar seu primeiro backend em python num repositório do Github, basta criar um repo na plataforma e configurar o remote e fazer o push, da seus pulos. (Inclusive quando vc cria o repo no github ele já te da um passo a passo de como criar ou apontar o repo. #fikadika)





Utilizando o vscode conseguimos configurar o Debug para o flask de forma simples.

Refências:

https://docs.pytest.org/en/7.4.x/

https://flask.palletsprojects.com/en/3.0.x/

https://flask-sqlalchemy.palletsprojects.com/

https://marshmallow-sqlalchemy.readthedocs.io/

https://marshmallow.readthedocs.io/

https://flask.palletsprojects.com/en/2.2.x/testing/

https://github.com/josesantosdev/bhub/blob/main/requirements.txt

https://pipenv.pypa.io/en/latest/index.html







