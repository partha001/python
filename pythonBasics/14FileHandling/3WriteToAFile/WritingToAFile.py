#if the doesnt exit then the file will be created by the below code
#however if the file exists then python will not add content to it. 
#rather it will replace the file enterily with the new content
filename = "sampleFile.txt"
with open(filename,"w") as fileObject:
    fileObject.write("this is line1")
    fileObject.write("this is line2") ##this will add "Hello file.line2" to the end of previous line
    ##to have line breaks we need to have new line characters as show below 
    fileObject.write("\nthis is line3")