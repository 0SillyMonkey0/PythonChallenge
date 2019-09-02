# Look-and-say sequence

import re
a = '1'
for i in range(30):
    next_a = ''
    for j, c in enumerate(a):
        if j == 0:
            counter = 1
            last_c = c
        else:
            if c == last_c:
                counter += 1
            else:
                next_a += (str(counter) + last_c)
                counter = 1
            if j == len(a) - 1:
                next_a += (str(counter) + c)
            
        last_c = c

    if next_a == '':
        next_a += (str(counter) + last_c)
    a  = next_a
    # print(a)
    print(len(a))
# print(len(next_a))

