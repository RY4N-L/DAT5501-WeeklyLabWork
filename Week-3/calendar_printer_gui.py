import tkinter as tk
from tkinter import messagebox

days_dict = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 0
}

def generate_calendar():
    try:
        days_in_month = int(days_entry.get())
        starting_day = day_entry.get().lower()
        gaps_to_leave = days_dict[starting_day]
    except ValueError:
        messagebox.showerror("Invalid Input, please enter a valid number of days.")
        return
    except KeyError:
        messagebox.showerror("Invalid Day, please enter a valid day of the week.")
        return

    for widget in calendar_frame.winfo_children():
        widget.destroy()

    headers = ["S", "M", "T", "W", "T", "F", "S"]
    for i, day in enumerate(headers):
        tk.Label(calendar_frame, text=day, width=5, borderwidth=1, relief="solid").grid(row=0, column=i)

    row = 1
    col = gaps_to_leave
    for day in range(1, days_in_month + 1):
        tk.Label(calendar_frame, text=str(day), width=5, borderwidth=1, relief="solid").grid(row=row, column=col)
        col += 1
        if col > 6:
            col = 0
            row += 1

# GUI setup
root = tk.Tk()
root.title("Calendar Printer")

tk.Label(root, text="Number of days in month:").pack()
days_entry = tk.Entry(root)
days_entry.pack()

tk.Label(root, text="Starting day of the week:").pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Button(root, text="Generate Calendar", command=generate_calendar).pack(pady=10)

calendar_frame = tk.Frame(root)
calendar_frame.pack()

root.mainloop()
