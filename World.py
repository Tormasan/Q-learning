from Tkinter import *
master = Tk()

triangle_size = 0.1
cell_score_min = -0.2
cell_score_max = 0.2
Width = 30
(x, y) = (45, 21)
actions = ["up", "down", "left", "right"]

board = Canvas(master, width=x*Width, height=y*Width)
player = (0, y-1)
score = 1
restart = False
walk_reward = -0.04

walls = [
(0, 2),
(0, 3),
(0, 4),
(0, 5),
(0, 6),
(0, 7),
(0, 8),
(0, 9),
(0, 10),
(0, 11),
(0, 12),
(0, 13),
(0, 14),
(0, 15),
(0, 16),
(0, 17),
(0, 18),
(1, 0),
(1, 20),
(2, 0),
(2, 1),
(2, 2),
(2, 4),
(2, 5),
(2, 6),
(2, 8),
(2, 9),
(2, 10),
(2, 11),
(2, 12),
(2, 14),
(2, 15),
(2, 16),
(2, 18),
(2, 19),
(2, 20),
(3, 0),
(3, 2),
(3, 4),
(3, 6),
(3, 8),
(3, 12),
(3, 16),
(3, 20),
(4, 0),
(4, 2),
(4, 4),
(4, 6),
(4, 7),
(4, 8),
(4, 10),
(4, 11),
(4, 12),
(4, 14),
(4, 16),
(4, 17),
(4, 18),
(4, 20),
(5, 0),
(5, 2),
(5, 4),
(5, 14),
(5, 18),
(5, 20),
(6, 0),
(6, 2),
(6, 4),
(6, 6),
(6, 7),
(6, 8),
(6, 10),
(6, 11),
(6, 12),
(6, 13),
(6, 14),
(6, 15),
(6, 16),
(6, 18),
(6, 20),
(7, 0),
(7, 2),
(7, 4),
(7, 6),
(7, 8),
(7, 16),
(7, 18),
(7, 20),
(8, 0),
(8, 2),
(8, 4),
(8, 5),
(8, 6),
(8, 8),
(8, 9),
(8, 10),
(8, 12),
(8, 14),
(8, 15),
(8, 16),
(8, 18),
(8, 20),
(9, 0),
(9, 10),
(9, 12),
(9, 14),
(9, 18),
(9, 20),
(10, 0),
(10, 2),
(10, 3),
(10, 4),
(10, 6),
(10, 7),
(10, 8),
(10, 9),
(10, 10),
(10, 12),
(10, 13),
(10, 14),
(10, 16),
(10, 18),
(10, 20),
(11, 0),
(11, 2),
(11, 4),
(11, 6),
(11, 10),
(11, 16),
(11, 18),
(11, 20),
(12, 0),
(12, 2),
(12, 4),
(12, 5),
(12, 6),
(12, 7),
(12, 8),
(12, 10),
(12, 12),
(12, 13),
(12, 14),
(12, 15),
(12, 16),
(12, 17),
(12, 18),
(12, 20),
(13, 0),
(13, 2),
(13, 8),
(13, 10),
(13, 12),
(13, 16),
(13, 18),
(13, 20),
(14, 0),
(14, 2),
(14, 3),
(14, 4),
(14, 5),
(14, 6),
(14, 8),
(14, 10),
(14, 12),
(14, 14),
(14, 15),
(14, 16),
(14, 18),
(14, 20),
(15, 0),
(15, 6),
(15, 8),
(15, 12),
(15, 14),
(15, 20),
(16, 0),
(16, 2),
(16, 3),
(16, 4),
(16, 6),
(16, 8),
(16, 10),
(16, 11),
(16, 12),
(16, 14),
(16, 15),
(16, 16),
(16, 17),
(16, 18),
(16, 20),
(17, 0),
(17, 2),
(17, 6),
(17, 8),
(17, 10),
(17, 18),
(17, 20),
(18, 0),
(18, 2),
(18, 3),
(18, 4),
(18, 6),
(18, 8),
(18, 10),
(18, 11),
(18, 12),
(18, 14),
(18, 16),
(18, 17),
(18, 18),
(18, 20),
(19, 0),
(19, 6),
(19, 12),
(19, 14),
(19, 16),
(19, 20),
(20, 0),
(20, 2),
(20, 3),
(20, 4),
(20, 6),
(20, 7),
(20, 8),
(20, 10),
(20, 11),
(20, 12),
(20, 14),
(20, 16),
(20, 17),
(20, 18),
(20, 20),
(21, 0),
(21, 2),
(21, 6),
(21, 8),
(21, 10),
(21, 12),
(21, 14),
(21, 20),
(22, 0),
(22, 2),
(22, 3),
(22, 4),
(22, 6),
(22, 8),
(22, 10),
(22, 12),
(22, 14),
(22, 15),
(22, 16),
(22, 17),
(22, 18),
(22, 20),
(23, 0),
(23, 2),
(23, 4),
(23, 6),
(23, 8),
(23, 10),
(23, 14),
(23, 18),
(23, 20),
(24, 0),
(24, 2),
(24, 4),
(24, 6),
(24, 8),
(24, 10),
(24, 11),
(24, 12),
(24, 13),
(24, 14),
(24, 16),
(24, 17),
(24, 18),
(24, 20),
(25, 0),
(25, 2),
(25, 4),
(25, 8),
(25, 16),
(25, 20),
(26, 0),
(26, 2),
(26, 4),
(26, 5),
(26, 6),
(26, 8),
(26, 10),
(26, 11),
(26, 12),
(26, 14),
(26, 15),
(26, 16),
(26, 17),
(26, 18),
(26, 20),
(27, 0),
(27, 2),
(27, 6),
(27, 8),
(27, 12),
(27, 18),
(27, 20),
(28, 0),
(28, 2),
(28, 4),
(28, 5),
(28, 6),
(28, 8),
(28, 9),
(28, 10),
(28, 11),
(28, 12),
(28, 14),
(28, 15),
(28, 16),
(28, 17),
(28, 18),
(28, 20),
(29, 0),
(29, 4),
(29, 14),
(29, 20),
(30, 0),
(30, 2),
(30, 3),
(30, 4),
(30, 6),
(30, 7),
(30, 8),
(30, 10),
(30, 11),
(30, 12),
(30, 14),
(30, 15),
(30, 16),
(30, 18),
(30, 20),
(31, 0),
(31, 2),
(31, 6),
(31, 10),
(31, 12),
(31, 16),
(31, 18),
(31, 20),
(32, 0),
(32, 2),
(32, 4),
(32, 6),
(32, 7),
(32, 8),
(32, 9),
(32, 10),
(32, 12),
(32, 14),
(32, 15),
(32, 16),
(32, 18),
(32, 20),
(33, 0),
(33, 2),
(33, 4),
(33, 12),
(33, 14),
(33, 18),
(33, 20),
(34, 0),
(34, 2),
(34, 3),
(34, 4),
(34, 6),
(34, 8),
(34, 9),
(34, 10),
(34, 12),
(34, 14),
(34, 15),
(34, 16),
(34, 18),
(34, 20),
(35, 0),
(35, 6),
(35, 8),
(35, 16),
(35, 18),
(35, 20),
(36, 0),
(36, 2),
(36, 3),
(36, 4),
(36, 5),
(36, 6),
(36, 8),
(36, 9),
(36, 10),
(36, 11),
(36, 12),
(36, 13),
(36, 14),
(36, 15),
(36, 16),
(36, 18),
(36, 20),
(37, 0),
(37, 2),
(37, 12),
(37, 16),
(37, 18),
(37, 20),
(38, 0),
(38, 2),
(38, 3),
(38, 4),
(38, 6),
(38, 7),
(38, 8),
(38, 10),
(38, 11),
(38, 12),
(38, 14),
(38, 16),
(38, 18),
(38, 20),
(39, 0),
(39, 2),
(39, 6),
(39, 8),
(39, 10),
(39, 14),
(39, 16),
(39, 18),
(39, 20),
(40, 0),
(40, 2),
(40, 3),
(40, 4),
(40, 6),
(40, 8),
(40, 10),
(40, 11),
(40, 12),
(40, 14),
(40, 15),
(40, 16),
(40, 18),
(40, 20),
(41, 0),
(41, 4),
(41, 6),
(41, 8),
(41, 12),
(41, 18),
(41, 20),
(42, 0),
(42, 2),
(42, 4),
(42, 5),
(42, 6),
(42, 8),
(42, 9),
(42, 10),
(42, 12),
(42, 13),
(42, 14),
(42, 15),
(42, 16),
(42, 17),
(42, 18),
(42, 20),
(43, 0),
(43, 2),
(43, 20),
(44, 0),
(44, 1),
(44, 2),
(44, 3),
(44, 4),
(44, 5),
(44, 6),
(44, 7),
(44, 8),
(44, 9),
(44, 10),
(44, 11),
(44, 12),
(44, 13),
(44, 14),
(44, 15),
(44, 16),
(44, 17),
(44, 18),
(44, 19),
(44, 20),

]
specials = [(4, 1, "red", -1), (23, 11, "green", 1),(3, 1, "red", -1),(8, 2,"green" ,1),(1,0,"green",1)]
cell_scores = {}


