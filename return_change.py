
def get_change(denominations: list, target_money: int):
    if target_money == 0:
        return True
    if target_money < 0:
        return False
    
    for denomination in denominations:
        if get_change(denominations, target_money - denomination):
            return True
        

print(get_change([5,10,25,100,200], 95))
