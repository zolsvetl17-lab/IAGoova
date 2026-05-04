import tkinter as tk
from tkinter import ttk, messagebox
import json

class WeatherDiary:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Diary")
        self.root.geometry("600x400")

        # Создаем поля ввода
        self.date_entry = tk.Entry(root, width=20)
        self.temp_entry = tk.Entry(root, width=20)
        self.desc_entry = tk.Entry(root, width=40)
        self.rain_var = tk.IntVar()
        self.rain_chk = tk.Checkbutton(root, text="Осадки", variable=self.rain_var)

        # Расположение элементов
        date_label = tk.Label(root, text="Дата:")
        date_label.pack(pady=10)
        self.date_entry.pack(pady=5)

        temp_label = tk.Label(root, text="Температура (°C):")
        temp_label.pack(pady=10)
        self.temp_entry.pack(pady=5)

        desc_label = tk.Label(root, text="Описание:")
        desc_label.pack(pady=10)
        self.desc_entry.pack(pady=5)

        self.rain_chk.pack(pady=10)

        add_btn = tk.Button(root, text="Добавить запись", command=self.add_record)
        add_btn.pack(pady=10)

        self.load_data()

    def add_record(self):
        date = self.date_entry.get()
        temp = float(self.temp_entry.get())
        desc = self.desc_entry.get()
        rain = self.rain_var.get()

        if not date or temp <= 0 or not desc:
            messagebox.showerror("Ошибка", "Проверьте правильность ввода!")
            return

        self.records.append({
            'date': date,
            'temp': temp,
            'desc': desc,
            'rain': rain
        })
        self.save_data()
        self.display_records()

    def load_data(self):
        try:
            with open('weather_data.json', 'r', encoding='utf-8') as f:
                self.records = json.load(f) or []
            self.display_records()
        except FileNotFoundError:
            self.records = []

    def save_data(self):
        with open('weather_data.json', 'w', encoding='utf-8') as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)

    def display_records(self):
        # Реализация отображения записей в таблице
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDiary(root)
    root.mainloop()
