adverse_count=0

def check_adverse(last_fill_price, mid_after):
    global adverse_count

    if mid_after> last_fill_price:
        adverse_count += 1
    else:
        adverse_count = max(adverse_count-1, 0)

    if adverse_count>=3:
        return True   #Toxic flow detected
    return False


check_adverse(110.05, 110.15)
