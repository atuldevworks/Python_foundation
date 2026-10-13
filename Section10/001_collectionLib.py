from collections import Counter,defaultdict,OrderedDict,deque as dq


lst1=[111,1,1,12,221,1,1,11,1,1,1]
ctr=Counter(lst1)
print(ctr)


fruits=["apple","orange","mango","apple"]
defaultValue=10000
cnt=defaultdict(lambda:defaultValue)

for f in fruits:
    cnt[f]+=1
    
print(cnt)

print(cnt["tomato"])


ordDict=OrderedDict()
ordDict["rolf"]=4
ordDict["mike"]=33

print(ordDict["mike"])



friends=dq(('rolf','mike','tomson','ram'))
print(friends)
friends.append('shyam')
print(friends)
friends.appendleft("rahman")
print(friends)
print(friends.popleft())
print(friends)
print(friends.pop())
print(friends)