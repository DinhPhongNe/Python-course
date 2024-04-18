import sys
import math
from math import pi, e, sin, cos, tan, log, factorial, sqrt, ceil, floor, exp
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QInputDialog
from sympy import symbols, Eq, solve as sympy_solve
from sympy import sympify
from PyQt6 import uic


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
        self.button_phanSo.clicked.connect(self.button_onclick)
        self.button_cang.clicked.connect(self.button_onclick)
        self.button_xBinh.clicked.connect(self.button_onclick)
        self.button_xbinhChamHoi.clicked.connect(self.button_onclick)
        self.button_logarit.clicked.connect(self.button_onclick)
        self.button_ln.clicked.connect(self.button_onclick)
        self.button_honso.clicked.connect(self.button_onclick)
        self.button_chiaR.clicked.connect(self.button_onclick)
        self.button_baCan.clicked.connect(self.button_onclick)
        self.button_MoDong.clicked.connect(self.button_onclick)
        self.button_xmu3.clicked.connect(self.button_onclick)
        self.button_dec.clicked.connect(self.button_onclick)
        self.button_canchamhoi.clicked.connect(self.button_onclick)
        self.button_hex.clicked.connect(self.button_onclick)
        self.button_muoiMuChamHoi.clicked.connect(self.button_onclick)
        self.button_bin.clicked.connect(self.button_onclick)
        self.button_mu.clicked.connect(self.button_onclick)
        self.button_oct.clicked.connect(self.button_onclick)
        
        # dòng số 8 trong app
        self.button_optn.clicked.connect(self.button_onclick)
        self.button_calc.clicked.connect(self.calc)
        self.button_tichphan.clicked.connect(self.button_onclick)
        self.button_xSymbol.clicked.connect(self.button_onclick)
        self.button_solve.clicked.connect(self.solve)
        self.button_equalSymbol.clicked.connect(self.addEqual)
        self.button_ddxPhanSo.clicked.connect(self.button_onclick)
        self.button_splitSymbol.clicked.connect(self.button_onclick)
        self.button_kyHieuTong.clicked.connect(self.button_onclick)
        self.button_kyHieuSanPham.clicked.connect(self.button_onclick)
        
        # dòng số 9 trong app
        self.button_shift.clicked.connect(self.feature)
        self.button_alpha.clicked.connect(self.feature)
        self.button_shift_2.clicked.connect(self.feature)
        self.button_alpha_2.clicked.connect(self.feature)
        self.button_menu.clicked.connect(self.menu)
        self.button_on.clicked.connect(self.button_onclick)
        self.button_setup.clicked.connect(self.button_onclick)
        # dòng số 10 trong app


    def button_onclick(self):
        button = self.sender()
        current_text = self.main_label.text()
        
        if current_text == "0":
            current_text = ""
        
        if button.text() == "=":
            self.calc()
        elif button.text() == "DEL":
            if len(current_text) > 0:
                current_text = current_text[:-1]
                self.main_label.setText(current_text)
                self.main_label_2.setText(current_text)
        elif button.text() == "AC":
            self.main_label.setText("0")
            self.main_label_2.setText("")
                
        else:
            self.main_label.setText(current_text + button.text())
            self.main_label_2.setText(current_text + button.text())

            
    def off(self):
        window.close()
        
        
    def feature(self):
        button = self.sender()
        current_text = self.feature_label.text()
    
        if current_text == "Feature":
            current_text = ""
    
        if button.text() == "SHIFT" and current_text != "":
            self.feature_label.setText("")
        elif button.text() == "SHIFT":
            self.feature_label.setText("shift")
    
        if button.text() == "ALPHA" and current_text != "":
            self.feature_label.setText("")
        elif button.text() == "ALPHA":
            self.feature_label.setText("alpha")
            
    def menu(self):
        pass
    
    def addEqual(self):
        current_text = self.main_label.text()
        if "=" not in current_text:
            self.main_label.setText(current_text + "=")
            self.main_label_2.setText(current_text + "=")
            
    def solve(self):
        equation = self.main_label.text()
        if "=" in equation:
            sides = equation.split("=")
            if len(sides) == 2:
                x = symbols('x')
                try:
                    expr_left = sympify(sides[0].replace("^", "**").replace("x", "*x"))  # Fix power operator and replace 'x' with '*x'
                    expr_right = sympify(sides[1].replace("^", "**").replace("x", "*x"))  # Fix power operator and replace 'x' with '*x'
                    result = sympy_solve(Eq(expr_left, expr_right), x)
                    if len(result) > 0:
                        self.main_label.setText(f"x = {result[0]}")
                        self.main_label_2.setText(f"x = {result[0]}")
                    else:
                        self.main_label.setText("No solution")
                except Exception as e:
                    self.main_label.setText("Error: Invalid equation")
            else:
                self.main_label.setText("Error: Invalid equation")
        else:
            self.main_label.setText("Error: Invalid equation")
            
    def calc(self):
        equation = self.main_label.text()
        if 'x' in equation:
            x_value, ok = QInputDialog.getInt(self, "Enter X value", "X:")
            if ok:
                equation_with_x = equation.replace('x', f'*{x_value}')
                try:
                    result = eval(equation_with_x)
                    self.main_label.setText(str(result))
                    self.main_label_2.setText(equation + "=" + str(result))
                except Exception as e:
                    self.main_label.setText("Error: Invalid expression")
        else:
            self.main_label.setText("Error: Invalid equation")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec())