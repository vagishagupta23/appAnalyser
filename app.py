from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
   return render_template('index.html')

@app.route('/getStarted')
def starting():
    return render_template('started.html')
   
@app.route('/appSearch')
def appsearch():
    return render_template('search.html')


@app.route('/similarApp')
def appsimilar():
    return render_template('similar.html')   

if __name__ == '__main__':
   app.run(debug = True)
