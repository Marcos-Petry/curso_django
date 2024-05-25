# Um pouco sobre django

## O que é django 

1. É uma framework web de código aberto escrita em Python.

2. Segue o Padrão MVT (Model, View, Template)
    - MODEL: **Responsável pela definição e manipulação dos dados**, Inclui a estrutura do banco de dados, as relações entre os diferentes tipos de dados e operações de leitura e escrita.
    
    - VIEW: **Responsável pela lógica de negócios e pela interação com os dados**, processam as requisições dos usuários, acessam os dados do modelo conforme necessário e retornam uma resposta, geralmente em forma de HTML, JSON ou outro formato adequado para o cliente.
    
    - TEMPLATE: **Responsável pela apresentação dos dados ao usuário**, definem a aparência da interface do usuário, misturando HTML com código Python (usando a linguagem de template do Django). Recebem dados das views e os renderizam de forma dinâmica para o usuário final. 

3. Utiliza o ORM (Object-Relational Mapping): Para interagir com o banco de dados de forma orientada a objetos, em vez de escrever SQL diretamente.    

### Interações entre os componentes

1. A interação começa quando o usuário faz uma requisição HTTP através do navegador. Essa requisição é enviada para a URL, que mapeia a URL para a View correspondente.

2. A View processa essa requisição, interagindo com o Model, conforme necessário, para obter ou modificar dados no banco. A View também poderá realizar operações adicionais, como autenticações ou validações.

3. O Model interage com o banco de dados por meio do ORM e executa operações de consulta, atualização, criação ou exclusão de dados no banco de dados. Ele então retorna os dados para as Views que envia para o Template, que insere esses dados no código HTML, enviando para a View uma página HTML renderizada como resposta.

4. A View envia a resposta final para o navegador e o usuário recebe a resposta da aplicação, que é a página HTML com os dados dinâmicos. 

5. Vale ressaltar que há situações em que pode ter views e templates que não precisam interagir diretamente com o model, como páginas estáticas ou páginas de informações e erros personalizadas.

![Imagem Ilustrativa das interações entre os componentes](image.png)

### Como instalar

1. Criar um ambente virtual.

2. Ativar o ambiente virtual e dentro do ambiente executar o comando `pip install django`

3. Criar o arquivo de requirements `pip freeze > requirements.txt`

## Primeiros passos 

1. Se necessário executar o comando ``django-admin help`

2. Iniciar o projeto `django-admin startproject setup .`  isso vai armazenar as configurações do projeto e criar um arquivo manage.py, esse arquivo é responsável por realizar a maioria dos comandos.

3. Se atentar a versão do python sendo utilizada ser a mesma do ambiente virtual.

4. Subir o servidor do projeto `python manage.py runserver`

5. Para interromper o server "Ctrl + c";

6. Tudo que afeta o projeto como um todo vai estar dentro do arquivo settings.py

## Variáveis de ambiente

1. Tem certas coisas no código que a gente não pode subir para o git por causa de segurança. A **SECRET_KEY** é uma delas. Se a gente tentar subir o próprio git avisa.

2. Se a gente remover do código para de funcionar, Então é preciso manter ele no código mas não subir para o git, e as variáveis de ambiente servem para isso.

3. Para resolver isso é preciso baixar um pacote `pip install python-dotenv`, atualiza o requirements e ve se ele ta lá para garantir `pip freeze > requirements.txt`.

4. Após baixar, criar um arquivo `.env` fora da pasta setup e dentro dele colar a variavel de ambiente
`SECRET_KEY = SUA_SECRET_KEY`

5. Após isso dentro do arquivo settings.py importar a classe doteenv exemplo abaixo
``` PY
# o "os" é usado para fornecer funcionalidades para manipular as variáveis.

from pathlib import Path, os # from pathlib import Path já estava no arquivo
from dotenv import load_dotenv

load_dotenv() # carrega as variáveis de ambiente.
```

6. Nesse momento as variáveis de ambiente estão carregadas, mas elas só não estão sendo usadas.

7. Para carregar as variáveis de ambiente, no caso a secret_key que é a que eu to vendo
``` PY
SECRET_KEY = str(os.getenv('SECRET_KEY')) # o nome da variavel que eu defini no arq .env    
```

## gitIgnore, "Subir apenas arquivos que eu quero e não todos"

1. Criar um arquivo `.gitignore` fora da pasta setup e venv.

2. O .gitignore é algo muito comum de se fazer, então já existe muitos prontos, e da de pegar eles através do **gitignore.io** um site onde eu coloco a linguagem/framework que estou codando, e ele me fornece um arquivo .gitignore pronto.

3. Copiando esse arq e colando no projeto, na maioria das vezes já da de subir o projeto, mas é importante sempre verificar.

## Como Subir pro gitHub 

- Na primeira vez do repositório

1. `git init` criar um repositório local 

2. `git add .` copia tudo pro repositório

3. `git commit -m "mensagem que aparece no comit` 

- Nesse momento as alterações estão no repositório local.

4. Vamos acessar o repositório que criamos no Github. Nele, na seção "...or create a new repository on the command line", copiaremos a linha que traz, além de git remote add origin, o link do repositório. No meu caso, o comando era `git remote add origin https://github.com/Marcos-Petry/curso_django.git`.

5. `git push origin master` aqui as alterações vão pro repositório do git.

