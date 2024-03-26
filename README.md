# Django Backend Challenge
Projeto da API feito em Django e com autenticação JWT. 

# Funcionalidade

A finalidade dessa aplicação é para criar tasks no formato ToDo list. 

## Autenticação 
Foi criado um superuser para acessar a aplicação e testar a autenticação JWT. 
Para solicitar o token de acesso basta enviar o body com a requisição a seguir: 
   POST https://djangoapichallenge-production.up.railway.app/api/token/
  {
    "username": "client",
    "password": 123456
}

## **Todas as operações a seguir exigem o token validado e passado no Authorization pelo Bearer**
Para usar no postman basta seguir essa imagem
![Inserindo token via postman](https://i.imgur.com/GRF6MEz.png)

     GET https://djangoapichallenge-production.up.railway.app/tasks

Listará todas as tasks

    GET https://djangoapichallenge-production.up.railway.app/tasks/{id_task}/
Retorna a task específica 

    PUT  https://djangoapichallenge-production.up.railway.app/tasks/{id_task}/
    {
      "title": "Testando put",
      "description": "alguma coisa legal aqui"
    }

Esse body irá editar a task escolhida 

    DELETE https://djangoapichallenge-production.up.railway.app/tasks/{id_task}/

Remove a task escolhida. 

**

## Bibliotecas essenciais utilizadas:

** 

 - django rest framework para fazer a função rest, 
 - drf-yasg foi utilizado para criar o swagger https://djangoapichallenge-production.up.railway.app/swagger/schema/
 - gunicorn para o deploy no railways 
 - psycopg2-binary para a integração com o postgresql
 - djangorestframework-simplejwt para fazer a autenticação jwt

**

## Algumas estruturas


![enter image description here](https://i.imgur.com/vIEYL2h.png)


![enter image description here](https://i.imgur.com/SHB4xQ2.png)

![enter image description here](https://i.imgur.com/Ki524o5.png)
![enter image description here](https://i.imgur.com/go9JoQi.png)

## Hospedado em railway
https://djangoapichallenge-production.up.railway.app
