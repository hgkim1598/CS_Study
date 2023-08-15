from datetime import datetime


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
