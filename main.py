from tkinter import *

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 0
timer = None


# TIMER RESET
def reset_pomodoro():
    window.after_cancel(timer)
    check_mark_label.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")
    label.config(text="Timer")
    global reps
    reps = 0


# TIMER MECHANISM

def start_timer():
    global reps
    reps += 1
    work_sec = 25 * 60
    short_break_sec = 5 * 60
    long_break_sec = 20 * 60
    if reps in [2, 4, 6]:
        label.config(text="Break")
        count_down(short_break_sec)
    elif reps == 8:
        label.config(text="Break")
        count_down(long_break_sec)
    elif reps in [1, 3, 5, 7]:
        label.config(text="Work")
        count_down(work_sec)


# COUNTDOWN MECHANISM

def count_down(count):
    global reps
    global timer
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    if count_min == 0:
        count_min = "00"
    if count_sec in range(1, 10):
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(int(reps / 2)):
            mark += "✔"
            check_mark_label.config(text=mark)


# UI SETUP

window = Tk()
window.title("POMODORO APP")
window.config(padx=50, pady=20, bg=YELLOW)

canvas = Canvas(width=202, height=225, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_image)
canvas_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 35, "normal"), foreground=RED, bg=YELLOW)
label.grid(column=1, row=0)

start_button = Button(text="Start", bg=GREEN, font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=GREEN, font=(FONT_NAME, 10, "bold"), command=reset_pomodoro)
reset_button.grid(column=2, row=2)

check_mark_label = Label(bg=YELLOW, foreground=GREEN, font="bold")
check_mark_label.grid(column=1, row=3)
check_mark_label.config(pady=20)
window.mainloop()
