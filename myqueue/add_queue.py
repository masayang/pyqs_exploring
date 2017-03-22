from qqq.tasks import another_task, send_email
from settings import config

for i in range(0, 100):
    send_email.delay(subject='hogehoge')
    another_task.delay(message='hogehogehoge')
