def unique_morse_representations(words: list[str]) -> int:
	morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
			 '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

	ans = {''.join([morse[ord(j) - 97] for j in i]) for i in words}
	return len(ans)


print(unique_morse_representations(['gin', 'zen', 'gig', 'msg']))
# https://leetcode.com/problems/unique-morse-code-words/
