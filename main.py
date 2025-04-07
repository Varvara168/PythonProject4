import sys
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMessageBox, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsTextItem
from ui import Ui_MainWindow
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont, QPen
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        loadUi("ui.ui", self)
        self.markers = []
        self.t = QLineEdit(self.centralwidget)
        self.pushButton_2.clicked.connect(self.update_input_fields)
        # self.pushButton.clicked.connect(self.update)
        # self.load_data()

    # def load_data(self):
        # super().__init__()
        # self.setupUi(self)
        # loadUi("ui.ui", self)
        #
        # self.setWindowTitle("My App")
        # button = QPushButton("Нажмите на меня!")
        #
        # # Устанавливаем центральный виджет Window.
        # self.setCentralWidget(button)


    def update_input_fields(self):
        """Updates coordinate input fields when a row is selected"""
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        desc = self.lineEdit_4.text()
        name = self.lineEdit_3.text()
        self.markers.append({"x": int(x), "y": int(y), 'desk': desc, 'name': name})
        print(self.markers)
        try:
            self.update_map()
        except Exception as e:
            print(e)


    def update_map(self):
        """Обновляет отображение карты с маркерами."""
        # self.set_map_image("map.png")  # Перезагрузка изображения карты
        base_map = QPixmap("map.png")  # Создание объекта QPixmap из изображения карты
        painter = QPainter(base_map)  # Создание объекта QPainter для рисования на карте
        painter.setPen(QPen(Qt.GlobalColor.red, 5))  # Установка цвета и толщины пера для рисования маркеров

        for marker in self.markers:  # Перебор всех маркеров
            x = marker["x"]  # Получение координаты X маркера
            y = marker["y"]  # Получение координаты Y маркера
            painter.drawPoint(x, y)  # Рисование маркера в виде точки
        painter.end()  # Завершение рисования
        self.label_4.setPixmap(base_map)  # Установка обновленного изображения карты в виджет карты
        # self.map_widget.mousePressEvent = self.marker_clicked  # Установка обработчика клика на маркер


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

'''
        # Find the widgets from the loaded UI file
        self.map_label = self.findChild(QLabel, "map_label")
        self.x_coord_input = self.findChild(QLineEdit, "x_coord_input")
        self.y_coord_input = self.findChild(QLineEdit, "y_coord_input")
        self.draw_button = self.findChild(QPushButton, "draw_button")
        self.description_input = self.findChild(QLineEdit, "description_input") # Add input for the description

        if not all([self.map_label, self.x_coord_input, self.y_coord_input, self.draw_button, self.description_input]):
            print("Error: One or more UI elements not found. Check the names in your .ui file.")
            sys.exit(1)

        # Load the initial map image (replace with your image path)
        self.original_pixmap = QPixmap("your_map_image.png")  # Replace with your actual map image file
        self.map_label.setPixmap(self.original_pixmap)
        self.map_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Connect the "Draw Point" button to a function
        self.draw_button.clicked.connect(self.add_point)  # Changed to add_point

    def add_point(self):
        """Adds a point (and description) to the map using QGraphicsScene."""
        try:
            # 1. Get the coordinates from the QLineEdit widgets
            x = int(self.x_coord_input.text())
            y = int(self.y_coord_input.text())

            # 2. Get the description text
            description = self.description_input.text()

            # 3. Validate that the point is within bounds
            if x < 0 or x > self.original_pixmap.width() or y < 0 or y > self.original_pixmap.height():
                QMessageBox.warning(self, "Error", "Coordinates are out of bounds.")
                return

            # 4. Create a QGraphicsScene if it doesn't exist (first click)
            if not hasattr(self, 'scene'):
                self.scene = QGraphicsScene()
                self.map_label.setPixmap(self.original_pixmap)  # Reset the pixmap
                self.map_label.setScaledContents(True)  # Allow QLabel to scale image

                # Optional: Set the scene's size to match the pixmap,
                # but only if the label is the same size as the original image.
                self.scene.setSceneRect(0, 0, self.original_pixmap.width(), self.original_pixmap.height())

                # Create a QGraphicsView and add it to the layout
                self.graphics_view = QtWidgets.QGraphicsView(self.scene, self.map_label) #Add the graphics view, passing our scene to it.
                self.graphics_view.setFixedSize(self.map_label.size())#sets fixed dimensions of our map_label to our map
                self.graphics_view.show()

            # 5. Create the point (ellipse)
            point_radius = 5
            ellipse = QGraphicsEllipseItem(x - point_radius, y - point_radius, point_radius * 2, point_radius * 2)
            ellipse.setBrush(QColor(255, 0, 0))  # Red color
            self.scene.addItem(ellipse)

            # 6. Add the description
            text_item = QGraphicsTextItem(description)
            text_item.setPos(x + point_radius + 2, y - point_radius)  # Adjust position as needed
            text_item.setDefaultTextColor(QColor(0, 0, 0))  # Black text
            self.scene.addItem(text_item)

            # 7. Optionally refresh the map label (only needed if you're *not* using QGraphicsView)
            # self.map_label.setPixmap(self.scene.toImage())

        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid coordinates. Please enter integers.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An unexpected error occurred: {e}")

'''