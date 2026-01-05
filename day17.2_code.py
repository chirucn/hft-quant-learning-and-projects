price=[100, 100.1,100.05,100.2,100.15]

for p in price:
    if p>100.1:
        print("Price moved up:", p)
    else:
        print("No strong move:", p)
