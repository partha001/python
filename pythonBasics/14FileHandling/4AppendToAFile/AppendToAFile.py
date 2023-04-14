#for appending we have to open the file in append mode
#here again if the file doesnt exist then python will creat the file for us
filename = "sampleFile.txt"
with open(filename,"a") as fileObject:
    fileObject.write("this is line4")
    fileObject.write("this is line5") ##this will add "Hello file.line2" to the end of previous line
    ##to have line breaks we need to have new line characters as show below 
    fileObject.write("\nthis is line6")