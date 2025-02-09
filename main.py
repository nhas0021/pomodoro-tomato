from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#07689f"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button.after_cancel(timer)
    canvas.itemconfig(canvas_text, text = "00:00")
    tick_text_label.config(text = "")
    timer_text_label.config(text = "Title", fg = RED)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text_label.config(text="Break" ,fg = BLUE)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        timer_text_label.config(text="Break", fg = BLUE)
    else:
        count_down(work_sec)
        timer_text_label.config(text = "Work", fg= RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if len(str(count_sec)) < 2:
        canvas.itemconfig(canvas_text, text=f'{count_min}:0{count_sec}')
    else:
        canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer =  window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for i in range (math.floor(reps/2)):
            mark += "✔"
        if reps%2 == 0:
            tick_text_label.config(text=mark)
            window.attributes('-topmost', 1)

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.config(padx = 70, pady=40, bg= GREEN)
window.title("Pomodoro")

timer_text_label = Label(text = "Timer", font = ("Times new roman", 60, ), fg = RED, bg = GREEN)
timer_text_label.grid(column = 2, row =0)


tick_text_label = Label( font = ("ariel", 15, "bold"), fg = RED, bg = GREEN)
tick_text_label.place(x = 100, y=-20)


canvas = Canvas(width = 250, height = 250, bg = PINK, highlightthickness = 15)
tomato = PhotoImage(file= "tomato.png")
canvas.create_image(140,135,image = tomato)
canvas_text = canvas.create_text(140,160,text = "00:00", font=(FONT_NAME,35, "bold"), fill= "white")
canvas.grid(column = 2, row = 1)


start_button = Button(text="Start", width= 8, bg = PINK, font = (FONT_NAME, 8, "bold"),fg = YELLOW, command = start_timer)
start_button.place(x= -30, y= 60)

reset_button = Button(text="Reset", width= 8, bg= PINK, font = (FONT_NAME, 8, "bold"), fg = YELLOW, command = reset_timer)
reset_button.place(x= 245, y= 60)



window.mainloop()
