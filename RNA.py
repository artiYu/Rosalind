import os

def compute_rna(d):
	rna = ""
	for char in d:
		if char == 'T':
			rna += 'U'
		else:
			rna += char
	return rna
	
	
def main():
	with open(os.getcwd() + "\\Data\\rosalind_rna.txt", "r") as input_file:
		r = str(input_file.readline())
	
	rna = compute_rna(r)

	with open(os.getcwd() + "\\Data\\test.txt", "w") as output_file:
		output_file.write(rna)

if __name__ == '__main__':
	main()
