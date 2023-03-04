webBrowsers= ["chrome","firefox","safari","Opera"]

print(enumerate(webBrowsers)) #<enumerate object at 0x000001FDB88767F0>
print(type(enumerate(webBrowsers))) #<class 'enumerate'>

for i, browser in enumerate(webBrowsers):
    print(f"{i} value {browser}")


#now if there is a requirement to traverse all element from the second position
#one way we can do it as    for element in elements[1:]
#however we can do the same using enumerator as shown below 
for idx, browser in enumerate(webBrowsers,1):
     print(f"{idx} value {browser}")


