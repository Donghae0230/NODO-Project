from curses import flash
from flask import Blueprint, render_template, request, flash
import psycopg2
import pickle
import pandas as pd
from datetime import datetime

bp = Blueprint('main', __name__, url_prefix='/')

# postgreSQL 연동
conn = psycopg2.connect(
    host="salt.db.elephantsql.com",
    database="bwvmpjyr",
    user="bwvmpjyr",
    password="p1K37MwTlB6-9XNHgrGnIzZ-As7xc0iQ")

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_name = request.form.get('user_name')
        user_age = request.form.get('user_age')
        user_gender = request.form.get('user_gender')
        book_title = request.form.get('book_title')
        current_time = datetime.now()

        cur = conn.cursor()
        
        # 키워드로 제목 검색
        book_title = '%' + book_title + '%'
        sql_isbn = f'SELECT title, isbn, cover FROM books WHERE title LIKE \'{book_title}\''
        cur.execute(sql_isbn)
        book = cur.fetchone()
        
        # 사용자가 검색한 도서정보 저장
        try:
            book_title = book[0]
            book_isbn = book[1]
            book_cover = book[2]
        except TypeError:
            flash('해당 도서는 준비중입니다')
            return render_template('index.html')
        
        # 사용자 정보 DB에 저장
        sql_insert = f"""INSERT INTO users (name, age, gender, isbn, tiem) 
                        VALUES (%s, %s, %s, %s)"""
        cur.execute(sql_insert, (user_name, user_age, user_gender, book_isbn, current_time))
        conn.commit()
                
        # 추천 도서 검색
        isbn_list = recommendation(book_isbn)
    
        sql_books = f'''SELECT cover, title, writer, publisher, link FROM books 
                 WHERE isbn in (%s, %s, %s, %s, %s, %s)'''
        cur.execute(sql_books, (isbn_list[0], isbn_list[1], isbn_list[2], isbn_list[3], isbn_list[4], isbn_list[5]))
        book_list = cur.fetchall()
        
        user = {'name': user_name,
                'title': book_title,
                'cover': book_cover}
        return render_template('result.html', user=user, book_list=book_list)

with open("book_app\data.pickle","rb") as fr:
    data = pickle.load(fr)

# 유사한 도서 5권의 TSBN을 반환하는 함수
def recommendation(ISBN):
    indices = pd.read_csv('book_app\indices.csv', 
                          index_col=0,
                          squeeze=True)     # 인덱스를 활용하기 위해 Series 형태로 불러오기
    idx = indices[indices==ISBN].index[0]
    
    # 유사도 높은 책 5개 선정
    sim_score = list(enumerate(data[idx]))
    sim_scores = sorted(sim_score, key = lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:7]

    idx_list = [i[0] for i in sim_scores]                   # 유사한 도서 5권의 인덱스
    isbn_list = [indices[idx] for idx in idx_list]
    return isbn_list