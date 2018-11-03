#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 08:29:56 2018

@author: jurriaan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:05:36 2018

@author: jurriaan
"""
from random import sample
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot, Qt

from questions import dict_zuipuh

class App(QWidget):      
    def __init__(self):
        super().__init__()
        self.title = 'Het grote Data Science zuipspelletje - Yolo'
        self.dict_shuffled = self.shuffle_questions(dict_zuipuh)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(10, 10, 1200, 600)

        self.button_easy = QPushButton('niveautje BI \n (1 punt)', self)
        self.button_easy.setGeometry(20, 450, 300, 100)
        self.button_easy.setFont(QFont('SansSerif', 20))
        self.button_easy.clicked.connect(self.on_click_easy)
        #self.button_easy.enter_Pressed.connect(self.on_click_easy)
    
        self.button_medium = QPushButton('niveau Dataworkz Engineer \n (3 punten)', self)
        self.button_medium.setGeometry(440, 450, 300, 100)
        self.button_medium.setFont(QFont('SansSerif', 20))
        self.button_medium.clicked.connect(self.on_click_medium)
        #self.button_medium.returnPressed.connect(self.on_click_medium)
        #self.button_medium.focusInEvent(self)

        self.button_hard = QPushButton('niveau Dataworkz Scientist \n (10 punten)', self)
        self.button_hard.setGeometry(860, 450, 300, 100)
        self.button_hard.setFont(QFont('SansSerif', 20))
        self.button_hard.clicked.connect(self.on_click_hard)
        #self.button_hard.returnPressed.connect(self.on_click_hard)

        self.label_leg_uit = QLabel(self)
        self.label_leg_uit.setFont(QFont('SansSerif', 20))        
        self.label_leg_uit.setGeometry(20, 20, 100, 30)
        self.label_leg_uit.setText('Leg uit...')
         
        self.label_q = QLabel(self)
        self.label_q.setFont(QFont('SansSerif', 40))        
        self.label_q.setGeometry(100, 50, 1000, 400)
        self.label_q.setAlignment(Qt.AlignCenter)


    @pyqtSlot()
    def on_click_easy(self):
        question = self.choose_random_question(self.dict_shuffled, 1)
        self.label_q.setText(question)
        self.button_easy.setFocus()
        
    @pyqtSlot()
    def on_click_medium(self):
        question = self.choose_random_question(self.dict_shuffled, 2)
        self.label_q.setText(question)
        self.button_medium.setFocus()
        
    @pyqtSlot()
    def on_click_hard(self):
        question = self.choose_random_question(self.dict_shuffled, 3)
        self.label_q.setText(question)
        self.button_hard.setFocus()
  
    def shuffle_questions(self, dic):
        dict_shuffle = {}
        for key in dic:
            dict_shuffle[key] = iter(sample(dic[key], len(dic[key])))            
        return dict_shuffle
    
    def choose_random_question(self, dict_shuffled, level):      
        question = next(dict_shuffled[level], None)
        
        if not question:
            print('deck empty, deck reshuffled')
            self.dict_shuffled = self.shuffle_questions(dict_zuipuh)
            question = next(self.dict_shuffled, None)  
        
        return question
            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())

