class Task:
    def __init__(self, description, deadline, status="не выполнено"):
        self.description = description  # Описание задачи
        self.deadline = deadline  # Срок выполнения
        self.status = status  # Статус: "выполнено" или "не выполнено"

    def mark_done(self):
        """Отметить задачу как выполненную"""
        self.status = "выполнено"

    def __str__(self):
        """Красивый вывод информации о задаче"""
        return f"{self.description} (срок: {self.deadline}) - {self.status}"


# Функции для работы с задачами
tasks = []  # Список всех задач


def add_task(description, deadline):
    """Добавить новую задачу"""
    task = Task(description, deadline)
    tasks.append(task)
    print(f"Добавлена задача: {task}")


def mark_task_done(description):
    """Отметить задачу как выполненную по описанию"""
    for task in tasks:
        if task.description == description and task.status == "не выполнено":
            task.mark_done()
            print(f"Задача выполнена: {task}")
            return
    print("Задача не найдена или уже выполнена")


def show_current_tasks():
    """Показать текущие (не выполненные) задачи"""
    print("\nТекущие задачи по закупкам:")
    current_tasks = [task for task in tasks if task.status == "не выполнено"]

    if not current_tasks:
        print("Все задачи выполнены! ✓")
    else:
        for i, task in enumerate(current_tasks, 1):
            print(f"{i}. {task}")


# Пример использования для закупок оборудования
add_task("Закупить новые станки для цеха №3", "15.12.2024")
add_task("Заказать расходные материалы", "20.12.2024")
add_task("Согласовать бюджет на новое оборудование", "10.12.2024")

print("\n--- Первоначальный список ---")
show_current_tasks()

# Отмечаем выполненную задачу
mark_task_done("Согласовать бюджет на новое оборудование")

print("\n--- После выполнения одной задачи ---")
show_current_tasks()

# Добавляем еще задачи
add_task("Заключить договор с поставщиком", "25.12.2025")
add_task("Проверить качество поставленных материалов", "28.12.2025")

print("\n--- Финальный список ---")
show_current_tasks()