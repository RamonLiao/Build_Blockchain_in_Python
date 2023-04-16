# Caesar Encryption

def txt_shift(txt, shift):
	result = ""
	for idx in range(0, len(txt)):
		char = txt[idx]
		if char.isalpha():
			if char.isupper():
				order = ord(char) - 65 + shift
				order %= 26
				order += 65
			elif char.islower():
				order = ord(char) - 97 + shift
				order %= 26
				order += 97
			char = chr(order)
		result += char
	return result

def caesar_encryption(txt, shift):
	return txt_shift(txt, shift)

def caesar_decryption(txt, shift):
	return txt_shift(txt, -1 * shift)

plain_txt = "Hello!"
shift_amount = 10

print(f"Plain text: {plain_txt}")
cipher_txt = caesar_encryption(plain_txt, shift_amount)
print(f"Encrypted text: {cipher_txt}")
decryption_cipher_txt = caesar_decryption(cipher_txt, shift_amount)
print(f"Deciphered text: {decryption_cipher_txt}")