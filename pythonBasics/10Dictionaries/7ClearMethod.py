websites = {
    "wikipedia" : "http://www.wikipedia.org",
    "google": "http://www.google.com",
    "netflix": "http://www.netflix.com"
}

print(websites) #op: {'wikipedia': 'http://www.wikipedia.org', 'google': 'http://www.google.com', 'netflix': 'http://www.netflix.com'}
websites.clear()
print(websites) #op: {}
# it is to be noted that the dictionary object still continues exist in the memory as an empty dictionary and can be resused
# just that all its contents i.e. key value pairs are removed from it and 

