"""데이터베이스 테스트 케이스"""
from databaseLayer.db import DatabaseManager
from common.settings import TABLE_INFO


class TestDatabaseCommand:
    def setup_method(self):
        self.db = DatabaseManager()
        self.db.connection.select_db(self.db.db_name)

    def test_connection(self):
        """Database connection test"""
        self.db.get_connecter()

        assert self.db.connection is not None

    def test_create_table(self):
        """create table unittest"""

        self.db.create_table()

        is_exists_table = self.db.if_exists_table_check()
        assert is_exists_table is True

    def test_add(self):
        """Add task"""

        test_value = "공부하기"

        self.db.cursor.execute(
            f"SELECT task FROM {self.db.table_name} WHERE task='{test_value}'"
        )
        result = self.db.cursor.fetchone()[0]

        if not result:
            self.db.add(test_value)
            self.db.cursor.execute(
                f"SELECT task FROM {self.db.table_name} WHERE task='{test_value}'"
            )
            result = self.db.cursor.fetchone()[0]

        assert result == test_value

    def test_delete(self):
        """Delete task"""

        test_value = "공부하기"
        self.db.cursor.execute(
            f"SELECT task FROM {self.db.table_name} WHERE task='{test_value}'"
        )
        result = self.db.cursor.fetchone()[0]

        if result:
            self.db.delete(test_value)

            self.db.cursor.execute(
                f"SELECT task FROM {self.db.table_name} WHERE task='{test_value}'"
            )
            none_result = self.db.cursor.fetchone()

        assert none_result is None

    def test_select(self):
        """select date field by today or another date"""

        self.db.add("공부하기")
        select_date_task = self.db.select()

        # fetchall -> ((id, task, created_at, done),): indexing
        assert select_date_task[0][1] == "공부하기"

    def test_update(self):
        """select date field by today or another date"""

        self.db.update("공부하기", "잠자기")
        select_task = self.db.select()[0][1]

        if select_task == "잠자기":
            self.db.update("잠자기", "공부하기")
            select_task = self.db.select()[0][1]

        assert select_task == "공부하기"
