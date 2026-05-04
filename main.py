import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

# Настройки
HISTORY_FILE = "tasks.json"
DEFAULT_TASKS = [
    {"text": "Прочитать статью", "type": "учёба"},
    {"text": "Сделать зарядку", "type": "спорт"},
    {"text": "Написать отчёт", "type": "работа"},
    {"text": "Посмотреть обучающее видео", "type": "учёба"},
    {"text": "Разобрать почту", "type": "работа"},
    {"text": "Погулять на свежем воздухе", "type": "отдых"},
]

class TaskGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор случайных задач")
        self.root.geometry("500x500")

        # Загрузка данных
        self.tasks = self.load_tasks()
        self.history = []

        # Отображение текущей задачи
        task_frame = tk.Frame(root)
        task_frame.pack(pady=10, fill=tk.X)
        self.current_task_label = tk.Label(
            task_frame,
            text="Нажмите «Сгенерировать задачу»",
            wraplength=450,
            justify="center",
            font=("Arial", 12)
        )
        self.current_task_label.pack()

        # Кнопка генерации
        generate_btn = tk.Button(
            root,
            text="Сгенерировать задачу",
            command=self.generate_task,
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white"
        )
        generate_btn.pack(pady=5)

        # Фильтр по типам
        filter_frame = tk.Frame(root)
        filter_frame.pack(pady=5, fill=tk.X)
        tk.Label(filter_frame, text="Фильтр:", font=("Arial", 10)).pack(side=tk.LEFT)
        self.filter_var = tk.StringVar(value="все")
        filter_combo = ttk.Combobox(
            filter_frame,
            textvariable=self.filter_var,
            values=["все", "учёба", "работа", "спорт", "отдых"],
            state="readonly",
            width=10
        )
        filter_combo.pack(side=tk.RIGHT)
        filter_combo.bind("<<ComboboxSelected>>", self.update_history_list)

        # История задач
        history_frame = tk.Frame(root)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        tk.Label(history_frame, text="История задач:", font=("Arial", 10, "bold")).pack()
        self.history_listbox = tk.Listbox(history_frame, height=10)
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.history_listbox.yview)

        # Добавление новой задачи
        add_frame = tk.Frame(root)
        add_frame.pack(pady=5, fill=tk.X)
        self.new_task_entry = tk.Entry(add_frame, width=30)
        self.new_task_entry.pack(side=tk.LEFT, expand=True)
        self.new_task_type = ttk.Combobox(add_frame, values=["учёба", "работа", "спорт", "отдых"], state="readonly", width=10)
        self.new_task_type.set("работа")
        self.new_task_type.pack(side=tk.LEFT, padx=5)
        tk.Button(add_frame, text="Добавить в список", command=self.add_new_task).pack(side=tk.LEFT)

        self.update_history_list()

    def load_tasks(self):
        """Загрузка задач из JSON или создание файла с дефолтными задачами."""
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return DEFAULT_TASKS.copy()
        else:
            # Создаём файл с дефолтными задачами
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(DEFAULT_TASKS, f, ensure_ascii=False, indent=2)
            return DEFAULT_TASKS.copy()

    def save_tasks(self):
        """Сохранение задач в JSON."""
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def generate_task(self):
        """Генерация случайной задачи."""
        if not self.tasks:
            messagebox.showwarning("Предупреждение", "Список задач пуст! Добавьте новые задачи.")
            return
        selected_task = random.choice(self.tasks)
        # Добавляем в историю
        self.history.append(selected_task)
        self.save_tasks()  # Сохраняем историю
        # Отображаем задачу в главном лейбле
        self.current_task_label.config(
            text=f"Задача: {selected_task['text']}\nТип: {selected_task['type'].capitalize()}",
            bg="#f0f0f0",
            relief="solid"
        )
        self.update_history_list()

    def add_new_task(self):
        """Добавление новой задачи с валидацией."""
        task_text = self.new_task_entry.get().strip()
        task_type = self.new_task_type.get()
        if not task_text:
            messagebox.showerror("Ошибка", "Задача не может быть пустой!")
            return
        new_task = {"text": task_text, "type": task_type}
        self.tasks.append(new_task)
        self.save_tasks()
        # Очищаем поля ввода
        self.new_task_entry.delete(0, tk.END)
        self.update_history_list()

    def update_history_list(self, event=None):
        """Обновление списка истории с учётом фильтра."""
        self.history_listbox.delete(0, tk.END)
        filter_type = self.filter_var.get()
        for task in self.history:
            if filter_type == "все" or task["type"] == filter_type:
                self.history_listbox.insert(tk.END, f"{task['text']} ({task['type']})")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskGeneratorApp(root)
    root.mainloop()
