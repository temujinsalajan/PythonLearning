# Turtle Pong — smooth, single-file, polished
# (keeps your structure: same variable names & key handlers; adds levels, restart, UI)

import turtle, time, math, random

# ------------ Helpers ------------
def clamp(v, lo, hi): return max(lo, min(hi, v))

# ------------ Controls (keep your function names) ------------
def left_up():  left_rod.sety(clamp(left_rod.ycor()+PADDLE_STEP, -H+PADDLE_HH,  H-PADDLE_HH))
def left_down():left_rod.sety(clamp(left_rod.ycor()-PADDLE_STEP, -H+PADDLE_HH,  H-PADDLE_HH))
def right_up(): right_rod.sety(clamp(right_rod.ycor()+PADDLE_STEP,-H+PADDLE_HH, H-PADDLE_HH))
def right_down():right_rod.sety(clamp(right_rod.ycor()-PADDLE_STEP,-H+PADDLE_HH, H-PADDLE_HH))

def reset_ball(dir_to_right=True):
    global x_position, y_position, x_direction, y_direction, speed, rally, paused
    x_position, y_position = 0, 0
    angle = random.uniform(-35, 35)
    spd = BASE_SPEED + LEVEL_SPEED_BONUS*(level-1)
    x_direction =  spd*math.cos(math.radians(angle))*(1 if dir_to_right else -1)
    y_direction =  spd*math.sin(math.radians(angle))
    speed = spd
    rally = 0
    ball.goto(x_position, y_position)
    paused = True
    draw_banner(f"Level {level} — Press SPACE to start")

def point_scored(left_side_wins):
    global score_left, score_right, level
    if left_side_wins: score_left += 1
    else: score_right += 1
    update_score()
    draw_flash("SCORE!", 0.6)
    if score_left >= WIN_SCORE or score_right >= WIN_SCORE:
        game_over()
    else:
        reset_ball(dir_to_right=not left_side_wins)

def toggle_pause():
    global paused
    paused = not paused
    if paused: draw_banner("Paused — Press SPACE to resume")
    else:      clear_banner()

def restart():
    global score_left, score_right, level, game_running
    score_left = score_right = 0
    level = 1
    game_running = True
    update_score()
    draw_arena()
    reset_ball(dir_to_right=bool(random.getrandbits(1)))

# ------------ Drawing UI ------------
def draw_text_writer():
    t = turtle.Turtle(visible=False)
    t.penup(); t.color("#f8f8f2"); t.speed(0)
    return t

def draw_arena():
    bg.clear()
    # background gradient stripes
    stripe_h = 40
    for i, y in enumerate(range(-H, H, stripe_h)):
        bg.goto(-W, y); bg.color("#1e2a1f" if i%2==0 else "#213023")
        bg.begin_fill()
        for _ in range(2):
            bg.forward(2*W); bg.left(90); bg.forward(stripe_h); bg.left(90)
        bg.end_fill()

    # border
    border.clear()
    border.penup(); border.goto(-W, -H); border.pendown()
    border.color("#a6e3a1"); border.pensize(4)
    for _ in range(2):
        border.forward(2*W); border.left(90); border.forward(2*H); border.left(90)

    # center dashed line
    mid.clear()
    mid.color("#cdd6f4"); mid.pensize(6)
    mid.penup(); mid.goto(0, H-10); mid.setheading(270)
    for _ in range(20):
        mid.pendown(); mid.forward(2*H/40); mid.penup(); mid.forward(2*H/40)

    # title
    title_writer.clear()
    title_writer.goto(0, H+20)
    title_writer.write("Ping Pong (Turtle Edition)", align="center", font=("Arial", 24, "bold"))

def update_score():
    score_writer.clear()
    score_writer.goto(0, H-40)
    score_writer.write(f"{score_left}  :  {score_right}   |   Level {level}",
                       align="center", font=("Courier", 22, "bold"))

def draw_banner(msg):
    banner_writer.clear()
    banner_writer.goto(0, -H-35)
    banner_writer.write(msg, align="center", font=("Arial", 16, "normal"))

def clear_banner(): banner_writer.clear()

def draw_flash(msg, dur=0.4):
    flash_writer.clear()
    flash_writer.goto(0, 0)
    flash_writer.write(msg, align="center", font=("Arial", 36, "bold"))
    win.update(); time.sleep(dur)
    flash_writer.clear()

def game_over():
    global game_running, paused
    game_running = False
    paused = True
    winner = "Player 1 (Left)" if score_left > score_right else "Player 2 (Right)"
    draw_flash("GAME OVER", 1.0)
    banner_writer.clear()
    banner_writer.goto(0, -20)
    banner_writer.write(f"{winner} wins!  Press R to restart, Q to quit",
                        align="center", font=("Arial", 20, "bold"))

# ------------ Collision ------------
def paddle_collision(pad):
    # AABB check for better feel
    px, py = pad.xcor(), pad.ycor()
    bx, by = ball.xcor(), ball.ycor()
    if abs(bx - px) <= (PADDLE_HW + BALL_R) and abs(by - py) <= (PADDLE_HH + BALL_R):
        return True
    return False

