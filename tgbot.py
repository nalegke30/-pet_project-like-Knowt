from collections import OrderedDict
def custom_sort(data):
    result = OrderedDict()
    lst = []
    for i in sorted(data):
        data.move_to_end(i,last=True)
    
data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)