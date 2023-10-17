x = input() #replace with whatever if you want
p = 0; l = [0]; L = 0; c = 0; C = [] #data
for i in enumerate(x): #[] stuff
    if i[1] == '[': c += 1; C.append([i[0]])
    try: 
        if i[1] == ']': c -= 1; C[c].append(i[0])   
    except Exception: print(f"left ] at {i[0]}"); exit(1)
for i in C:
    if not len(i) == 2: print(f"""\
left [ at {i[0]}""" if len(i) < 2 else f"left ] at {i[2]}"); exit(1)
c = -1; i = 0 #this is the fun part
while i < len(x):
    match x[i]: #which instruction?
        case '+': l[p+L] += 1; i += 1; continue
        case '-': l[p+L] -= 1; i += 1; continue
        case '>': 
            if p == 0: l.append(0)
            p += 1; i += 1; continue
        case '.': print(';'+chr(l[p+L])); i += 1; continue
        case ',': l[p+L] = ord(input(':')); i += 1; continue
        case '<':
            if p == len(l): l.insert(0, 0)
            L += 1; p -= 1; i += 1; continue
        case '[':
            c += 1;
            if l[p+L] == 0: i = C[c][1]
            else: i += 1; continue
        case ']':
            if not l[p+L] == 0: i = C[c][0] 
            else: c -= 1
            i += 1; continue
        case _: i += 1; continue
