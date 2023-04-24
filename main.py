from flask import Flask, render_template
app = Flask(__name__)

@app.route('/customers/<int:id>')
def getCustomer(id):
    return 'Devuelve un cliente otros'

@app.route('/customers')
def getAllCustomers():
    return 'Devuelve listado de clientes'


@app.route('/customers', methods=['POST'])     
def saveCustomer():
    return 'Envia un cliente'

@app.route('/customers/<int:id>', methods=['DELETE'])    
def removeCustomer(id):
    return 'Elimina un cliente'



