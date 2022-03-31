import random
import turtle


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
            if is_number(tree[i+1]):
                skip_next = True
                numtimesten = int(tree[i] * 10)
                secondNumber = int(tree[i+1])
                output += str(numtimesten + secondNumber + 1)


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
    while i < len(path):
        if path[i] == "f":
            tim.forward(tim_distance)

        if is_number(path[i]):
            repeat_counter = int(path[i])
        
        elif path[i] == "[":
            go_back_to_this_p1ace = i
            saved_states.append(get_turtle_state(tim))            

        elif path[i] == "]":
            tim.penup()
            restore_turtle_state(tim, saved_states[-1])
            tim.pendown()
            del saved_states[-1]
            if repeat_counter > 0:
                repeat_counter -= 1
                

    i += 1 

def get_turtle_state(_turtle):
    return _turtle.heading(), _turtle.position()


def restore_turtle_state(_turtle, state):
    _turtle.setheading(state[0])
    _turtle.setposition(state[1][0], state[1][1])


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
wn.tracer(0)#

tim = turtle.Turtle()

tim.color('blue', 'purple')
tim.begin_fill()
tim.speed(0)


tim.left(90)
tim.penup()
tim.backward(400)
tim.pendown()
draw_my_tree(12, 4)
wn.update()

turtle.done()
print(my_tree("f0", 7))
