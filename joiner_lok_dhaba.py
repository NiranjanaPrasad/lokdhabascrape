import os
import glob

path = '.'
extension = 'csv'
os.chdir(path)
results = glob.glob('*.{}'.format(extension))

with open('Debugged_Assembly_Election_Data.csv', 'w+') as all_file:
	for line in results[0]:
		all_file.write(line)

	for filename in results[1:]:
		print('joining: ', filename)
		with open(filename) as file:
			contents = file.read()
			for line in contents[1:]:
				all_file.write(line)