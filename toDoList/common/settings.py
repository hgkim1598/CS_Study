from typing import TypeVar


Cursor = TypeVar("T")
Connect = TypeVar("T")


TABLE_INFO = {
    "id": "INT NOT NULL AUTO_INCREMENT PRIMARY KEY",
    "task": "VARCHAR(255)",
    "created_at": "DATE DEFAULT (current_date)",
    "done": "BOOL DEFAULT FALSE",
}
