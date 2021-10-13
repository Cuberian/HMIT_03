#!flask/bin/python
from flask import Flask, request, abort, json
from flask_cors import CORS
import urllib3
import certifi

app = Flask(__name__)
CORS(app)


@app.route('/find', methods=['POST'])
def index():
    if not request.json:
        abort(400)
    data = request.json
    encoded_data = json.dumps(data).encode('utf-8')

    url = 'https://ussouthcentral.services.azureml.net/workspaces/71c9c006a95243ce80d4a6a62d774f3e/services/463525060e94436f8d32da9d0ca07e09/execute?api-version=2.0&details=true'
    api_key = 'FxO2dYbHUbzZUTcjrpN4r6FkS67LRcBqEteAZXFCUEdOPQtG8KX7WoUBtoD9KWu2E3tvIxsvT8Ox/UnYwmpGiw=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
    r = http.request('POST',
                     url,
                     body=encoded_data,
                     headers=headers
                     )
    print(r.status)
    return json.loads(r.data.decode('utf-8'))


if __name__ == '__main__':
    app.run(debug=True)