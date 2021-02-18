#returns approved, incresed/decreased, number
def main(last2, last1, new):
    if new >= 100 or last1 >= 100 or last2 >= 100: #if too far
        return ["FAR", new]
    if abs(last1 - new) >= 30: #if big difference
        return ["BIG", new]
    if abs(last1 - new) <= 0.5: #if very small difference
        return ["SMALL", new]
    if last2 < last1 < new: #if stable increase
        if (last1-last2)/last2 >= 0.02 and (new-last1)/last1 >= 0.02: #if stable changes above 5% of distance
            amount = int(((last1-last2)/last2 + (new-last1)/last1) * 20)
            return [True, "increase", amount] #increase
    if last2 > last1 > new: #if stable decrease
        #if (last2-last1)/last1 >= 0.01 and (last1-new)/new >= 0.01: #if stable changes above 5% of distance
        if (last1-new)/new >= 0.007:
            amount = int(((last1-new)/new) * 30)
            return [True, "decrease", amount] #decrase
    else:
        return ["ELSE", last2, last1, new]
        
if __name__ == "__main__":
    main(args)
