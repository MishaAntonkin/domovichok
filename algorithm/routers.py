from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.data)
    print(request.args)
    print(request.args.get('district'))
    print(request.form.get('district'))
    print(request.form.get('price'))
    return 'Ok'

if __name__ == "__main__":
    app.run(debug=True, port=5000)