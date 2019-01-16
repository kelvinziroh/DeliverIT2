#flask/bin/python
"""Create api endpoints for create a parcel order, retrieve parcel by id,
    get all parcels and cancel a parcel order"""
    
from flask import Flask, jsonify, request, abort


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

    # """Get all parcel orders"""
@app.route('/api/v1/parcels', methods=['GET'])
def get_parcels():
    return jsonify({'parcels': parcels})

    # """Get parcel by id"""
@app.route('/api/v1/parcels/<int:parcel_id>', methods=['GET'])
def get_parcel(parcel_id):
    parcel = [parcel for parcel in parcels if parcel['id'] == parcel_id]
    if len(parcel) == 0:
        abort(404)
    return jsonify({'parcel': parcel[0]})

    # """Create a parcel delivery order"""
@app.route('/api/v1/parcels', methods=['POST'])
def create_parcel():
    if not request.json or not 'Item' in request.json:
        abort(400)
    parcel = {
        'id': parcels[-1]['id'] + 1,
        'Sender\'s email address': request.json.get('hey@gmail.com'),
        'Receiver\'s email address': request.json.get('ken@gmail.com'),
        'Item': request.json['Item'],
        'Pick-up location': request.json.get('Nairobi'),
        'Delivery Destination': request.json.get('Kitale'),
    }
    parcels.append(parcel)
    return jsonify({'parcel': parcel }), 201

if __name__ == '__main__':
    app.run(debug=True)
