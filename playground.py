from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html",phrase = 'default',times=1)
@app.route('/play/')
def playground_init():
    class Playground():
        def __init__(self,num=3,color='lightblue'):
            self.num = num
            self.color = color
        def times():
    play1 = Playground()
    return render_template("playground.html",times =play1.num,this_color=play1.color)
@app.route('/play/<times>/')
def playground_init_2(times):
    time_py = int(times)
    return render_template("playground.html",phrase = 'default',times =time_py)
@app.route('/play/<times>/<this_color>/')
def playground_init_3(times,this_color):
    time_py = int(times)
    this_color_py = this_color
    return render_template("playground.html",phrase = 'default',times =time_py,this_color=this_color_py)







app.run(debug=True)