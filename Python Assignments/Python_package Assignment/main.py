from List import Custom_list
from Dictionary import Custom_dict
from Set import Custom_set
from Tuple import Custom_tuple

##################### list ########################################

l = [1,2,3]
l_obj = Custom_list(l)
print(l_obj.lst)
l_obj.append_list('s')
print(l_obj.lst)
#l_obj.clear_list()
#print(l_obj.l)
y=l_obj.copy_list()
print(l_obj.lst)
print(y)
y.append([4,5])
print(y)
print(l_obj.lst)
print(l_obj.count_list([4,5]))
print(l_obj.lst)
print(l_obj.extend_list([4,5,[66,77]]))
print(l_obj.lst)
print('hi')
#print(l_obj.pop_list(2))
#print(l_obj.l)
#print(l_obj.remove_list([66, 77]))
#print(l_obj.l)
print(l_obj.reverse_list())
print(l_obj.lst)

##################### dictionary ########################################
d={1: 2,
 3: 4,
 5: {7: 8, 's': 'sush'},
 7: [1, 55, 66, 88],
 12: 'lll',
 222222: 'dddddddddddd'}
d_obj = Custom_dict(d)
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)

##################### set ########################################
s = {34,12,56}
s_obj = Custom_set(s)
print(s_obj.s)
print(s_obj.add_set(26))
print(s_obj.s)
print(s_obj.copy_set())
print(s_obj.difference_set({11,45,32}))
print(s_obj.difference_update_set({34,26,12}))
print(s_obj.discard_set(12))


##################### tuple ########################################

t = (100, 200, 300,200,)
t_obj = Custom_tuple(t)
print(t_obj.t)
print(t_obj.count_tuple(200))
print(t_obj.index_tuple(300))