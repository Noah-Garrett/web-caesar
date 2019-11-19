from flask import Flask, request
import caesar
import helpers


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/rotated_text", methods=['POST'])
def encrypt():
    rot=request.args.get("rot")
    text=request.args.get("text")
    new_text=rotate_string(text, int(rot))

    return new_text



form = '''
<!DOCTYPE html>
<html>
  <html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
    <form rotate="/rotated_text" method='POST'>
    Rotate By:<input name="rot" type="text" value=0> 
   <textarea name="text"> </textarea>
   <input type="submit" value= rotate>
         
      
    </body>
</html>
'''
@app.route("/")
def index():
    return "Lets get ROTATING!" + form  



app.run()

