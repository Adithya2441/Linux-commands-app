from __future__ import absolute_import,unicode_literals
from celery import Celery, shared_task
import time,subprocess

app = Celery('tasks', broker='redis://localhost:6379',include=['problem.tasks.add'])

@shared_task
def celery_run(cmd,rep,dur):
    output=''
    for i in range(int(rep)):
        time.sleep(int(dur))
        p=subprocess.run(cmd,capture_output=True,text=True,shell=True)
        output += p.stdout
    return output