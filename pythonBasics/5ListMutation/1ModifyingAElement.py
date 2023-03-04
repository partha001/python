webBrowsers= ["chrome","firefox","safari"]
print(webBrowsers) #op: ['chrome', 'firefox', 'safari']

webBrowsers[-1] ="Opera"
webBrowsers[0] = "google chrome"
print(webBrowsers) #op: ['google chrome', 'firefox', 'Opera']


#note that this can not be used to add new element to the end of the list
#webBrowsers[3] ="Opera" #this will give IndexError

#this is only used to modify the element at a particular index of the list

