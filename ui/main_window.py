from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QLineEdit, QTextEdit, QColorDialog
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from core.color import Color
from core.solver import Solver


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SVG Filter Studio")
        self.setFixedSize(420, 380)

        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        # --- Color input ---
        row = QHBoxLayout()
        self.hex_input = QLineEdit("#ff5722")
        self.hex_input.setPlaceholderText("#RRGGBB")

        pick_btn = QPushButton("🎨 Pick")
        pick_btn.clicked.connect(self.pick_color)

        gen_btn = QPushButton("Generate")
        gen_btn.clicked.connect(self.generate_filter)

        row.addWidget(self.hex_input)
        row.addWidget(pick_btn)
        row.addWidget(gen_btn)
        layout.addLayout(row)

        # --- Preview ---
        preview_row = QHBoxLayout()
        self.preview_target = QLabel("Target")
        self.preview_result = QLabel("Result")

        for box in (self.preview_target, self.preview_result):
            box.setFixedSize(160, 80)
            box.setAlignment(Qt.AlignCenter)
            box.setPixmap(QPixmap("assets/preview.svg").scaled(80, 80))

        preview_row.addWidget(self.preview_target)
        preview_row.addWidget(self.preview_result)
        layout.addLayout(preview_row)

        # --- Output ---
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        copy_btn = QPushButton("📋 Copy CSS Filter")
        copy_btn.clicked.connect(self.copy_css)
        layout.addWidget(copy_btn)

    # ---------------- logic ----------------

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.hex_input.setText(color.name())
            self.generate_filter()

    def generate_filter(self):
        try:
            hex_color = self.hex_input.text()
            target = Color.from_hex(hex_color)

            solver = Solver(target)
            result, loss = solver.solve()

            confidence = max(0, 100 - loss / 7.65)

            css = (
                f"filter: invert({result[0] * 100:.0f}%) "
                f"sepia({result[1] * 100:.0f}%) "
                f"saturate({result[2] * 100:.0f}%) "
                f"hue-rotate({result[3]:.0f}deg) "
                f"brightness({result[4] * 100:.0f}%) "
                f"contrast({result[5] * 100:.0f}%);\n\n"
                f"Loss: {loss:.2f}\n"
                f"Confidence: {confidence:.1f}%"
            )

            self.output.setText(css)

            # previews
            self.preview_target.setStyleSheet(
                f"background:{hex_color};"
            )

            self.preview_result.setStyleSheet(
                css
            )

        except Exception as e:
            self.output.setText(str(e))

    def copy_css(self):
        self.output.selectAll()
        self.output.copy()
