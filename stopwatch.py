# "Stopwatch: The Game"

# Click start, stop, and reset buttons to start, stop, and reset the stopwatch. 
# Score one point every time the timer is stopped on .0 seconds. 
# Counter tracks total attempts.

import simplegui

# define global variables
a = 0 	# minutes
b = 0	# tens of seconds
c = 0	# ones of seconds
d = 0	# tenths of seconds

x_wins = 0	# number of times counter stopped on a whole second (1.0, 2.0, 3.0, etc.).
y_attempts = 0	# total number of times counter stopped


#timer_interval = 1000 # In milliseconds (1000 ms = 1 s)
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d
    
    a = t // 600
    b = t // 10 % 60 // 10
    c = t // 10 % 60 % 10
    d = t % 10
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global running
    timer.start()
    
def stop_timer():
    global x_wins, y_attempts
    if timer.is_running():
        timer.stop()
    
        y_attempts = y_attempts + 1
        if d == 0:
           x_wins = x_wins + 1
        else:
            return
    else:
        return
    
# reset time, a, b, c, d, x_wins, y_attempts to zero
def reset():
    global time
    global a, b, c, d
    global x_wins, y_attempts
    time = 0
    a = 0
    b = 0
    c = 0
    d = 0
    y_attempts = 0
    x_wins = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    
    time = time + 1
    format(time)

# define draw handler for stopwatch and scoreboard
def draw(canvas):    
    canvas.draw_text(str(a) + ":" + str(b) + str(c) + "." + str(d), (100, 100), 24, "White")
    canvas.draw_text(str(x_wins) + "/" + str(y_attempts), [200, 30], 24, "Blue")

# create frame
frame = simplegui.create_frame("Stopwatch", 250, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler) #change this back to 100
frame.add_button("Start", start_timer)
frame.add_button("Stop", stop_timer)
frame.add_button("Reset", reset)

# start frame
frame.start()
