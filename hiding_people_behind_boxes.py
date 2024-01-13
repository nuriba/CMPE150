size = int(input())
box_width = int(input())
box_height = int(input())

head = "   o "
body = "  ooo"
legs = "  o o"
box = "x"
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
for a in range(1):
    if (2*size)-box_height<0:
        if box_width == 1:
            for b in range(box_width):
                print(box, end=" ")
            print(head[2:])
        elif box_width == 2:
            for b in range(box_width):
                print(box, end="")
            print(head[2:])
        elif box_width == 3:
            for b in range(box_width):
                print(box, end="")
            print(head[3:])
        elif box_width == 4:
            for b in range(box_width):
                print(box, end="")
            print(head[4])
        else:
            for j in range(box_width):
                print(box, end="")
            print()
    else:
        print(head)
if (2*size)-box_height<0:
    for i in range(((2*size)-box_height)+1):
        print(body)
elif size>=box_height:
    for i in range(size):
        print(body)
elif 2*size>=box_height>size:
    for i in range((2*size)-box_height):
        print(body)
if box_height>2*size:
    for i in range(size):
        if box_width == 1:
            for b in range(box_width):
                print(box, end=" ")
            print(body[2:])
        elif box_width == 2:
            for b in range(box_width):
                print(box, end="")
            print(body[2:])
        elif box_width == 3:
            for b in range(box_width):
                print(box, end="")
            print(body[3:])
        elif box_width == 4:
            for b in range(box_width):
                print(box, end="")
            print(body[4])
        else:
            for j in range(box_width):
                print(box, end="")
            print()
else:
    for i in range(box_height-size):
        if box_width == 1:
            for b in range(box_width):
                print(box, end=" ")
            print(body[2:])
        elif box_width == 2:
            for b in range(box_width):
                print(box, end="")
            print(body[2:])
        elif box_width == 3:
            for b in range(box_width):
                print(box, end="")
            print(body[3:])
        elif box_width == 4:
            for b in range(box_width):
                print(box, end="")
            print(body[4])
        else:
            for j in range(box_width):
                print(box, end="")
            print()
if size-box_height>0:
    for j in range(size-box_height):
        print(legs)
if box_height<=size:
    for k in range(box_height):
        if box_width==1:
            for b in range(box_width):
                print(box, end=" ")
            print(legs[2:])
        elif box_width == 2:
            for b in range(box_width):
                print(box, end="")
            print(legs[2:])
        elif box_width == 3:
            for b in range(box_width):
                print(box, end="")
            print(legs[3:])
        elif box_width == 4:
            for b in range(box_width):
                print(box, end="")
            print(legs[4])
        else:
            for j in range(box_width):
                print(box, end="")
            print()
else:
    for k in range(size):
        if box_width==1:
            for b in range(box_width):
                print(box,end=" ")
            print(legs[2:])
        elif box_width==2:
            for b in range(box_width):
                print(box,end="")
            print(legs[2:])
        elif box_width==3:
            for b in range(box_width):
                print(box, end="")
            print(legs[3:])
        elif box_width==4:
            for b in range(box_width):
                print(box, end="")
            print(legs[4])
        else:
            for j in range(box_width):
                print(box,end="")
            print()
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE