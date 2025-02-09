from PyQt6.QtWidgets import *

import main2
from main2 import *


def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Запитання")
    quest_input = QLineEdit()
    try_ans_lbl = QLabel("Правильна відповідь")
    try_ans_input = QLineEdit()
    fouls_ans_lbl = QLabel("Неправильна відповідь")
    fouls_ans_input = QLineEdit()
    fouls_ans2_lbl = QLabel("Неправильна відповідь 2")
    fouls_ans2_input = QLineEdit()

    dodatu_btn = QPushButton("Додати питання")

    main_line = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_input)
    main_line.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(try_ans_lbl)
    h2.addWidget(try_ans_input)
    main_line.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(fouls_ans_lbl)
    h3.addWidget(fouls_ans_input)
    main_line.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(fouls_ans2_lbl)
    h4.addWidget(fouls_ans2_input)
    main_line.addLayout(h4)
    main_line.addWidget(dodatu_btn)



    def add_func():
        main2.questions.append(
            {
        "Запитання": quest_input.text(),
        "Правильна відповідь": try_ans_input.text(),
        "Неправильна відповідь1": fouls_ans_input.text(),
        "Неправильна відповідь2": fouls_ans2_input.text()
    })

    dodatu_btn.clicked.connect(add_func)



    window.setLayout(main_line)
    window.exec()

