import random
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
wn.tracer(0)

tim = turtle.Turtle()

tim.color('blue', 'purple')
tim.begin_fill()
tim.speed(0)


def my_tree(tree, recursion_number):
    output = ""
    X_1_11random = []
    for i in range(40):
        X_1_11random.append("1")
    for i in range(40):
        X_1_11random.append("11")
    for i in range(20):
        X_1_11random.append("X")

    for i in range(len(tree)):
        if tree[i] == "1":

            output = output + random.choice(X_1_11random)

        elif tree[i] == "0":
            output += "1[0]0"
, "10[0]"
        elif tree[i] == "X":
            output += random.choice(["^0|"])


        else:
            output += tree[i]

    if recursion_number == 0:
        return output
    else:
        output = my_tree(output, recursion_number - 1)
        return output


def draw_my_tree(recursion_depth, tim_distance):
    path = my_tree("0", recursion_depth)
    print(path)
    saved_states = []
    for i in range(len(path)):
        if path[i] == "1":
            tim.forward(tim_distance)

        elif path[i] == "0":
            tim.color("green")
            tim.forward(tim_distance)
            tim.color("blue")

        elif path[i] == "X":
            tim.color("red")
            tim.forward(tim_distance)
            tim.color("blue")

        elif path[i] == "[":
            saved_states.append(get_turtle_state(tim))
            tim.left(random.choice([10, 10, 15, 15, 20, 20, 30, 35, 40]))

        elif path[i] == "]":
            tim.penup()
            restore_turtle_state(tim, saved_states[-1])
            tim.pendown()
            del saved_states[-1]
            tim.right(random.choice([10, 10, 10, 10, 10, 20, 20, 20, 30, 35, 40]))


        elif path[i] == "|":
            tim.penup()
            restore_turtle_state(tim, saved_states[-1])
            tim.pendown()
            del saved_states[-1]

        elif path[i] == "^":
            saved_states.append(get_turtle_state(tim))
            tim.left(random.randint(-30, 30))


def fractal_tree(tree, recursion_number):
    output = ""
    for i in range(len(tree)):
        # print(f"tree[i] = {tree[i]}")
        if tree[i] == "1":
            output = output + "11"

        elif tree[i] == "0":
            output += "1[0]0"

        elif tree[i] == "]":
            output = output + "]"

        elif tree[i] == "[":
            output = output + "["

    if recursion_number == 0:
        return output
    else:
        output = fractal_tree(output, recursion_number - 1)
        return output


def draw_fractal_tree(recursion_depth, tim_distance):
    path = fractal_tree("0", recursion_depth)
    print(path)
    saved_states = []
    for i in range(len(path)):
        if path[i] == "1":
            tim.forward(tim_distance)

        elif path[i] == "0":
            tim.color("green")
            tim.forward(tim_distance)
            tim.color("blue")

        elif path[i] == "[":
            saved_states.append(get_turtle_state(tim))
            tim.left(45)

        elif path[i] == "]":
            tim.penup()
            restore_turtle_state(tim, saved_states[-1])
            tim.pendown()
            del saved_states[-1]
            tim.right(45)


def get_turtle_state(_turtle):
    return _turtle.heading(), _turtle.position()


def restore_turtle_state(_turtle, state):
    _turtle.setheading(state[0])
    _turtle.setposition(state[1][0], state[1][1])


tim.left(90)
tim.penup()
tim.backward(400)
tim.pendown()
draw_my_tree(11, 6)
wn.update()

turtle.done()
