import os
from collections import defaultdict

def getDDegrees(edges, v):
	neighbors = defaultdict(list)

	for a,b in edges:
		neighbors[a].append(b)
		neighbors[b].append(a)

	neighbors_sum = lambda node: sum([len(neighbors[n]) for n in neighbors[node]])
	return [neighbors_sum(n) for n in range(1, v + 1)]

def main():
	with open(os.getcwd() + "/Data/rosalind_ddeg.txt", "r") as input_file:
		v, e = map(int, input_file.readline().strip().split())
		edges = [map(int, line.strip().split()) for line in input_file.readlines()]

	deg = getDDegrees(edges, v)

	with open(os.getcwd() + "/Data/test.txt", "w") as output_file:
		output_file.write(' '.join(map(str, deg)))

if __name__ == '__main__':
	main()
