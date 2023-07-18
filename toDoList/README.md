### Get Started
---

**First Step**
- Environment Setup
    - databaseLayer/.env
 
        ```
            host="host"
            port=port
            user="user"
            passwd="password"

        ```

**Finally Run**
---
- main.py
    ```
        python3 main.py
    ```

**unit-test**
---
- tests/test_database.py
    ```
        1. 데이터베이스 커넥션
        2. 테이블 생성
        3. 할 일 등록
        4. 할 일 삭제
        5. 할 일 조회
        6. 할 일 수정

        cmd pytest tests/test_database.py
    ```