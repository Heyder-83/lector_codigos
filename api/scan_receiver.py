from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Escanea y envía tu código</h2>
    <form action="/scan" method="POST">
        <input type="text" name="codigo" placeholder="Pega aquí el código escaneado" />
        <input type="submit" value="Enviar" />
    </form>
    '''


@app.route('/scan', methods=['POST'])
def scan():
    codigo = request.form.get('codigo')
    if not codigo:
        return "Codigo no recibido", 400
    
    print(f"Código recibido desde celular: {codigo}")
    return f"Codigo recibido: {codigo}"