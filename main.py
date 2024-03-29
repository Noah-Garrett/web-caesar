from flask import Flask, request, redirect
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True




form = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
    <form action="/rotate-text" method='POST'>
    Rotate By:<input name="rot" type="text" value=0> 
   <textarea name="text"> {0} </textarea>
   <input type="submit" value= rotate>
    </form>
         
      
    </body>
</html>
'''
@app.route("/")
def index():
    return form.format("")




@app.route("/rotate-text", methods=['POST'])
def encrypt():
    rot=request.form['rot']
    text=request.form['text']
    rot=int(rot)
    new_text=rotate_string(text, rot)
    
    return form.format(new_text)



app.run()

