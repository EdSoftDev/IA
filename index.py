from flask import Flask, render_template, Response, request, redirect, url_for

import tensorflow as tf
from tensorflow import keras

import numpy as np

from tensorflow.keras.utils import to_categorical


app = Flask(__name__)

data = np.loadtxt("data.txt" , delimiter=" ")
datos = []
numero_final = 0

x=data[:,:35]
y=data[:,35:36]

x_grafico = x.reshape(40,7,5)
y_data = to_categorical(y, num_classes=10)


from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

@app.route('/')
def home():
    return render_template('home.html',
                            datos=numero_final
    )
@app.route('/enviar', methods=["POST"])
def enviar():
    dato = request.form.get("datos")
    dato_auxiliar = list(dato)
    global datos
    model_recuperado = keras.models.load_model('entrenamiento.h5')
    x1 = float(dato_auxiliar[0])
    x2 = float(dato_auxiliar[2])
    x3 = float(dato_auxiliar[4])
    x4 = float(dato_auxiliar[6])
    x5 = float(dato_auxiliar[8])
    x6 = float(dato_auxiliar[10])
    x7 = float(dato_auxiliar[12])
    x8 = float(dato_auxiliar[14])
    x9 = float(dato_auxiliar[16])
    x10 = float(dato_auxiliar[18])
    x11 = float(dato_auxiliar[20])
    x12 = float(dato_auxiliar[22])
    x13 = float(dato_auxiliar[24])
    x14 = float(dato_auxiliar[26])
    x15 = float(dato_auxiliar[28])
    x16 = float(dato_auxiliar[30])
    x17 = float(dato_auxiliar[32])
    x18 = float(dato_auxiliar[34])
    x19 = float(dato_auxiliar[36])
    x20 = float(dato_auxiliar[38])
    x21 = float(dato_auxiliar[40])
    x22 = float(dato_auxiliar[42])
    x23 = float(dato_auxiliar[44])
    x24 = float(dato_auxiliar[46])
    x25 = float(dato_auxiliar[48])
    x26 = float(dato_auxiliar[50])
    x27 = float(dato_auxiliar[52])
    x28 = float(dato_auxiliar[54])
    x29 = float(dato_auxiliar[56])
    x30 = float(dato_auxiliar[58])
    x31 = float(dato_auxiliar[60])
    x32 = float(dato_auxiliar[62])
    x33 = float(dato_auxiliar[64])
    x34 = float(dato_auxiliar[66])
    x35 = float(dato_auxiliar[68])
    salida_nn = model_recuperado.predict([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35]])

    global numero_final
    numero_final = np.argmax(salida_nn[0])
    return redirect("/")

@app.route('/clear', methods=["POST"])
def clear():
    global datos
    datos.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)


