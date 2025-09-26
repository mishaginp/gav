import tkinter as tk
from tkinter import ttk
from DemExam2 import db
from DemExam4 import view_partner
import os


def window():
    root = tk.Tk()
    root.title("Партнеры и скидки")
    root.geometry("910x900")
    root.config(bg="#FFFFFF")

    # Попытка установить иконку только если файл существует
    icon_path = "Мастер пол.ico"
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(default=icon_path)
        except tk.TclError:
            pass  # Игнорируем ошибку, если иконка не поддерживается (например, на Linux)

    font_text = "Segoe UI"
    colors = ["#FFFFFF", "#F4E8D3", "#67BA80"]

    # Основной canvas с прокруткой
    canvas = tk.Canvas(root, bg="white", highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=colors[0])

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Кнопка "Добавить"
    add_btn = tk.Button(
        root,
        text="Добавить",
        font=(font_text, 12, 'bold'),
        bg=colors[1],
        fg=colors[2],
        command=lambda: view_partner(None)
    )
    add_btn.pack(fill="x", side="top")

    # Список для хранения ссылок на фреймы (чтобы можно было удалять)
    partner_frames = []

    def refresh_display():
        """Обновляет отображение данных из БД"""
        try:
            data = db()
            info = data[0]
            sale = data[1]
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
            return

        # Удаляем старые фреймы
        for frame in partner_frames:
            frame.destroy()
        partner_frames.clear()

        # Создаём новые
        for i in range(len(info)):
            frame = tk.Frame(
                scrollable_frame,
                bg=colors[1],
                borderwidth=2,
                relief='groove',
                width=800,
                height=200
            )
            frame.grid(row=i, column=0, pady=5, sticky="ew")
            frame.grid_propagate(False)  # Сохраняем размер
            partner_frames.append(frame)

            # Извлекаем данные
            p_type, name, director, phone, rating = info[i]
            discount = sale[i]

            # Заголовок: тип | имя
            header = tk.Label(
                frame,
                text=f"{p_type} | {name}",
                font=(font_text, 16, 'bold'),
                bg=colors[1],
                fg=colors[2],
                anchor="w"
            )
            header.grid(row=0, column=0, columnspan=2, sticky="w")

            # Скидка
            disc_label = tk.Label(
                frame,
                text=f"{discount}%",
                font=(font_text, 24, 'bold'),
                bg=colors[1],
                fg=colors[2]
            )
            disc_label.grid(row=0, column=2, padx=200, sticky="e")

            # Директор
            dir_label = tk.Label(
                frame,
                text=director,
                font=(font_text, 12, 'bold'),
                bg=colors[1],
                fg=colors[2],
                anchor="w"
            )
            dir_label.grid(row=1, column=0, columnspan=3, sticky="w")

            # Телефон
            phone_label = tk.Label(
                frame,
                text=phone,
                font=(font_text, 12, 'bold'),
                bg=colors[1],
                fg=colors[2],
                anchor="w"
            )
            phone_label.grid(row=2, column=0, columnspan=3, sticky="w")

            # Рейтинг
            rating_label = tk.Label(
                frame,
                text=f"Рейтинг: {rating}",
                font=(font_text, 12, 'bold'),
                bg=colors[1],
                fg=colors[2],
                anchor="w"
            )
            rating_label.grid(row=3, column=0, columnspan=3, sticky="w")

            # Кнопка редактирования — фиксируем значение name
            edit_btn = tk.Button(
                frame,
                text="Редактировать",
                font=(font_text, 12, 'bold'),
                bg=colors[1],
                fg=colors[2],
                command=lambda n=name: view_partner(n)
            )
            edit_btn.grid(row=4, column=0, columnspan=3, pady=(5, 0), sticky="se")

        # Обновляем прокрутку
        root.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Изначальная загрузка
    refresh_display()

    # Опционально: обновлять раз в 5 секунд (а не 100 мс!)
    # Если автоподгрузка не нужна — закомментируйте эту строку
    # root.after(5000, lambda: _auto_refresh(root, refresh_display))

    root.mainloop()


def _auto_refresh(root, refresh_func):
    """Вспомогательная функция для периодического обновления"""
    try:
        refresh_func()
    except Exception as e:
        print(f"Ошибка при автообновлении: {e}")
    root.after(5000, lambda: _auto_refresh(root, refresh_func))


# Запуск
if __name__ == "__main__":
    window()