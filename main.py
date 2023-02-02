import math
from functools import partial
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
my_app = QApplication([])

loader = QUiLoader()
main_window = loader.load("Assignment 17/qtmain.ui")
main_window.show()

global NUMBERS
NUMBERS = []
op = ""

def sub():
    global a
    global op
    a = float(main_window.textbox.text())
    main_window.textbox.setText("")
    op = "sub"

def sum():
    global a
    global op
    a = float(main_window.textbox.text())
    main_window.textbox.setText("")
    op = "sum"

def sqr():
    global a
    global op
    op = "sqr"

def sin():
    global a
    global op
    op = "sin"

def cos():
    global a
    global op
    op = "cos"

def tan():
    global a
    global op
    op = "tan"

def cot():
    global a
    global op
    op = "cot"

def fac():
    global a
    global op
    op = "fac"

def div():
    global a
    global op
    a = float(main_window.textbox.text())
    main_window.textbox.setText("")
    op = "div"

def mul():
    global a
    global op
    a = float(main_window.textbox.text())
    main_window.textbox.setText("")
    op = "mul"

def Num(number):
    o_num = main_window.textbox.text()
    n_num = o_num + number
    main_window.textbox.setText(n_num)

def b_s():
    NUMBERS = main_window.textbox.text()
    NUMBERS = NUMBERS[:-1]
    main_window.textbox.setText("")
    main_window.textbox.setText(NUMBERS)

def c():
    NUMBERS = main_window.textbox.text()
    NUMBERS = []
    main_window.textbox.setText("")

def equal():
    b = float(main_window.textbox.text())
    if op == "sub":
        c = a - b
    if op == "sum":
        c = a + b
    if op == "div":
        c = a / b
    if op == "mul":
        c = a * b
    if op == "sqr":
        c = math.sqrt(b)
    if op == "sin":
        n = math.radians(b)
        c = math.sin(n)
    if op == "cos":
        n = math.radians(b)
        c = math.cos(n)
    if op == "tan":
        n = math.radians(b)
        c = math.tan(n)
    if op == "cot":
        n = math.radians(b)
        c = math.atan(n)
    if op == "fac":
        c = math.factorial(b)
    main_window.textbox.setText(str(c))

main_window.btn_equal.clicked.connect(equal)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_sum.clicked.connect(sum)
main_window.btn_sqr.clicked.connect(sqr)
main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_foc.clicked.connect(fac)
main_window.btn_div.clicked.connect(div)
main_window.btn_mul.clicked.connect(mul)
main_window.b_s.clicked.connect(b_s)
main_window.c.clicked.connect(c)
main_window.one.clicked.connect(partial(Num,"1"))
main_window.two.clicked.connect(partial(Num,"2"))
main_window.three.clicked.connect(partial(Num,"3"))
main_window.four.clicked.connect(partial(Num,"4"))
main_window.five.clicked.connect(partial(Num,"5"))
main_window.six.clicked.connect(partial(Num,"6"))
main_window.seven.clicked.connect(partial(Num,"7"))
main_window.eight.clicked.connect(partial(Num,"8"))
main_window.nine.clicked.connect(partial(Num,"9"))
main_window.zero.clicked.connect(partial(Num,"0"))
main_window.dat.clicked.connect(partial(Num,"."))

my_app.exec_()