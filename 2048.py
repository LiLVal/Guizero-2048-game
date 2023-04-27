# Add a reset board button
# Fix bug with tiles on top of eachother
from guizero import App, Waffle, PushButton
from random import randint, choice


game_tiles = {"2": "#eee4da", "4": "#f4d8a5", "8": "#eca467", "16": "#f69360",\
"32": "#eb6648", "64": "#f94015", "128": "#edcf73", "256": "#edc22d", "512": "#7bc2f3", "1024": "#49adf3", "2048": "#fdc5ed" }
two_or_four = {"2": "#eee4da", "4": "#f4d8a5"}

board_array = [[None, None, None, None],
               [None, None, None, None],
               [None, None, None, None],
               [None, None, None, None]]

def move_tiles_left():
    #for loop for to check all rows for items in 2D array
    for row in range(4):
    #idx will retrive index of every None value in each row
    #None values are deleted and added at the end of row
        idx = [i for i, x in enumerate(board_array[row]) if x == None]
        for index in sorted(idx, reverse=True):
            del board_array[row][index]
            board_array[row].append(None)
    #waffle tiles are set to white and update board routine
    #is called
    waffle.set_all("White")
    update_board_left_right()
    add_tile()

def move_tiles_right():
    for row in range(4):
        idx = [i for i, x in enumerate(board_array[row]) if x == None]
        for index in sorted(idx, reverse=True):
            del board_array[row][index]
            board_array[row].append(None)
    #after None is append to end of row it is reversed
        board_array[row].reverse()

    waffle.set_all("White")
    update_board_left_right()
    add_tile()

def move_tiles_up():
    for row in range(4):
        idx = [i for i, x in enumerate(board_array[row]) if x == None]
        for index in sorted(idx, reverse=True):
            del board_array[row][index]
            board_array[row].append(None)

    waffle.set_all("White")
    update_board_up_down()
    add_tile()

def move_tiles_down():
    for row in range(4):
        idx = [i for i, x in enumerate(board_array[row]) if x == None]
        for index in sorted(idx, reverse=True):
            del board_array[row][index]
            board_array[row].append(None)
        board_array[row].reverse()
    print(board_array)
    waffle.set_all("White")
    update_board_up_down()
    add_tile()

def update_board_left_right():
    for y in range(4):
        for x in range(4):
            if board_array[x][y] != None:
                waffle.pixel(x=y, y=x).color = board_array[x][y]

def update_board_up_down():
    for y in range(4):
        for x in range(4):
            if board_array[x][y] != None:
                waffle.pixel(x=x, y=y).color = board_array[x][y]

def add_tile():
    x = randint(0, 3)
    y = randint(0, 3)
    waffle.pixel(x= x, y= y).color = choice(list(two_or_four.values()))
    board_array[x][y] = choice(list(two_or_four.values()))

def new_board():
    for i in range(2):
        random_axis = randint(0, 3)
        waffle.pixel(x= random_axis, y= random_axis).color = game_tiles["2"]
        board_array[random_axis][random_axis] = game_tiles["2"]
    PushButton(window, text="↑", command=move_tiles_up)
    PushButton(window, text="↓", command=move_tiles_down, align="bottom")
    PushButton(window, text="←", command=move_tiles_left, align="left")
    PushButton(window, text="→", command=move_tiles_right, align="right")


window = App("2048", width = 200, height = 230)
waffle = Waffle(window, height = 4, width = 4)
new_board()
window.display()
