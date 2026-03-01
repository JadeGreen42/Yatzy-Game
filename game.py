
from logic import SingleRound
from scoring import scoring, slots


def run_game():
    total = 0
    minisum = 0
    used = set()
    for rounds in range(13):
        cb = SingleRound()
        #print("cb: ", cb)
        for k in slots:
            if k not in used:
                print(k,":", slots[k])
        while True:
            choice = int(input("Pick slot: "))
            if choice in slots:
                break
            print("Already used or invalid. Pick again")
        b,flag = scoring(choice, cb)
        if flag == True:
            minisum = minisum + b
        if minisum >= 63:
            total = total + 35
        print("Your score: ", b)
        total = total + b
        used.add(choice)
        # del slots[choice]
        print("Total score:", total)
        print("Mini score:", minisum)
    return total
