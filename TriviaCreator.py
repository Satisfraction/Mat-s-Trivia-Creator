import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QPushButton, QButtonGroup


class Trivia(QWidget):
    def __init__(self):
        super().__init__()
        self.question = ""
        self.choices = []
        self.correct_answers = []
        self.initUI()

    def initUI(self):
        # Question Input
        question_layout = QHBoxLayout()
        question_label = QLabel('Question:')
        self.question_input = QLineEdit()
        question_layout.addWidget(question_label)
        question_layout.addWidget(self.question_input)

        # Answer Options
        answer_layout = QVBoxLayout()
        answer_label = QLabel('Answer Options:')
        answer_layout.addWidget(answer_label)

        self.answer_group = QButtonGroup()

        for i in range(4):
            answer_option_layout = QHBoxLayout()
            answer_option = QRadioButton()
            answer_text = QLineEdit()
            answer_option_layout.addWidget(answer_option)
            answer_option_layout.addWidget(answer_text)
            answer_layout.addLayout(answer_option_layout)

            self.answer_group.addButton(answer_option, i)
            self.choices.append(answer_text)

        # Correct Answers
        correct_layout = QHBoxLayout()
        correct_label = QLabel('Correct Answers (Check all that apply):')
        correct_layout.addWidget(correct_label)

        self.correct_group = []

        for i in range(4):
            correct_button = QRadioButton(str(i+1))
            correct_layout.addWidget(correct_button)
            self.correct_group.append(correct_button)

        # Save Button
        save_button = QPushButton('Save', self)
        save_button.clicked.connect(self.saveQuestion)

        # Layout
        vbox = QVBoxLayout()
        vbox.addLayout(question_layout)
        vbox.addLayout(answer_layout)
        vbox.addLayout(correct_layout)
        vbox.addWidget(save_button)

        self.setLayout(vbox)
        self.setWindowTitle('Mat´s Trivia Creator App')

    def saveQuestion(self):
        self.question = self.question_input.text()

        for choice in self.choices:
            self.correct_answers.append(choice.text())
            choice.clear()

        for i in range(4):
            if self.correct_group[i].isChecked():
                self.correct_answers.append(i)

        # Save question to JSON file
        question_data = {
            'question': self.question,
            'choices': [choice.text() for choice in self.choices],
            'correct_answers': self.correct_answers
        }

        with open('questions.json', 'a') as file:
            json.dump(question_data, file)
            file.write('\n')

        self.question_input.clear()
        for button in self.answer_group.buttons():
            button.setChecked(False)
        for button in self.correct_group:
            button.setChecked(False)
        self.correct_answers.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    trivia = Trivia()
    trivia.show()
    app.exec_()
