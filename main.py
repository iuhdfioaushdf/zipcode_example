
import os
from flask import Flask


app = Flask(__name__)


# load file before app starts
with open('zip_code_list.txt', 'r') as f:
    zips = {}
    for lines in f.readlines():
        data = lines.strip().split(',')
        zips[data[0].strip()] = data[1:]



@app.route('/<zipcode>/', methods=['GET'])
def get_coords(zipcode):

    return str(zips[zipcode])





if __name__ == '__main__':

    with app.app_context():
        port = int(os.environ.get("PORT", 8801))
        app.run(host='0.0.0.0', port=port, debug=True)