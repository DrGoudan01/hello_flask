from flask import Flask,render_template
import json
import os




app = Flask(__name__)
#自动reload
app.config['TEMPLATES_AUTO_RELOAD']=True

def get_file():
    filenames=os.listdir('E:\\hello_flask\\files')
    titiles={}
    for Filename in filenames:
        with open('E:\\hello_flask\\files\\'+Filename,'r') as file :
            tt=json.loads(file.read())
            #输出{'1': 'Linux', '2': 'Vim', '3': 'Git'}
        titiles[Filename]=tt
    return titiles
#return type {aaa:{aaaa:xxx},}


@app.route('/')
def index():
    file=get_file()
    filenames={}
    for x in file.keys():
        filenames[x]=file[x]['title']


    return render_template('index.html',titiles=filenames)

if __name__ == '__main__':
    print(get_file())

    app.run()

