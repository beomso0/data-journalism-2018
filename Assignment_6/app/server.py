from flask import Flask, jsonify, request
app=Flask(__name__)

@app.rout("/")
def index():
	return "hello World!"

@app.route("/keyboard")

def keyboard():
	    res = {
        'type': 'buttons',
        'buttons': ['chat']
        }
        return jsonify(res)
        
if __name__ == "__main__":
        app.run(debug=True)
