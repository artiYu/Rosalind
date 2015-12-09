import os

with open(os.getcwd() + "/Data/rosalind_mer.txt", "r") as fr:
	n = int(fr.readline())
	a = map(int, fr.readline().strip().split())
	m = int(fr.readline())
	b = map(int, fr.readline().strip().split())

def Merge(a, b):
	return sorted(a + b)

def MergeImplement(a, b):
	c = []
	while a and b:
		if a[0] < b[0]:
			c.append(a.pop(0))
		else:
			c.append(b.pop(0))
	return c + a + b


def main():
	c = MergeImplement(a, b)
	with open(os.getcwd() + "/Data/test.txt", "w") as fw:
		fw.write(' '.join(map(str, c)))

if __name__ == '__main__':
	main()