import tkinter as tk

root = tk.Tk()
root.title("Cartoon Animated House")
root.geometry("700x500")

canvas = tk.Canvas(root, width=650, height=420, bg="skyblue")
canvas.pack()

# ---------------- SUN ----------------
sun = canvas.create_oval(520, 40, 590, 110,
                         fill="yellow", outline="orange", width=3)

# ---------------- CLOUD ----------------
cloud1 = canvas.create_oval(50, 60, 110, 100, fill="white", outline="white")
cloud2 = canvas.create_oval(80, 45, 150, 100, fill="white", outline="white")
cloud3 = canvas.create_oval(120, 60, 180, 100, fill="white", outline="white")

# ---------------- HOUSE ----------------

# House body
canvas.create_rectangle(180, 200, 450, 370,
                        fill="lightyellow", outline="black", width=3)

# Roof
canvas.create_polygon(150, 200, 315, 80, 480, 200,
                      fill="red", outline="black", width=3)

# Door
door = canvas.create_rectangle(285, 275, 345, 370,
                               fill="blue", outline="black", width=3)

# Door knob
knob = canvas.create_oval(330, 320, 338, 328,
                          fill="yellow", outline="black")

# Windows
canvas.create_rectangle(205, 235, 255, 285,
                        fill="lightblue", outline="black", width=3)

canvas.create_rectangle(375, 235, 425, 285,
                        fill="lightblue", outline="black", width=3)

# Window lines
canvas.create_line(230, 235, 230, 285, width=2)
canvas.create_line(205, 260, 255, 260, width=2)

canvas.create_line(400, 235, 400, 285, width=2)
canvas.create_line(375, 260, 425, 260, width=2)

# Chimney
canvas.create_rectangle(380, 120, 420, 180,
                        fill="brown", outline="black", width=3)

# Grass
canvas.create_rectangle(0, 370, 650, 420,
                        fill="green", outline="green")

# Flowers
canvas.create_oval(80, 380, 90, 390, fill="pink")
canvas.create_oval(95, 375, 105, 385, fill="yellow")
canvas.create_oval(530, 385, 540, 395, fill="pink")

# Title
canvas.create_text(315, 405,
                   text="My Cartoon House",
                   font=("Arial", 16, "bold"),
                   fill="white")


# ---------------- ANIMATION ----------------

cloud_speed = 2
sun_speed = 1
door_open = False


def animate_cloud():
    global cloud_speed

    canvas.move(cloud1, cloud_speed, 0)
    canvas.move(cloud2, cloud_speed, 0)
    canvas.move(cloud3, cloud_speed, 0)

    # Reset cloud when it leaves screen
    position = canvas.coords(cloud1)

    if position[0] > 650:
        canvas.move(cloud1, -700, 0)
        canvas.move(cloud2, -700, 0)
        canvas.move(cloud3, -700, 0)

    root.after(30, animate_cloud)


def animate_sun():
    global sun_speed

    canvas.move(sun, 0, sun_speed)

    position = canvas.coords(sun)

    if position[1] > 120 or position[1] < 30:
        sun_speed = -sun_speed

    root.after(50, animate_sun)


def open_door():
    global door_open

    if not door_open:
        canvas.itemconfig(door, fill="darkblue")
        canvas.itemconfig(knob, fill="white")
        door_open = True
    else:
        canvas.itemconfig(door, fill="blue")
        canvas.itemconfig(knob, fill="yellow")
        door_open = False

    root.after(1000, open_door)


# Start animations
animate_cloud()
animate_sun()
open_door()

# ---------------- CARTOON CAT ----------------

# Cat body
canvas.create_oval(500, 270, 570, 350,
                   fill="royalblue", outline="black", width=3)

# Cat head
canvas.create_oval(490, 220, 580, 300,
                   fill="royalblue", outline="black", width=3)

# Ears
canvas.create_polygon(495, 235, 505, 195, 530, 225,
                      fill="royalblue", outline="black", width=3)

canvas.create_polygon(540, 225, 565, 195, 575, 240,
                      fill="royalblue", outline="black", width=3)

# Eyes
canvas.create_oval(510, 240, 525, 255, fill="white", outline="black")
canvas.create_oval(545, 240, 560, 255, fill="white", outline="black")

# Pupils
canvas.create_oval(515, 243, 522, 252, fill="black")
canvas.create_oval(550, 243, 557, 252, fill="black")

# Nose
canvas.create_oval(532, 258, 540, 265, fill="pink", outline="black")

# Mouth
canvas.create_arc(520, 255, 550, 280,
                  start=200, extent=140, width=2)

# Whiskers
canvas.create_line(505, 265, 475, 255, width=2)
canvas.create_line(505, 270, 475, 270, width=2)
canvas.create_line(565, 265, 595, 255, width=2)
canvas.create_line(565, 270, 595, 270, width=2)

# Arms
canvas.create_line(505, 295, 475, 315, width=8)
canvas.create_line(565, 295, 595, 315, width=8)

# Legs
canvas.create_line(520, 340, 515, 370, width=8)
canvas.create_line(550, 340, 555, 370, width=8)

# Tail
canvas.create_line(570, 325, 610, 300, 620, 320,
                   smooth=True, width=7)

# Character name
canvas.create_text(535, 390,
                   text="Funny Cat",
                   font=("Arial", 12, "bold"),
                   fill="white")

root.mainloop()