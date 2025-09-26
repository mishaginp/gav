# Получаем имя партнера один раз внутри цикла
partner_name = info[i][1]

# Кнопка редактирования
edit_btn = tk.Button(
    frame_1,
    text="Редактировать",
    font=(font_text, 12, 'bold'),
    bg=colors[1],
    fg=colors[2],
    command=lambda n=partner_name: view_partner(n)
)
edit_btn.grid(row=4, column=0, columnspan=2, pady=(5, 0), sticky="sw")

# Кнопка истории продаж
history_btn = tk.Button(
    frame_1,
    text="История продаж",
    font=(font_text, 10, 'bold'),
    bg=colors[1],
    fg=colors[2],
    command=lambda n=partner_name: show_sales_history(n)
)
history_btn.grid(row=4, column=2, pady=(5, 0), sticky="se")