import os.path

from flask import Flask, request
from slugify import slugify

app = Flask(__name__)

filename = 'dl_all.sh'


@app.route("/", methods=['GET'])
def index():
    key = request.args.get('key', '')
    title = slugify(request.args.get('title', ''), separator='_')
    i = int(request.args.get('i', ''))
    if os.path.isfile(filename):
        with open(filename) as f:
            if key in f.read():
                return ''
    with open(filename, 'a') as f:
        f.write(f'curl "https://embedwistia-a.akamaihd.net/deliveries/{key}/file.mp4" --output "{i:03}_{title}.mp4"\n')
    return ''
