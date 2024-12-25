import tkinter as tk
from exercises import workout_gen

workout = workout_gen()
print(workout)

window = tk.Tk()

window.title("Workout Generator")
window.geometry("500x400")  # Width x Height in pixels

workout = workout_gen()  
workout_text = " | ".join([f"{key}: {value}" for key, value in workout.items()])
print(workout_text)

label = tk.Label(window, text=workout_text, padx=10, pady=10, fg="black", bg="white")
label.pack()
window.mainloop()

