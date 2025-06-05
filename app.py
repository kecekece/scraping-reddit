from flask import Flask, render_template, request, jsonify

from logic import getRedditData

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        dataJson = request.get_json()
        url = dataJson.get('url')
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

if __name__ == '__main__':
    app.run(debug=True)