def display_tasks(tasks):
    if not tasks:
        print("Aucune tâche.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def display_message(msg):
    print(msg)
