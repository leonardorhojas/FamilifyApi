# FamilifyApi


API to translate from text/morse 

Support following endpoints:

`POST /translate/2morse -H 'Authorization: Bearer acces_token' text='hola mundo'`

`POST /translate/2text -H 'Authorization: Bearer acces_token' 'text=.... --- .-.. .- -- ..- -. -.. ---'`


##Installation
Use the package manager pip to install API Familify, previously you should create a vertualenv.

python3 -m venv env
pip install -r requirements.txt
Usage
source env/bin/activate

cd somepath/Familify/familify

python manage.py runserver

## USAGE

In order to access the endpoint you should generate a jwt token accessing to the endpoint :

`http://127.0.0.1:8000/api/token/`

this will response with something like:

`{
    "refresh": "xxx.yyy.zzz",
    "access": "XXX.YYY.ZZZ"
}`

after that you can use the access token to access the endpoints:


`$ curl -X POST "http://localhost:8000/translate/2text" -H "access-token" -d
"text=.... --- .-.. .- -- ..- -. -.. ---" 
{ code:200, response: 'HOLA MUNDO’}`


`$ curl -X POST "http://localhost:8000/translate/2morse" -H "access-token" -d "text='HOLA MUNDO'}"
{code:200, response: '.... --- .-.. .- -- ..- -. -.. ---'}
`