def create_triangle(i, j, action):
    if action == actions[0]:
        return board.create_polygon((i+0.5-triangle_size)*Width, (j+triangle_size)*Width,
                                    (i+0.5+triangle_size)*Width, (j+triangle_size)*Width,
                                    (i+0.5)*Width, j*Width,
                                    fill="white", width=1)
    elif action == actions[1]:
        return board.create_polygon((i+0.5-triangle_size)*Width, (j+1-triangle_size)*Width,
                                    (i+0.5+triangle_size)*Width, (j+1-triangle_size)*Width,
                                    (i+0.5)*Width, (j+1)*Width,
                                    fill="white", width=1)
    elif action == actions[2]:
        return board.create_polygon((i+triangle_size)*Width, (j+0.5-triangle_size)*Width,
                                    (i+triangle_size)*Width, (j+0.5+triangle_size)*Width,
                                    i*Width, (j+0.5)*Width,
                                    fill="white", width=1)
    elif action == actions[3]:
        return board.create_polygon((i+1-triangle_size)*Width, (j+0.5-triangle_size)*Width,
                                    (i+1-triangle_size)*Width, (j+0.5+triangle_size)*Width,
                                    (i+1)*Width, (j+0.5)*Width,
                                    fill="white", width=1)


def render_grid():
    global specials, walls, Width, x, y, player
    for i in range(x):
        for j in range(y):
            board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill="white", width=1)
            temp = {}
            for action in actions:
                temp[action] = create_triangle(i, j, action)
            cell_scores[(i,j)] = temp
    for (i, j, c, w) in specials:
        board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill=c, width=1)
    for (i, j) in walls:
        board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill="black", width=1)

