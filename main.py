import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

class WeatherDiary:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Diary")
        self.root.geometry("800x600")

        self.records = []
        self.load_data()

        # Создаём поля ввода
        input_frame = ttk.LabelFrame(root, text="Добавить запись")
        input_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(input_frame, text="Дата (ДД.ММ.ГГГГ):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(input_frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Температура (°C):").grid(row=1, column=0, padx=5, pady=5)
        self.temp_entry = ttk.Entry(input_frame, width=15)
        self.temp_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Описание:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(input_frame, width=40)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        self.rain_var = tk.IntVar()
        ttk.Checkbutton(input_frame, text="Осадки", variable=self.rain_var).grid(row=3, column=0, padx=5, pady=5)

        add_btn = ttk.Button(input_frame, text="Добавить запись", command=self.add_record)
        add_btn.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Фильтры
        filter_frame = ttk.LabelFrame(root, text="Фильтры")
        filter_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(filter_frame, text="Фильтр по дате:").grid(row=0, column=0, padx=5, pady=5)
        self.filter_date_entry = ttk.Entry(filter_frame, width=15)
        self.filter_date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(filter_frame, text="Температура выше (°C):").grid(row=0, column=2, padx=5, pady=5)
        self.filter_temp_entry = ttk.Entry(filter_frame, width=10)
        self.filter_temp_entry.grid(row=0, column=3, padx=5, pady=5)

        filter_btn = ttk.Button(filter_frame, text="Применить фильтр", command=self.apply_filter)
        filter_btn.grid(row=0, column=4, padx=5, pady=5)

        reset_btn = ttk.Button(filter_frame, text="Сбросить фильтры", command=self.reset_filter)
        reset_btn.grid(row=0, column=5, padx=5, pady=5)

        # Таблица записей
        table_frame = ttk.LabelFrame(root, text="Записи о погоде")
        table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        columns = ("Дата", "Температура", "Описание", "Осадки")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.display_records()

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, '%d.%m.%Y')
            return True
        except ValueError:
            return False

    def add_record(self):
        date = self.date_entry.get().strip()
        temp_str = self.temp_entry.get().strip()
        desc = self.desc_entry.

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDiary(root)
    root.mainloop()
