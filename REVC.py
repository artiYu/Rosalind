import os

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
	
	
def main():
	with open(os.getcwd() + "\\Data\\rosalind_revc.txt", "r") as input_file:
		rev = str(input_file.readline())
	
	revc = compute_revc(rev)

	with open(os.getcwd() + "\\Data\\test.txt", "w") as output_file:
		output_file.write(revc)

if __name__ == '__main__':
	main()
