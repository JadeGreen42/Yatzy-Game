def scoring(option, copybar):
    if option in range(1,7):
        return option*str(copybar).count(str(option)), True
    
    elif option == 7:
        for x in set(copybar):
            if copybar.count(x) >=3:
                return sum(copybar), None
            
    elif option == 8:
        for x in set(copybar):
            if copybar.count(x) >=4:
                return sum(copybar), None

    elif option == 9:
        counts = [copybar.count(x) for x in set(copybar)]
        if sorted(counts) == [2,3]:
            return 25, None

    elif option == 10:
        s = set(copybar)
        straights = [{1,2,3,4},{2,3,4,5},{3,4,5,6}]
        if any(st.issubset(s) for st in straights) == True:
            return 30, None
        
    elif option == 11:
        s = set(copybar)
        straights = [{1,2,3,4,5},{2,3,4,5,6}]
        if any(st.issubset(s) for st in straights) == True:
            return 40, None
        
    elif option == 12:
        if len(set(copybar))==1:
            return 50, None
        
    elif option == 13:
        return sum(copybar), None

    return 0, None
    
slots = {
    1: "Sum of 1s",
    2: "Sum of 2s",
    3: "Sum of 3s",
    4: "Sum of 4s",
    5: "Sum of 5s",
    6: "Sum of 6s",
    7: "3 of a kind",
    8: "4 of a kind",
    9: "Full house",
    10: "Small",
    11: "Large",
    12: "Yatzy",
    13: "Chance"
}
