import tkinter as tk

root = tk.Tk()
root.title("Colorful House")
root.geometry("600x450")

canvas = tk.Canvas(root, width=550, height=360, bg="lightblue")
canvas.pack()

# Sun
canvas.create_oval(430, 20, 490, 80, fill="yellow", outline="orange")

# House body
canvas.create_rectangle(150, 170, 380, 330, fill="lightyellow")

# Roof
canvas.create_polygon(120, 170, 265, 60, 410, 170,
                      fill="red", outline="black")

# Door
canvas.create_rectangle(240, 250, 290, 330, fill="brown")

# Windows
canvas.create_rectangle(175, 200, 220, 240, fill="lightblue")
canvas.create_rectangle(310, 200, 355, 240, fill="lightblue")

# Window frames
canvas.create_line(197, 200, 197, 240, fill="black", width=2)
canvas.create_line(175, 220, 220, 220, fill="black", width=2)
canvas.create_line(332, 200, 332, 240, fill="black", width=2)
canvas.create_line(310, 220, 355, 220, fill="black", width=2)

# Grass
canvas.create_rectangle(0, 330, 550, 360, fill="green", outline="green")

# House name
canvas.create_text(265, 345, text="My House",
                   font=("Arial", 12, "bold"), fill="white")

root.mainloop()