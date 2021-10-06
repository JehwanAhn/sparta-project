#kim_app.py 에서 크롤링한 DB를 flask 서버에 연결
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbmovie_review_test


#HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/', methods=['GET'])
def play_time_less_10(): # 10분안에 리뷰 보기
    play_time_10 = list(db.movies_review5.find({'play_list1': {"$lt": 10}}, {'_id': False}).sort('play_list1',-1))
    return jsonify({'movie_review_10':play_time_10})

def play_time_less_30(): # 30분안에 리뷰 보기
    play_time_30 = list(db.movies_review5.find({'play_list1': {"$lt": 30}}, {'_id': False}).sort('play_list1',-1))
    return jsonify({'movie_review_30':play_time_30})

def play_time_less_60(): # 한 시간안에 리뷰 보기
    play_time_60 = list(db.movies_review5.find({'play_list1': {"$lt": 60}}, {'_id': False}).sort('play_list1',-1))
    return jsonify({'movie_review_60':play_time_60})

def play_time_more_60(): #한 시간 이상
    play_time_more_60 = list(db.movies_review5.find({'play_list1': {"$gt": 60}}, {'_id': False}).sort('play_list1',-1))
    return jsonify({'movie_review_more_60':play_time_more_60})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)