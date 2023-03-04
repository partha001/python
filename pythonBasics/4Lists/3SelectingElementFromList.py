webBrowsers= ["chrome","firefox","safari","Opera"]
print(webBrowsers[0]) #op: chrome

# however the below will throw IndexError
#print(webBrowsers[7])

# as we have seen in case of fetching characters from strings similarly we
# can use negative index to fetch values from the end of the list
print(webBrowsers[-1]) #op: Opera
#however the below will throw IndexError
#print(webBrowsers[-7]) #op: IndexError


