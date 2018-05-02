from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/dojo')
def dojo():
  return "Dojo" 

@app.route('/say/<word>') 
def say(word):
    print(word)
    return "hi "+word

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/repeat/<num_times>/<str1>')
def repeat(num_times,str1):
    num = int(num_times)
    ret = str1*num
    print(str1*num)
    return ret

#// your code here
#The above route would be triggered when a user request 
# localhost:5000/some_route

if __name__=="__main__": 
    app.run(debug=True)