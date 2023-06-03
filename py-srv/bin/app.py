from flask import Flask, render_template
from rocksdict import Rdict, Options, SstFileWriter
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def main(value: int=0):
    key = "123-456-789"
    writer = Rdict("file1.sst")
    writer[key] = value
    writer.close()

def increment() -> int:
    db = Rdict("file1.sst")
    key = "123-456-789"
    value = db[key]
    value += 1
    db.close()
    main(value)
    return value


@app.route("/")
def hello():
    title = 'Python Flask RocksDb MVC Example'
    visits = increment()
    return render_template("index.html", title=title, visits=visits)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5000)
