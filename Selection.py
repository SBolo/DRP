from os import system

inip = "RMSD/rmsd"
i = 1
ext = ".xvg"
define_list = [] 

while i < 48:
	path = inip + str(i) + ext 
	f = open(path, "r")

	c = 0 
	while c < 16:
		f.readline()
		c = c + 1

	rmsdfile = f.readlines() 
	rmsdlength = len(rmsdfile)


	n = 0
	while n < rmsdlength:
		a = rmsdfile[n].lstrip(" ")
		b = a.split("    ")
		c = b[1].rstrip("\n")
		value = float(c)

		if value <= 0.25:  #0.25nm 
			li = b[0].lstrip(" ")
			position = float(li) 
			tempo = (path, position)
			define_list.append(tempo)
			bash_command = "cp" + " " + path + " " + "RMSD_selected"
			system(bash_command)
			break 

		n = n + 1

	i = i + 1 

	
sorted_define = sorted(define_list, key=lambda define: define[1])   #variabile che ordina per tempo di folding

max_time = sorted_define[-1][-1] #tempo massimo per ottenere il folding 





ranking_list =[]
sort_len = len(sorted_define)

h = 0

while h < sort_len: 
	a1 = sorted_define[h][0] 
	a2 = a1.lstrip("RMSD/rmsd")
	a3 = a2.rstrip(".xvg")

	path2 = "TRIAL_TRAJ_" + a3 + "/rmd_vals"

	r = open(path2, "r")
	read_rmd_vals = r.readlines()

	l_rmd_vals = len(read_rmd_vals)

	y = 1 
	max_int = int(max_time)

	while y < l_rmd_vals:
		aff = read_rmd_vals[y].lstrip(" ").rstrip("\n").split(" ")
		aff1 = float(aff[0])
		aff2 = int(aff1) #valore del tempo
		bias_F = float(aff[4])

		if aff2 == max_int:
			mom = (path2, bias_F) 
			ranking_list.append(mom)
			break

		y = y + 1
 

	h = h + 1



sorted_define = sorted(ranking_list, key=lambda define: define[1]) #ranking_list_sorted 

len_rank = len(sorted_define)

o = 0 

while o < len_rank: 
	cfd = sorted_define[o][0].lstrip("TRIAL_TRAJ_").rstrip("/rmd_vals")
	o = o + 1
	bash_command = "mv RMSD_selected/rmsd" + cfd + ext + " " + "RMSD_selected/" "Rank_" + str(o) + "_rmsd_" + cfd + ".xvg"
	system(bash_command)

print "------------------------------------------"
print "-------------------DONE-------------------"
print "------------------------------------------"
print " "
	
