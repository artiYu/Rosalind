import os
from MER import MergeImplement

def MergeSort(a):
	if len(a) <= 1:
		return a
	mid = len(a)/2
	up = MergeSort(a[mid:])
	down = MergeSort(a[:mid])

	return MergeImplement(up, down)


def main():
	with open(os.getcwd() + "/Data/rosalind_ms.txt", "r") as input_file:
		n = int(input_file.readline().strip())
		a = map(int, input_file.readline().strip().split())

	sorted_a = MergeSort(a)
	assert sorted_a == sorted(a)

	with open(os.getcwd() + "/Data/test.txt", "w") as output_file:
		output_file.write(' '.join(map(str, sorted_a)))

if __name__ == '__main__':
	main()