def reflect_from_paddle(pad, is_left):
    global x_direction, y_direction, speed, rally, level
    offset = (ball.ycor() - pad.ycor()) / (PADDLE_HH)   # [-1, 1]
    angle = offset * 50  # add some spin/aim based on hit position
    spd = min(speed*1.05, MAX_SPEED)
    dir_sign = 1 if not is_left else -1  # after hit, ball goes away from paddle
    x_direction = dir_sign * spd * math.cos(math.radians(angle))
    y_direction = spd * math.sin(math.radians(angle))
    speed = spd
    rally += 1
    # Level up every N rallies
    if rally % RALLIES_PER_LEVEL == 0 and level < MAX_LEVEL:
        level += 1
        draw_flash(f"Level {level}!", 0.5)
        update_score()

# ------------ Setup ------------
win = turtle.Screen()
win.title('Ping pong with turtle')
win.bgcolor("#15251a")
win.setup(width=1200, height=800)     # fits most screens smoothly
win.tracer(0)

# world bounds
W, H = 560, 330             # half-width/half-height for play area (border drawn bigger visually)
MARGIN_X = W
MARGIN_Y = H

# paddles & ball sizes
PADDLE_W, PADDLE_H = 20, 130
PADDLE_HW, PADDLE_HH = PADDLE_W/2, PADDLE_H/2
BALL_R = 12

# speeds & levels
PADDLE_STEP = 40
BASE_SPEED = 5.0
MAX_SPEED = 18.0
LEVEL_SPEED_BONUS = 0.7
RALLIES_PER_LEVEL = 6
MAX_LEVEL = 10
WIN_SCORE = 7

# paddles
right_rod  = turtle.Turtle('square'); right_rod.penup();  right_rod.color('#ff6b6b')
right_rod.shapesize(stretch_wid=PADDLE_W/20, stretch_len=PADDLE_H/20); right_rod.setheading(90)
right_rod.goto(-MARGIN_X+40, 0)

left_rod = turtle.Turtle('square'); left_rod.penup(); left_rod.color('#74c0fc')
left_rod.shapesize(stretch_wid=PADDLE_W/20, stretch_len=PADDLE_H/20); left_rod.setheading(90)
left_rod.goto( MARGIN_X-40, 0)

# ball
ball = turtle.Turtle('circle'); ball.penup(); ball.color("#f8f8f2")
ball.shapesize(stretch_wid=BALL_R/10, stretch_len=BALL_R/10)

# writers
bg = turtle.Turtle(visible=False); bg.speed(0); bg.penup()
border = turtle.Turtle(visible=False); border.speed(0)
mid = turtle.Turtle(visible=False); mid.speed(0)
title_writer = draw_text_writer()
score_writer = draw_text_writer()
banner_writer = draw_text_writer()
flash_writer = draw_text_writer()

draw_arena()

# input
win.listen()
win.onkeypress(left_up,'w');    win.onkeypress(left_down,'s')
win.onkeypress(right_up,'Up');  win.onkeypress(right_down,'Down')
win.onkeypress(toggle_pause, 'space')
win.onkeypress(restart, 'r')
win.onkeypress(lambda: win.bye(), 'q')

# game state
score_left = score_right = 0
level = 1
update_score()
x_position, y_position = 0, 0
x_direction = y_direction = 0.0
speed = BASE_SPEED
rally = 0
game_running = True
paused = True
draw_banner("Controls: W/S & ↑/↓  |  SPACE pause  |  R restart  |  Q quit")
reset_ball(dir_to_right=bool(random.getrandbits(1)))

# ------------ Main Loop ------------
prev = time.perf_counter()
while True:
    now = time.perf_counter()
    dt = clamp(now - prev, 0, 0.03)    # cap dt for stability
    prev = now

    if game_running and not paused:
        # move ball
        x_position += x_direction * dt * 60
        y_position += y_direction * dt * 60
        ball.goto(x_position, y_position)

        # top/bottom collision
        if ball.ycor() >= (MARGIN_Y - BALL_R):
            y_direction = -abs(y_direction)
            ball.sety(MARGIN_Y - BALL_R)
        elif ball.ycor() <= -(MARGIN_Y - BALL_R):
            y_direction = abs(y_direction)
            ball.sety(-(MARGIN_Y - BALL_R))

        # left/right score
        if ball.xcor() >  MARGIN_X + 30:
            point_scored(left_side_wins=True)
        elif ball.xcor() < -MARGIN_X - 30:
            point_scored(left_side_wins=False)

        # paddle collisions (use x proximity to avoid back-face sticking)
        if ball.xcor() < left_rod.xcor() + PADDLE_HW + BALL_R + 2 and ball.xcor() > left_rod.xcor():
            if paddle_collision(left_rod): reflect_from_paddle(left_rod, is_left=True)
        if ball.xcor() > right_rod.xcor() - PADDLE_HW - BALL_R - 2 and ball.xcor() < right_rod.xcor():
            if paddle_collision(right_rod): reflect_from_paddle(right_rod, is_left=False)

    win.update()

turtle.done()
