"""데이터베이스 핸들링"""
from collections import namedtuple
from dotenv import load_dotenv
import os
import pymysql
from common.settings import Cursor, Connect, TABLE_INFO
from typing import NamedTuple, List


def load_secret_info() -> NamedTuple:
    """데이터베이스 인증 시크릿 정보 가져오기"""
    load_dotenv()

    connecter_params: List[str] = [
        "host",
        "port",
        "user",
        "passwd",
    ]
    host, port, user, passwd = [os.getenv(param) for param in connecter_params]
    mysql_info: NamedTuple = namedtuple("info", ["host", "port", "user", "passwd"])

    return mysql_info(host, int(port), user, passwd)


class DatabaseManager:
    def __init__(self):
        self.db_name: str = "todo_list"
        self.table_name: str = "task"
        self.connection: Connect = self.get_connecter()
        self.cursor: Cursor = self.connection.cursor()
        self.init_create_database()
        self.connection.select_db(self.db_name)

    def __del__(self):
        self.connection.close()

    def get_connecter(self) -> Connect:
        db_info: NamedTuple = load_secret_info()
        conn: Connect = pymysql.connect(
            host=db_info.host,
            port=db_info.port,
            user=db_info.user,
            password=db_info.passwd,
            charset="utf8",
        )
        return conn

    def _execute(self, statement: str, values=None) -> Cursor:
        """데이터베이스 핸들링"""

        self.cursor.execute(statement, values or [])
        self.connection.commit()
        return self.cursor

    def if_exists_database_check(self) -> bool:
        """데이터베이스 존재 여부 확인"""

        cur: Cursor = self._execute("SHOW DATABASES")
        database_list: List[str] = [
            i[0] for i in cur.fetchall()
        ]  # tuple type unpacking

        return self.db_name in database_list

    def if_exists_table_check(self) -> bool:
        cur: Cursor = self._execute("SHOW TABLES")
        table_list: List[str] = [i[0] for i in cur.fetchall()]  # tuple type unpacking

        return self.table_name in table_list

    def init_create_database(self):
        """최초 사용 데이터베이스 생성"""

        if not self.if_exists_database_check():
            self._execute(f"CREATE DATABASE {self.db_name}")

        return self.get_connecter().select_db(self.db_name)

    def create_table(self):
        """테이블 생성"""

        column_and_datatype: List[str, str] = [
            f"{column_name} {d_type}" for column_name, d_type in TABLE_INFO.items()
        ]
        statement = ",".join(column_and_datatype)

        if not self.if_exists_table_check():
            self._execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name}
                ({statement});
                """
            )
        return

    def add(self, value):
        """할 일 등록"""

        column_name = "task"
        self._execute(
            f"""
            INSERT INTO {self.table_name}
            ({column_name}) VALUES ('{value}');
            """
        )

    def delete(self, value):
        """할 일 삭제"""

        self._execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE task = '{value}';
            """,
        )

    def select(self, date="curdate()"):
        """날짜 기준으로 할 일을 조회하기"""

        date_field = "created_at"
        cur = self._execute(
            f"""
            SELECT {date_field}, task, done FROM {self.table_name}
            WHERE {date_field} = {date};
            """
        )
        return cur.fetchall()

    def update(self, old_values, new_values):
        """할 일 수정"""

        self._execute(
            f"""
            UPDATE {self.table_name}
            SET task = '{new_values}'
            WHERE task = '{old_values}';
            """
        )


if __name__ == "__main__":
    database_connecter = DatabaseManager()
