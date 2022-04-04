import random
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
wn.tracer(1)  #

tim = turtle.Turtle()

tim.color('blue', 'purple')
tim.speed(2)


def is_number(possibleNumber):
    try:
        int(possibleNumber)
    except:
        return False
    return True


def my_tree(tree, recursion_number):
    output = ""
    skip_next = False
    for i in range(len(tree)):
        if skip_next:
            continue

        if tree[i] == "f":

            output = output + "ff"

        elif tree[i] == "l":
            output += "2[fl]"
        elif is_number(tree[i]):
            output += str(int(tree[i]) + 1)
            if is_number(tree[i + 1]):
                skip_next = True
                number_times_ten = int(tree[i] * 10)
                second_number = int(tree[i + 1])
                output += str(number_times_ten + second_number + 1)


        else:
            output += tree[i]

    if recursion_number == 0:
        return output
    else:
        output = my_tree(output, recursion_number - 1)
        return output


def draw_my_tree(recursion_depth, tim_distance):
    path = my_tree("fl", recursion_depth)
    print(path)
    saved_states = []
    i = 0
    repeat_counters = [0]
    angles = [0]
    go_back_to_this_place = []
    while i < len(path):
        if path[i] == "f":
            tim.forward(tim_distance)

        elif is_number(path[i]):
            repeat_counters.append(int(path[i]))
            angles.append(180 / (int(path[i]) + 1))

        elif path[i] == "[":
            go_back_to_this_place.append(i)
            saved_states.append(get_turtle_state(tim))
            tim.left(90)
            tim.right((angles[-1] * repeat_counters[-1]) + angles[-1])
            print(f"angles = {angles}, current_angle = {(angles[-1] * repeat_counters[-1]) + angles[-1]} ")

        elif path[i] == "]":
            tim.penup()
            restore_turtle_state(tim, saved_states[-1])
            tim.pendown()

            if repeat_counters[-1] > 0:
                repeat_counters[-1] -= 1
                i = go_back_to_this_place[-1]
            else:
                del angles[-1]
                del go_back_to_this_place[-1]
                del repeat_counters[-1]
                del saved_states[-1]


        i += 1  # increments i by one before the loop ends (it's a bit like a for loop, but I can do more stuff with i


def get_turtle_state(_turtle):
    return _turtle.heading(), _turtle.position()


def restore_turtle_state(_turtle, state):
    _turtle.setheading(state[0])
    _turtle.setposition(state[1][0], state[1][1])


tim.left(90)
tim.penup()
tim.backward(400)
tim.pendown()
draw_my_tree(2, 50)
wn.update()

turtle.done()
print(my_tree("f0", 7))
