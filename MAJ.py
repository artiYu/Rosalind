import os

def majElement(a):
	maj_el, count = a[0], 1
	for el in a:
		if el == maj_el:
			count += 1
		else:
			count -= 1
		if count == 0:
			maj_el, count = el, 1
	if a.count(maj_el) > len(a)/2:
		return maj_el
	else:
		return -1

def main():
	with open(os.getcwd() + "/Data/rosalind_maj.txt", "r") as input_file:
		k, n = map(int, input_file.readline().strip().split())
		a = [map(int, line.strip().split()) for line in input_file.readlines()]

	maj_el = map(str, [majElement(ar) for ar in a])

	with open(os.getcwd() + "/Data/test.txt", "w") as output_file:
		output_file.write(' '.join(maj_el))

if __name__ == '__main__':
	main()
