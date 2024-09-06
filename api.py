from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Adesina joseph",
        "email": "adesina.joseph@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

#   POst route

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":   
    app.run(debug=True)






#request data from a specified resource
#   GET
#create a resource
# POST
#update a resource
# PUT
#delete a resource
# DELETE