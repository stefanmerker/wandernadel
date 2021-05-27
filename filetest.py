import os

ordner = 'filetest'

if not os.path.exists(ordner):
    os.makedirs(ordner)

i = 1
while i <= 5:
	j = 1
	while j <= 5:
		file_name = '{}\HWN_{}_{}.geojson'
		file = open(file_name.format(ordner,i,j), 'wt')
		output = 'HWN von {} nach {}'
		file.write(output.format(i,j))
		j += 1
	i += 1
