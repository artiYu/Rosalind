import os

def compute_dna(d):
	res = [0]*4
	for molecules in d:
		if molecules == 'A':
			res[0] += 1
		if molecules == 'C':
			res[1] += 1
		if molecules == 'G':
			res[2] += 1
		if molecules == 'T':
			res[3] += 1
	return res
	
def main():
	with open(os.getcwd() + "\\Data\\rosalind_dna.txt", "r") as input_file:
		d = str(input_file.readline())
	
	dna = compute_dna(d)

	with open(os.getcwd() + "\\Data\\test.txt", "w") as output_file:
		output_file.write(' '.join(map(str, dna)))

if __name__ == '__main__':
	main()
