import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
wn.tracer(0)

tim = turtle.Turtle()

tim.color('blue', 'purple')
tim.begin_fill()
tim.speed(0)


def fractal_tree(tree, recursion_number):
    output = ""
    for i in range(len(tree)):
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
draw_fractal_tree(7, 3)
wn.update()

turtle.done()
