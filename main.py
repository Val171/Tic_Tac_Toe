import time

square = "🔲"
cross = "❌"
circle = "🟢"

class Square():
    def __init__(self, typ, coords):
        self.typ = typ
        self.coord = coords

coods = ["(1,1)","(1,2)","(1,3)","(2,1)","(2,2)","(2,3)","(3,1)","(3,2)","(3,3)"]

boxes = []
for i in coods:
    boxes.append(Square(typ="🔲", coords=i))

while True:
    print(f"  1 2 3\n"
          f"1{boxes[0].typ}{boxes[1].typ}{boxes[2].typ}\n"
          f"2{boxes[3].typ}{boxes[4].typ}{boxes[5].typ}\n"
          f"3{boxes[6].typ}{boxes[7].typ}{boxes[8].typ}")
    play = input("Your Turn (player1): (y,x): ")

    for i in boxes:
        if i.coord == play:
            if i.typ == f"{circle}" or i.typ == f"{cross}":
                print(f"Invalid Move {cross}")
            else:
                i.typ = f"{cross}"

    print(f"  1 2 3\n"
          f"1{boxes[0].typ}{boxes[1].typ}{boxes[2].typ}\n"
          f"2{boxes[3].typ}{boxes[4].typ}{boxes[5].typ}\n"
          f"3{boxes[6].typ}{boxes[7].typ}{boxes[8].typ}")

    play2 = input("Your Turn (player2): (y,x): ")

    for i in boxes:
        if i.coord == play2:
            if i.typ == f"{circle}" or i.typ == f"{cross}":
                print(f"Invalid Move {cross}")
            else:
                i.typ = f"{circle}"

    if play2 == "R" or play == "R":
        for i in boxes:
            i.typ = f"{square}"
        print("\nResetting Board...\n")
        time.sleep(2)









