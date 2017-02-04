from celery.task import Task
from celery.registry import tasks

class Hello_World(Task):
    def hello_world(self,char):
        print('Hello World')

tasks.register(Hello_World)