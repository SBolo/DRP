#THIS SCRIPT DOWNLOADS ONLY FROM GCAZZOLLI

#Firstly, move files to the gcazzolli domain
#Go to ocracoke and type
#    scp yourfile gcazzolli@dogmans.umaryland.edu:~/send_to_ocracoke


import os
print "---------------------------------------------------------------------------------"
print "Get file or directory from gcazzolli (not ocracoke)"
print "---------------------------------------------------------------------------------"
print
#get string
g_path = raw_input("insert file/directory path in gcazzolli domain (as pwd output) \n")
home_path = raw_input("insert your local path \n")
os.system("sudo scp -r gcazzolli@dogmans.umaryland.edu:" + g_path + " " + home_path)
n = g_path.count("/") #count the number of / occurences
fd_name = g_path.rsplit("/",n)[n] #split the string every time you find "/" and return me the last piece, which is the directory/file name
os.system("sudo chmod -R 777 " + fd_name)