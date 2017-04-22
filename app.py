from flask import Flask, render_template, request, redirect, session, url_for
#from flask_images import resized_img_src
#from PIL import Image
import scrape3
app = Flask(__name__)
app.secret_key="whats up"
#image=Images(app)

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
      session['app_name']=search_tb
      #print search_tb
      #res,result=scrape3.search(search_tb)
      #print res
      #res=scrape3.app_details(result)
      #return render_template('searchResult.html', name=res)
      return redirect(url_for('search_result'))

@app.route('/searchResult', methods=['POST','GET'])
def search_result():
   aname=session['app_name']
   res,result=scrape3.search(aname)
   #print res
   res=scrape3.app_details(result)
   return render_template('searchResult.html', name =res)   


@app.route('/similarApp', methods=['POST','GET'])
def appsimilar():
   #session['appname'] = 0
   if request.method == 'GET':
      return render_template('similar.html')
   elif request.method == 'POST':
      searchtb= request.form['tb']
      session['appname']=searchtb
   return redirect(url_for('similar_result'))

@app.route('/similarResult', methods=['POST','GET'])
def similar_result():
   anme=session['appname']
   rest,results=scrape3.search(anme)
   #print res
   rest=scrape3.SimilarApps(results)
   return render_template('similarResult.html', name =rest)   

@app.route('/appCompare')
def comparing():
    return render_template('compare.html')   

if __name__ == '__main__':
   app.run(debug=True)
