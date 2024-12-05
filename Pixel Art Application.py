# PIXEL ART APPLICATION

CANVAS_SIZE = [16, 16]
MARK = chr(9632)
EMPTY = chr(9633)
canvas = []
cmd_history = []

############## ART FEATURES ##############


def clearCanvas():
    '''clears the canvas of ink'''
    c = []
    for y in range(CANVAS_SIZE[1]):
        c.append([EMPTY]*CANVAS_SIZE[0])
    return c


def showCanvas():
    '''show the canvas'''
    print("")
    for y in range(CANVAS_SIZE[1]):
        s = str(CANVAS_SIZE[1]-y).rjust(2) + " "
        for x in range(CANVAS_SIZE[0]):
            s += canvas[y][x] + " "
        print(s)
    r = [chr(97+i) for i in range(CANVAS_SIZE[0])]
    print("   " + " ".join(r))
    print("")


def alg2pos(pos:str):
    '''converts algebraic notation to x,y coordinates'''
    x = pos[0]
    y = int(pos[1:])
    return (ord(x)-97, CANVAS_SIZE[1]-y)


def point(canvas,p:str,ink=MARK):
    '''draws one pixel at the position'''
    pos = alg2pos(p)
    try:
        canvas[pos[1]][pos[0]] = ink
    except IndexError:
        print("Out of bounds!")
    return canvas


def sort_pos(a:tuple,b:tuple):
    '''sorts the position of 2 points'''
    minx = min(a[0],b[0])
    miny = min(a[1],b[1])
    maxx = max(a[0],b[0])
    maxy = max(a[1],b[1])
    return minx,miny,maxx,maxx,maxy

def block(canvas,a:str,b:str,ink=MARK):
    '''fill in the pixels between these 2 points a and b'''
    # convert to grid coordinates
    sp = alg2pos(a)
    ep = alg2pos(b)

    # sort
    x1,y1,x2,y2 = sort_pos(sp,ep)

    # fill in the points between the two points
    for x in range(x1,x2+1):
        for y in range(y1, y2+1):
            canvas[y][x] = ink

    return canvas

def mirror(canvas,flip:str):
    '''
        mirrors the pixels across the y axis
        l - flip left to right; r - flip right to left
    '''
    h = CANVAS_SIZE[0]//2
    for r in range(CANVAS_SIZE[1]):
        if flip == "l":
            row_copy = canvas[r][:h][::-1]
        elif flip == "r":
            row_copy = canvas[r][h:][::-1]

        for c in range(h):
            i = h if flip == 'l' else 0
            canvas[r][i+c] = row_copy[c]

    return canvas


################ MAIN APPLICATION ###############


if __name__ == "__main__":

    canvas = clearCanvas()      # reset canvas

    while True:
        # show the canvas on every loop
        showCanvas()

        user_in = input("> ")
        if user_in == "quit":       # end app
            break

        # split by command
        cmd_list = user_in.split(";")
        cmd_history.extend(cmd_list)

        #---  COMMAND PARSER ---#
        for cmd in cmd_list:
            cmd = cmd.strip()
            cmd_dat = cmd.split(" ")

            # set ink
            ink = EMPTY if 'e' in cmd_dat[0] else MARK

            if len(cmd_dat) == 1:
                # clear command
                if cmd == "clear":
                    canvas = clearCanvas()
                    cmd_history.clear()
                # export command
                elif cmd == "export":
                    output = [c.strip() for c in cmd_history if c != "export"]
                    print(";".join(output))
                    
            # point or point erase command
            elif len(cmd_dat) == 2:
                if "p" in cmd_dat[0]:
                    pos = cmd_dat[1]
                    canvas = point(canvas,pos,ink)
                elif cmd_dat[0] == "m":
                    d = cmd_dat[1]
                    canvas = mirror(canvas,d)
                    
            # block or block erase
            elif len(cmd_dat) == 3 and 'b' in cmd_dat[0]:
                a = cmd_dat[1]
                b = cmd_dat[2]
                canvas = block(canvas,a,b,ink)
            
