from flask import Flask
from flask import jsonify
from flask_cors import CORS
import ZyXel
app = Flask(__name__)
CORS(app)
zyxel = ZyXel.ZyXEL()

@app.route("/api/v1/zyxel/flow", methods=['GET'])
def zyxel_flow():
    data = zyxel.getParseingData
    return jsonify(data)


app.run(host="0.0.0.0", port=1291)
