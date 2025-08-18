
# Strings

s="Hello"
print(s[1])
s1= 'hello'
print(s1[::-1])
print(s[4])
print(s[-1])



list= [1, 2, [3, 4, 'hello']]
list[2][2]='goodbye'
print(list)

list1= [5, 3, 4, 6, 1]
list1.sort()
print(list1)


d= {'simple key':'hello'}
print(d["simple key"])

d1= {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d2=  {'k1':[{'nest key':['this is deep', ['hello']]}]}
print(d2['k1'][0]['nest key'][1][0])

d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])