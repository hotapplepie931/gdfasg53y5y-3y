def todo_list():
    tasks = []
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("4. Выход")
        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            task = input("Введите задачу: ")
            tasks.append(task)
            print("Задача добавлена!")
        elif choice == '2':
            if tasks:
                print("Ваши задачи:", *tasks, sep="\n")
            else:
                print("Список задач пуст!")
        elif choice == '3':
            if tasks:
                task = input("Введите задачу для удаления: ")
                if task in tasks:
                    tasks.remove(task)
                    print("Задача удалена!")
                else:
                    print("Задача не найдена!")
        elif choice == '4':
            print("До свидания!")
            break


todo_list()