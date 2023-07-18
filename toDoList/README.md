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
    <img width="300" alt="image" src="https://github.com/LeeJuHwan/Basic/assets/118493627/c46f12ab-d3ea-4eae-a767-e4bc5488f3d8">
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
    <img width="872" alt="image" src="https://github.com/LeeJuHwan/Basic/assets/118493627/17a30984-f0a3-4f1e-baa5-910f016965e3">