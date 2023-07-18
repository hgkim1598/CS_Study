"""비즈니스 로직 처리 계층"""
from typing import Tuple
from databaseLayer.db import DatabaseManager
from abc import ABCMeta
import sys

db_manager = DatabaseManager()


class Command(metaclass=ABCMeta):
    def execute(self):
        pass


class AddCommandManagaer(Command):
    """할 일 추가"""

    def execute(self, value: str):
        db_manager.add(value)


class ListCommandManagaer(Command):
    """할 일 목록 출력"""

    def execute(self, data):
        for created_at, task, done in db_manager.select():
            print(f"등록일: {created_at}\t할 일: {task}\t완료 여부: {bool(done)}")


class DeleteCommandManagaer(Command):
    """할 일 삭제"""

    def execute(self, data):
        db_manager.delete(data)


class EditCommandManagaer(Command):
    """할 일 수정"""

    def execute(self, data: Tuple):
        db_manager.update(data[0], data[1])


class QuitCommandManager(Command):
    """프로그램 종료"""

    def execute(self, _):
        sys.exit()
