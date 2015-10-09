from os import system

print "---------------------------------------------------------------------------------"
print "Send file or directory to ocracoke. The gateway password will be asked two times."
print "---------------------------------------------------------------------------------"
print

#Get string
path = raw_input("Insert file/directory local path: ") #ask the user for the local path

n = path.count("/") #count the number of / occurences
fd_name = path.rsplit("/",n)[n] #split the string every time you find "/" and return me the last piece, which is the directory/file name

#Define args
gateway = "gcazzolli@dogmans.umaryland.edu" #do not touch
remote = "cazzolli@ocracoke" #do not touch

bridge_directory = "send_to_ocracoke" #can be modified
target_dir = "DRP/implicit/" #can be modified

#Define the bash command
bash_command = "scp -r %s %s:~/%s && scp -r %s:~/%s/%s %s:~/%s" \
               % (path, gateway, bridge_directory, gateway, bridge_directory, fd_name, remote, target_dir)

#Run script
system(bash_command)






