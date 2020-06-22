#This code gets all the files in a folder and writes their locations
#line by line to a text file

#This function gets the filepath of a set of picture files in a folder
def getim_list(path):
    return[os.path.join(path,f) for f in os.listdir(path) if f.endswith('jpg')]

imlist=getim_list('infolder location')

#Loops through the files in a folder
for elem in imlist:
 #writes the file names to a textfile line by line
 fh = open("outfile location.txt", "a") 
 fh.write(str(elem)+'\n') 
 fh.close 