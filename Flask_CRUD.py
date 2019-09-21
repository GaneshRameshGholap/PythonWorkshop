from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript', 'id':1}, {'name' : 'Python', 'id': 2}, {'name' : 'Ruby', 'id': 3}]


@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})


@app.route('/id', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne():
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
	print(request.json['name'])
	language = {'name' : request.json['name']}

	languages.append(language)
	return jsonify({'languages' : languages})


@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languages if language['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'language' : langs[0]})


@app.route('/lang/<string:id>', methods=['DELETE'])
def removeOne(id):
	lang = [language for language in languages if language['id'] == int(id)]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True, port=8000) #run app on port 8080 in debug mode