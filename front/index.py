from flask import Flask, render_template
import ssl

app = Flask(__name__)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.crt', 'server_secret.key')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/english")
def english():
    return render_template("index.html")


if __name__ == "__main__":
    #app.run(host='0.0.0.0',port=5000,ssl_context=context, threaded=True,debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
