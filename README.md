# django_backend_challenge
  Foi utilizado JWT para fazer as autenticações, para isso é necessário utilizar seguinte a seguinte requisição para autenticar. 
  POST https://djangoapichallenge-production.up.railway.app/api/token/
  {
    "username": "client",
    "password": 123456
}
esse usuário foi criado para ter o acesso as tasks. 
Após essa chamada, TODAS as requisições a seguir exigem o Authentication Bearer com o access token que receberá de resposta. 

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

Bibliotecas essenciais utilizadas: 
django rest framework para fazer a função rest, 
drf-yasg foi utilizado para criar o swagger https://djangoapichallenge-production.up.railway.app/swagger/schema/
gunicorn para o deploy no railways 
psycopg2-binary para a integração com o postgresql
djangorestframework-simplejwt para fazer a autenticação jwt
