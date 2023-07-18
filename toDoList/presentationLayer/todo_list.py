"""프리젠테이션 계층 출력 관리"""
import businessLayer.command as commands
import os
from collections import OrderedDict
import datetime


class Option:
    def __init__(self, name, command, success_message=None, callable_function=None):
        self.name = name
        self.command = command
        self.callable_function = callable_function
        self.success_message = success_message

    def __str__(self):
        return self.name

    def choose(self):
        """콜러블 함수에서 데이터를 받아와 커맨드 실행"""

        data = self.callable_function() if self.callable_function else None
        self.command.execute(data)


def print_options(options):
    """옵션, 문구 출력"""

    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
    print()


def option_choice_is_valid(choice, options):
    """대소문자 입력 가능하게 함"""

    return choice in options or choice.upper() in options


def get_option_choice(options):
    """옵션 체크"""

    choose_option = input("옵션을 선택하세요.\n> ")
    while not option_choice_is_valid(choose_option, options):
        print("옵션을 잘못 고르셨습니다.")
        print_options(options)
        choose_option = input("옵션을 선택하세요.\n> ")
    return options[choose_option.upper()]


def get_user_input(label):
    """입력 값 핸들링"""

    value = input(f"{label}: ")
    return value


def add_task():
    """할 일 추가 유도 함수"""

    return get_user_input("할 일을 기록하세요")


def list_task():
    """할일 목록 출력 유도 함수"""

    return datetime.datetime.today().strftime("%Y-%m-%d")


def edit_task():
    """할 일 수정 유도 함수"""

    old_data = get_user_input("수정 할 할 일을 입력하세요")
    new_data = get_user_input("수정 될 할 일을 입력하여 변경하세요")
    return old_data, new_data


def del_task():
    """할 일 삭제 유도함수"""

    return get_user_input("삭제 할 할 일을 입력하세요")


def clear_screen():
    """화면 클리어"""

    clear = "cls" if os.name == "nt" else "clear"
    print(f"GET OS NAME: {os.name}")
    os.system(clear)


def loop():
    """메인 출력"""

    clear_screen()

    options = OrderedDict(
        {
            "A": Option(
                "할 일 등록하기",
                commands.AddCommandManagaer(),
                callable_function=add_task,
                success_message="등록이 완료 되었습니다.",
            ),
            "B": Option(
                "할 일 목록 보기",
                commands.ListCommandManagaer(),
                callable_function=list_task,
            ),
            "E": Option(
                "할 일 수정하기",
                commands.EditCommandManagaer(),
                callable_function=edit_task,
                success_message="수정이 완료 되었습니다.",
            ),
            "D": Option(
                "할 일 삭제",
                commands.DeleteCommandManagaer(),
                callable_function=del_task,
                success_message="삭제가 완료 되었습니다",
            ),
            "Q": Option("종료", commands.QuitCommandManager()),
        }
    )
    print_options(options)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input("엔터를 입력 하면 메뉴 화면으로 넘어갑니다.")


if __name__ == "__main__":
    while True:
        loop()
