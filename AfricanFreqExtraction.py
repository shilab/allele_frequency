# open the file "africanpop" which is the first column of ALFRED-Nigercongopopulation
# read all data
with open ('africanpop', 'r') as fileToRead1:
	read_data = fileToRead1.read()
	read_data = read_data.split('\n')
	read_data.pop(-1)

# close the first file				
fileToRead1.close()

# open the file to write the ALFRED population frequency 
fileToWrite = open ('NigerCongoFreq', 'w')

# adding a header for the fileToWrite
# open the second file 
# read line by line
# write any population/line which is the same as first file into the desired write file 

fileToWrite.write ('population'+'\t'+'pop-uid'+'\t'+'geo_region'+'\t'+'sample_uid'+'\t'
		   +'sample_size'+'\t'+'locus_name'+'\t'+'site_name'+'\t'+'allele_namefrequency'+'\n')

with open ('/projects/shilab_simplex/data/ALFRED/alfred.txt', 'r') as fileToRead2:
	for line in fileToRead2:
		population = line.split('\t')[0]
		if population in read_data:
			fileToWrite.write (line)

# close both files 			
fileToRead2.close()
fileToWrite.close()

