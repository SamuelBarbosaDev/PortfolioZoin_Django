<h1>Meu portfólio</h1>
<h3>Objetivo:</h3>
    <p>
        Nesse projeto busquei uma forma de condensar aquilo que 
        havia estudado sobre django e python, durante a criação 
        do Portfólio passei por todas as etapas, desde a ideia, 
        desenvolvimento, até que enfim ele fosse ao ar, no dia 3 
        de setembro, resumindo aprendi muito com essa experiência 
        desde como fazer um deploy, testar, montar a regra de 
        negócios, etc. 
    <a href="https://samuelbarbosa-portfolio.herokuapp.com/">Link para o site</a>: 
    </p>
    
<h3>Como Funciona:</h3>

- Crie um ambiente virtual
```
python -m venv venv
```

- Ative o ambiente virtual
```
source venv/bin/activate
```

- instale as dependências
```
pip install -r requirements.txt
```

- Entre na pasta apps/
```
cd apps/
```

- excute as migrations
```
python manage.py migrate
```

- Crie um usuario admin
```
python manage.py createsuperuser --email admin@admin.com --username admin
```

- Crie sua senha
```
******
```

- Repita a senha
```
******
```

- Excute o projeto localmente, Fim.
```
python manage.py runserver
```

<h3> O que aprendi:</h3>
    <p>
        De ante mão digo que aprendi muito coisa, por exemplo aprendi que é necessario estudo sobre AWS,
        para aumenta a qualidade dos projetos no futuru.
    </p>

<h3>Tecnologias utilizadas:</h3>

  - Linguagens:
    - python==3.10.4
  
  - Libs:
    - asgiref==3.5.2
    - autopep8==1.7.0
    - dj-database-url==1.0.0
    - Django==4.1
    - django-crispy-forms==1.14.0
    - django-filter==22.1
    - django-on-heroku==1.1.2
    - gunicorn==20.1.0
    - Pillow==9.2.0
    - psycopg2-binary==2.9.3
    - pycodestyle==2.9.1
    - python-decouple==3.6
    - sqlparse==0.4.2
    - toml==0.10.2  
    - whitenoise==6.2.0
  - Framework:
    - Django==4.1