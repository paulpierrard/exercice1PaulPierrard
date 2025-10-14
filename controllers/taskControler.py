from model.task import Task

class TaskController:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def remove_task(self, index):
        try:
            self.tasks.pop(index - 1)
        except IndexError:
            return False
        return True

    def mark_done(self, index):
        try:
            self.tasks[index - 1].mark_done()
        except IndexError:
            return False
        return True

    def get_tasks(self):
        return self.tasks