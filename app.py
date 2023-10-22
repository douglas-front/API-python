from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        'id': 1,
        'name': 'creatina atp',
        'price': 0.00,
        'image': 'imagem'
    },
    {
        'id': 2,
        'name': 'creatina atp',
        'price': 0.00,
        'image': 'imagem'
    },
    {
        'id': 3,
        'name': 'creatina atp',
        'price': 0.00,
        'image': 'imagem'
    },
]

@app.route('/produtos', methods=['GET'])
def GetProducts():
    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['GET'])
def GetProductById(id):
    for produto in produtos:
        if produto['id'] == id:
            return jsonify(produto)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/produtos/<int:id>', methods=['PUT'])
def EditProduct(id):
    produto_alt = request.get_json()
    for produto in produtos:
        if produto['id'] == id:
            produto.update(produto_alt)
            return jsonify(produto)
    return jsonify({'error': 'Product not found'}), 404


@app.route('/produtos', methods=['POST'])
def AddProduct():
    newProduct = request.get_json()
    produtos.append(newProduct)

    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['DELETE'])
def DeleteProduct(id):
    for index, produto in enumerate(produtos):
        if produto['id'] == id:
            del produtos[index]
            return jsonify(produtos)
    return jsonify({'error': 'Product not found'}), 404


if __name__ == "__main__":
    app.run(port=3000, host='localhost', debug=True)
