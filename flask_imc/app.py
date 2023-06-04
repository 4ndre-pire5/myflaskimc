from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/imccalc', methods=['POST'])

def calculateIMC():
    data = request.json
    weight = data['weight']
    height = data['height']

    imc = (weight/(height*height))
    description = getImcDescription(imc)

    return jsonify({
        "imc": imc,
        "description": description             
    })
  
def getImcDescription(imc):
    if imc < 18.5: return 'Magreza'
    elif imc < 24.9: return 'Normal'
    elif imc < 30: return 'Sobrepeso'
    return 'Obesidade'
    
app.run(host='localhost', port=8080, debug=True)

