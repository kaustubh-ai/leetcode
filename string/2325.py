import string


def decode_message(key: str, message: str) -> str:
	letters, cipher = string.ascii_lowercase, list(dict.fromkeys(key.replace(' ', '')))

	return ''.join([letters[cipher.index(i)] if i != ' ' else ' ' for i in message])


print(decode_message('the quick brown fox jumps over the lazy dog', 'vkbs bs t suepuv'))
# https://leetcode.com/problems/decode-the-message/
