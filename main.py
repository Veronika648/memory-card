import random

from PyQt6.QtWidgets import *
import menu

import main2
from main2 import *

app = QApplication([])
window = QWidget()
menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
spin = QSpinBox()
min_lbl = QLabel("Хвилин")
quest_lbl = QLabel("Яблуко")

group = QGroupBox("Варіанти відповідей")
answer1_btn = QRadioButton("building")
answer2_btn = QRadioButton("apple")
answer3_btn = QRadioButton("щось")
result_lbl = QLabel("Результат")
result_lbl.hide()
next_btn = QPushButton("Наступне запитання" )
answer_btn = QPushButton("Вітповісти")
main_line = QVBoxLayout()

h1 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addStretch(1)
h1.addWidget(rest_btn)
h1.addWidget(spin)
h1.addWidget(min_lbl)
main_line.addLayout(h1)
main_line.addWidget(quest_lbl)

group_line = QVBoxLayout()
group_line.addWidget(answer1_btn)
group_line.addWidget(answer2_btn)
group_line.addWidget(answer3_btn)
group_line.addWidget(result_lbl)
group.setLayout(group_line)
main_line.addWidget(group)
main_line.addWidget(next_btn)
main_line.addWidget(answer_btn)


answers = [answer1_btn, answer2_btn, answer3_btn]

def set_quest():
    random.shuffle(answers)
    quest = main2.questions[main2.number]
    quest_lbl.setText(quest["Запитання"])
    answers[0].setText(quest["Правильна відповідь"])
    answers[1].setText(quest["Неправильна відповідь1"])
    answers[2].setText(quest["Неправильна відповідь2"])

set_quest()


def ans_funs():

    answers[0].hide()
    answers[1].hide()
    answer_btn.hide()
    result_lbl.show()
    if answers[0].isChecked():
        result_lbl.setText("ПРАВИЛЬНО!")

    else:
        result_lbl.setText("Ой ой... Не правильно!")


answer_btn.clicked.connect(ans_funs)

def next_func():
    main2.number += 1
    set_quest()
    answers[0].show()
    answers[1].show()
    answer_btn.show()
    result_lbl.hide()

next_btn.clicked.connect(next_func)
menu_btn.clicked.connect(menu.menu_window)


window.setLayout(main_line)
window.show()
app.exec()