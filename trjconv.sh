source /usr/local/gromacs/bin/GMXRC #optional 

a=1

while [ $a -lt 4 ] #insert_folders_number+1
do
	cd TRIAL_$a
	echo 1 | trjconv -f md-gb.trr -s md-gb.tpr -o md.gb.pdb 
	cd .. 
	a=`expr $a + 1`
done

