"""Computing the number of swaps in insertion sort"""

import os

with open(os.getcwd() + "/Data/rosalind_ins.txt", "r") as fr:
	n = int(fr.readline())
	a = map(int, fr.readline().strip().split())

def insertionSort(a, c=0):
	for i in range(1, int(n)):
		k = i
		while k >= 1 and a[k] < a[k-1]:
			a[k], a[k-1] = a[k-1], a[k]
			c += 1
			k -= 1
	return c

def main():
	with open(os.getcwd() + "/Data/test.txt", "w") as fw:
		fw.write(str(insertionSort(a, c = 0)))

if __name__ == '__main__':
	main()