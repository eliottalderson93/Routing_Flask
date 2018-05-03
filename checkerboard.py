from flask import Flask,render_template
app = Flask(__name__)
@app.route('/<x>/<y>')
def checkerboard_init(x,y):
    x=int(int(x)/2)
    y=int(y)
    block_px=50
    num_px_w=block_px*x
    num_px_h=block_px
    color_light = 'red'
    color_dark = 'black'
    return render_template("checkerboard.html",x=x,y=y,block_px=block_px,num_px_w=num_px_w,num_px_h=num_px_h,color_light=color_light,color_dark=color_dark)
# @app.route('/play/')
# def playground_init():
#     class Playground():
#         def __init__(self,num=3,color='lightblue'):
#             self.num = num
#             self.color = color
#         def times():
#     play1 = Playground()
#     return render_template("playground.html",times =play1.num,this_color=play1.color)
# @app.route('/play/<times>/')
# def playground_init_2(times):
#     time_py = int(times)
#     return render_template("playground.html",phrase = 'default',times =time_py)
# @app.route('/play/<times>/<this_color>/')
# def playground_init_3(times,this_color):
#     time_py = int(times)
#     this_color_py = this_color
#     return render_template("playground.html",phrase = 'default',times =time_py,this_color=this_color_py)


app.run(debug=True)