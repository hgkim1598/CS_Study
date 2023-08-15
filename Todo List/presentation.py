# 사용자에게 보여져야할 요소들
## 사용자가 할 일 등록
## 사용자가 날짜를 검색
## 사용자가 끝마친 일을 '완료'처리
## 사용자가 업무를 삭제
## 오늘 날짜의 할 일 목록을 보여줌
# 선택 가능한 기능들 보여주고 선택 사항을 입력 받음
## 1. 조건문
# if a == quit:
#     quit()

## 2. 딕서너리
# t = {'a' : quit,
#      'b' : add_func,}
# c = input()
# t.get(c)()

import base_application


class Presentation:
    def show_todo(self):
        self.today = base_application.get_date()


class ChooseMenu:
    """기능 목록을 보여줌"""

    def shwo_functions(self):
        self.num = input(
            "1. 할 일 추가 \n\
                2. 완료 \n\
                3. 날짜 검색 \n\
                4. 삭제 \n\
                5. 종료"
        )
        return self.num


class MakeTodolist:
    def add_todo(self):
        """1. 할 일 추가"""
        self.add = input("할 일을 입력하세요: ")
        return self.add


class SearchDate:
    # def search_date(self):
    # """3. 날짜 검색"""
    #     self.search = input("날짜를 검색")

    pass


class Complete:
    def get_statu(self):
        """2. 완료 여부"""
        # 각 항목과 index 리스트를 보여준 뒤

        # 삭제를 원하는 항목 선택
        self.delete = input("삭제 처리를 원하는 항목의 번호를 입력하세요: ")
