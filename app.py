from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        url = request.form.get('url')
        return jsonify(url)

if __name__ == '__main__':
    app.run(debug=True)