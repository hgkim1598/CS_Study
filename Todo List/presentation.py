# 사용자에게 보여져야할 요소들
## 사용자가 할 일 등록할 창
## 사용자가 날짜를 검색할 수 있는 창
## 사용자가 끝마친 일을 '완료'처리할 수 있는 완료 버튼
## 사용자가 업무를 삭제할 수 있는 삭제 버튼
## 오늘 날짜의 할 일 목록을 보여줌
from datetime import datetime


class Presentation:
    def show_todo():
        date_time = datetime.now()
        today = date_time.date()
        # get...today

    def register_todo():
        todo = input("할 일 입력: ")
        return todo


# button -> Tkinter?
