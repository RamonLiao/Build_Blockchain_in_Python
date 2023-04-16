## Substitution-Permutation Network(SPN)
## Issued by Claude Shannon (1949)
##
## Features:
### 1. Diffusion: Eliminate the statistical structure that may appear in the ciphertext, and a small change in the plaintext will cause a big change in the ciphertext
### 2. Confusion: Complicate the relationship between ciphertext and key
##
## Processes:
### 1. Substitute: S-boxes
### 2. Permutation: P-boxes
### 3. XOR Cipher
### 4. Repeat 1 - 3


import random


#------- XOR Cipher -------
def generate_key(key, rounds):
	key += key
	keys = [] 
	for idx in range(rounds):
		key_this_round = key[4*idx+4:4*idx+20]
		keys.append(key_this_round)
	return keys

def xor_operation(text, key):
	if text == key:
		return "0"
	else:
		return "1"

def xor_en_decrypt(text, key):
	result = ""
	len_txt = len(text)
	len_key = len(key)
	for idx in range(0, len_txt):
		if idx >= len_key:
			key_idx = idx % len_key
		else:
			key_idx = idx
		xor_result = xor_operation(text[idx], key[key_idx])
		result += xor_result
	return result


#------- S-boxes -------
def substitution(input, s_box):
	output = ""
	for idx in range(4):
		data = input[4*idx:4*(idx+1)]

		## int(value, base)
		### base (opt) : the number system that the value is currently in
		### int("0b101", 2)) -> binary 
		### int("0o16", 8)) -> octal 
		### int("16.6", 10)) -> decimal 
		### int("0xA", 16)) -> hexidecimmal 
		number = int(data, 2)

		number_substitution = s_box[number]
		# Convert to binary string
		# ex: 9 -> "1001"
		binary_number = ""
		for i in range(3, -1, -1):
			binary_number += str((number_substitution >> i) & 1)

		output += binary_number
	return output


#------- P-boxes -------
def permutation(input, p_box):
	output = list("0" * 16)
	for idx, value in enumerate(p_box):
		output[value] = input[idx]
	return "".join(output)


#------- SPN Encryption -------
def spn_encryption(text, rounds, key, s_box, p_box):
	output = text
	for idx in range(rounds):
		output = xor_en_decrypt(output, key[idx])
		output = substitution(output, s_box)
		output = permutation(output, p_box)
	output = xor_en_decrypt(output, key[rounds])
	return output

#------- SPN Decryption -------
def spn_decryption(text, rounds, key, s_box, p_box):
	output = text
	s_box_inverse = [0] * 16
	p_box_inverse = [0] * 16
	for idx in range(16):
		s_box_inverse[s_box[idx]] = idx
		p_box_inverse[p_box[idx]] = idx
	for idx in range(rounds):
		output = xor_en_decrypt(output, key[rounds-idx])
		output = permutation(output, p_box_inverse)
		output = substitution(output, s_box_inverse)
	output = xor_en_decrypt(output, key[0])
	return output



if __name__ == '__main__':
	rounds = 3
	key = "1011101000111110"
	keys = generate_key(key, rounds + 1)
	print(f"Initial key: {key}")
	print(f"Generated keys: {keys}")

	s_box = random.sample(range(0, 16), 16)
	print(f"s_box: {s_box}")
	p_box = random.sample(range(0, 16), 16)
	print(f"p_box: {p_box}")

	# First test
	print("\nFirst test")
	message = "1001001110100101"
	print(f"Plain text: {message}")
	encryption = spn_encryption(message, rounds, keys, s_box, p_box)
	print(f"Encrypted text: {encryption}")
	decryption = spn_decryption(encryption, rounds, keys, s_box, p_box)
	print(f"Plain text: {decryption}")


	# 1001001110100101 -> 1001001110100111

	# Second test
	print("\nSecond test")
	message = "1001001110100111"
	print(f"Plain text: {message}")
	encryption = spn_encryption(message, rounds, keys, s_box, p_box)
	print(f"Encrypted text: {encryption}")
	decryption = spn_decryption(encryption, rounds, keys, s_box, p_box)
	print(f"Plain text: {decryption}")









