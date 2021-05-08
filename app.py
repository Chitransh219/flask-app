from flask import Flask, render_template, request


app=Flask(__name__,template_folder='template')


@app.route('/')

def index():
    return render_template('index.html')

@app.route('/app.py', methods=['POST'])
def getvalue():
    bkpserver=request.form['bkpserver']
    srcserver=request.form['srcserver']
    tcktno=request.form['tcktno']
    dor=request.form['dor']
    filepath=request.form['filepath']
    
    print(bkpserver)
    print(srcserver)
    print(tcktno)
    print(dor)
    print(filepath)
    return render_template('/pass.html',b=bkpserver,s=srcserver,t=tcktno,d=dor,f=filepath)
    

if __name__=='__main__':
    app.run()
