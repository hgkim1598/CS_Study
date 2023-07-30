# mysql 커넥션
## 1. pymysql 패키지 설치
## 2. connection 정보 변수에 저장
## 3. connection 생성
## 4. 쿼리 실행

# 할 일 저장
## ID
## 할 일 내용 (todo)
## 등록일 (registration date)
## 완료 여부 (completion)

# +------+---------+---------+-------------+
# |  id  |  할 일  |  등록일  |  완료 여부  |
# +------+---------+---------+-------------+
# |      |         |         |             |
# +------+---------+---------+-------------+
# |                                        |

import pymysql
from dotenv import load_dotenv
import os

load_dotenv()


class Data:
    def __init__(self):
        self.conn = pymysql.connect(
            host=os.environ.get("host"),
            port=os.environ.get("port"),
            database=os.environ.get("database"),
            username=os.environ.get("username"),
            password=os.environ.get("password"),
        )

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
