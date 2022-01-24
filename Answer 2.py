#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Answer 2
marks = {}
n = int(input())
for x in range(n):
    name = input()
    mark = float(input())
    
    if mark in marks:
        marks[mark].append(name)
    else:
        marks[mark] = [name]
        
all_marks = list(set(marks.keys()))
all_marks.sort()
names_ordered = marks[all_marks[1]]
names_ordered.sort()

for name in names_ordered:
    print(name)


# In[ ]:




