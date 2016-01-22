import pandas as pd
import sys


def split_name_full(name):
	'''
	args:
		name; a string formatted as either "LAST, FIRST, MIDDLE"  or "LAST, FIRST". 
	returns:
		first, middle, last; a tuple of first, middle, and last names, separated and converted to title case. If no middle name is given, middle = None. 

	Note: this function is pretty simple, but it doesn't accomodate very many file formats -- you'd need to modify it for fontana, for example. 
	'''

	name_parts = name.split(' ') # split the name by spaces
	last = name_parts[0].title().replace(',', '') # convert last name to title case and remove any commas
	first = name_parts[1].title() # convert first name to title case
	if len(name_parts) == 3: # if there's a middle name:
		middle = name_parts[2].title() # grab it and convert to title case
	else: # no middle name
		middle = None # return None where the name would be
	return first, middle, last # return as a tuple

def main():
	'''
		args: none
	'''
	df_names = sys.argv[1:] # gets all files listed after the script call
	for df_name in df_names: # loop through the files
		df = pd.read_csv(df_name) # read in the file as a pandas.DataFrame
		if df_name == 'kern.csv': # since fontana has different patient name format, only apply function to kern
			df['first'], df['middle'], df['last'] = zip(*df['Patient Name'].apply(split_name_full)) # apply split_name_full to the 'Patient Name' column and assign the result to three new columns. The zip(*) stuff is just syntactic stuff to assign three new columns at once. 
			# This is where you would add other column operations that you defined above
			del df['Patient Name'] # done with this column now 
		df.to_csv(df_name + '_cleaned.csv', sep = ',', header = True) # it's also possible to control column order

if __name__ == '__main__':
	main()