source /usr/local/gromacs/bin/GMXRC

a=1

while [ $a -lt 4 ] #insert_folders_number+1
do
	cd TRIAL_TRAJ_$a
	echo 1 1 | gmx rms -s ../em-gb.pdb -f md-gb.trr -o rmsd.xvg 
	cd .. 
	a=`expr $a + 1`
done


mkdir RMSD 

a=1
while [ $a -lt 4 ] #insert_folders_number+1
do
	cd TRIAL_TRAJ_$a
	mv rmsd.xvg ../RMSD
	cd ../RMSD
	mv rmsd.xvg rmsd$a.xvg
	cd .. 
	a=`expr $a + 1`
done
