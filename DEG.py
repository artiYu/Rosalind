import os

def getDegrees(edges, v):
	deg_array = [0]*v

	for edge in edges:
		for node in edge:
			deg_array[node-1] += 1
	return deg_array

def main():
	with open(os.getcwd() + "/Data/rosalind_deg.txt", "r") as input_file:
		v, e = map(int, input_file.readline().strip().split())
		edges = [map(int, line.strip().split()) for line in input_file.readlines()]

	deg = getDegrees(edges, v)

	with open(os.getcwd() + "/Data/test.txt", "w") as output_file:
		output_file.write(' '.join(map(str, deg)))

if __name__ == '__main__':
	main()
