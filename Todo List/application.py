# 사용자가 등록한 내용 받아오기
## 1. 할 일 내용 받아오기
## 2. 등록일 받아오기
###   Datetime?
## 3. 완료 여부 받아오기
### 완료 처리
### 만약 완료 버튼이 눌리면~

# 날짜 검색
## 검색창에 입력된 날짜
### get method? 혹은 HTML form tag?

# 삭제 처리
## 만약 삭제 버튼이 눌리면~

# 종료 처리
## ??
from datetime import datetime
import mysql.connector


class Application:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="",
            port="",
            database="",
            username="",
            password="",
        )

    def add_todo():
        # INSERT
        pass

    def get_date():
        date_time = datetime.now()
        register_date = date_time.date()
        return register_date

    def complete_todo():
        # query = UPDATE table SET complete_column = 1 WHERE id_column = 완료가 눌린 todo의 id
        pass

    def search_date():
        # query = SELECT FROM table WHERE date_column = 검색된 날짜
        pass

    def delete_todo():
        # query = DELETE FROM table WHERE id_column = 지우려는 todo의 id
        pass
