from tkinter import *
from tkinter import Tk
import random
import copy
import webbrowser


global window_play, first_click
window_start = Tk()
width = window_start.winfo_screenwidth()
height = window_start.winfo_screenheight()
window_start.geometry(f"{int(width * 0.7)}x{int(height * 0.7)}+{int(width * 0.15)}+{int(height * 0.15)}")
window_start.title("Kai Cao's Final Project")
l = Label(window_start, text="Different Kinds Of Nerve Cells", font=('Times New Roman', 35, 'bold'))
l.place(x=(width * 0.17), y=(height * 0.23))
Label(window_start, text="Kai Cao", font=('Times New Roman', 30, 'bold')).place(x=(width * 0.3), y=(height * 0.4))
Label(window_start, text="Click the title to continue", font=('Times New Roman', 17, 'bold')).place(x=(width * 0.28), y=(height * 0.6))
def exit(event):
    window_start.destroy()

l.bind("<Button-1>", exit)

window_start = mainloop()


root = Tk()
root.title("Memory Game")
root.geometry('500x300+480+200')

# print(width)
count = 0


cardContent_1 = ["Unipolar neuron",
                 "Bipolar neuron",
                 "Golgi cell",
                 "Anaxonic neuron",
                 "Pseudounipolar neuron",
                 "Basket cells",
                 "Lugaro cells",
                 """Medium spiny neurons (MSNs)
(aka spiny projection neurons (SPNs)) """,
                 "Purkinje cells",
                 "Pyramidal cells",
                 "Renshaw cells",
                 "Unipolar brush cells\n(UBCs)",
                 "Granule cell",
                 "Von Economo neurons (VENs)\n(spindle neurons)",
                 """Betz cells 
(aka pyramidal cells of Betz)"""]

cardContent_2 = ["""a neuron in which only one process,
called a neurite, 
extends from the cell body""",

"""a type of neuron that has two extensions
(one axon and one dendrite)""",

"""a kind of inhibitory interneurons found
within the granular layer of the cerebellum.
They were first identified
as inhibitory in 1964""",

"""a type of neuron where there is no axon
or it cannot be differentiated
from the dendrites.""",

"""This type of neuron contains an axon
that has split into two branches;
one branch travels to the
peripheral nervous system and the
other to the central nervous system""",

"""a kind of inhibitory
GABAergic interneurons
of the brain, found throughout
different regions of
the cortex and cerebellum""",

"""sensory interneurons of the cerebellum,
that have an inhibitory function.
They are fusiform, having a spindle shape
that tapers at each end. 
They were first described 
in the early 20th century.""",

"""a special type of GABAergic inhibitory 
cell representing 95% of neurons 
within the human striatum,
a basal ganglia structure.
have two phenotypes: 
D1-type MSNs of the direct pathway 
& D2-type MSNs of the indirect pathway.""",

"""a class of GABAergic inhibitory neurons 
located in the cerebellum. 
These cells are some of the 
largest neurons in the human brain.""",

"""a type of multipolar neuron found 
in areas of the brain including 
the cerebral cortex, the hippocampus, 
and the amygdala""",

"""inhibitory interneurons found in
the gray matter of the spinal cord.
They can receive an 
excitatory collateral from the alpha 
neuron's axon or send an inhibitory 
axon to synapse with the cell body 
of the initial alpha neuron & an alpha 
motor neuron of the same motor pool.""",

"""a class of excitatory 
glutamatergic interneuron
found in the granular layer of
the cerebellar cortex
and also in the granule cell
domain of the cochlear nucleus.""",

"""a number of different types of neuron
whose only common feature is
that they all have very small cell bodies.
They are found within the granular
layer of the cerebellum,
the dentate gyrus of the hippocampus""",

"""a specific class of 
mammalian cortical neurons
characterized by a large spindle-shaped
soma gradually tapering into
a single apical axon in
one direction, with only
a single dendrite facing opposite""",

"""giant pyramidal cells located within
the fifth layer of the grey matter
in the primary motor cortex.
These neurons are the largest in the
central nervous system, sometimes
reaching 100 μm in diameter.
"""
]
errorcount = 0


def mode_learn():
    window_learn = Tk()
    window_learn.title("Types of the neuron cells")
    window_learn.geometry(f"{int(width * 0.7)}x{int(height * 0.7)}+{int(width * 0.15)}+{int(height * 0.15)}")

    Label(window_learn, text="All the points about the types of nerve cells are in the following slide",
          font=('Times', 26, 'bold italic underline')).place(x=(width * 0.1), y=(height * 0.1))

    download = Label(window_learn, text="View online: https://1drv.ms/x/s!AqRZ-dI0T6ICgyghzldbKPZPt3CC?e=l91UDG",
                     font=('Times New Roman', 22, 'bold italic'))
    download.place(x=(width * 0.1), y=(height * 0.35))

    def open_url(event):
        webbrowser.open("https://1drv.ms/x/s!AqRZ-dI0T6ICgyghzldbKPZPt3CC?e=l91UDG", new=0)

    download.bind("<Button-1>", open_url)

    window_learn.mainloop()


