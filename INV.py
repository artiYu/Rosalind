import os

def merge(a, b):
	itA, itB, count, c = 0, 0, 0, []

	while itA < len(a) and itB < len(b):
		if a[itA] <= b[itB]:
			c.append(a[itA])
			itA += 1
		else:
			c.append(b[itB])
			count += len(a) - itA
			itB += 1

	c += a[itA:] + b[itB:]

	return c, count


def merge_sort(a):

	if len(a) <= 1:
		return a, 0

	mid = len(a)/2

	down, down_count = merge_sort(a[:mid])
	up, up_count = merge_sort(a[mid:])
	
	all_el, all_el_count = merge(down, up)

	return all_el, up_count + down_count + all_el_count



def main():
	with open(os.getcwd() + "/Data/rosalind_inv.txt", "r") as input_file:
		n = input_file.readline()
		a = map(int, input_file.readline().strip().split())

	inv = merge_sort(a)[1]

	with open(os.getcwd() + "/Data/test.txt", "w") as output_file:
		output_file.write(str(inv))

if __name__ == '__main__':
	main()


