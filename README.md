#Minha API REST com Flask
Bem-vindo ao repositório da minha primeira API REST construída com Flask em Python. Este projeto é um tutorial prático que abrange desde a configuração inicial até o desenvolvimento de uma aplicação de gerenciamento de livros com operações CRUD.

#Requisitos
Certifique-se de ter o Python instalado em sua máquina. Para usuários do Windows, faça o download e instale o executável do site oficial. Usuários Linux provavelmente já têm o Python instalado; caso contrário, instale-o via terminal:

```bash
sudo apt install python3 
python3 --version
```
#Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:

```bash
Copy code
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
#Desenvolvendo a Aplicação
Este tutorial abrange desde a configuração do ambiente até o desenvolvimento da aplicação, incluindo a implementação de testes com o Pytest. O projeto segue o padrão MVC (Model-View-Controller), introduzindo serviços para gerenciar a lógica de controle.

#Preparando o Ambiente
Utilizamos o Pipenv para gerenciar as dependências da aplicação. Certifique-se de ter o Pipenv instalado e, em seguida, instale as dependências com o seguinte comando:

```bash

pipenv install flask flask-marshmallow flask-migrate flask-sqlalchemy marshmallow marshmallow-sqlalchemy sqlalchemy pymysql
```

#Testando a Aplicação
Implementamos testes utilizando o Pytest para garantir o bom funcionamento da aplicação. Execute os testes com o comando:

```bash
pytest
```

#Contribuição
Sinta-se à vontade para explorar, fazer melhorias e contribuir para este projeto. Caso encontre problemas ou queira sugerir melhorias, abra uma issue ou envie um pull request.




