dd = {33:'a', 5:'g', 10: 'h'}

dd = dict(sorted(dd.items()))

for k in dd:
    print(dd.get(k))


