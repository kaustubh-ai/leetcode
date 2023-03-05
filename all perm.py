def permutations(ch, curr_index=0):
	print('perm called')
	if curr_index == len(ch) - 1:
		# print(''.join(ch))
		...

	for i in range(curr_index, len(ch)):
		ch[curr_index], ch[i] = ch[i], ch[curr_index]
		print(f'curr_index: {curr_index} | ch: {ch} | i: {i}')
		permutations(ch, curr_index + 1)
		print('...')
		ch[curr_index], ch[i] = ch[i], ch[curr_index]


if __name__ == '__main__':
	s = 'ABC'
	permutations(list(s))
