from pyqs import task
import time


@task('queue0')
def another_task(message):
    print "another_task: message={}".format(message)


@task('queue0')
def send_email(subject):
    print "send_email: subject={}".format(subject)
