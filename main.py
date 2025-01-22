from PyQt6.QtWidgets import *

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
result_lbl = QLabel("Результат")
result_lbl.hide()
next_btn = QPushButton("Наступне запитання" )

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
group_line.addWidget(result_lbl)
group.setLayout(group_line)
main_line.addWidget(group)



window.setLayout(main_line)
window.show()
app.exec()