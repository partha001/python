# for slicing we pass list[startInde:endIndex] where startIndex is inclusive and the endIndex is exclusive
webBrowsers= ["chrome","firefox","safari","Opera"]
print(webBrowsers[0:1]) #op: ['chrome']

#using slicing actually returns a new list object

#not mentioning any endIndex will read all the elements including the last
print(webBrowsers[2:])  #op: ['safari', 'Opera']

#similarly not mentioning the startIndex will slice it from the start of the list
print(webBrowsers[: 2]) #op: ['chrome', 'firefox']


#we can also additionally provide a third parameter to the slicing method i.e the sliceInterval
print(webBrowsers[::1])  #op: ['chrome', 'firefox', 'safari', 'Opera']
print(webBrowsers[::2]) #op: ['chrome', 'safari']

#making use of it we can easily reverse a list as shown below 
print(webBrowsers[::-1])  #op: ['Opera', 'safari', 'firefox', 'chrome']
print(webBrowsers[::-2])  #op: ['Opera', 'firefox']


#using slicing actually returns a new list object
#and hence the initial list remains same
print(webBrowsers) #op: ['chrome', 'firefox', 'safari', 'Opera']