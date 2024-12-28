
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Recuperar o cookie de visitas
    visits = request.cookies.get('visits')

    if visits is None:
        visits = 1
    else:
        visits = int(visits) + 1

    # Criar a resposta com a mensagem de visitas
    response = make_response(f"<html><head><title>Visits</title></head><body style='background-color:#000000;color:#ffffff'>visits: {visits} times<body></html>")

    # Definir o cookie com o número atualizado de visitas
    response.set_cookie('visits', str(visits), max_age=60*60*24*365)  # Cookie válido por 1 ano

    return response

if __name__ == '__main__':
    app.run(debug=True)
