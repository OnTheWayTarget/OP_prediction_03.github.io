from flask import Flask, request, render_template



# # #
app = Flask(__name__)

@app.route('/')
def hello():
    return '很有精神!'


app.run(debug=True)