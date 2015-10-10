#this is a python script which is able to send files directly to ocracoke from whichever directory on your pc and to get
#files from ocracoke on the directory in which you are running the script. Both the operations will ask you twice the
#gateway password. There is the possibility to ask the password only once, but of course I'm not going to implement it as long
# as the script exists in GitHub.


import pxssh #python ssh
import getpass #a special kind of raw_input which does not show what you are writing
import os #run bash commands

#we have 2 machines here: dogmans (avalon) and ocracoke. We want to send and receive files from ocracoke.
#The package pxssh opens an ssh session and permits us to send remote commands without quitting python

print "---------------------------------------------------"
print "| Send/get a file or a directory to/from ocracoke |"
print "---------------------------------------------------"
print

#INFO
g_username = "gcazzolli"
g_hostname = "dogmans.umaryland.edu"
c_address = "cazzolli@ocracoke"
bridge_directory = "send_to_ocracoke" #can be modified
target_dir = "DRP/implicit/" #can be modified
pass_string = g_username + "@" + g_hostname + "'s password: "

#ACTIONS
what_to_do = raw_input("Send or get? (s or g): ") #ask the user if he wants to send or get stuff
path = raw_input("Insert file/directory path: ") #ask the user for the local path
n = path.count("/") #count the number of / occurences
fd_name = path.rsplit("/",n)[n] #split the string every time you find "/" and return me the last piece, which is the directory/file name

if( what_to_do == "s" ):
    bash_command = "scp -r " + path + " " + g_username + "@" + g_hostname + ":~/" + bridge_directory
    os.system(bash_command) #run script: password will be asked

    try:
        #establish ssh connection with gateway
        print
        print "Establishing ssh connection"
        s = pxssh.pxssh()
        password = getpass.getpass(pass_string)
        s.login (g_hostname, g_username, password)

        print
        print "Changing directory"
        #change directory to the bridge directory
        s.sendline ('cd send_to_ocracoke') # run a command
        s.prompt() # match the prompt
        print s.before # print everything before the prompt.

        print "Copying file to ocracoke"
        #secure copy the files to ocracoke
        scp_string = "scp -r " + fd_name + " " + c_address + ":~/" + target_dir + fd_name
        s.sendline (scp_string)
        s.prompt()
        print s.before

        print "Deleting file from dogmans"
        #delete everything from the bridge directory
        del_string = "rm -r " + fd_name
        s.sendline (del_string)
        s.prompt()
        print s.before

        s.logout()

    except pxssh.ExceptionPxssh, e:
        print "Pxssh failed on login."
        print str(e)

elif( what_to_do == "g" ):
    try:
        #establish ssh connection with gateway
        print
        print "Establishing ssh connection"
        s = pxssh.pxssh()
        password = getpass.getpass(pass_string)
        s.login (g_hostname, g_username, password)

        print
        print "Changing directory"
        #change directory to the bridge directory
        s.sendline ('cd send_to_ocracoke') # run a command
        s.prompt() # match the prompt
        print s.before # print everything before the prompt.

        print "Copying file to dogmans"
        #secure copy the files to dogmans from ocracoke
        scp_string = "scp -r " + c_address + ":~/" + target_dir + fd_name + " ."
        s.sendline (scp_string)
        s.prompt()
        print s.before

        print "Copying locally"
        bash_command = "scp -r " + g_username + "@" + g_hostname + ":~/" + bridge_directory + "/" + fd_name + " ."
        os.system(bash_command) #run script: password will be asked

        print
        print "Deleting file from dogmans"
        #delete everything from the bridge directory
        del_string = "rm -r " + fd_name
        s.sendline (del_string)
        s.prompt()
        print s.before

        s.logout()

    except pxssh.ExceptionPxssh, e:
        print "Pxssh failed on login."
        print str(e)

else:
    print "No match found."