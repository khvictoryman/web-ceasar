from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eeeeee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method='post'>
            <lable for="rotateby">
                Rotate by:
                    <input type="text" id="rot" name="rot" value=0 />
            </lable>
            <br>
            <textarea id="text" name="text" >{0}</textarea>
            <input type="submit" id="submit" name="submit" value="Submit" />
        </form>

    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    encrypted_text = rotate_string(text, int(rot))

    return form.format(encrypted_text)

@app.route("/")
def index():
    return form.format("")

app.run()

