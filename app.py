#flask/bin/python
from flask import Flask, jsonify


app = Flask(__name__)

parcels = [
  {
    'id': 1,
    'Sender\'s email address': 'kelvin.ziroh@gmail.com',
    'Receiver\'s email address': 'favourgrl254@gmail.com',
    'Item': 'necklace',
    'Pick-up location': 'Nairobi',
    'Delivery Destination': 'Kilifi'
  },
  {
    'id': 2,
    'Sender\'s email address': 'kelvin.ziroh@gmail.com',
    'Receiver\'s email address': 'victorianzalee234@gmail.com',
    'Item': 'curl_sponge',
    'Pick-up location': 'Nairobi',
    'Delivery Destination': 'kilifi'
  }
]

@app.route('/api/v1/parcels', methods=['GET'])
def get_parcels():
    return jsonify({'parcels': parcels})

@app.route('/api/v1/parcels/<int:parcel_id>', methods=['GET'])
def get_parcel(parcel_id):
    parcel = [parcel for parcel in parcels if parcel['id'] == parcel_id]
    if len(parcel) == 0:
        abort(404)
    return jsonify({'parcel': parcel[0]})

if __name__ == '__main__':
    app.run(debug=True)
