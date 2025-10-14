from controllers.taskControler import TaskController
from views.cli import display_tasks, display_message

def show_menu():
    print("\nMenu :")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Supprimer une tâche")
    print("4. Marquer une tâche comme faite")
    print("5. Quitter")

def main():
    controller = TaskController()

    while True:
        show_menu()
        choice = input("Choix : ")

        if choice == "1":
            display_tasks(controller.get_tasks())
        elif choice == "2":
            title = input("Titre de la tâche : ")
            controller.add_task(title)
        elif choice == "3":
            index = int(input("Numéro de la tâche à supprimer : "))
            if not controller.remove_task(index):
                display_message("Indice invalide.")
        elif choice == "4":
            index = int(input("Numéro de la tâche à marquer comme faite : "))
            if not controller.mark_done(index):
                display_message("Indice invalide.")
        elif choice == "5":
            break
        else:
            display_message("Choix invalide.")

if __name__ == "__main__":
    main()
