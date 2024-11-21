import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QPainter, QPainterPath
from PyQt5.QtCore import Qt, QRectF

class MinimalLoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(400, 200)  # Ukuran dialog
        self.radius = 15  # Radius sudut kotak dialog

        # Layout utama
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(20)  # Mengurangi jarak antara gambar dan teks

        # Tambahkan gambar di sisi kiri
        self.photo_label = QLabel(self)
        original_pixmap = QPixmap("/home/elfnd/Pictures/riss2.jpg").scaled(120, 100, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        # Membuat gambar dengan sudut melengkung
        rounded_pixmap = QPixmap(original_pixmap.size())
        rounded_pixmap.fill(Qt.transparent)

        path = QPainterPath()
        path.addRoundedRect(QRectF(rounded_pixmap.rect()), 12, 12)

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, original_pixmap)
        painter.end()

        self.photo_label.setPixmap(rounded_pixmap)
        main_layout.addWidget(self.photo_label)

        # Layout vertikal untuk teks dan tombol OK
        right_layout = QVBoxLayout()

        # Label teks dengan dukungan word wrap
        self.text_label = QLabel("Weolcome to the system, Have a nice day, el:)            .                                ~urlovee", self)
        self.text_label.setFont(QFont("Arial", 12))
        self.text_label.setStyleSheet("color: #FFFFFF;")
        self.text_label.setWordWrap(True)  # Aktifkan word wrap
        right_layout.addWidget(self.text_label)

        # Tombol OK
        ok_button = QPushButton("OK")
        ok_button.setFixedSize(60, 30)
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: #FFFFFF;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #777777;
            }
        """)
        ok_button.clicked.connect(self.accept)
        right_layout.addWidget(ok_button, alignment=Qt.AlignRight | Qt.AlignBottom)

        # Tambahkan layout kanan ke layout utama
        main_layout.addLayout(right_layout)

    def paintEvent(self, event):
        # Menggambar kotak dialog dengan sudut rounded
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), self.radius, self.radius)  # Konversi ke QRectF
        painter.fillPath(path, Qt.darkGray)  # Ganti warna sesuai kebutuhan
        painter.end()

# Fungsi utama
def main():
    app = QApplication(sys.argv)
    dialog = MinimalLoginDialog()
    dialog.exec_()

if __name__ == "__main__":
    main()
