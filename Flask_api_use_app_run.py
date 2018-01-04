from flask import Flask,request,make_response,jsonify
from ptt_crawler import PTT_Crawler

app = Flask('flask-api')
@app.route('/')
def hello_world():
    message = {'message' : 'hello world'}
    return jsonify(message)
@app.route('/postPTT',methods = ['GET','POST'])
def run_Crawler():
    if request.method == 'GET':
        crawler = PTT_Crawler(board = 'Gossiping',page = 1)
    elif request.method == 'POST':
        board = request.get_json().get('board','Gossiping')
        page = request.get_json().get('page',1)
        crawler = PTT_Crawler(board = board,page = page)
    res = crawler.run()
    return jsonify(res)

if __name__ == '__main__':
    app.run(port=8000)