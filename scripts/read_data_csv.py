
def read_data_csv(filename):
	data = []
	with open(filename, 'r') as f:
		data = f.readlines()
		f.close()

	datalines = []
	for line in data:
		datalines = datalines + [line.split(',')]

	return datalines


if __name__ == "__main__":
	import sys
	args = sys.argv[1:]
	read_data_csv(args[0])