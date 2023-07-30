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
from dotenv import load_dotenv
import os
from data import Data
from presentation import MakeTodolist

def test():
    pass


class BaseApplication:
    def get_date(self):
        date_time = datetime.now()
        register_date = date_time.date()
        return register_date

    def index(self):
        # id를 index로 주기 위해
        # todo list가 종료되기 전까지
        # for문을 돌면서 +1씩 증가하며 id를 부여???
        # 삭제된 항목의 id(=index)는 항목 삭제와 함께 사라진다
        # return id
        pass
    
    def get_funtions_num(self):
        """실행할 기능 번호 입력 받아옴"""
        self.functions = self.shwo_functions()
        # functions = {'1': add_todo(),
        #              '2': complete_todo(),
        #              '3': search_date(),
        #              '4': delete_todo(),
        #              '5': close_todo()}


class Application(BaseApplication):
    def __init__(self):
        super().__init__()
        self.today = self.get_date()

        self.db = Data()

    def add_todo(self):
        """할 일 추가"""
        self.add = input("할 일을 입력하세요: ")
        self.id = self.index()
        query = INSERT INTO TodoList VALUES(self.id, self.add, self.today, '0')
        self.cur.execute(query)
        pass

    def complete_todo(self):
        """완료 처리"""
        # 각 항목과 index 리스트를 보여준 뒤
        print()
        # 완료를 원하는 항목 선택
        self.complete = input('완료 처리를 원하는 항목의 번호를 입력하세요: ')
        query = UPDATE TodoList SET complete = 1 WHERE id = self.complete
        self.cur.execute(query)
        pass

    def search_date(self):
        """날짜 검색"""
        # query = SELECT FROM TodoList WHERE date_column = 검색된 날짜
        # self.cur.execute(query)
        pass

    def delete_todo(self):
        """항목 삭제"""
        # 각 항목과 index 리스트를 보여준 뒤
        print()
        # 삭제를 원하는 항목 선택
        self.delete = input('삭제 처리를 원하는 항목의 번호를 입력하세요: ')
        query = DELETE FROM TodoList WHERE id = self.delete
        self.cur.execute(query)
        pass

    def close_todolist(self):
        """실행 종료"""
        pass