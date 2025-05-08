import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QVBoxLayout, QStackedWidget, QGridLayout
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer

class SplashScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel()
        pixmap = QPixmap("assets/splash.jpg")
        label.setPixmap(pixmap.scaled(600, 400, Qt.KeepAspectRatio))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)

class MainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # === 🌈 设置背景渐变色 ===
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 #f0f2f5, stop:1 #dbe2ef
                );
            }
        """)

        layout = QGridLayout()
        layout.setSpacing(20)

        font = QFont("Arial", 12, QFont.Bold)

        # === 📋 四大功能按钮（带图标/多行） ===
        self.btn_ocr = QPushButton("📄 财报账单\nOCR识别")
        self.btn_advisor = QPushButton("🤖 审计问题\n智能咨询")
        self.btn_analysis = QPushButton("🔍 智能分析\n风险检测")
        self.btn_chart = QPushButton("📊 审计图表\n可视化")

        for btn in [self.btn_ocr, self.btn_advisor, self.btn_analysis, self.btn_chart]:
            btn.setFont(font)
            btn.setMinimumSize(160, 100)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4e73df;
                    color: white;
                    border-radius: 12px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #2e59d9;
                }
            """)

        # === 🎯 网格四象限布局 ===
        layout.addWidget(self.btn_ocr, 0, 0)
        layout.addWidget(self.btn_advisor, 0, 2)
        layout.addWidget(self.btn_analysis, 2, 0)
        layout.addWidget(self.btn_chart, 2, 2)

        # === 🧠 中间标题 ===
        title = QLabel(" 智能审计助手平台 ")
        title.setFont(QFont("幼圆", 22, QFont.Bold))
        title.setStyleSheet("color: #2f4f6f;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title, 1, 1)

        self.setLayout(layout)

        # === 🧩 功能模块绑定 ===
        self.btn_ocr.clicked.connect(self.run_ocr_module)
        self.btn_advisor.clicked.connect(self.run_advisor_module)
        self.btn_analysis.clicked.connect(self.run_report_module)
        self.btn_chart.clicked.connect(self.run_chart_module)

    def run_script_hidden(self, relative_path):
        import os
        abs_path = os.path.abspath(relative_path)
        subprocess.Popen(["python", abs_path])  # 先让终端弹出来看报错

    def run_chart_module(self):
        self.run_script_hidden("Audit-chart/gradio_app.py")

    def run_ocr_module(self):
        self.run_script_hidden("ocr-main/app.py")

    def run_report_module(self):
        self.run_script_hidden("AuditAndCompliance-main/Gui.py")

    def run_advisor_module(self):
        self.run_script_hidden("AuditAdvisor/AuditAdvisor.py")


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CYMcolony 审计助手平台")
        self.resize(800, 600)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.splash = SplashScreen()
        self.menu = MainMenu()

        self.stack.addWidget(self.splash)
        self.stack.addWidget(self.menu)

        QTimer.singleShot(2000, lambda: self.stack.setCurrentWidget(self.menu))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
