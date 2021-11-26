import sys
input = open(sys.argv[1], "r")
commands = [line.split() for line in input.readlines()]
input.close()
ki_list = []
KI_list = []
n1_list = []
n2_list = []
N1_list = []
N2_list = []
r1_list = []
r2_list = []
R1_list = []
R2_list = []
b1_list = []
b2_list = []
B1_list = []
B2_list = []
qu_list = []
QU_list = []
ki1_list = []
KI1_list = []
n11_list = []
n21_list = []
N11_list = []
N21_list = []
r11_list = []
r21_list = []
R11_list = []
R21_list = []
b11_list = []
b21_list = []
B11_list = []
B21_list = []
qu1_list = []
QU1_list = []
p1_list = []
p2_list = []
p3_list = []
p4_list = []
p6_list = []
p5_list = []
p7_list = []
p8_list = []
P1_list = []
P2_list = []
P3_list = []
P4_list = []
P5_list = []
P6_list = []
P7_list = []
P8_list = []
board =[
    ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"],
    ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
    ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]
]
showmove_board = [
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
]
changable_board=[
    ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"],
    ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
    ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]
]
def f_ind(x):
    for i in changable_board:
        if x in i:
            a = i.index(x)
            b = changable_board.index(i)
            return a,b
def s_how(y):
    for i in showmove_board:
        if y in i:
            f = i.index(y)
            s = showmove_board.index(i)
            return f,s
