from flask import Flask, render_template, request, jsonify
from prawcore import exceptions as pcExcp
from praw import exceptions as prawExcp
import re

from core.logic import getRedditData

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        dataJson = request.get_json()
        url = dataJson.get('url')
        
        URL_REGEX = re.compile(
            r'^(https?:\/\/)[\w\-\.]+(\.[\w\-]+)+([\/\w\-\.\?\=\&\#]*)*$', re.IGNORECASE
        )
        if not URL_REGEX.match(url):
            return jsonify({"error":"URL tidak valid"}), 400

        # return jsonify(dataJson)
        try:
            data = getRedditData(redditUrl=url)
            return jsonify(data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except TypeError as e:
            return jsonify({
                "data" : 'error',
                "error": str(e),
                # "error": e.args,
            }), 405
        except RuntimeError as e:
            return jsonify({
                "error": str(e),
            }), 500
        except prawExcp.InvalidURL as e:
            return jsonify({
                "error": str(e),
            }), 500


if __name__ == '__main__':
    app.run(debug=True)