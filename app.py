from flask import Flask, render_template, request, redirect
from scrape3 import *
app = Flask(__name__)

@app.route("/")
def main():
   return render_template('index.html')

@app.route('/getStarted')
def starting():
    return render_template('started.html')

@app.route('/appSearch', methods=['POST','GET'])
def appsearch():
   if request.method == 'GET':
      return render_template('search.html')
   elif request.method == 'POST':
      search_tb= request.form['sr']
      res,result=search(search_tb)
      #print res
      res=app_details(result)
      return render_template('searchResult.html', name=res)
      #return redirect(url_for('search_result'))

@app.route('/searchResult', methods=['POST','GET'])
def search_result():
    return render_template('searchResult.html', name = {})   


@app.route('/similarApp')
def appsimilar():
    return render_template('similar.html')

@app.route('/appCompare')
def comparing():
    return render_template('compare.html')   

if __name__ == '__main__':
   app.run(debug=True)
