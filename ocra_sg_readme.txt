Description of ocra_sg.py:
this is a python script which is able to send files directly to ocracoke from whichever directory on your pc and to get files from ocracoke on the directory in which you are running the script. Both the operations will ask you twice the gateway password. There is the possibility to ask the password only once, but I'm not going to implement it as long as the script exists in GitHub. 

#BUGS:
- if the directory you are copying from ocracoke (i.e. test_dir/) already exists inside the directory in which you are running the script, the script will copy the directory inside the other one (so you will find test_dir/test_dir). We have to find out why and fix it;

#TODO:
- we can implement automated compression of a directory before sending
- if you fail in writing the password when establishing the ssh connection, the script crashes and the password will not be asked again. We should implement a while loop which asks the password until you get it correctly. 
- if you fail at writing something, the script will go on returning errors and stuff so that you will need to start over. We should think about a better way to deal with such situation. 