from flask import Flask

from app import app

if __name__ == '__main__':
    app.run(debug=True, port=8001)