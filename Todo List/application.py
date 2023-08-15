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

import mysql.connector
from dotenv import load_dotenv
import os
from data import Data
from presentation import MakeTodolist
import base_application
import presentation
from datetime import datetime


def input_date():
    date = input("할 일의 날짜를 YYYY-MM-DD 형식에 맞춰 입력하세요: ")
    # 이 문구가 먼저 뜨면 사용자는 '오늘'이어도 입력을 할텐데
    # 그럼 default 값을 설정하는 게 의미가 없는 거 아닌가?
    # '다른 날짜에 추가하기'이런걸 따로 만들어야하나?
    if date:
        try:
            # 문자열을 datetime 객체로 변환
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            return date_obj

        except ValueError:
            return print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


class Application:
    def __init__(self):
        super().__init__()
        day_instance = base_application
        self.date = day_instance.get_date()
        self.today = input_date() or self.date

        self.db = Data()

    def add_todo(self):
        """할 일 추가"""
        instance = presentation.MakeTodolist()
        self.add = instance.add_todo()

        self.id = self.index()
        query = "INSERT INTO TodoList VALUES(self.id, self.add, self.today, '0')"
        self.cur.execute(query)
        pass

    def complete_todo(self):
        """완료 처리"""
        # 각 항목과 index 리스트를 보여준 뒤
        print()
        # 완료를 원하는 항목 선택
        self.complete = input("완료 처리를 원하는 항목의 번호를 입력하세요: ")
        query = "UPDATE TodoList SET complete = 1 WHERE id = self.complete"
        self.cur.execute(query)
        pass

    def search_date(self):
        """날짜 검색"""
        # input()과 f-string을 통해 월과 일을 따로 받아 이를 통해 검색? -> 월을 입력하세요 / 일을 입력하세요
        # query = SELECT FROM TodoList WHERE date_column = 검색된 날짜
        # self.cur.execute(query)
        pass

    def delete_todo(self):
        """항목 삭제"""
        query = "DELETE FROM TodoList WHERE id = self.delete"
        self.cur.execute(query)
        pass

    def close_todolist(self):
        """실행 종료"""
        pass
