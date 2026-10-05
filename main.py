import tkinter as tk

root = tk.Tk()
root.title("Colorful House")
root.geometry("600x450")

canvas = tk.Canvas(root, width=550, height=360, bg="lightblue")
canvas.pack()

# Sun
canvas.create_oval(430, 20, 490, 80, fill="yellow", outline="orange")

# Main House Body
canvas.create_rectangle(150, 170, 380, 330, fill="lightyellow")

# Main House Roof
canvas.create_polygon(120, 170, 265, 60, 410, 170,
                      fill="red", outline="black")

# Door
canvas.create_rectangle(240, 250, 290, 330, fill="brown")

# Windows
canvas.create_rectangle(175, 200, 220, 240, fill="lightblue")
canvas.create_rectangle(310, 200, 355, 240, fill="lightblue")

# Window Frames
canvas.create_line(197, 200, 197, 240, fill="black", width=2)
canvas.create_line(175, 220, 220, 220, fill="black", width=2)
canvas.create_line(332, 200, 332, 240, fill="black", width=2)
canvas.create_line(310, 220, 355, 220, fill="black", width=2)

# Dog House Body
canvas.create_rectangle(400, 270, 500, 330, fill="orange")

# Dog House Roof
canvas.create_polygon(385, 270, 450, 220, 515, 270,
                      fill="brown", outline="black")

# Dog House Door
canvas.create_oval(425, 285, 475, 335, fill="black")

# Small Dog House Label
canvas.create_text(450, 345, text="Dog House",
                   font=("Arial", 10, "bold"), fill="black")

# Grass
canvas.create_rectangle(0, 330, 550, 360,
                        fill="green", outline="green")

# House Name
canvas.create_text(265, 345, text="My Colorful House",
                   font=("Arial", 12, "bold"), fill="white")

root.mainloop()