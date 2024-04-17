import sys
import math
from math import pi, e, sin, cos, tan, log, factorial, sqrt, ceil, floor, exp
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

# class Calc(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("calc.ui", self)

#         self.main_label.setText("0")
#         self.main_label_2.setText("")

#         # Connect buttons
#         self.button_0.clicked.connect(self.button_onclick)
#         self.button_1.clicked.connect(self.button_onclick)
#         self.button_2.clicked.connect(self.button_onclick)
#         self.button_3.clicked.connect(self.button_onclick)
#         self.button_4.clicked.connect(self.button_onclick)
#         self.button_5.clicked.connect(self.button_onclick)
#         self.button_6.clicked.connect(self.button_onclick)
#         self.button_7.clicked.connect(self.button_onclick)
#         self.button_8.clicked.connect(self.button_onclick)
#         self.button_9.clicked.connect(self.button_onclick)

#         self.button_plus.clicked.connect(self.button_onclick)
#         self.button_minus.clicked.connect(self.button_onclick)
#         self.button_times.clicked.connect(self.button_onclick)
#         self.button_split.clicked.connect(self.button_onclick)
#         self.button_equal.clicked.connect(self.button_onclick)
#         self.button_clear.clicked.connect(self.button_onclick)
#         self.button_open.clicked.connect(self.button_onclick)
#         self.button_close.clicked.connect(self.button_onclick)
#         self.button_percentage.clicked.connect(self.button_onclick)

#         self.button_pi.clicked.connect(self.button_onclick)
#         self.button_e.clicked.connect(self.button_onclick)
#         self.button_inv.clicked.connect(self.button_onclick)
#         self.button_sin.clicked.connect(self.button_onclick)
#         self.button_cos.clicked.connect(self.button_onclick)
#         self.button_tan.clicked.connect(self.button_onclick)
#         self.button_log.clicked.connect(self.button_onclick)
#         self.button_fact.clicked.connect(self.button_onclick)
#         self.button_pow.clicked.connect(self.button_onclick)
#         self.button_sqrt.clicked.connect(self.button_onclick)
#         self.button_abs.clicked.connect(self.button_onclick)
#         self.button_ceil.clicked.connect(self.button_onclick)
#         self.button_floor.clicked.connect(self.button_onclick)
#         self.button_exp.clicked.connect(self.button_onclick)

#     def button_onclick(self):
#         button = self.sender()
#         current_text = self.main_label.text()

#         if current_text == "0":
#             current_text = ""

#         if button.text() == "C":
#             self.main_label.setText("0")
#             self.main_label_2.setText("")
#         elif button.text() == "=":
#             try:
#                 result = str(eval(current_text))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(current_text + " = " + result)
#             except ZeroDivisionError:
#                 self.main_label.setText("Error: Division by Zero")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "π":
#             result = str(pi)
#             self.main_label.setText(result)
#             self.main_label_2.setText(result)
#         elif button.text() == "e":
#             result = str(e)
#             self.main_label.setText(result)
#             self.main_label_2.setText(result)
#         elif button.text() == "inv":
#             try:
#                 result = str(1 / float(current_text))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"1/{current_text} = {result}")
#             except ZeroDivisionError:
#                 self.main_label.setText("Error: Division by Zero")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "sin":
#             try:
#                 result = str(sin(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"sin({current_text}) = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "cos":
#             try:
#                 result = str(cos(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"cos({current_text}) = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "tan":
#             try:
#                 result = str(tan(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"tan({current_text}) = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "log":
#             try:
#                 result = str(log(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"log({current_text}) = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "!":
#             try:
#                 result = str(factorial(int(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"{current_text}! = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "pow":
#             self.main_label.setText(current_text + "^")
#         elif button.text() == "√":
#             try:
#                 result = str(sqrt(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"√{current_text} = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "abs":
#             try:
#                 result = str(abs(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"|{current_text}| = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "ceil":
#             try:
#                 result = str(ceil(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"ceil({current_text}) = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "floor":
#             try:
#                 result = str(floor(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"floor({current_text}) = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         elif button.text() == "exp":
#             try:
#                 result = str(exp(float(current_text)))
#                 self.main_label.setText(result)
#                 self.main_label_2.setText(f"exp({current_text}) = {result}")
#             except Exception as e:
#                 self.main_label.setText("Error: Invalid expression")
#         else:
#             self.main_label.setText(current_text + button.text())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Calc()
#     window.show()
#     sys.exit(app.exec())


