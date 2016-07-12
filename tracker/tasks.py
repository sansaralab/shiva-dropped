from __future__ import absolute_import
import time
from app import app


@app.task()
def mega_task():
    print("First task staaarts...")
    time.sleep(5)
    print("and stops!")
    return 123
