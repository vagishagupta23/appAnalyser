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
      return redirect(url_for('search_result'))

@app.route('/searchResult', methods=['POST','GET'])
def search_result():
   search_tb= request.form['sr']
   res,result=search(search_tb)
   res=app_details(result)
   return render_template('searchResult.html', name=res) 
   


@app.route('/similarApp')
def appsimilar():
    return render_template('similar.html')

@app.route('/appCompare')
def comparing():
    return render_template('compare.html')   

if __name__ == '__main__':
   app.run()