def mode_play():

    def erase():
        window_play.destroy()

    window_play = Tk()
    window_play.title("Memory Game")
    window_play.geometry('500x300+480+200')
    Button(window_play, text="Easy", width=15, height=3, command=lambda: [level("easy"), erase()]).place(x=170, y=30)
    Button(window_play, text="Median", width=15, height=3, command=lambda: [level("median"), erase()]).place(x=170, y=105)
    Button(window_play, text="Hard", width=15, height=3, command=lambda: [level("hard"), erase()]).place(x=170, y=180)
    window_play.mainloop()


def level(level):
    gameView = Tk()
    gameView.title("Memory Game")
    gameView.geometry(f"{int(width * 0.7)}x{int(height * 0.7)}+{int(width * 0.15)}+{int(height * 0.15)}")

    Label(gameView,
        text="Please match the names of the cells and their corresponding functions in the nervous system",
        font=('Times', 20, 'bold italic'))\
        .grid(row=0, column=1, sticky=E+W)
    label = Label(gameView, text=f"Number of errors: {errorcount}", font=('microsoft yahei', 16, 'bold'))
    label.grid(row=1, column=1)
    cardcontent_1 = copy.deepcopy(cardContent_1)
    cardcontent_2 = []
    random.shuffle(cardcontent_1)
    for item in range(0, len(cardcontent_1)):
        for index in range(0, len(cardContent_1)):
            if cardcontent_1[item] == cardContent_1[index]:
                pairIndex = index
                cardcontent_2.append(cardContent_2[pairIndex])
    possible = []

    def id(index):
        global count, possible
        count += 1
        print(count)
        if count % 2 == 1:
            possible = copy.deepcopy(index)
            print(possible)
            buttons[possible[0]]['state'] = "disabled"
        else:
            print(index)
            print(possible)
            if possible[1] == index[1]:
                buttons[possible[0]].destroy()
                buttons[index[0]].destroy()
            else:
                global errorcount
                errorcount += 1
                label.configure(text=f"Number of errors: {errorcount}")
                label.grid(row=1, column=1)
                buttons[possible[0]]['state'] = "normal"

    if level == "easy":
        bt1 = Button(gameView, text=cardcontent_1[0], width=int(width * 0.02), height=int(height * 0.01), font=('Cambria', 12, 'bold'), command=lambda: id([0, 0]))
        bt2 = Button(gameView, text=cardcontent_2[0], width=int(width * 0.02), height=int(height * 0.01), font=('Cambria', 12, 'bold'), command=lambda: id([1, 0]))
        bt3 = Button(gameView, text=cardcontent_1[1], width=int(width * 0.02), height=int(height * 0.01), font=('Cambria', 12, 'bold'), command=lambda: id([2, 1]))
        bt4 = Button(gameView, text=cardcontent_2[1], width=int(width * 0.02), height=int(height * 0.01), font=('Cambria', 12, 'bold'), command=lambda: id([3, 1]))
        bt5 = Button(gameView, text=cardcontent_1[2], width=int(width * 0.02), height=int(height * 0.01), font=('Cambria', 12, 'bold'), command=lambda: id([4, 2]))
        bt6 = Button(gameView, text=cardcontent_2[2], width=int(width * 0.02), height=int(height * 0.01), font=('Cambria', 12, 'bold'), command=lambda: id([5, 2]))
        buttons = [bt1, bt2, bt3, bt4, bt5, bt6]
        buttons_copy = copy.copy(buttons)
        random.shuffle(buttons_copy)

        for index in range(0, 6):
            if index % 3 == 0:
                hgt = height * 0.1
            elif index % 3 == 1:
                hgt = height * 0.3
            else:
                hgt = height * 0.5

            if index % 2 == 0:
                wdt = width * 0.1
            else:
                wdt = width * 0.4

            buttons_copy[index].place(x=wdt, y=hgt)

    elif level == "median":
        gameView.geometry(f"{int(width * 0.8)}x{int(height * 0.85)}+{int(width * 0.1)}+{int(height * 0.05)}")

        bt1 = Button(gameView, text=cardcontent_1[0], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([0, 0]))
        bt2 = Button(gameView, text=cardcontent_2[0], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([1, 0]))
        bt3 = Button(gameView, text=cardcontent_1[1], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([2, 1]))
        bt4 = Button(gameView, text=cardcontent_2[1], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([3, 1]))
        bt5 = Button(gameView, text=cardcontent_1[2], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([4, 2]))
        bt6 = Button(gameView, text=cardcontent_2[2], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([5, 2]))
        bt7 = Button(gameView, text=cardContent_1[3], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([6, 3]))
        bt8 = Button(gameView, text=cardContent_2[3], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([7, 3]))
        bt9 = Button(gameView, text=cardContent_1[4], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([8, 4]))
        bt10 = Button(gameView, text=cardContent_2[4], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([9, 4]))
        bt11 = Button(gameView, text=cardContent_1[5], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([10, 5]))
        bt12 = Button(gameView, text=cardContent_2[5], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([11, 5]))

        buttons = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt10, bt11, bt12]
        buttons_copy = copy.copy(buttons)
        random.shuffle(buttons_copy)

        for index in range(0, len(buttons)):
            if index % 4 == 0:
                hgt = height * 0.1
            elif index % 4 == 1:
                hgt = height * 0.28
            elif index % 4 == 2:
                hgt = height * 0.46
            else:
                hgt = height * 0.64

            if index % 3 == 0:
                wdt = width * 0.05
            elif index % 3 == 1:
                wdt = width * 0.3
            else:
                wdt = width * 0.55

            buttons_copy[index].place(x=wdt, y=hgt)

    elif level == "hard":
        gameView.geometry(f"{width}x{height}")

        bt1 = Button(gameView, text=cardcontent_1[0], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([0, 0]))
        bt2 = Button(gameView, text=cardcontent_2[0], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([1, 0]))
        bt3 = Button(gameView, text=cardcontent_1[1], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([2, 1]))
        bt4 = Button(gameView, text=cardcontent_2[1], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([3, 1]))
        bt5 = Button(gameView, text=cardcontent_1[2], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([4, 2]))
        bt6 = Button(gameView, text=cardcontent_2[2], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([5, 2]))
        bt7 = Button(gameView, text=cardContent_1[3], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([6, 3]))
        bt8 = Button(gameView, text=cardContent_2[3], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([7, 3]))
        bt9 = Button(gameView, text=cardContent_1[4], width=int(width * 0.02), height=int(height * 0.01),
                     font=('Cambria', 12, 'bold'), command=lambda: id([8, 4]))
        bt10 = Button(gameView, text=cardContent_2[4], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([9, 4]))
        bt11 = Button(gameView, text=cardContent_1[5], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([10, 5]))
        bt12 = Button(gameView, text=cardContent_2[5], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([11, 5]))
        bt13 = Button(gameView, text=cardContent_1[6], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([12, 6]))
        bt14 = Button(gameView, text=cardContent_2[6], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([13, 6]))
        bt15 = Button(gameView, text=cardContent_1[7], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([14, 7]))
        bt16 = Button(gameView, text=cardContent_2[7], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([15, 7]))
        bt17 = Button(gameView, text=cardContent_1[8], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([16, 8]))
        bt18 = Button(gameView, text=cardContent_2[8], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([17, 8]))
        bt19 = Button(gameView, text=cardContent_1[9], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([18, 9]))
        bt20 = Button(gameView, text=cardContent_2[9], width=int(width * 0.02), height=int(height * 0.01),
                      font=('Cambria', 12, 'bold'), command=lambda: id([19, 9]))

        buttons = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt10,
                   bt11, bt12, bt13, bt14, bt15, bt16, bt17, bt18, bt19, bt20]

        buttons_copy = copy.copy(buttons)
        random.shuffle(buttons_copy)

        for index in range(0, len(buttons)):
            if index % 4 == 0:
                hgt = height * 0.1
            elif index % 4 == 1:
                hgt = height * 0.28
            elif index % 4 == 2:
                hgt = height * 0.46
            else:
                hgt = height * 0.64

            if index % 5 == 0:
                wdt = width * 0.03
            elif index % 5 == 1:
                wdt = width * 0.22
            elif index % 5 == 2:
                wdt = width * 0.41
            elif index % 5 == 3:
                wdt = width * 0.6
            else:
                wdt = width * 0.79

            buttons_copy[index].place(x=wdt, y=hgt)

    gameView.mainloop()


Button(root, text="Learn for a while", width=20, height=5, command=mode_learn).place(x=147, y=30)
Button(root, text="Play for a while", width=20, height=5, command=mode_play).place(x=147, y=150)

root.mainloop()




