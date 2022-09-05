from flask import Flask, request, render_template
from PredictWithPickle_module import PredictResult
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/stady.html')
def stady():
    return render_template('stady.html')

@app.route('/tools.html')
def tools():
    return render_template('tools.html')

@app.route('/Kuan_resume.html')
def Kuan_resume():
    return render_template('Kuan_resume.html')

@app.route('/Resume_Jimmy.html')
def Resume_Jimmy():
    return render_template('Resume_Jimmy.html')

@app.route('/Resume_Patrick.html')
def Resume_Patrick():
    return render_template('Resume_Patrick.html')

@app.route('/resume_Ya.html')
def resume_Ya():
    return render_template('resume_Ya.html')

@app.route('/Est_resume.html')
def Est_resume():
    return render_template('Est_resume.html')

@app.route('/Resume_Charlie.html')
def CV():
    return render_template('Resume_Charlie.html')

'''
@app.route('/data')
def data():
    x1 = int(request.args.get('x1'))
    x2 = int(request.args.get('x2'))
    x3 = int(request.args.get('x3'))
    #載入機器學習模型的pickle檔
    Y = PredictResult(x1,x2,x3)
    #Y傳給要顯示的頁面
    #return '<p>'+x1+','+y1+'</p>'
    #return '<p>'+str(Y)+'</p>'
    #render_template('sample.html',Y = Y)
    #return render_template('Presontationresult.html',Y = Y)
'''
'''
@app.route('/Presontation.html',methods=['x1','x2','x3'])
def Presontation():
    x1 = request.args.get('x1')
    x2 = request.args.get('x2')
    x3 = request.args.get('x3')
    #載入機器學習模型的pickle檔
    Y = PredictResult(x1,x2,x3)
    #Y傳給要顯示的頁面
    return '<p>'+Y+'</p>'
    #return render_template('Presontationresult.html')
'''


@app.route('/Presontation.html')
def Presontation():
    return render_template('Presontation.html')

@app.route('/submit')
def submit():
    x1 = int(request.args.get('x1'))
    x2 = int(request.args.get('x2'))
    x3 = int(request.args.get('x3'))
    #載入機器學習模型的pickle檔
    Y = PredictResult(x1,x2,x3)
    #Y傳給要顯示的頁面
    #return '<p>'+Y+'</p>'
    #R = '<p>'+Y+'</p>'
    return render_template('Presontationresult.html',Y = Y)

'''
    for Y2 in list(Y):
        R = print(Y2,end=' ')
        print(R)
'''

app.run(debug=True)