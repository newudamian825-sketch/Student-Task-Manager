from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, task_name):
        self.tasks.append(Task(task_id, task_name))
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            print(f"{task.task_id}. {task.task_name} | Completed: {task.is_completed}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_completed = True
                print("Task marked as completed.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")
