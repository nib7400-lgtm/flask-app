from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return '''
    <html><body>
        <h2>Bank A - Smart Transfer</h2>
        <form method="POST">
            Nama Penerima: <input name="input_text"><br><br>
            <input type="submit" value="Cek">
        </form>
    </body></html>
    '''

@app.route('/', methods=['POST'])
def my_form_post():
    input_text = request.form['input_text']
    return f"You entered: {input_text} - System recommends internal transfer to keep CASA"

if __name__ == "__main__":
    app.run(debug=True)