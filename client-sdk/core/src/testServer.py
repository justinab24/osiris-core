from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/addNumbers', methods=['POST'])#binds POST requests to /addNumbers to this function
def add_numbers():
    try:
        data = request.json#retrieves data from incoming requests
        # Assuming data is a list of numbers pas sed as args
        result = sum(data)
        return jsonify(result=result), 200 #returns JSON response with successful HTTP status code
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=False)