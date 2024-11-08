#################################################################################
# Author: Diliara and Gerard
# Username: galievad nagelg
#
# Assignment: P01: Final Project
# Purpose: Collaborate with your partner to synthesize key learning elements
# from the entire course into a final project, incorporating a GUI using Turtle
# graphics, and apply Agile methodologies throughout the development process.
#################################################################################
import turtle
import tkinter as tk
from tkinter import ttk


class Madlib:
    def __init__(self, windowtext="Game MadLibs"):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """
        self.root = tk.Tk()  # Create the root window where all widgets go
        self.root.minsize(width=400, height=500)  # Sets the window's minimum size
        self.root.maxsize(width=400, height=500)  # Sets the window's maximum size
        self.root.title(windowtext)  # Sets root window title
        self.turtle = None
        self.turtle1 = None
        self.screen = None

        self.start_button = None

        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1Text = tk.StringVar()  # Makes a Tkinter string variable
        self.myTextLabel1 = None

        self.myTextBox2 = tk.Entry(self.root)
        self.myTextLabel2Text = tk.StringVar()  # Makes a Tkinter string variable
        self.myTextLabel2 = None

        self.myTextBox3 = tk.Entry(self.root)
        self.myTextLabel3Text = tk.StringVar()  # Makes a Tkinter string variable
        self.myTextLabel3 = None

        self.myTextBox4 = tk.Entry(self.root)
        self.myTextLabel4Text = tk.StringVar()  # Makes a Tkinter string variable
        self.myTextLabel4 = None

        self.myTextBox5 = tk.Entry(self.root)
        self.myTextLabel5Text = tk.StringVar()
        self.myTextLabel5 = None

        self.myTextBox6 = tk.Entry(self.root)
        self.myTextLabel6Text = tk.StringVar()
        self.myTextLabel6 = None

        self.myTextBox7 = tk.Entry(self.root)
        self.myTextLabel7Text = tk.StringVar()
        self.myTextLabel7 = None

        self.myTextBox8 = tk.Entry(self.root)
        self.myTextLabel8Text = tk.StringVar()
        self.myTextLabel8 = None

        self.myTextBox9 = tk.Entry(self.root)
        self.myTextLabel9Text = tk.StringVar()
        self.myTextLabel9 = None

        self.myTextBox10 = tk.Entry(self.root)
        self.myTextLabel10Text = tk.StringVar()
        self.myTextLabel10 = None

        self.myTextBox11 = tk.Entry(self.root)
        self.myTextLabel11Text = tk.StringVar()
        self.myTextLabel11 = None

        self.word1 = None
        self.word2 = None
        self.word3 = None
        self.word4 = None
        self.word5 = None
        self.word6 = None
        self.word7 = None

    def create_textbox(self):
        """
        Creates a textbox into which the user can type

        :return: None
        """

        self.myTextBox1.grid(row=0, column=1, sticky=tk.E + tk.W, pady=10)
        self.myTextBox2.grid(row=1, column=1, sticky=tk.E + tk.W, pady=10)
        self.myTextBox3.grid(row=2, column=1, sticky=tk.E + tk.W, pady=10)
        self.myTextBox4.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)
        self.myTextBox5.grid(row=4, column=1, sticky=tk.E + tk.W, pady=10)
        self.myTextBox6.grid(row=5, column=1, sticky=tk.E + tk.W, pady=10)
        self.myTextBox7.grid(row=6, column=1, sticky=tk.E + tk.W, pady=10)

    def create_start_button(self, buttontext="Let's look at our MadLib!"):
        """
               Creates a button with the given buttontext

               :param buttontext: The text on the button
               :return: None
               """
        self.start_button = tk.Button(self.root, text=buttontext, command=self.create_start_button_handler)
        # Note that when myButton1 button is pushed, self.button1handler is called
        self.start_button.grid(row=10, column=1, sticky=tk.E + tk.W, pady=10)

    def create_labels(self, labeltext=" Choose a noun: "):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """
        self.myTextLabel1Text.set(labeltext)  # Sets the Tkinter string variable
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text)
        self.myTextLabel1.grid(row=0, column=0, sticky=tk.E + tk.W, pady=10)

        self.myTextLabel2Text.set("Choose a adjective")  # Sets the Tkinter string variable
        self.myTextLabel2 = tk.Label(self.root, textvariable=self.myTextLabel2Text)
        self.myTextLabel2.grid(row=1, column=0, sticky=tk.E + tk.W, pady=10)

        self.myTextLabel3Text.set("Choose a noun")  # Sets the Tkinter string variable
        self.myTextLabel3 = tk.Label(self.root, textvariable=self.myTextLabel3Text)
        self.myTextLabel3.grid(row=2, column=0, sticky=tk.E + tk.W, pady=10)

        self.myTextLabel4Text.set("Choose a noun")  # Sets the Tkinter string variable
        self.myTextLabel4 = tk.Label(self.root, textvariable=self.myTextLabel4Text)
        self.myTextLabel4.grid(row=3, column=0, sticky=tk.E + tk.W, pady=10)

        self.myTextLabel5Text.set("Choose a noun")  # Sets the Tkinter string variable
        self.myTextLabel5 = tk.Label(self.root, textvariable=self.myTextLabel5Text)
        self.myTextLabel5.grid(row=4, column=0, sticky=tk.E + tk.W, pady=10)

        self.myTextLabel6Text.set("Choose a noun")  # Sets the Tkinter string variable
        self.myTextLabel6 = tk.Label(self.root, textvariable=self.myTextLabel6Text)
        self.myTextLabel6.grid(row=5, column=0, sticky=tk.E + tk.W, pady=10)

        self.myTextLabel7Text.set("Choose a noun")  # Sets the Tkinter string variable
        self.myTextLabel7 = tk.Label(self.root, textvariable=self.myTextLabel7Text)
        self.myTextLabel7.grid(row=6, column=0, sticky=tk.E + tk.W, pady=10)

    def create_start_button_handler(self):
        """
        Event handler for myButton1 above.
        Gets the text from the textbox and writes in myTextLabel1

        :return: None
        """
        self.word1 = self.myTextBox1.get()
        self.word2 = self.myTextBox2.get()
        self.word3 = self.myTextBox3.get()

        self.word5 = self.myTextBox5.get()
        self.word6 = self.myTextBox6.get()
        self.word7 = self.myTextBox7.get()
        self.word4 = self.myTextBox4.get()

        self.turtle = turtle.Turtle()
        self.turtle1 = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.addshape("circus2.gif")
        self.turtle1.shape("circus2.gif")

        story_string = '''Oh, the Places You'll Go!
        Congratulations!
        Today is your {0}.
        You're off to {1} {2}!
        You're off and away!
        You have {3} in your pocket.
        You have a mouse in your {4}
        You can {5} yourself
        Any direction you choose.
        You're on your way. And you know what you know.
        And YOU are the {6} who'll decide where to go!
        '''.format(self.word1, self.word2, self.word3, self.word4, self.word5, self.word6, self.word7)
        self.turtle.penup()
        self.turtle.goto(-250, -100)
        self.turtle.pendown()
        self.turtle.write(story_string, font=("a Alloy Ink", 15, "normal"))  # Draws Madlib
        self.turtle.penup()
        self.turtle.goto(-95, 260)
        self.turtle.pendown()
        self.turtle.write("MadLibs!", font=("a Alloy Ink", 30, "normal"))
        self.screen.exitonclick()


def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    myGUI = Madlib("Hello, let's play MadLibs")  # Create a new myTkinter object
    myGUI.create_start_button()

    myGUI.create_textbox()  # Calls the create textbox method for capturing user input
    myGUI.create_labels()

    # Create a label to writing text into

    myGUI.root.mainloop()  # Needed to start the event loop


if __name__ == "__main__":
    main()