for control in commands:
    print(">",end=" ")
    print(*control)
    for to_do in control:
        if to_do == "initialize":
            print("OK")
            print("-----------------------")
            for elements in board:
                for initialize in elements:
                    changable_board = board
                    print(initialize, end=" ")
                print()
            print("-----------------------")
        elif to_do == "exit":
            exit()
        elif to_do == "showmoves":
            if control[1] == "ki":
                a, b = f_ind("ki")
                if a>0 and changable_board[b][a-1] != "KI" and (changable_board[b][a-1][0].isupper() or changable_board[b][a-1] == "  "):
                    ki_list.append(showmove_board[b][a-1])
                if a<7 and changable_board[b][a+1] != "KI" and (changable_board[b][a+1][0].isupper() or changable_board[b][a+1] == "  "):
                    ki_list.append(showmove_board[b][a+1])
                if b>0 and changable_board[b-1][a] != "KI" and  (changable_board[b-1][a][0].isupper() or changable_board[b-1][a] == "  "):
                    ki_list.append(showmove_board[b-1][a])
                if b>0 and a>0 and changable_board[b-1][a-1] != "KI" and (changable_board[b-1][a-1][0].isupper() or changable_board[b-1][a-1] == "  "):
                    ki_list.append(showmove_board[b-1][a-1])
                if b>0 and a<7 and changable_board[b-1][a+1] != "KI" and (changable_board[b-1][a+1][0].isupper() or changable_board[b-1][a+1] == "  "):
                    ki_list.append(showmove_board[b - 1][a+1])
                if b<7 and changable_board[b+1][a] != "KI" and (changable_board[b+1][a][0].isupper() or changable_board[b+1][a] == "  "):
                    ki_list.append(showmove_board[b+1][a])
                if b<7 and a>0 and  changable_board[b+1][a-1] != "KI" and (changable_board[b+1][a-1][0].isupper() or changable_board[b+1][a-1] == "  "):
                    ki_list.append(showmove_board[b+1][a-1])
                if b<7 and a<7 and changable_board[b+1][a+1] != "KI" and (changable_board[b+1][a+1][0].isupper() or changable_board[b+1][a+1] == "  "):
                    ki_list.append(showmove_board[b+1][a+1])
                if ki_list == []:
                    print("FAILED")
                    break
                ki_list.sort()
                for i in ki_list:
                    print(i,end=" ")
                print()
                ki_list = []
            elif control[1] == "KI":
                a,b = f_ind("KI")
                if a>0 and changable_board[b][a - 1] != "ki" and (changable_board[b][a - 1][0].islower() or changable_board[b][a-1] == "  "):
                    KI_list.append(showmove_board[b][a-1])
                if a<7 and changable_board[b][a + 1] != "ki" and (changable_board[b][a+1][0].islower() or changable_board[b][a+1] == "  "):
                    KI_list.append(showmove_board[b][a+1])
                if b>0 and changable_board[b-1][a] != "ki" and (changable_board[b-1][a][0].islower() or changable_board[b-1][a] == "  "):
                    KI_list.append(showmove_board[b-1][a])
                if b>0 and changable_board[b - 1][a - 1] != "ki" and (changable_board[b - 1][a - 1][0].islower() or changable_board[b-1][a-1] == "  "):
                    KI_list.append(showmove_board[b-1][a-1])
                if b>0 and changable_board[b-1][a+1] != "ki" and (changable_board[b-1][a+1][0].islower() or changable_board[b-1][a+1] == "  "):
                    KI_list.append(showmove_board[b-1][a+1])
                if b<7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b+1][a] == "  "):
                    KI_list.append(showmove_board[b+1][a])
                if b<7 and a>0 and changable_board[b+1][a-1] != "ki" and (changable_board[b+1][a-1][0].islower() or changable_board[b+1][a-1] == "  "):
                    KI_list.append(showmove_board[b+1][a-1])
                if b<7 and a<7 and changable_board[b+1][a+1] != "ki" and (changable_board[b+1][a+1][0].islower() or changable_board[b+1][a+1] == "  "):
                    KI_list.append(showmove_board[b+1][a+1])
                if KI_list == []:
                    print("FAILED")
                    break
                KI_list.sort()
                for i in KI_list:
                    print(i,end=" ")
                print()
                KI_list = []
            elif control[1] == "p1":
                a, b = f_ind("p1")
                if b>0 and changable_board[b-1][a] != "KI" and (changable_board[b-1][a][0].isupper() or changable_board[b-1][a] == "  "):
                    print(showmove_board[b-1][a])
                else:
                    print("FAILED")
            elif control[1] == "p2":
                a, b = f_ind("p2")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    print(showmove_board[b - 1][a])
                else:
                    print("FAILED")
            elif control[1] == "p3":
                a, b = f_ind("p3")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    print(showmove_board[b - 1][a])
                else:
                    print("FAILED")
            elif control[1] == "p4":
                a, b = f_ind("p4")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    print(showmove_board[b - 1][a])
                else:
                    print("FAILED")
            elif control[1] == "p5":
                a, b = f_ind("p5")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    print(showmove_board[b - 1][a])
                else:
                    print("FAILED")
            elif control[1] == "p6":
                a, b = f_ind("p6")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    print(showmove_board[b - 1][a])
                else:
                    print("FAILED")
            elif control[1] == "p7":
                a, b = f_ind("p7")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    print(showmove_board[b - 1][a])
                else:
                    print("FAILED")
            elif control[1] == "p8":
                a, b = f_ind("p8")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    print(showmove_board[b - 1][a])
                else:
                    print("FAILED")
            elif control[1] == "P1":
                a, b = f_ind("P1")
                if b<7 and changable_board[b+1][a] != "ki" and (changable_board[b+1][a][0].islower() or changable_board[b+1][a] == "  "):
                    print(showmove_board[b+1][a])
                else:
                    print("FAILED")
            elif control[1] == "P2":
                a, b = f_ind("P2")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    print(showmove_board[b + 1][a])
                else:
                    print("FAILED")
            elif control[1] == "P3":
                a, b = f_ind("P3")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    print(showmove_board[b + 1][a])
                else:
                     print("FAILED")
            elif control[1] == "P4":
                a, b = f_ind("P4")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    print(showmove_board[b + 1][a])
                else:
                    print("FAILED")
            elif control[1] == "P5":
                a, b = f_ind("P5")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    print(showmove_board[b + 1][a])
                else:
                    print("FAILED")
            elif control[1] == "P6":
                a, b = f_ind("P6")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    print(showmove_board[b + 1][a])
                else:
                    print("FAILED")
            elif control[1] == "P7":
                a, b = f_ind("P7")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    print(showmove_board[b + 1][a])
                else:
                    print("FAILED")
            elif control[1] == "P8":
                a, b = f_ind("P8")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    print(showmove_board[b + 1][a])
                else:
                    print("FAILED")
            elif control[1] == "n1":
                a, b = f_ind("n1")
                if b>1 and a>0 and changable_board[b-2][a-1] != "KI" and (changable_board[b-2][a-1][0].isupper() or changable_board[b-2][a-1] == "  "):
                    n1_list.append(showmove_board[b-2][a-1])
                if b>1 and a<7 and changable_board[b-2][a+1] != "KI" and (changable_board[b-2][a+1][0].isupper() or changable_board[b-2][a+1] == "  "):
                    n1_list.append(showmove_board[b-2][a+1])
                if b>0 and a<6 and changable_board[b-1][a+2] != "KI" and (changable_board[b-1][a+2][0].isupper() or changable_board[b-1][a+2] == "  "):
                    n1_list.append(showmove_board[b-1][a+2])
                if b<7 and a<6 and changable_board[b+1][a+2] != "KI" and (changable_board[b+1][a+2][0].isupper() or changable_board[b+1][a+2] == "  "):
                    n1_list.append(showmove_board[b+1][a+2])
                if b<6 and a<7 and changable_board[b+2][a+1] != "KI" and (changable_board[b+2][a+1][0].isupper() or changable_board[b+2][a+1] == "  "):
                    n1_list.append(showmove_board[b+2][a+1])
                if b<6 and a>0 and changable_board[b+2][a-1] != "KI" and (changable_board[b+2][a-1][0].isupper() or changable_board[b+2][a-1] == "  "):
                    n1_list.append(showmove_board[b+2][a-1])
                if b<7 and a>1 and changable_board[b+1][a-2] != "KI" and (changable_board[b+1][a-2][0].isupper() or changable_board[b+1][a-2] == "  "):
                    n1_list.append(showmove_board[b+1][a-2])
                if b>0 and a>1 and changable_board[b-1][a-2] != "KI" and (changable_board[b-1][a-2][0].isupper() or changable_board[b-1][a-2] == "  "):
                    n1_list.append(showmove_board[b-1][a-2])
                if b>0 and a<7 and changable_board[b-1][a+1] == "  ":
                    n1_list.append(showmove_board[b-1][a+1])
                if b<7 and a<7 and changable_board[b+1][a+1] == "  ":
                    n1_list.append(showmove_board[b+1][a+1])
                if b<7 and a>0 and changable_board[b+1][a-1] == "  ":
                    n1_list.append(showmove_board[b+1][a-1])
                if b>0 and a>0 and changable_board[b-1][a-1] == "  ":
                    n1_list.append(showmove_board[b-1][a-1])
                if n1_list == []:
                    print("FAILED")
                    break
                n1_list.sort()
                for i in n1_list:
                    print(i,end=" ")
                print()
                n1_list = []
            elif control[1] == "n2":
                a, b = f_ind("n2")
                if b > 1 and a > 0 and changable_board[b-2][a-1] != "KI" and (changable_board[b-2][a-1][0].isupper() or changable_board[b-2][a-1] == "  "):
                    n2_list.append(showmove_board[b - 2][a - 1])
                if b > 1 and a < 7 and changable_board[b - 2][a + 1] != "KI" and (
                        changable_board[b - 2][a + 1][0].isupper() or changable_board[b - 2][a + 1] == "  "):
                    n2_list.append(showmove_board[b - 2][a + 1])
                if b > 0 and a < 6 and changable_board[b - 1][a + 2] != "KI" and (changable_board[b-1][a+2][0].isupper() or changable_board[b - 1][a + 2] == "  "):
                    n2_list.append(showmove_board[b - 1][a + 2])
                if b < 7 and a < 6 and changable_board[b + 1][a + 2] != "KI" and (changable_board[b + 1][a + 2][0].isupper() or changable_board[b + 1][a + 2] == "  "):
                    n2_list.append(showmove_board[b + 1][a + 2])
                if b < 6 and a < 7 and changable_board[b + 2][a + 1] != "KI" and (changable_board[b + 2][a + 1][0].isupper() or changable_board[b+2][a + 1] == "  "):
                    n2_list.append(showmove_board[b + 2][a + 1])
                if b < 6 and a > 0 and changable_board[b + 2][a - 1] != "KI" and (changable_board[b + 2][a - 1][0].isupper() or changable_board[b + 2][a - 1] == "  "):
                    n2_list.append(showmove_board[b + 2][a - 1])
                if b < 7 and a > 1 and changable_board[b + 1][a - 2] != "KI" and (changable_board[b + 1][a - 2][0].isupper() or changable_board[b + 1][a - 2] == "  "):
                    n2_list.append(showmove_board[b + 1][a - 2])
                if b > 0 and a > 1 and changable_board[b - 1][a - 2] != "KI" and (changable_board[b-1][a-2][0].isupper() or changable_board[b-1][a-2] == "  "):
                    n2_list.append(showmove_board[b - 1][a - 2])
                if b>0 and a<7 and changable_board[b-1][a+1] == "  ":
                    n2_list.append(showmove_board[b-1][a+1])
                if b<7 and a<7 and changable_board[b+1][a+1] == "  ":
                    n2_list.append(showmove_board[b+1][a+1])
                if b<7 and a>0 and changable_board[b+1][a-1] == "  ":
                    n2_list.append(showmove_board[b+1][a-1])
                if b>0 and a>0 and changable_board[b-1][a-1] == "  ":
                    n2_list.append(showmove_board[b-1][a-1])
                if n2_list == []:
                    print("FAILED")
                n2_list.sort()
                for i in n2_list:
                    print(i, end=" ")
                print()
                n2_list = []
            elif control[1] == "N1":
                a, b = f_ind("N1")
                if b > 1 and a > 0 and changable_board[b - 2][a - 1] != "ki" and (changable_board[b - 2][a - 1][0].islower() or changable_board[b - 2][a - 1] == "  "):
                    N1_list.append(showmove_board[b - 2][a - 1])
                if b > 1 and a < 7 and changable_board[b - 2][a + 1] != "ki" and (changable_board[b - 2][a + 1][0].islower() or changable_board[b - 2][a + 1] == "  "):
                    N1_list.append(showmove_board[b - 2][a + 1])
                if b > 0 and a < 6 and changable_board[b - 1][a + 2] != "ki" and (changable_board[b - 1][a + 2][0].islower() or changable_board[b - 1][a + 2] == "  "):
                    N1_list.append(showmove_board[b - 1][a + 2])
                if b < 7 and a < 6 and changable_board[b + 1][a + 2] != "ki" and (changable_board[b + 1][a + 2][0].islower() or changable_board[b + 1][a + 2] == "  "):
                    N1_list.append(showmove_board[b + 1][a + 2])
                if b < 6 and a < 7 and changable_board[b + 2][a + 1] != "ki" and (changable_board[b + 2][a + 1][0].islower() or changable_board[b + 2][a + 1] == "  "):
                    N1_list.append(showmove_board[b + 2][a + 1])
                if b < 6 and a > 0 and changable_board[b + 2][a - 1] != "ki" and (changable_board[b + 2][a - 1][0].islower() or changable_board[b + 2][a - 1] == "  "):
                    N1_list.append(showmove_board[b + 2][a - 1])
                if b < 7 and a > 1 and changable_board[b + 1][a - 2] != "ki" and (changable_board[b + 1][a - 2][0].islower() or changable_board[b + 1][a - 2] == "  "):
                    N1_list.append(showmove_board[b + 1][a - 2])
                if b > 0 and a > 1 and changable_board[b - 1][a - 2] != "ki" and (changable_board[b - 1][a - 2][0].islower() or changable_board[b - 1][a - 2] == "  "):
                    N1_list.append(showmove_board[b - 1][a - 2])
                if b > 0 and a < 7 and changable_board[b - 1][a + 1] == "  ":
                    N1_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] == "  ":
                    N1_list.append(showmove_board[b + 1][a + 1])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] == "  ":
                    N1_list.append(showmove_board[b + 1][a - 1])
                if b > 0 and a > 0 and changable_board[b - 1][a - 1] == "  ":
                    N1_list.append(showmove_board[b - 1][a - 1])
                if N1_list == []:
                    print("FAILED")
                    break
                N1_list.sort()
                for i in N1_list:
                    print(i,end=" ")
                print()
                N1_list = []
            elif control[1] == "N2":
                a, b = f_ind("N2")
                if b > 1 and a > 0 and changable_board[b - 2][a - 1] != "ki" and (changable_board[b - 2][a - 1][0].islower() or changable_board[b - 2][a - 1] == "  "):
                    N2_list.append(showmove_board[b - 2][a - 1])
                if b > 1 and a < 7 and changable_board[b - 2][a + 1] != "ki" and (changable_board[b - 2][a + 1][0].islower() or changable_board[b - 2][a + 1] == "  "):
                    N2_list.append(showmove_board[b - 2][a + 1])
                if b > 0 and a < 6 and changable_board[b - 1][a + 2] != "ki" and (changable_board[b - 1][a + 2][0].islower() or changable_board[b - 1][a + 2] == "  "):
                    N2_list.append(showmove_board[b - 1][a + 2])
                if b < 7 and a < 6 and changable_board[b + 1][a + 2] != "ki" and (changable_board[b + 1][a + 2][0].islower() or changable_board[b + 1][a + 2] == "  "):
                    N2_list.append(showmove_board[b + 1][a + 2])
                if b < 6 and a < 7 and changable_board[b + 2][a + 1] != "ki" and (changable_board[b + 2][a + 1][0].islower() or changable_board[b + 2][a + 1] == "  "):
                    N2_list.append(showmove_board[b + 2][a + 1])
                if b < 6 and a > 0 and changable_board[b + 2][a - 1] != "ki" and (changable_board[b + 2][a - 1][0].islower() or changable_board[b + 2][a - 1] == "  "):
                    N2_list.append(showmove_board[b + 2][a - 1])
                if b < 7 and a > 1 and changable_board[b + 1][a - 2] != "ki" and (changable_board[b + 1][a - 2][0].islower() or changable_board[b + 1][a - 2] == "  "):
                    N2_list.append(showmove_board[b + 1][a - 2])
                if b > 0 and a > 1 and changable_board[b - 1][a - 2] != "ki" and (changable_board[b - 1][a - 2][0].islower() or changable_board[b - 1][a - 2] == "  "):
                    N2_list.append(showmove_board[b - 1][a - 2])
                if b > 0 and a < 7 and changable_board[b - 1][a + 1] == "  ":
                    N2_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] == "  ":
                    N2_list.append(showmove_board[b + 1][a + 1])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] == "  ":
                    N2_list.append(showmove_board[b + 1][a - 1])
                if b > 0 and a > 0 and changable_board[b - 1][a - 1] == "  ":
                    N2_list.append(showmove_board[b - 1][a - 1])
                if N2_list == []:
                    print("FAILED")
                    break
                N2_list.sort()
                for i in N2_list:
                    print(i,end=" ")
                print()
                N2_list = []
            elif control[1] == "r1":
                a, b = f_ind("r1")
                for z in range(1, 8):
                    if a+z<8 and changable_board[b][a+z] != "KI" and (changable_board[b][a+z][0].isupper() or changable_board[b][a+z] == "  "):
                        r1_list.append(showmove_board[b][a+z])
                    if a+z<8 and changable_board[b][a+z] != "  ":
                        break
                for z1 in range(1,8):
                    if a-z1 > (-1) and changable_board[b][a-z1] != "KI" and (changable_board[b][a-z1][0].isupper() or changable_board[b][a-z1] == "  "):
                        r1_list.append(showmove_board[b][a-z1])
                    if a-z1 >(-1) and changable_board[b][a-z1] != "  ":
                        break
                for z2 in range(1,8):
                    if b+z2<8 and changable_board[b+z2][a] !="KI" and (changable_board[b+z2][a][0].isupper() or changable_board[b+z2][a] == "  "):
                        r1_list.append(showmove_board[b+z2][a])
                    if b+z2<8 and changable_board[b+z2][a] != "  ":
                        break
                for z3 in range(1,8):
                    if b-z3> (-1) and changable_board[b-z3][a] != "KI" and (changable_board[b-z3][a][0].isupper() or changable_board[b-z3][a] == "  "):
                        r1_list.append(showmove_board[b-z3][a])
                    if b-z3>(-1) and changable_board[b-z3][a] != "  ":
                        break
                if r1_list == []:
                    print("FAILED")
                    break
                else:
                    r1_list = set(r1_list)
                    r1_list = list(r1_list)
                    r1_list.sort()
                    for i in r1_list:
                        print(i,end=" ")
                    print()
                r1_list = []
            elif control[1] == "r2":
                a, b = f_ind("r2")
                for z in range(1, 8):
                    if a+z<8 and changable_board[b][a+z] != "KI" and (changable_board[b][a+z][0].isupper() or changable_board[b][a+z] == "  "):
                        r2_list.append(showmove_board[b][a+z])
                    if a+z<8 and changable_board[b][a+z] != "  ":
                        break
                for z1 in range(1,8):
                    if a-z1 > (-1) and changable_board[b][a-z1] != "KI" and (changable_board[b][a-z1][0].isupper() or changable_board[b][a-z1] == "  "):
                        r2_list.append(showmove_board[b][a-z1])
                    if a-z1 > (-1) and changable_board[b][a-z1] != "  ":
                        break
                for z2 in range(1,8):
                    if b+z2<8 and changable_board[b+z2][a] !="KI" and (changable_board[b+z2][a][0].isupper() or changable_board[b+z2][a] == "  "):
                        r2_list.append(showmove_board[b+z2][a])
                    if b+z2<8 and changable_board[b+z2][a] != "  ":
                        break
                for z3 in range(1,8):
                    if b-z3> (-1) and changable_board[b-z3][a] != "KI" and (changable_board[b-z3][a][0].isupper() or changable_board[b-z3][a] == "  "):
                        r2_list.append(showmove_board[b-z3][a])
                    if b-z3 >(-1) and changable_board[b-z3][a] != "  ":
                        break
                if r2_list == []:
                    print("FAILED")
                    break
                else:
                    r2_list = set(r2_list)
                    r2_list = list(r2_list)
                    r2_list.sort()
                    for i in r2_list:
                        print(i, end=" ")
                    print()
                r2_list = []
            elif control[1] == "R1":
                a, b = f_ind("R1")
                for z in range(1, 8):
                    if a+z<8 and changable_board[b][a+z] != "ki" and (changable_board[b][a+z][0].islower() or changable_board[b][a+z] == "  "):
                        R1_list.append(showmove_board[b][a+z])
                    if a+z<8 and changable_board[b][a+z] != "  ":
                        break
                for z1 in range(1,8):
                    if a-z1 > (-1) and changable_board[b][a-z1] != "ki" and (changable_board[b][a-z1][0].islower() or changable_board[b][a-z1] == "  "):
                        R1_list.append(showmove_board[b][a-z1])
                    if a-z1 > (-1) and changable_board[b][a-z1] != "  ":
                        break
                for z2 in range(1,8):
                    if b+z2<8 and changable_board[b+z2][a] !="ki" and (changable_board[b+z2][a][0].islower() or changable_board[b+z2][a] == "  "):
                        R1_list.append(showmove_board[b+z2][a])
                    if b+z2<8 and changable_board[b+z2][a] != "  ":
                        break
                for z3 in range(1,8):
                    if b-z3> (-1) and changable_board[b-z3][a] != "ki" and (changable_board[b-z3][a][0].islower() or changable_board[b-z3][a] == "  "):
                        R1_list.append(showmove_board[b-z3][a])
                    if b-z3 >(-1) and changable_board[b-z3][a] != "  ":
                        break
                if R1_list == []:
                    print("FAILED")
                    break
                else:
                    R1_list = set(R1_list)
                    R1_list = list(R1_list)
                    R1_list.sort()
                    for i in R1_list:
                        print(i, end=" ")
                    print()
                R1_list = []
            elif control[1] == "R2":
                a, b = f_ind("R2")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "ki" and (changable_board[b][a + z][0].islower() or changable_board[b][a + z] == "  "):
                        R2_list.append(showmove_board[b][a + z])
                    if a+z <8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "ki" and (changable_board[b][a - z1][0].islower() or changable_board[b][a - z1] == "  "):
                        R2_list.append(showmove_board[b][a - z1])
                    if a-z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "ki" and (changable_board[b + z2][a][0].islower() or changable_board[b + z2][a] == "  "):
                        R2_list.append(showmove_board[b + z2][a])
                    if b+z2<8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b-z3][a] != "ki" and (changable_board[b-z3][a][0].islower() or changable_board[b-z3][a] == "  "):
                        R2_list.append(showmove_board[b - z3][a])
                    if b-z3>(-1) and changable_board[b - z3][a] != "  ":
                        break
                if R2_list == []:
                    print("FAILED")
                    break
                else:
                    R2_list = set(R2_list)
                    R2_list = list(R2_list)
                    R2_list.sort()
                    for i in R2_list:
                        print(i, end=" ")
                    print()
                R2_list = []
            elif control[1] == "b1":
                a, b = f_ind("b1")
                for z in range(1,8):
                    if b-z>(-1) and a+z<8 and changable_board[b-z][a+z] != "KI" and (changable_board[b-z][a+z][0].isupper() or changable_board[b-z][a+z] == "  "):
                      b1_list.append(showmove_board[b-z][a+z])
                    if b-z>(-1) and a+z<8 and changable_board[b-z][a+z] != "  ":
                        break
                for z1 in range(1,8):
                    if b-z1>(-1) and a-z1>(-1) and changable_board[b-z1][a-z1] != "KI" and (changable_board[b-z1][a-z1][0].isupper() or changable_board[b-z1][a-z1] == "  "):
                      b1_list.append(showmove_board[b-z1][a-z1])
                    if b-z1>(-1) and a-z1>(-1) and changable_board[b-z1][a-z1] != "  ":
                        break
                if b1_list == []:
                    print("FAILED")
                    break
                else:
                    b1_list = set(b1_list)
                    b1_list = list(b1_list)
                    b1_list.sort()
                    for i in b1_list:
                        print(i, end=" ")
                    print()
                b1_list = []
            elif control[1] == "b2":
                a, b = f_ind("b2")
                for z in range(1, 8):
                    if b - z > (-1) and a + z < 8 and changable_board[b - z][a + z] != "KI" and (changable_board[b - z][a + z][0].isupper() or changable_board[b - z][a + z] == "  "):
                        b2_list.append(showmove_board[b - z][a + z])
                    if b - z > (-1) and a + z < 8 and changable_board[b - z][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if b - z1 > (-1) and a - z1 > (-1) and changable_board[b - z1][a - z1] != "KI" and (changable_board[b - z1][a - z1][0].isupper() or changable_board[b - z1][a - z1] == "  "):
                        b2_list.append(showmove_board[b - z1][a - z1])
                    if b - z1 > (-1) and a - z1 > (-1) and changable_board[b - z1][a - z1] != "  ":
                        break
                if b2_list == []:
                    print("FAILED")
                    break
                else:
                    b2_list = set(b2_list)
                    b2_list = list(b2_list)
                    b2_list.sort()
                    for i in b2_list:
                        print(i, end=" ")
                    print()
                b2_list = []
            elif control[1] == "B1":
                a, b = f_ind("B1")
                for z in range(1,8):
                    if b+z<8 and a-z>(-1) and changable_board[b+z][a-z] != "ki" and (changable_board[b+z][a-z][0].islower() or changable_board[b+z][a-z] == "  "):
                        B1_list.append(showmove_board[b+z][a-z])
                    if b+z <8 and a-z >(-1) and changable_board[b+z][a-z] != "  ":
                        break
                for z1 in range(1,8):
                    if b+z1<8 and a+z1<8 and changable_board[b+z1][a+z1] != "ki" and (changable_board[b+z1][a+z1][0].islower() or changable_board[b+z1][a+z1] == "  "):
                        B1_list.append(showmove_board[b+z1][a+z1])
                    if b+z1 <8 and a+z1 < 8 and changable_board[b+z1][a+z1] != "  ":
                        break
                if B1_list == []:
                    print("FAILED")
                    break
                else:
                    B1_list = set(B1_list)
                    B1_list = list(B1_list)
                    B1_list.sort()
                    for i in B1_list:
                        print(i, end=" ")
                    print()
                B1_list = []
            elif control[1] == "B2":
                a, b = f_ind("B2")
                for z in range(1, 8):
                    if b + z < 8 and a - z > (-1) and changable_board[b + z][a - z] != "ki" and (changable_board[b + z][a - z][0].islower() or changable_board[b + z][a - z] == "  "):
                        B2_list.append(showmove_board[b + z][a - z])
                    if b + z < 8 and a - z > (-1) and changable_board[b + z][a - z] != "  ":
                        break
                for z1 in range(1, 8):
                    if b + z1 < 8 and a + z1 < 8 and changable_board[b + z1][a + z1] != "ki" and (changable_board[b + z1][a + z1][0].islower() or changable_board[b + z1][a + z1] == "  "):
                        B2_list.append(showmove_board[b + z1][a + z1])
                    if b + z1 < 8 and a + z1 < 8 and changable_board[b + z1][a + z1] != "  ":
                        break
                if B2_list == []:
                    print("FAILED")
                    break
                else:
                    B2_list = set(B2_list)
                    B2_list = list(B2_list)
                    B2_list.sort()
                    for i in B2_list:
                        print(i, end=" ")
                    print()
                B2_list = []
            elif control[1] == "qu":
                a,b = f_ind("qu")
                for z in range(1, 8):
                    if a+z<8 and changable_board[b][a+z] != "KI" and (changable_board[b][a+z][0].isupper() or changable_board[b][a+z] == "  "):
                        qu_list.append(showmove_board[b][a+z])
                    if a+z<8 and changable_board[b][a+z] != "  ":
                        break
                for z1 in range(1,8):
                    if a-z1 > (-1) and changable_board[b][a-z1] != "KI" and (changable_board[b][a-z1][0].isupper() or changable_board[b][a-z1] == "  "):
                        qu_list.append(showmove_board[b][a-z1])
                    if a-z1 >(-1) and changable_board[b][a-z1] != "  ":
                        break
                for z2 in range(1,8):
                    if b+z2<8 and changable_board[b+z2][a] !="KI" and (changable_board[b+z2][a][0].isupper() or changable_board[b+z2][a] == "  "):
                        qu_list.append(showmove_board[b+z2][a])
                    if b+z2<8 and changable_board[b+z2][a] != "  ":
                        break
                for z3 in range(1,8):
                    if b-z3> (-1) and changable_board[b-z3][a] != "KI" and (changable_board[b-z3][a][0].isupper() or changable_board[b-z3][a] == "  "):
                        qu_list.append(showmove_board[b-z3][a])
                    if b-z3>(-1) and changable_board[b-z3][a] != "  ":
                        break
                for z4 in range(1, 8):
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "KI" and (changable_board[b - z4][a + z4][0].isupper() or changable_board[b - z4][a + z4] == "  "):
                        qu_list.append(showmove_board[b - z4][a + z4])
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "  ":
                        break
                for z5 in range(1, 8):
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "KI" and (changable_board[b - z5][a - z5][0].isupper() or changable_board[b - z5][a - z5] == "  "):
                        qu_list.append(showmove_board[b - z5][a - z5])
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "  ":
                        break
                for z6 in range(1,8):
                    if b+z6<8 and a-z6>(-1) and changable_board[b+z6][a-z6] != "KI" and (changable_board[b+z6][a-z6][0].isupper() or changable_board[b+z6][a-z6] == "  "):
                        qu_list.append(showmove_board[b+z6][a-z6])
                    if b+z6 <8 and a-z6>(-1) and changable_board[b+z6][a-z6] != "  ":
                        break
                for z7 in range(1,8):
                    if b + z7 < 8 and a+z7 < 8 and changable_board[b + z7][a+z7] != "KI" and (changable_board[b+z7][a+z7][0].isupper() or changable_board[b + z7][a+z7] == "  "):
                        qu_list.append(showmove_board[b + z7][a+z7])
                    if b + z7 < 8 and a+z7 <8 and changable_board[b + z7][a+z7] != "  ":
                        break
                if qu_list == []:
                    print("FAILED")
                    break
                else:
                    qu_list = set(qu_list)
                    qu_list = list(qu_list)
                    qu_list.sort()
                    for i in qu_list:
                        print(i, end=" ")
                    print()
                qu_list = []
            elif control[1] == "QU":
                a, b = f_ind("QU")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "ki" and (changable_board[b][a + z][0].islower() or changable_board[b][a + z] == "  "):
                        QU_list.append(showmove_board[b][a + z])
                    if a + z < 8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "ki" and (changable_board[b][a - z1][0].islower() or changable_board[b][a - z1] == "  "):
                        QU_list.append(showmove_board[b][a - z1])
                    if a - z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "ki" and (changable_board[b + z2][a][0].islower() or changable_board[b + z2][a] == "  "):
                        QU_list.append(showmove_board[b + z2][a])
                    if b + z2 < 8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b - z3][a] != "ki" and (changable_board[b - z3][a][0].islower() or changable_board[b - z3][a] == "  "):
                        QU_list.append(showmove_board[b - z3][a])
                    if b - z3 > (-1) and changable_board[b - z3][a] != "  ":
                        break
                for z4 in range(1, 8):
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "ki" and (changable_board[b - z4][a + z4][0].islower() or changable_board[b - z4][a + z4] == "  "):
                        QU_list.append(showmove_board[b - z4][a + z4])
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "  ":
                        break
                for z5 in range(1, 8):
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "ki" and (changable_board[b - z5][a - z5][0].islower() or changable_board[b - z5][a - z5] == "  "):
                        QU_list.append(showmove_board[b - z5][a - z5])
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "  ":
                        break
                for z6 in range(1, 8):
                    if b + z6 < 8 and a - z6 > (-1) and changable_board[b + z6][a - z6] != "ki" and (changable_board[b + z6][a - z6][0].islower() or changable_board[b + z6][a - z6] == "  "):
                        QU_list.append(showmove_board[b + z6][a - z6])
                    if b + z6 < 8 and a - z6 > (-1) and changable_board[b + z6][a - z6] != "  ":
                        break
                for z7 in range(1, 8):
                    if b + z7 < 8 and a + z7 < 8 and changable_board[b + z7][a + z7] != "ki" and (changable_board[b + z7][a + z7][0].islower() or changable_board[b + z7][a + z7] == "  "):
                        QU_list.append(showmove_board[b + z7][a + z7])
                    if b + z7 < 8 and a + z7 < 8 and changable_board[b + z7][a + z7] != "  ":
                        break
                if QU_list == []:
                    print("FAILED")
                    break
                else:
                    QU_list = set(QU_list)
                    QU_list = list(QU_list)
                    QU_list.sort()
                    for i in QU_list:
                        print(i, end=" ")
                    print()
                QU_list = []
        elif to_do == "move":
            if control[1] == "ki":
                a, b = f_ind("ki")
                if a > 0 and changable_board[b][a - 1] != "KI" and (changable_board[b][a - 1][0].isupper() or changable_board[b][a - 1] == "  "):
                    ki1_list.append(showmove_board[b][a - 1])
                if a < 7 and changable_board[b][a + 1] != "KI" and (changable_board[b][a + 1][0].isupper() or changable_board[b][a + 1] == "  "):
                    ki1_list.append(showmove_board[b][a + 1])
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    ki1_list.append(showmove_board[b - 1][a])
                if b > 0 and a > 0 and changable_board[b - 1][a - 1] != "KI" and (changable_board[b - 1][a - 1][0].isupper() or changable_board[b - 1][a - 1] == "  "):
                    ki1_list.append(showmove_board[b - 1][a - 1])
                if b > 0 and a < 7 and changable_board[b - 1][a + 1] != "KI" and (changable_board[b - 1][a + 1][0].isupper() or changable_board[b - 1][a + 1] == "  "):
                    ki1_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and changable_board[b + 1][a] != "KI" and (changable_board[b + 1][a][0].isupper() or changable_board[b + 1][a] == "  "):
                    ki1_list.append(showmove_board[b + 1][a])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] != "KI" and (changable_board[b + 1][a - 1][0].isupper() or changable_board[b + 1][a - 1] == "  "):
                    ki1_list.append(showmove_board[b + 1][a - 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] != "KI" and (changable_board[b + 1][a + 1][0].isupper() or changable_board[b + 1][a + 1] == "  "):
                    ki1_list.append(showmove_board[b + 1][a + 1])
                if control[2] not in ki1_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "ki"
                    changable_board[b][a] = "  "
                    ki1_list = []
                    print("OK")
            elif control[1] == "KI":
                a, b = f_ind("KI")
                if a > 0 and changable_board[b][a - 1] != "ki" and (changable_board[b][a - 1][0].islower() or changable_board[b][a - 1] == "  "):
                    KI1_list.append(showmove_board[b][a - 1])
                if a < 7 and changable_board[b][a + 1] != "ki" and (changable_board[b][a + 1][0].islower() or changable_board[b][a + 1] == "  "):
                    KI1_list.append(showmove_board[b][a + 1])
                if b > 0 and changable_board[b - 1][a] != "ki" and (changable_board[b - 1][a][0].islower() or changable_board[b - 1][a] == "  "):
                    KI1_list.append(showmove_board[b - 1][a])
                if b > 0 and changable_board[b - 1][a - 1] != "ki" and (changable_board[b - 1][a - 1][0].islower() or changable_board[b - 1][a - 1] == "  "):
                    KI1_list.append(showmove_board[b - 1][a - 1])
                if b > 0 and changable_board[b - 1][a + 1] != "ki" and (changable_board[b - 1][a + 1][0].islower() or changable_board[b - 1][a + 1] == "  "):
                    KI1_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    KI1_list.append(showmove_board[b + 1][a])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] != "ki" and (changable_board[b + 1][a - 1][0].islower() or changable_board[b + 1][a - 1] == "  "):
                    KI1_list.append(showmove_board[b + 1][a - 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] != "ki" and (changable_board[b + 1][a + 1][0].islower() or changable_board[b + 1][a + 1] == "  "):
                    KI1_list.append(showmove_board[b + 1][a + 1])
                if control[2] not in KI1_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "KI"
                    changable_board[b][a] = "  "
                    KI1_list = []
                    print("OK")
            elif control[1] == "p1":
                a, b = f_ind("p1")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p1_list.append(showmove_board[b-1][a])
                if control[2] not in p1_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p1"
                    changable_board[b][a] = "  "
                    p1_list = []
                    print("OK")
            elif control[1] == "p2":
                a, b = f_ind("p2")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p2_list.append(showmove_board[b - 1][a])
                if control[2] not in p2_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p2"
                    changable_board[b][a] = "  "
                    p2_list = []
                    print("OK")
            elif control[1] == "p3":
                a, b = f_ind("p3")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p3_list.append(showmove_board[b - 1][a])
                if control[2] not in p3_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p3"
                    changable_board[b][a] = "  "
                    p3_list = []
                    print("OK")
            elif control[1] == "p4":
                a, b = f_ind("p4")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p4_list.append(showmove_board[b - 1][a])
                if control[2] not in p4_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p4"
                    changable_board[b][a] = "  "
                    p4_list = []
                    print("OK")
            elif control[1] == "p5":
                a, b = f_ind("p5")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p5_list.append(showmove_board[b - 1][a])
                if control[2] not in p5_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p5"
                    changable_board[b][a] = "  "
                    p5_list = []
                    print("OK")
            elif control[1] == "p6":
                a, b = f_ind("p6")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p6_list.append(showmove_board[b - 1][a])
                if control[2] not in p6_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p6"
                    changable_board[b][a] = "  "
                    p6_list = []
                    print("OK")
            elif control[1] == "p7":
                a, b = f_ind("p7")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p7_list.append(showmove_board[b - 1][a])
                if control[2] not in p7_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p7"
                    changable_board[b][a] = "  "
                    p7_list = []
                    print("OK")
            elif control[1] == "p8":
                a, b = f_ind("p8")
                if b > 0 and changable_board[b - 1][a] != "KI" and (changable_board[b - 1][a][0].isupper() or changable_board[b - 1][a] == "  "):
                    p8_list.append(showmove_board[b - 1][a])
                if control[2] not in p8_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "p8"
                    changable_board[b][a] = "  "
                    p8_list = []
                    print("OK")
            elif control[1] == "P1":
                a, b = f_ind("P1")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P1_list.append(showmove_board[b+1][a])
                if control[2] not in P1_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P1"
                    changable_board[b][a] = "  "
                    P1_list = []
                    print("OK")
            elif control[1] == "P2":
                a, b = f_ind("P2")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P2_list.append(showmove_board[b + 1][a])
                if control[2] not in P2_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P2"
                    changable_board[b][a] = "  "
                    P2_list = []
                    print("OK")
            elif control[1] == "P3":
                a, b = f_ind("P3")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P3_list.append(showmove_board[b + 1][a])
                if control[2] not in P3_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P3"
                    changable_board[b][a] = "  "
                    P3_list = []
                    print("OK")
            elif control[1] == "P4":
                a, b = f_ind("P4")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P4_list.append(showmove_board[b + 1][a])
                if control[2] not in P4_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P4"
                    changable_board[b][a] = "  "
                    P4_list = []
                    print("OK")
            elif control[1] == "P5":
                a, b = f_ind("P5")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P5_list.append(showmove_board[b + 1][a])
                if control[2] not in P5_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P5"
                    changable_board[b][a] = "  "
                    P5_list = []
                    print("OK")
            elif control[1] == "P6":
                a, b = f_ind("P6")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P6_list.append(showmove_board[b + 1][a])
                if control[2] not in P6_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P6"
                    changable_board[b][a] = "  "
                    P6_list = []
                    print("OK")
            elif control[1] == "P7":
                a, b = f_ind("P7")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P7_list.append(showmove_board[b + 1][a])
                if control[2] not in P7_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P7"
                    changable_board[b][a] = "  "
                    P7_list = []
                    print("OK")
            elif control[1] == "P8":
                a, b = f_ind("P8")
                if b < 7 and changable_board[b + 1][a] != "ki" and (changable_board[b + 1][a][0].islower() or changable_board[b + 1][a] == "  "):
                    P8_list.append(showmove_board[b + 1][a])
                if control[2] not in P8_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "P8"
                    changable_board[b][a] = "  "
                    P8_list = []
                    print("OK")
            elif control[1] == "n1":
                a, b = f_ind("n1")
                if b > 1 and a > 0 and changable_board[b - 2][a - 1] != "KI" and (changable_board[b - 2][a - 1][0].isupper() or changable_board[b - 2][a - 1] == "  "):
                    n11_list.append(showmove_board[b - 2][a - 1])
                if b > 1 and a < 7 and changable_board[b - 2][a + 1] != "KI" and (changable_board[b - 2][a + 1][0].isupper() or changable_board[b - 2][a + 1] == "  "):
                    n11_list.append(showmove_board[b - 2][a + 1])
                if b > 0 and a < 6 and changable_board[b - 1][a + 2] != "KI" and (changable_board[b - 1][a + 2][0].isupper() or changable_board[b - 1][a + 2] == "  "):
                    n11_list.append(showmove_board[b - 1][a + 2])
                if b < 7 and a < 6 and changable_board[b + 1][a + 2] != "KI" and (changable_board[b + 1][a + 2][0].isupper() or changable_board[b + 1][a + 2] == "  "):
                    n11_list.append(showmove_board[b + 1][a + 2])
                if b < 6 and a < 7 and changable_board[b + 2][a + 1] != "KI" and (changable_board[b + 2][a + 1][0].isupper() or changable_board[b + 2][a + 1] == "  "):
                    n11_list.append(showmove_board[b + 2][a + 1])
                if b < 6 and a > 0 and changable_board[b + 2][a - 1] != "KI" and (changable_board[b + 2][a - 1][0].isupper() or changable_board[b + 2][a - 1] == "  "):
                    n11_list.append(showmove_board[b + 2][a - 1])
                if b < 7 and a > 1 and changable_board[b + 1][a - 2] != "KI" and (changable_board[b + 1][a - 2][0].isupper() or changable_board[b + 1][a - 2] == "  "):
                    n11_list.append(showmove_board[b + 1][a - 2])
                if b > 0 and a > 1 and changable_board[b - 1][a - 2] != "KI" and (changable_board[b - 1][a - 2][0].isupper() or changable_board[b - 1][a - 2] == "  "):
                    n11_list.append(showmove_board[b - 1][a - 2])
                if b > 0 and a < 7 and changable_board[b - 1][a + 1] == "  ":
                    n11_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] == "  ":
                    n11_list.append(showmove_board[b + 1][a + 1])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] == "  ":
                    n11_list.append(showmove_board[b + 1][a - 1])
                if b > 0 and a > 0 and changable_board[b - 1][a - 1] == "  ":
                    n11_list.append(showmove_board[b - 1][a - 1])
                if control[2] not in n11_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "n1"
                    changable_board[b][a] = "  "
                    n11_list = []
                    print("OK")
            elif control[1] == "n2":
                a, b = f_ind("n2")
                if b > 1 and a > 0 and changable_board[b - 2][a - 1] != "KI" and (changable_board[b - 2][a - 1][0].isupper() or changable_board[b - 2][a - 1] == "  "):
                    n21_list.append(showmove_board[b - 2][a - 1])
                if b > 1 and a < 7 and changable_board[b - 2][a + 1] != "KI" and (changable_board[b - 2][a + 1][0].isupper() or changable_board[b - 2][a + 1] == "  "):
                    n21_list.append(showmove_board[b - 2][a + 1])
                if b > 0 and a < 6 and changable_board[b - 1][a + 2] != "KI" and (changable_board[b - 1][a + 2][0].isupper() or changable_board[b - 1][a + 2] == "  "):
                    n21_list.append(showmove_board[b - 1][a + 2])
                if b < 7 and a < 6 and changable_board[b + 1][a + 2] != "KI" and (changable_board[b + 1][a + 2][0].isupper() or changable_board[b + 1][a + 2] == "  "):
                    n21_list.append(showmove_board[b + 1][a + 2])
                if b < 6 and a < 7 and changable_board[b + 2][a + 1] != "KI" and (changable_board[b + 2][a + 1][0].isupper() or changable_board[b + 2][a + 1] == "  "):
                    n21_list.append(showmove_board[b + 2][a + 1])
                if b < 6 and a > 0 and changable_board[b + 2][a - 1] != "KI" and (changable_board[b + 2][a - 1][0].isupper() or changable_board[b + 2][a - 1] == "  "):
                    n21_list.append(showmove_board[b + 2][a - 1])
                if b < 7 and a > 1 and changable_board[b + 1][a - 2] != "KI" and (changable_board[b + 1][a - 2][0].isupper() or changable_board[b + 1][a - 2] == "  "):
                    n21_list.append(showmove_board[b + 1][a - 2])
                if b > 0 and a > 1 and changable_board[b - 1][a - 2] != "KI" and (changable_board[b - 1][a - 2][0].isupper() or changable_board[b - 1][a - 2] == "  "):
                    n21_list.append(showmove_board[b - 1][a - 2])
                if b > 0 and a < 7 and changable_board[b - 1][a + 1] == "  ":
                    n21_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] == "  ":
                    n21_list.append(showmove_board[b + 1][a + 1])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] == "  ":
                    n21_list.append(showmove_board[b + 1][a - 1])
                if b > 0 and a > 0 and changable_board[b - 1][a - 1] == "  ":
                    n21_list.append(showmove_board[b - 1][a - 1])
                if control[2] not in n21_list:
                    print("FAILED")
                else:
                    f, s = s_how(control[2])
                    changable_board[s][f] = "n2"
                    changable_board[b][a] = "  "
                    n21_list = []
                    print("OK")
            elif control[1] == "N1":
                a, b = f_ind("N1")
                if b > 1 and a > 0 and changable_board[b - 2][a - 1] != "ki" and (changable_board[b - 2][a - 1][0].islower() or changable_board[b - 2][a - 1] == "  "):
                    N11_list.append(showmove_board[b - 2][a - 1])
                if b > 1 and a < 7 and changable_board[b - 2][a + 1] != "ki" and (changable_board[b - 2][a + 1][0].islower() or changable_board[b - 2][a + 1] == "  "):
                    N11_list.append(showmove_board[b - 2][a + 1])
                if b > 0 and a < 6 and changable_board[b - 1][a + 2] != "ki" and (changable_board[b - 1][a + 2][0].islower() or changable_board[b - 1][a + 2] == "  "):
                    N11_list.append(showmove_board[b - 1][a + 2])
                if b < 7 and a < 6 and changable_board[b + 1][a + 2] != "ki" and (changable_board[b + 1][a + 2][0].islower() or changable_board[b + 1][a + 2] == "  "):
                    N11_list.append(showmove_board[b + 1][a + 2])
                if b < 6 and a < 7 and changable_board[b + 2][a + 1] != "ki" and (changable_board[b + 2][a + 1][0].islower() or changable_board[b + 2][a + 1] == "  "):
                    N11_list.append(showmove_board[b + 2][a + 1])
                if b < 6 and a > 0 and changable_board[b + 2][a - 1] != "ki" and (changable_board[b + 2][a - 1][0].islower() or changable_board[b + 2][a - 1] == "  "):
                    N11_list.append(showmove_board[b + 2][a - 1])
                if b < 7 and a > 1 and changable_board[b + 1][a - 2] != "ki" and (changable_board[b + 1][a - 2][0].islower() or changable_board[b + 1][a - 2] == "  "):
                    N11_list.append(showmove_board[b + 1][a - 2])
                if b > 0 and a > 1 and changable_board[b - 1][a - 2] != "ki" and (changable_board[b - 1][a - 2][0].islower() or changable_board[b - 1][a - 2] == "  "):
                    N11_list.append(showmove_board[b - 1][a - 2])
                if b > 0 and a < 7 and changable_board[b - 1][a + 1] == "  ":
                    N11_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] == "  ":
                    N11_list.append(showmove_board[b + 1][a + 1])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] == "  ":
                    N11_list.append(showmove_board[b + 1][a - 1])
                if b > 0 and a > 0 and changable_board[b - 1][a - 1] == "  ":
                    N11_list.append(showmove_board[b - 1][a - 1])
                if control[2] not in N11_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "N1"
                    changable_board[b][a] = "  "
                    N11_list = []
                    print("OK")
            elif control[1] == "N2":
                a, b = f_ind("N2")
                if b > 1 and a > 0 and changable_board[b - 2][a - 1] != "ki" and (changable_board[b - 2][a - 1][0].islower() or changable_board[b - 2][a - 1] == "  "):
                    N21_list.append(showmove_board[b - 2][a - 1])
                if b > 1 and a < 7 and changable_board[b - 2][a + 1] != "ki" and (changable_board[b - 2][a + 1][0].islower() or changable_board[b - 2][a + 1] == "  "):
                    N21_list.append(showmove_board[b - 2][a + 1])
                if b > 0 and a < 6 and changable_board[b - 1][a + 2] != "ki" and (changable_board[b - 1][a + 2][0].islower() or changable_board[b - 1][a + 2] == "  "):
                    N21_list.append(showmove_board[b - 1][a + 2])
                if b < 7 and a < 6 and changable_board[b + 1][a + 2] != "ki" and (changable_board[b + 1][a + 2][0].islower() or changable_board[b + 1][a + 2] == "  "):
                    N21_list.append(showmove_board[b + 1][a + 2])
                if b < 6 and a < 7 and changable_board[b + 2][a + 1] != "ki" and (changable_board[b + 2][a + 1][0].islower() or changable_board[b + 2][a + 1] == "  "):
                    N21_list.append(showmove_board[b + 2][a + 1])
                if b < 6 and a > 0 and changable_board[b + 2][a - 1] != "ki" and (changable_board[b + 2][a - 1][0].islower() or changable_board[b + 2][a - 1] == "  "):
                    N21_list.append(showmove_board[b + 2][a - 1])
                if b < 7 and a > 1 and changable_board[b + 1][a - 2] != "ki" and (changable_board[b + 1][a - 2][0].islower() or changable_board[b + 1][a - 2] == "  "):
                    N21_list.append(showmove_board[b + 1][a - 2])
                if b > 0 and a > 1 and changable_board[b - 1][a - 2] != "ki" and (changable_board[b - 1][a - 2][0].islower() or changable_board[b - 1][a - 2] == "  "):
                    N21_list.append(showmove_board[b - 1][a - 2])
                if b > 0 and a < 7 and changable_board[b - 1][a + 1] == "  ":
                    N21_list.append(showmove_board[b - 1][a + 1])
                if b < 7 and a < 7 and changable_board[b + 1][a + 1] == "  ":
                    N21_list.append(showmove_board[b + 1][a + 1])
                if b < 7 and a > 0 and changable_board[b + 1][a - 1] == "  ":
                    N21_list.append(showmove_board[b + 1][a - 1])
                if b > 0 and a > 0 and changable_board[b - 1][a - 1] == "  ":
                    N21_list.append(showmove_board[b - 1][a - 1])
                if control[2] not in N21_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "N2"
                    changable_board[b][a] = "  "
                    N21_list = []
                    print("OK")
            elif control[1] == "r1":
                a, b = f_ind("r1")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "KI" and (changable_board[b][a + z][0].isupper() or changable_board[b][a + z] == "  "):
                        r11_list.append(showmove_board[b][a + z])
                    if a + z < 8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "KI" and (changable_board[b][a - z1][0].isupper() or changable_board[b][a - z1] == "  "):
                        r11_list.append(showmove_board[b][a - z1])
                    if a - z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "KI" and (changable_board[b + z2][a][0].isupper() or changable_board[b + z2][a] == "  "):
                        r11_list.append(showmove_board[b + z2][a])
                    if b + z2 < 8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b - z3][a] != "KI" and (changable_board[b - z3][a][0].isupper() or changable_board[b - z3][a] == "  "):
                        r11_list.append(showmove_board[b - z3][a])
                    if b - z3 > (-1) and changable_board[b - z3][a] != "  ":
                        break
                if control[2] not in r11_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "r1"
                    changable_board[b][a] = "  "
                    r11_list = []
                    print("OK")
            elif control[1] == "r2":
                a, b = f_ind("r2")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "KI" and (changable_board[b][a + z][0].isupper() or changable_board[b][a + z] == "  "):
                        r21_list.append(showmove_board[b][a + z])
                    if a + z < 8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "KI" and (changable_board[b][a - z1][0].isupper() or changable_board[b][a - z1] == "  "):
                        r21_list.append(showmove_board[b][a - z1])
                    if a - z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "KI" and (changable_board[b + z2][a][0].isupper() or changable_board[b + z2][a] == "  "):
                        r21_list.append(showmove_board[b + z2][a])
                    if b + z2 < 8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b - z3][a] != "KI" and (changable_board[b - z3][a][0].isupper() or changable_board[b - z3][a] == "  "):
                        r21_list.append(showmove_board[b - z3][a])
                    if b - z3 > (-1) and changable_board[b - z3][a] != "  ":
                        break
                if control[2] not in r21_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "r2"
                    changable_board[b][a] = "  "
                    r21_list = []
                    print("OK")
            elif control[1] == "R1":
                a, b = f_ind("R1")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "ki" and (changable_board[b][a + z][0].islower() or changable_board[b][a + z] == "  "):
                        R11_list.append(showmove_board[b][a + z])
                    if a + z < 8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "ki" and (changable_board[b][a - z1][0].islower() or changable_board[b][a - z1] == "  "):
                        R11_list.append(showmove_board[b][a - z1])
                    if a - z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "ki" and (changable_board[b + z2][a][0].islower() or changable_board[b + z2][a] == "  "):
                        R11_list.append(showmove_board[b + z2][a])
                    if b + z2 < 8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b - z3][a] != "ki" and (changable_board[b - z3][a][0].islower() or changable_board[b - z3][a] == "  "):
                        R11_list.append(showmove_board[b - z3][a])
                    if b - z3 > (-1) and changable_board[b - z3][a] != "  ":
                        break
                if control[2] not in R11_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "R1"
                    changable_board[b][s] = "  "
                    R11_list = []
                    print("OK")
            elif control[1] == "R2":
                a, b = f_ind("R2")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "ki" and (changable_board[b][a + z][0].islower() or changable_board[b][a + z] == "  "):
                        R21_list.append(showmove_board[b][a + z])
                    if a + z < 8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "ki" and (changable_board[b][a - z1][0].islower() or changable_board[b][a - z1] == "  "):
                        R21_list.append(showmove_board[b][a - z1])
                    if a - z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "ki" and (changable_board[b + z2][a][0].islower() or changable_board[b + z2][a] == "  "):
                        R21_list.append(showmove_board[b + z2][a])
                    if b + z2 < 8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b - z3][a] != "ki" and (changable_board[b - z3][a][0].islower() or changable_board[b - z3][a] == "  "):
                        R21_list.append(showmove_board[b - z3][a])
                    if b - z3 > (-1) and changable_board[b - z3][a] != "  ":
                        break
                if control[2] not in R21_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "R2"
                    changable_board[b][a] = "  "
                    R21_list = []
                    print("OK")
            elif control[1] == "b1":
                a, b = f_ind("b1")
                for z in range(1, 8):
                    if b - z > (-1) and a + z < 8 and changable_board[b - z][a + z] != "KI" and (changable_board[b - z][a + z][0].isupper() or changable_board[b - z][a + z] == "  "):
                        b11_list.append(showmove_board[b - z][a + z])
                    if b - z > (-1) and a + z < 8 and changable_board[b - z][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if b - z1 > (-1) and a - z1 > (-1) and changable_board[b - z1][a - z1] != "KI" and (changable_board[b - z1][a - z1][0].isupper() or changable_board[b - z1][a - z1] == "  "):
                        b11_list.append(showmove_board[b - z1][a - z1])
                    if b - z1 > (-1) and a - z1 > (-1) and changable_board[b - z1][a - z1] != "  ":
                        break
                if control[2] not in b11_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "b1"
                    changable_board[b][a] = "  "
                    b11_list = []
                    print("OK")
            elif control[1] == "b2":
                a, b = f_ind("b2")
                for z in range(1, 8):
                    if b - z > (-1) and a + z < 8 and changable_board[b - z][a + z] != "KI" and (changable_board[b - z][a + z][0].isupper() or changable_board[b - z][a + z] == "  "):
                        b21_list.append(showmove_board[b - z][a + z])
                    if b - z > (-1) and a + z < 8 and changable_board[b - z][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if b - z1 > (-1) and a - z1 > (-1) and changable_board[b - z1][a - z1] != "KI" and (changable_board[b - z1][a - z1][0].isupper() or changable_board[b - z1][a - z1] == "  "):
                        b21_list.append(showmove_board[b - z1][a - z1])
                    if b - z1 > (-1) and a - z1 > (-1) and changable_board[b - z1][a - z1] != "  ":
                        break
                if control[2] not in b21_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "b2"
                    changable_board[b][a] = "  "
                    b21_list = []
                    print("OK")
            elif control[1] == "B1":
                a, b = f_ind("B1")
                for z in range(1, 8):
                    if b + z < 8 and a - z > (-1) and changable_board[b + z][a - z] != "ki" and (changable_board[b + z][a - z][0].islower() or changable_board[b + z][a - z] == "  "):
                        B11_list.append(showmove_board[b + z][a - z])
                    if b + z < 8 and a - z > (-1) and changable_board[b + z][a - z] != "  ":
                        break
                for z1 in range(1, 8):
                    if b + z1 < 8 and a + z1 < 8 and changable_board[b + z1][a + z1] != "ki" and (changable_board[b + z1][a + z1][0].islower() or changable_board[b + z1][a + z1] == "  "):
                        B11_list.append(showmove_board[b + z1][a + z1])
                    if b + z1 < 8 and a + z1 < 8 and changable_board[b + z1][a + z1] != "  ":
                        break
                if control[2] not in B11_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "B1"
                    changable_board[b][a] = "  "
                    B11_list = []
                    print("OK")
            elif control[1] == "B2":
                a, b = f_ind("B2")
                for z in range(1, 8):
                    if b + z < 8 and a - z > (-1) and changable_board[b + z][a - z] != "ki" and (changable_board[b + z][a - z][0].islower() or changable_board[b + z][a - z] == "  "):
                        B21_list.append(showmove_board[b + z][a - z])
                    if b + z < 8 and a - z > (-1) and changable_board[b + z][a - z] != "  ":
                        break
                for z1 in range(1, 8):
                    if b + z1 < 8 and a + z1 < 8 and changable_board[b + z1][a + z1] != "ki" and (changable_board[b + z1][a + z1][0].islower() or changable_board[b + z1][a + z1] == "  "):
                        B21_list.append(showmove_board[b + z1][a + z1])
                    if b + z1 < 8 and a + z1 < 8 and changable_board[b + z1][a + z1] != "  ":
                        break
                if control[2] not in B21_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "B2"
                    changable_board[b][a] = "  "
                    B21_list = []
                    print("OK")
            elif control[1] == "qu":
                a, b = f_ind("qu")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "KI" and (changable_board[b][a + z][0].isupper() or changable_board[b][a + z] == "  "):
                        qu1_list.append(showmove_board[b][a + z])
                    if a + z < 8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "KI" and (changable_board[b][a - z1][0].isupper() or changable_board[b][a - z1] == "  "):
                        qu1_list.append(showmove_board[b][a - z1])
                    if a - z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "KI" and (changable_board[b + z2][a][0].isupper() or changable_board[b + z2][a] == "  "):
                        qu1_list.append(showmove_board[b + z2][a])
                    if b + z2 < 8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b - z3][a] != "KI" and (changable_board[b - z3][a][0].isupper() or changable_board[b - z3][a] == "  "):
                        qu1_list.append(showmove_board[b - z3][a])
                    if b - z3 > (-1) and changable_board[b - z3][a] != "  ":
                        break
                for z4 in range(1, 8):
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "KI" and (changable_board[b - z4][a + z4][0].isupper() or changable_board[b - z4][a + z4] == "  "):
                        qu1_list.append(showmove_board[b - z4][a + z4])
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "  ":
                        break
                for z5 in range(1, 8):
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "KI" and (changable_board[b - z5][a - z5][0].isupper() or changable_board[b - z5][a - z5] == "  "):
                        qu1_list.append(showmove_board[b - z5][a - z5])
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "  ":
                        break
                for z6 in range(1, 8):
                    if b + z6 < 8 and a - z6 > (-1) and changable_board[b + z6][a - z6] != "KI" and (changable_board[b + z6][a - z6][0].isupper() or changable_board[b + z6][a - z6] == "  "):
                        qu1_list.append(showmove_board[b + z6][a - z6])
                    if b + z6 < 8 and a - z6 > (-1) and changable_board[b + z6][a - z6] != "  ":
                        break
                for z7 in range(1, 8):
                    if b + z7 < 8 and a + z7 < 8 and changable_board[b + z7][a + z7] != "KI" and (changable_board[b + z7][a + z7][0].isupper() or changable_board[b + z7][a + z7] == "  "):
                        qu1_list.append(showmove_board[b + z7][a + z7])
                    if b + z7 < 8 and a + z7 < 8 and changable_board[b + z7][a + z7] != "  ":
                        break
                if control[2] not in qu1_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "qu"
                    changable_board[b][a] = "  "
                    qu1_list = []
                    print("OK")
            elif control[1] == "QU":
                a, b = f_ind("QU")
                for z in range(1, 8):
                    if a + z < 8 and changable_board[b][a + z] != "ki" and (changable_board[b][a + z][0].islower() or changable_board[b][a + z] == "  "):
                        QU1_list.append(showmove_board[b][a + z])
                    if a + z < 8 and changable_board[b][a + z] != "  ":
                        break
                for z1 in range(1, 8):
                    if a - z1 > (-1) and changable_board[b][a - z1] != "ki" and (changable_board[b][a - z1][0].islower() or changable_board[b][a - z1] == "  "):
                        QU1_list.append(showmove_board[b][a - z1])
                    if a - z1 > (-1) and changable_board[b][a - z1] != "  ":
                        break
                for z2 in range(1, 8):
                    if b + z2 < 8 and changable_board[b + z2][a] != "ki" and (changable_board[b + z2][a][0].islower() or changable_board[b + z2][a] == "  "):
                        QU1_list.append(showmove_board[b + z2][a])
                    if b + z2 < 8 and changable_board[b + z2][a] != "  ":
                        break
                for z3 in range(1, 8):
                    if b - z3 > (-1) and changable_board[b - z3][a] != "ki" and (changable_board[b - z3][a][0].islower() or changable_board[b - z3][a] == "  "):
                        QU1_list.append(showmove_board[b - z3][a])
                    if b - z3 > (-1) and changable_board[b - z3][a] != "  ":
                        break
                for z4 in range(1, 8):
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "ki" and (changable_board[b - z4][a + z4][0].islower() or changable_board[b - z4][a + z4] == "  "):
                        QU1_list.append(showmove_board[b - z4][a + z4])
                    if b - z4 > (-1) and a + z4 < 8 and changable_board[b - z4][a + z4] != "  ":
                        break
                for z5 in range(1, 8):
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "ki" and (changable_board[b - z5][a - z5][0].islower() or changable_board[b - z5][a - z5] == "  "):
                        QU1_list.append(showmove_board[b - z5][a - z5])
                    if b - z5 > (-1) and a - z5 > (-1) and changable_board[b - z5][a - z5] != "  ":
                        break
                for z6 in range(1, 8):
                    if b + z6 < 8 and a - z6 > (-1) and changable_board[b + z6][a - z6] != "ki" and (changable_board[b + z6][a - z6][0].islower() or changable_board[b + z6][a - z6] == "  "):
                        QU1_list.append(showmove_board[b + z6][a - z6])
                    if b + z6 < 8 and a - z6 > (-1) and changable_board[b + z6][a - z6] != "  ":
                        break
                for z7 in range(1, 8):
                    if b + z7 < 8 and a + z7 < 8 and changable_board[b + z7][a + z7] != "ki" and (changable_board[b + z7][a + z7][0].islower() or changable_board[b + z7][a + z7] == "  "):
                        QU1_list.append(showmove_board[b + z7][a + z7])
                    if b + z7 < 8 and a + z7 < 8 and changable_board[b + z7][a + z7] != "  ":
                        break
                if control[2] not in QU1_list:
                    print("FAILED")
                else:
                    f,s = s_how(control[2])
                    changable_board[s][f] = "QU"
                    changable_board[b][a] = "  "
                    QU1_list = []
                    print("OK")
        elif to_do == "print":
            print("-----------------------")
            for i in changable_board:
                for k in i:
                    print(k,end=" ")
                print()
            print("-----------------------")