import sys

from PyQt5.QtWidgets import (QWidget, QMainWindow, QApplication, QLabel,
                            QComboBox, QSpinBox, QPushButton,
                            QVBoxLayout, QAction)
from PyQt5.QtCore import Qt

class InfoWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(InfoWindow, self).__init__(*args, **kwargs)
        
        nevjegy = "Fatömegszámító program:\n\n\
        Készítette: Lászlók András (2022)\n\n\
        Készült az alábbi műben lévő paraméterek\n\
        és fatérfogat függvény felhasznlásával:\n\
        Dr. Sopp László, Kolozs László (2000):\n\
        Fatömegszámítási táblázatok (harmadik átdolgozott kiadás).\n\
        Állami Erdészeti Szolgálat, Budapest.\n\n\
        A program a vágáslap feletti összes\n\
        (vastag+vékony) fatömeget számítja ki.\n\n\
        Vastagfa: kéreggel együtt 5 cm-nél vastagabb faanyag.\n\
        Vékonyfa: kéreggel együtt 5 cm és annál vékonyabb faanyag.\n\n\
        A program egy hobbiprojekt. \n\n\
        Nem használható fel semmilyen hivatalos célra különösen:\n\
            - gazdasági tervek készítéséhez,\n\
            - hatósági eljárások során,\n\
            - üzleti célra."
        
        self.setWindowTitle("Névjegy")
        
        layout = QVBoxLayout()
        self.label = QLabel(nevjegy)

        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Fatömegszámító program")

        self.widget1 = QLabel("Válasszon fafajt:")
        font = self.widget1.font()
        font.setPointSize(10)
        self.widget1.setFont(font)
        self.widget1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.widget2 = QComboBox()
        self.widget2.addItems(["Akác",
            "Bükk",
            "Cser",
            "Fekete dió",
            "Gyertyán",
            "Juharok",
            "Kocsányos tölgy",
            "Kocsánytalan tölgy",
            "Kőris",
            "Vörös tölgy",
            "Agathe-F nyár",
            "Éger",
            "Fehér fűz",
            "Fehér nyár",
            "Fekete nyár",
            "Hársak",
            "I-214 nyár",
            "Kései nyár",
            "Korai nyár",
            "Közönséges nyír",
            "Óriás nyár",
            "Rezgő nyár",
            "Duglászfenyő",
            "Erdeifenyő",
            "Feketefenyő",
            "Jegenyefenyő",
            "Lucfenyő",
            "Vörösfenyő"])

        self.widget3 = QLabel("Adja meg a mellmagassági átmérőt (cm):")
        font = self.widget3.font()
        font.setPointSize(10)
        self.widget3.setFont(font)
        self.widget3.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.widget3a = QSpinBox()

        self.widget4 = QLabel("Adja meg a famagasságot (m):")
        font = self.widget4.font()
        font.setPointSize(10)
        self.widget4.setFont(font)
        self.widget4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.widget4a = QSpinBox()

        self.widget5 = QPushButton("Számolás")
        font = self.widget5.font()
        font.setPointSize(10)
        self.widget5.setFont(font)
        self.widget5.pressed.connect(self.onMyButtonClick)

        self.widget6 = QLabel("Vágáslap feletti összes fatömeg (m\u00b3):")
        font = self.widget6.font()
        font.setPointSize(10)
        self.widget6.setFont(font)
        self.widget6.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.widget7 = QLabel("")
        font = self.widget7.font()
        font.setPointSize(15)
        font.setBold(True)
        self.widget7.setFont(font)
        self.widget7.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.widget1)
        layout.addWidget(self.widget2)
        layout.addWidget(self.widget3)
        layout.addWidget(self.widget3a)
        layout.addWidget(self.widget4)
        layout.addWidget(self.widget4a)
        layout.addWidget(self.widget5)
        layout.addWidget(self.widget6)
        layout.addWidget(self.widget7)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        button_kilep = QAction("Kilépés", self)
        button_kilep.triggered.connect(self.Exit)

        button_info = QAction("Névjegy", self)
        button_info.triggered.connect(self.Info)

        menu = self.menuBar()

        file_menu = menu.addMenu("&Menü")
        file_menu.addAction(button_info)
        file_menu.addAction(button_kilep)

    def Exit(self):
        """Kilépés a programból"""
        sys.exit()

    def Info(self):
        """Névjegy"""
        self.w = InfoWindow()
        self.w.show()

    def onMyButtonClick(self):
        """Számolás végzése"""

        f = self.widget2.currentIndex()

        PAR = [
            [3.2003E+03,2.9442E-01,-1.8069E+00,-8.4771E+00,4.0000E+00],
            [4.6130E+03,7.1602E-01,-5.2382E+00,-3.4003E+01,1.0000E+00],
            [3.5023E+03,-1.5094E-01,8.3832E+00,1.3218E+00,2.0000E+00],
            [2.6353E+03,-6.5142E-01,3.5781E+01,1.0963E+01,4.0000E+00],
            [2.6863E+03,-6.6721E-01,4.9944E+01,2.2083E+01,2.0000E+00],
            [4.1732E+03,-8.4755E-03,4.9389E-01,-8.4324E+00,1.0000E+00],
            [2.3979E+03,-5.2279E-01,2.5230E+01,2.5880E+01,4.0000E+00],
            [2.7771E+03,-7.5112E-01,3.1496E+01,3.0352E+01,3.0000E+00],
            [2.8171E+03,6.2094E-02,-1.0991E+00,1.9500E+01,3.0000E+00],
            [4.4289E+03,2.0855E-01,-1.2585E+01,-1.2265E+01,1.0000E+00],
            [2.2920E+03,1.4296E-01,-6.3633E+00,3.0914E+01,4.0000E+00],
            [3.6318E+03,-2.5983E-02,2.7393E+00,1.5578E+00,1.0000E+00],
            [3.2188E+03,1.4227E-01,-3.7035E+00,-1.1502E+01,3.0000E+00],
            [3.1848E+03,-3.4369E-01,1.0211E+01,2.4682E+00,3.0000E+00],
            [3.4216E+03,-9.6765E-02,3.1602E+00,-9.3335E+00,2.0000E+00],
            [4.1422E+03,1.3081E-01,-2.7146E+00,-1.9825E+01,1.0000E+00],
            [2.3411E+03,-1.3816E-01,1.4439E+01,1.5625E+01,4.0000E+00],
            [2.6780E+03,-3.5070E-01,1.0302E+01,1.2449E+01,3.0000E+00],
            [2.7200E+03,-1.5568E-01,8.4776E+00,6.3624E+00,2.0000E+00],
            [4.7389E+03,1.1636E+00,-3.5994E+01,-4.0625E+01,1.0000E+00],
            [3.1991E+03,-1.4467E-01,7.3741E+00,7.8955E-01,2.0000E+00],
            [2.9624E+03,-3.9647E-01,1.5260E+01,1.4990E+01,3.0000E+00],
            [3.8939E+03,2.5449E-01,-1.8017E+01,-8.1867E+00,3.0000E+00],
            [3.2381E+03,5.1273E-02,5.7325E+00,-1.4593E+01,4.0000E+00],
            [3.3482E+03,-2.2665E-01,1.1599E+01,-3.0405E+00,4.0000E+00],
            [5.3501E+03,-1.2820E-02,1.0617E+00,-3.9182E+01,1.0000E+00],
            [3.9833E+03,-1.5907E-01,-8.3139E+00,5.0847E+00,3.0000E+00],
            [2.6830E+03,4.8460E-03,-1.4928E+01,4.0281E+01,3.0000E+00]
        ]

        p1 = PAR[f][0]
        p2 = PAR[f][1]
        p3 = PAR[f][2]
        p4 = PAR[f][3]
        k = PAR[f][4]

        D = self.widget3a.value()
        H = self.widget4a.value()
        V = (p1 + p2*D*H + p3*D + p4*H) * (H/(H-1.3))**k * D**2 * H/10**8

        self.widget7.setText(f"{round(V,2)}")

def run():
    """Modul futtatása"""
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
