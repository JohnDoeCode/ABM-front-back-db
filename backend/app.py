from flask import Flask, request, jsonify
usuarios = {
    "Guillermo":"1234"
}
app = Flask(__name__)
@app.route("/login", methods = ["POST"])
def login():
    usuario = request.json["username"]
    password = request.json["password"]
    if usuario in usuarios:
        if usuarios[usuario] == password:
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "error"})
    else:
        return jsonify({"status": "error"})

app.run(debug=True)