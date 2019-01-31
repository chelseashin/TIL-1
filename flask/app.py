from flask import Flask, render_template, request, redirect
import os
import datetime
import requests
from bs4 import BeautifulSoup
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello there!'
    
    
# 5월 20일부터 d-day 카운트 출력
@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    vacation = datetime.datetime(2019, 5, 20)
    td = vacation - today
    return f'{td.days} 일 남았습니다.'


# variable routing
@app.route('/hi/<string:name>')
def greeting(name):
    # return f'안녕, {name}'
    return render_template('greeting.html', html_name=name)
    
    
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 3제곱은 {number**3} 입니다.'
    

# 반복문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)
    
    
# fake google
@app.route('/google')
def google():
    return render_template('google.html')


# pingpong
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # print(request.args)
    # name = request.args['name']
    name = request.args.get('name')
    msg = request.args.get('msg')
    return render_template('pong.html', name=name, msg=msg)


# pingpong GET/POST
@app.route("/ping_new")
def ping_new():
    return render_template('ping_new.html')
    
@app.route("/pong_new", methods=['POST'])
def pong_new():
    # name = request.form['name']
    name = request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)



# OPGG
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)


# CSV
@app.route('/timeline')
def timeline():
    # 지금까지 기록되어있는 방명록들을 보여주자!
    timelines = []
    with open('timeline.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            timelines.append(row)
    return render_template('timeline.html', timelines=timelines)

@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        filednames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=filednames)
        # writer = csv.DictWriter(f, fieldnames=['username', 'message'])
        
        writer.writerow({
            'username': username,
            'message': message
        })

    return redirect('/timeline')
    # return render_template('timeline_create.html', username=username, message=message)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)