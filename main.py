from flask import Flask, request
import time, json, requests

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        'Home':'Enter these urls on http://127.0.0.1/[url]. Returns data as json',
        'urls':['/iss/', '/chuck-norris/', '/dog/', '/breweries/', '/pokemon/?pokemon=ENTER_POKEMON_NAME/', '/random-user/', '/cat-fact/', '/joke/'],
        'time stamp:': time.time()
    }
    jdump = json.dumps(data, indent=4)
    return f'<pre>{jdump}</pre>'

@app.route('/iss/')
def get_iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        data = json.dumps(data, indent=4)
        return f'<pre>{data}</pre>'
    else:
        return 'Error: Failed to get request'
    

@app.route('/chuck-norris/')
def get_chuck_norris_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        data = json.dumps(data, indent=4)
        return f"<pre>{data}</pre>"
    else:
        return 'Error: Failed to get request'


@app.route('/dog/')
def get_dog_image():
    url = 'https://dog.ceo/api/breeds/image/random'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        jdump = json.dumps(data, indent=4)
        return f'<pre>{jdump}</pre>'
    else:
        return 'Error: Failed to get request'


@app.route('/breweries/')
def get_breweries():
    url = 'https://api.openbrewerydb.org/breweries'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        jdump = json.dumps(data, indent=4)
        return f'<pre>{jdump}</pre>'
    else:
        return 'Error: Failed to get request'


@app.route('/pokemon/', methods=['GET'])
def get_pokemon():
    pokemon = str(request.args.get('pokemon'))  #pokemon/?pokemon=ENTER_POKEMON_NAME/
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        jdump = json.dumps(data, indent=4)
        return f'<pre>{jdump}</pre>'
    else:
        return 'Error: Failed to get request'



@app.route('/random-user/')
def get_random_user():
    url = 'https://randomuser.me/api/'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        jdump = json.dumps(data, indent=4)
        return f'<pre>{jdump}</pre>'
    else:
        return 'Error: Failed to get request'



@app.route('/cat-fact/')
def get_cat_fact():
    url = 'https://catfact.ninja/fact'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        jdump = json.dumps(data, indent=4)
        return f'<pre>{jdump}</pre>'
    else:
        return 'Error: Failed to get request'


@app.route('/joke/')
def get_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    data = requests.get(url)
    
    if data.status_code == 200:
        data = data.json()
        jdump = json.dumps(data, indent=4)
        return f'<pre>{jdump}</pre>'
    else:
        return 'Error: Failed to get request'


if __name__ == '__main__':
    app.run()