class Calc(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("calc.ui", self)
        
        # dòng số 1 trong app
        self.button_0.clicked.connect(self.button_onclick)
        self.button_dots.clicked.connect(self.button_onclick)
        self.button_x10.clicked.connect(self.button_onclick)
        self.button_ans.clicked.connect(self.button_onclick)
        self.button_equal.clicked.connect(self.button_onclick)
        self.button_rnd.clicked.connect(self.button_onclick)
        self.button_ran.clicked.connect(self.button_onclick)
        self.button_ranInt.clicked.connect(self.button_onclick)
        self.button_pi.clicked.connect(self.button_onclick)
        self.button_e.clicked.connect(self.button_onclick)
        self.button_percentage.clicked.connect(self.button_onclick)
        self.button_pre_ans.clicked.connect(self.button_onclick)
        self.button_estimate.clicked.connect(self.button_onclick)
        self.button_uien.clicked.connect(self.button_onclick)
        self.button_an.clicked.connect(self.button_onclick)

        # dòng số 2 trong app
        self.button_1.clicked.connect(self.button_onclick)
        self.button_2.clicked.connect(self.button_onclick)
        self.button_3.clicked.connect(self.button_onclick)
        self.button_plus.clicked.connect(self.button_onclick)
        self.button_minus.clicked.connect(self.button_onclick)
        self.button_pol.clicked.connect(self.button_onclick)
        self.button_int.clicked.connect(self.button_onclick)
        self.button_rec.clicked.connect(self.button_onclick)
        self.button_intg.clicked.connect(self.button_onclick)
        
        # dòng số 3 trong app
        self.button_4.clicked.connect(self.button_onclick)
        self.button_5.clicked.connect(self.button_onclick)
        self.button_6.clicked.connect(self.button_onclick)
        self.button_times.clicked.connect(self.button_onclick)
        self.button_split.clicked.connect(self.button_onclick)
        self.button_nPr.clicked.connect(self.button_onclick)
        self.button_gcd.clicked.connect(self.button_onclick)
        self.button_ncr.clicked.connect(self.button_onclick)
        self.button_lcm.clicked.connect(self.button_onclick)
        
        # dòng số 4 trong app
        self.button_7.clicked.connect(self.button_onclick)
        self.button_8.clicked.connect(self.button_onclick)
        self.button_9.clicked.connect(self.button_onclick)
        self.button_del.clicked.connect(self.button_onclick)
        self.button_allClear.clicked.connect(self.button_onclick)
        self.button_CONST.clicked.connect(self.button_onclick)
        self.button_CONV.clicked.connect(self.button_onclick)
        self.button_RESET.clicked.connect(self.button_onclick)
        self.button_INS.clicked.connect(self.button_onclick)
        self.button_UNDO.clicked.connect(self.button_onclick)
        self.button_off.clicked.connect(self.off)
        
        # dòng số 5 trong app
        self.button_sto.clicked.connect(self.button_onclick)
        self.button_eng.clicked.connect(self.button_onclick)
        self.button_open.clicked.connect(self.button_onclick)
        self.button_close.clicked.connect(self.button_onclick)
        self.button_s_to_d.clicked.connect(self.button_onclick)
        self.button_mPlus.clicked.connect(self.button_onclick)
        self.button_RECALL.clicked.connect(self.button_onclick)
        self.button_x.clicked.connect(self.button_onclick)
        self.button_abs.clicked.connect(self.button_onclick)
        self.button_comma.clicked.connect(self.button_onclick)
        self.button_y.clicked.connect(self.button_onclick)
        self.button_fact.clicked.connect(self.button_onclick)
        self.button_z.clicked.connect(self.button_onclick)
        self.button_mminus.clicked.connect(self.button_onclick)
        self.button_purpleM.clicked.connect(self.button_onclick)

        # dòng số 6 trong app
        self.button_OpenClose.clicked.connect(self.button_onclick)
        self.button_timer.clicked.connect(self.button_onclick)
        self.button_xMinus1.clicked.connect(self.button_onclick)
        self.button_sin.clicked.connect(self.button_onclick)
        self.button_cos.clicked.connect(self.button_onclick)
        self.button_tan.clicked.connect(self.button_onclick)
        self.button_log.clicked.connect(self.button_onclick)
        self.button_a.clicked.connect(self.button_onclick)
        self.button_fact_2.clicked.connect(self.button_onclick)
        self.button_b.clicked.connect(self.button_onclick)
        self.button_xdots.clicked.connect(self.button_onclick)
        self.button_c.clicked.connect(self.button_onclick)
        self.button_sinMinus1.clicked.connect(self.button_onclick)
        self.button_d.clicked.connect(self.button_onclick)
        self.button_cosMinus1.clicked.connect(self.button_onclick)
        self.button_e_2.clicked.connect(self.button_onclick)
        self.button_tanMinus1.clicked.connect(self.button_onclick)
        self.button_f.clicked.connect(self.button_onclick)

        # dòng số 7 trong app
        # dòng số 8 trong app
        # dòng số 9 trong app
        # dòng số 10 trong app



        
    def button_onclick(self):
        button = self.sender()
        current_text = self.main_label.text()
        
        if current_text == "0":
            current_text = ""
        
        if button.text() == "=":
            try:
                result = str(eval(current_text))
                self.main_label.setText(result)
                self.main_label_2.setText(current_text + button.text())
            
            except ZeroDivisionError:
                self.main_label.setText("Error: Division by Zero")
            except Exception as e:
                self.main_label.setText("Error: Invalid expression")
                
        else:
            self.main_label.setText(current_text + button.text())
            self.main_label_2.setText(current_text + button.text())
            
        if button.text() == "DEL":
            self.main_label.setText("0")
            self.main_label_2.setText("")
            
    def off(self):
        window.close()
            

            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec())