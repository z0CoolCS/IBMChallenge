from flask import Flask, request, session, jsonify
import api_rest as serv

app = Flask(__name__)
app.secret_key = 'myclavesecreta'
scores = []

@app.route("/", methods = ["POST", "GET"])
def query():
    if request.method == "GET":
        return "Hello world"
    elif request.method == "POST":
        payload = request.json
        global scores

        if payload.get("reset") :
            scores = []
            print("size of scores:: ",len(scores))
            return jsonify({"done":"done"})

        question = payload['respuesta']
        name = payload['nombre']
        print(question)

        score = serv.get_score(question)
        print(score)
        scores.append(score)

        response = {"hola" : "Alright"}
        if payload.get("evaluacion") :
            print(sum(scores), len(scores))
            average = sum(scores) * 1.0 / len(scores)
            response["average"] = average
            print(average)
            if average < 5:
                response["contratado"] = "no"
            else :
                response["contratado"] = "si"

        return jsonify(response)
    else:
        print(request.data)
        return "200"

if __name__ == "__main__" :
    app.run(debug = True, port = 8000)

