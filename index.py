from flask import Flask, render_template
import jyserver.Flask as jsf
app = Flask(__name__)
x11 = 0
@app.route('/')
def home():
    return render_template('home.html',
                            y11=x11
    )
if __name__ == '__main__':
    app.run(debug=True)

@jsf.use(app)
class App:
    def change(id):
        if x11 == 0:
            x11=1
        else:
            x11=0