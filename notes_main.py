from PyQt5.QtCore import Qt
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QInputDialog
ap = QApplication([])
n = {'Добро пожаловать!' : 
    {'текст' : 'Это самое лучшее приложение для заметок в мире',
    'теги' : ['Добро', 'инструкция']}}
with open('notes_data.json', 'w', encoding='utf-8') as file:
    json.dump(n, file)
nw = QWidget()
nw.setWindowTitle('Умные заметки')
nw.resize(900, 600)
ln = QListWidget()
lnl = QLabel('Список заметок')
bnc = QPushButton('Создать заметку')
bnd = QPushButton('Удалить заметку')
bns = QPushButton('Сохранить заметку')
ft = QLineEdit('')
ft.setPlaceholderText('Введите тег...')
ftx = QTextEdit()
bta = QPushButton('Добавить к заметке')
btd = QPushButton('Открепить от заметки')
btn = QPushButton('Искать заметки по тегу')
lt = QListWidget()
ltl = QLabel('Список тегов')
lyn = QHBoxLayout()
c1 = QVBoxLayout()
c1.addWidget(ftx)
c2 = QVBoxLayout()
c2.addWidget(lnl)
c2.addWidget(ln)
r1 = QHBoxLayout()
r1.addWidget(bnc)
r1.addWidget(bnd)
r2 = QHBoxLayout()
r2.addWidget(bns)
c2.addLayout(r1)
c2.addLayout(r2)
c2.addWidget(ltl)
c2.addWidget(lt)
c2.addWidget(ft)
r3 = QHBoxLayout()
r3.addWidget(bta)
r3.addWidget(btd)
r4 = QHBoxLayout()
r4.addWidget(btn)
c2.addLayout(r3)
c2.addLayout(r4)
lyn.addLayout(c1, stretch=2)
lyn.addLayout(c2, stretch=1)
nw.setLayout(lyn)
def swn():
    k = ln.selectedItems()[0].text()
    ftx.setText(n[k]['текст'])
    lt.clear()
    lt.addItems(n[k]['теги'])
def an():
    nn, ok = QInputDialog.getText(nw, 'Добавить заметку', 'Название заметки: ')
    if ok and nn != '':
        n[nn] = {'текст' : '', 'теги' : []}
        ln.addItem(nn)
        lt.addItems(n[nn]['теги'])
        print(n)
    else:
        print('Заметка не выбрана!')
bnc.clicked.connect(an)
def svn():
    if ln.selectedItems():
        k = ln.selectedItems()[0].text()
        n[k]['текст'] = ftx.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(n, file, sort_keys=True, ensure_ascii=False)
        print(n)
    else:
        print('Заметка не выбрана!')
bns.clicked.connect(svn)
def dln():
    if ln.selectedItems():
        k = ln.selectedItems()[0].text()
        del n[k]
        ln.clear()
        lt.clear()
        ftx.clear()
        ln.addItems(n)
        with open('notes_data.json', 'w') as file:
            json.dump(n, file, sort_keys=True, ensure_ascii=False)
        print(n)
    else:
        print('Заметка не выбрана!')
bnd.clicked.connect(dln)
def at():
    if ln.selectedItems():
        k = ln.selectedItems()[0].text()
        t = ft.text()
        if not t in n[k]['теги']:
            n[k]['теги'].append(t)
            lt.addItem(t)
            ft.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(n, file, sort_keys=True, ensure_ascii=False)
        print(n)
    else:
        print('Тег не выбран!')
bta.clicked.connect(at)
def dt():
    if ln.selectedItems():
        k = ln.selectedItems()[0].text()
        t = lt.selectedItems()[0].text()
        n[k]['теги'].remove(t)
        lt.clear()
        lt.addItems(n[k]['теги'])
        with open('notes_data.json', 'w') as file:
                json.dump(n, file, sort_keys=True, ensure_ascii=False)
        print(n)
    else:
        print('Тег не выбран!')
btd.clicked.connect(dt)
def st():
    t = ft.text()
    if btn.text() == 'Искать заметки по тегу' and t:
        nf = {}
        for ns in n:
            if t in n[ns]['теги']:
                nf[ns] = n[ns]
        btn.setText('Сбросить поиск')
        ln.clear()
        lt.clear()
        ln.addItems(nf)
    elif btn.text() == 'Сбросить поиск':
        ft.clear()
        ln.clear()
        lt.clear()
        ln.addItems(n)
        btn.setText('Искать заметки по тегу')
    else:
        pass
btn.clicked.connect(st)
nw.show()
ln.addItems(n)
ln.itemClicked.connect(swn)
ap.exec_()