render_grid()


def set_cell_score(state, action, val):
    global cell_score_min, cell_score_max
    triangle = cell_scores[state][action]
    green_dec = int(min(255, max(0, (val - cell_score_min) * 255.0 / (cell_score_max - cell_score_min))))
    green = hex(green_dec)[2:]
    red = hex(255-green_dec)[2:]
    if len(red) == 1:
        red += "0"
    if len(green) == 1:
        green += "0"
    color = "#" + red + green + "00"
    board.itemconfigure(triangle, fill=color)


def try_move(dx, dy):
    global player, x, y, score, walk_reward, me, restart
    if restart == True:
        restart_game()
    new_x = player[0] + dx
    new_y = player[1] + dy
    score += walk_reward
    if (new_x >= 0) and (new_x < x) and (new_y >= 0) and (new_y < y) and not ((new_x, new_y) in walls):
        board.coords(me, new_x*Width+Width*2/10, new_y*Width+Width*2/10, new_x*Width+Width*8/10, new_y*Width+Width*8/10)
        player = (new_x, new_y)
    for (i, j, c, w) in specials:
        if new_x == i and new_y == j:
            score -= walk_reward
            score += w
            if score > 0:
                print "Success! score: ", score
            else:
                print "Fail! score: ", score
            restart = True
            return
    #print "score: ", score


def call_up(event):
    try_move(0, -1)


def call_down(event):
    try_move(0, 1)


def call_left(event):
    try_move(-1, 0)


def call_right(event):
    try_move(1, 0)


def restart_game():
    global player, score, me, restart
    player = (0, y-1)
    score = 1
    restart = False
    board.coords(me, player[0]*Width+Width*2/10, player[1]*Width+Width*2/10, player[0]*Width+Width*8/10, player[1]*Width+Width*8/10)

def has_restarted():
    return restart

master.bind("<Up>", call_up)
master.bind("<Down>", call_down)
master.bind("<Right>", call_right)
master.bind("<Left>", call_left)

me = board.create_rectangle(player[0]*Width+Width*2/10, player[1]*Width+Width*2/10,
                            player[0]*Width+Width*8/10, player[1]*Width+Width*8/10, fill="orange", width=1, tag="me")

board.grid(row=1, column=0)


def start_game():
    master.mainloop()