- Outras vezes

1. `git status` para verificar.

2. git add <arquivos modificados> ou `git add .` para adicionar todos.

3. `git status` para verificar se tudo está ok.

4. `git commit -m "Mensagem do commit"`

5. `git push` envia as alterações para o repositório local.

6. Nesse momento as alterações estão salvas no repositório local, para subir de fato pro git executar `git branch` para descobrir o branch e depois `git push origin <nome-do-seu-branch>`

---

# Projeto, app e views

1. App e Projeto (startapp e startproject)
    - APP: É uma funcionalidade, um app é um pedaço da aplicação, que faz alguma coisa, **vários apps podem formar um projeto**
    - Projeto: Um projeto é a coleção de tudo que a gente tem, todas as configurações e etc. **um Projeto contém vários apps**.

2. Como criar um app
    - Executar o comando `python manage.py startapp NOME_APP`.
    - Após executar o comando uma pasta é criada, e dentro dela possui vários arquivos.
    - Agora é preciso ir até o arquivo settings.py  e em "INSTALLED_APPS" adicionar o app que foi criado.
    - Nesse momento o app já deve ter influência sobre o projeto.

3. Arquivos existentes ao criar um app
    - ___init__.py

    - admin.py

    - apps.py

    - models.py

    - tests.py

    - views.py -> responsável por tratar uma resposta e definir o que vai ser apresentado, qual página vai ser apresentada, qual o conteúdo dessa página.

4. Primeiros passos, criando uma view:
    - Dentro de views.py. Criar uma função para responder a requisição
        ``` py
            from django.shortcuts import render

            # responsável pela página principal da aplicação
            def index(request):
                return render(request, 'index.html') # chama o arq html dentro de templates
        ```
5. Definir/configurar as rotas
    1. Criar uma arquivo urls.py dentro do app, onde vai ficar as rotas do nosso app.
        ``` py
            from django.urls import path
            from galeria.views import index # importa o método criado na view

            urlpatterns = [
                path('', index) # define o método criado na view para a rota principal.
            ]
        ```
    2. Ir até o arquivo urls.py do projeto e incluir o arquivo de urls do app
        ``` py
            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('galeria.urls')) # rota principal
            ]
        ```
6. Templates
    1. Criar uma pasta "templates" dentro da pasta do projeto e fora de apps e setup, ou seja, na raiz do projeto.
    2. Ir até settings.py >> TEMPLATES e dentro de "DIR" definir o diretório da pasta templates que foi criada.
        ``` py
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ```
    3. Criar o arquivo dentro da pasta de templates. ex: index.html e adicionar o html desejado.

# Arquivos estáticos 

1. Para carregar os arquivos estáticos será necessário criar uma pasta onde ficaram TODOS os arquivos estáticos do Projeto, então dentro de setup criar uma pasta definida como 'static'.

2. Ir até `settings.py` e abaixo de "STATIC_URL" criar o caminho para os arquivos estáticos.
    ``` py
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'setup/static') # aponta para a classe "static" criada.
        ]
    ```

3. Criar o caminho absoluto para que o diretório consiga pegar os arquivos estáticos. Para isso, vamos inserir a "raiz" dos caminhos usando:
    ``` py
        STATIC_ROOT = os.path.join(BASE_DIR, 'static') # o python vai tratar e criar uma pasta quando rodar o camando abaixo onde aqui aponta
    ```

- Nesse ponto se existir algum arquivo estático ele não vai estar afetando o projeto, pois é necessário rodar o comando `python manage.py collectstatic` para fazer com que o Django manipule os arquivos estáticos da aplicação, para que possamos visualizá-los. Quando executado e se tudo estiver certo uma pasta static vai ser criada na raiz do projeto

4. Aceassar "templates/galeria > index.html" e adicionar o  seguinte trexo na primeira linha `{% load static %}` isso faz com que os arquivos estáticos sejam carregados.

5. Também é preciso mexer na forma que o arquivo css está sendo chamado, fica algo parecido com:
    ``` html
        <link rel="stylesheet" href="{% static '/styles/style.css' %}">
    ```
    - Estamos usando código python junto ao html, o que é denominado de **embedado**

6. Para todos os arquivos estáticos presente dentro do html é necessário fazer com que ele busque a informação do arquivo estático. então precisa adicionar `{% static'` na frente do caminho do arquivo e `' %}` ao final

7. É importante lembrar que para cada coisa que eu to tentando chamar aqui do html lá dos arquivos estáticos esse arquivo precisa existir, e eu preciso ter o controle a partir da view e a rota criada.

# Evitar repetições de código em arquivos html

1. Criar arquivos bases para o html comum entre arquivos.

2. No arquivo pai utilizar algo como `{% block content %}{% endblock %}` dentor do body

3. Nos arquivos filhos é preciso definir aonde o bloco será aberto e onde será fechado:
    `{% block content %} <!--Define um início de bloco()-->`
    `{% endblock %} <!--Define o final do bloco()-->`

4. Se existe muitas partes iguais no html é usado o partials "pedaços"
de código.
    - Criar uma classe partials dentro do nosso app.
        - aqui é por prática sempre começar o nome do arquivo com "_" no começo exemplo: `_footer.html`;
    
    - A partir do momento que temos o pedaço de código pronto é necessário adicionar ele na classe base para que classes filhas utilize-o.
        
