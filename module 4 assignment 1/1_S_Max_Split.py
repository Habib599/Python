S = input()

bln_string = []  
c_string = ""
count = 0

for char in S:
    c_string += char  
    if char == 'L':
        count += 1
    else:
        count -= 1
    
    if count == 0:
        bln_string.append(c_string)
        c_string = ""

print(len(bln_string))
for out in bln_string:
    print(out)