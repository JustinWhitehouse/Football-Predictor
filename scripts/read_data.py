
def read_data(filename, format):
	if format == 'csv':
		return read_data_csv(filename)
	elif format == 'json':
		return read_data_json(filename)
	else:
		raise ValueError('Format not recognised: ' + format)

def read_data_csv(filename):
	data = []
	with open(filename, 'r') as f:
		data = f.readlines()
		f.close()

	datalines = []
	for line in data:
		datalines = datalines + [line.split(',')]
	return datalines

def read_data_json(filename):
	print "Method 'read_data_json' not yet implemented!"
	return None

def read_data_csv_cols(filename, list_cols):
	datalines = read_data_csv(filename)
	new_data = []
	for line in datalines:
		temp_list = []
		for col in list_cols:
			temp_list = temp_list + [line[col]]
		new_data = new_data + [temp_list]
	return new_data

def get_results_csv(filename):
	data = read_data_csv_cols(filename, [1,2,3,4,5])
	return data

def get_all_results_cs():
	filenames = ['season-0910_csv.csv', 'season-1011_csv.csv', 'season-1112_csv.csv', 'season-1213_csv.csv', 'season-1314_csv.csv', 'season-1415_csv.csv', 'season-1516_csv.csv', 'season-1617_csv.csv', 'season-1718_csv.csv', 'season-1819_csv.csv']
	data_path = '../data/english-premier-league/data/'
	all_data = []
	for f in filenames:
		all_data = all_data + [[f, read_data.get_results_csv(data_path + f)]]
	return all_data
	
if __name__ == "__main__":
	import sys
	args = sys.argv[1:]
	read_data_csv(args[0])