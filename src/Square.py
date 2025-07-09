import tkinter as tk
from tkinter import Canvas
from Shape import Shape


class Square(Shape):
    def __init__(self, canvas: Canvas, x: int = 60, y: int = 50, length: int = 30, width: int = 30, line: int = 100, color: str = "black", fill: str = None):
        super().__init__(canvas=canvas, x=x, y=y, color=color, fill=fill, line=line)
        self.length = length
        self.width = width


    def draw(self):
        if self.is_visible:
            print(f"Drawing square at ({self.x_position},{self.y_position}) length {self.length} width {self.width} color {self.color} fill {self.fill} line {self.line}")
            self.shape_id = self.canvas.create_rectangle(
                self.x_position, self.y_position,
                self.x_position + self.length, self.y_position + self.width,
                outline=self.color, fill=self.fill, width=self.line
            )

    def erase(self):
        if self.is_visible:
            print("Erasing square")
            super().erase()
