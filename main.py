from flask import Flask, request
from pprint import pp

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hola():
    """para fines demostrativos :)"""

    data = request.json
    pp(data)
    contraints = data["constraints"]
    pp(contraints)

    min([1, 3, 4])
    max([1, 3, 4])

    return data


app.run("0.0.0.0", debug=True)