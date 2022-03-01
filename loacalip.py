from crypt import methods
from ipaddress import ip_address
from flask import Flask, render_template, request
import flask
import IRIS_DATASET

# from MNIST_DATASET import *
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def ids():
    if request.method == "POST":
        sepal_length = request.form["sepallength"]
        sepal_width = request.form["petalwidth"]
        petal_length = request.form["petallength"]
        petal_width = request.form["petalwidth"]
        y_pred = [[sepal_length, sepal_width, petal_length, petal_width]]
        trained_model = IRIS_DATASET.training_model()
        prediction_value = trained_model.predict(y_pred)
        setosa = "setosa"
        versicolor = "versicolor"
        virginica = "virginica"
        if prediction_value == 0:
            return render_template("index.html", setosa=setosa)
        elif prediction_value == 1:
            return render_template("index.html", versicolor=versicolor)
        else:
            return render_template("index.html", virginica=virginica)
    return render_template("index.html")


@app.route("/getip")
def ip():
    ip_address = flask.request.remote_addr
    return "IP:" + ip_address


if __name__ == "__main__":
    app.run(debug=True)
# app.run(host='0.0.0.0', port=5000)
