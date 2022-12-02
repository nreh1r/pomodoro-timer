from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    text_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        text_timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        text_timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        text_timer.config(text="Work")
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Enter the canvas you want to update and then what you want to change as a kwarg
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check.config(text=f"{'✔' * (reps // 2)}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,
              )

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# Half width and half height to center the imgage
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Timer
text_timer = Label(text="Timer", fg=GREEN, bg=YELLOW,
                   font=(FONT_NAME, 50))
text_timer.grid(row=0, column=1)

# Start button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

# Stop button
stop = Button(text="Stop", highlightthickness=0, command=reset_timer)
stop.grid(row=2, column=2)

# Check mark
check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)


window.mainloop()
