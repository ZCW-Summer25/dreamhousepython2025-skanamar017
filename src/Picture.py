import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle

import random


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='tomato')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        
        self.ground = None
        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None

        self.draw()

    def draw(self):

        self.sun = Circle(canvas=self.canvas, diameter=60, color="dark orange", fill="dark orange", line=1)
        self.sun.move_horizontal(450)
        self.sun.move_vertical(220)
        self.sun.make_visible()

        self.ocean = Square(canvas=self.canvas, length=600, width=400, color="salmon", fill="salmon", line=2)
        self.ocean.move_horizontal(-20)
        self.ocean.move_vertical(265)
        self.ocean.make_visible()

        self.ground = Circle(canvas=self.canvas, diameter=700, color="black", fill="black", line=1)
        self.ground.move_horizontal(-200)
        self.ground.move_vertical(220)
        self.ground.make_visible()

        self.wall = Square(canvas=self.canvas, length=140, width=90, color="black", fill="black", line=2)
        self.wall.move_horizontal(30)
        self.wall.move_vertical(150)
        self.wall.make_visible()

        self.window = Square(canvas=self.canvas, length=30, width=30, color="yellow", fill="yellow", line=1)
        self.window.move_horizontal(50)
        self.window.move_vertical(188)
        self.window.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=65, width=170, color="black", fill="black", line=2)
        self.roof.move_horizontal(25)
        self.roof.move_vertical(183)
        self.roof.make_visible()


        for i in range(6):
            self.smoke = Circle(canvas=self.canvas, diameter=15, color="gray17", fill="gray17", line=1)
            self.smoke.move_horizontal(82-10*i)
            self.smoke.move_vertical(78-6*i)
            self.smoke.make_visible()


        self.chimney = Square(canvas=self.canvas, length=20, width=30, color="black", fill="black", line=1)
        self.chimney.move_horizontal(40)
        self.chimney.move_vertical(100)
        self.chimney.make_visible()

        

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
