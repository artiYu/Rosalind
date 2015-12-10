import os
from string import maketrans

def compute_revc(rev):
	revc = ""
	for char in rev[::-1]:
		if char == 'A':
			revc += 'T'
		elif char == 'T':
			revc += 'A'
		elif char == 'C':
			revc += 'G'
		elif char == 'G':
			revc += 'C'
		else:
			revc += char
	return revc

def complement_strand_dna(rev):
	trans = maketrans('ACGT', 'TGCA')
	return rev.translate(trans)[::-1]
	
	
def main():
	with open(os.getcwd() + "\\Data\\rosalind_revc.txt", "r") as input_file:
		rev = str(input_file.readline())
	
	revc = compute_revc(rev)
	rev2 = complement_strand_dna(rev)
	print revc == rev2

	with open(os.getcwd() + "\\Data\\test.txt", "w") as output_file:
		output_file.write(rev2)

if __name__ == '__main__':
	main()
