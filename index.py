from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

datos = []
@app.route('/')
def home():
    return render_template('home.html',
                            datos=datos
    )
@app.route('/enviar', methods=["POST"])
def enviar():
    dato = request.form.get("datos")
    datos.clear()
    datos.append(dato)
    return redirect("/")

@app.route('/clear', methods=["POST"])
def clear():
    datos.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)


