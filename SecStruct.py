path = raw_input("filepath: ")
f = open(path, "r")
l1 = f.readline() #header
l2 = f.readline() #file_creator
l3 = f.readline() #molecule_name
l4 = f.readline() #data_title
l5 = f.readline() #file_version
l6 = f.readline() #frame_number
l7 = f.readline() #atoms_number

f.readline()
f.readline()

l3a = l3.split(" ")
l3b = l3a[2].split(".")
filename = l3b[0] #define_filename_for_output_file

l6a = l6.split(" ")
framenumber = int(l6a[2])

l7a = l7.split(" ")
atomnumber = int(l7a[2])


#define_structure_type_counter

Ttime = []
Etime = []
Btime = []
Htime = []
Gtime = []
Itime = []
Ctime = []

n = 0
while n < framenumber:
	T = 0
	E = 0
	B = 0
	H = 0
	G = 0
	I = 0
	C = 0

	i = 0 
	while i < atomnumber:
		line = f.readline()
		a = line.split(" ")
		a1 = a[4].rstrip("\n")

		if a1 == "T":
			T = T+1

		elif a1 == "E":
			E = E+1

		elif a1 == "B":
			B = B+1

		elif a1 == "H":
			H = H+1

		elif a1 == "G":
			G = G+1

		elif a1 == "I":
			I = I+1

		else:
			C = C+1

		i = i + 1
		

	Ttime.append(T)
	Etime.append(E)
	Btime.append(B)
	Htime.append(H)
	Gtime.append(G)
	Itime.append(I)
	Ctime.append(C)

	n = n+1


Timeline_name = filename + "_SecondaryStructures.csv"
g = open(Timeline_name, "w")
g.write("frame_number	TURN	EXT_CONF	BRIDGE	ALPHA_HELIX	3-10_HELIX	PI_HELIX	COIL\n")
p = 0
while p < framenumber:
	linetoprint = str(p) + "	" + str(Ttime[p]) + "	" + str(Etime[p]) + "	" + str(Btime[p]) + "	" + str(Htime[p]) + "	" + str(Gtime[p]) + "	" + str(Itime[p]) + "	" + str(Ctime[p]) + "\n"
	g.write(linetoprint)
	p = p+1
g.close()

print "DONE!"


	

