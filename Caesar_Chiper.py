import string

# Inputan plaintext yang akan dienkripsi
plaintext = input("Masukkan teks yang akan dienkripsi: ")

def caesar_encrypt(plaintext):
    res = ""
    for x in range(len(plaintext)):
        if plaintext[x].isupper(): # Jika karakter adalah huruf kapital
            enc = (string.ascii_uppercase.index(plaintext[x]) + 50) % 26 # Geser 'NIM' 50 posisi ke depan dalam alfabet kapital
            res += string.ascii_uppercase[enc]
        elif plaintext[x].islower(): # Jika karakter adalah huruf kecil
            enc = (string.ascii_lowercase.index(plaintext[x]) + 50) % 26 # Geser 'NIM' 50 posisi ke depan dalam alfabet kecil
            res += string.ascii_lowercase[enc] # Tambahkan karakter terenkripsi ke hasil
        elif plaintext[x].isdigit(): # Jika karakter adalah angka
            res += chr(((ord(plaintext[x]) - ord('0') + 50) % 10) + ord('0')) # Geser 'NIM' 50 posisi ke depan dalam angka (modulo 10)
        else:
            res += plaintext[x]
    return res

# Pemanggilan fungsi untuk enkripsi
encrypted_text = caesar_encrypt(plaintext)
print("Teks terenkripsi:", encrypted_text)

# Inputan ciphertext yang akan didekripsi
ciphertext = input("Masukkan teks yang akan didekripsi: ")

def caesar_decrypt(ciphertext):
    res = ""
    for x in range(len(ciphertext)):
        if ciphertext[x].isupper():
            dec = (string.ascii_uppercase.index(ciphertext[x]) - 50) % 26
            res += string.ascii_uppercase[dec]
        elif ciphertext[x].islower():
            dec = (string.ascii_lowercase.index(ciphertext[x]) - 50) % 26
            res += string.ascii_lowercase[dec]
        elif ciphertext[x].isdigit():
            res += chr(((ord(ciphertext[x]) - ord('0') - 50) % 10) + ord('0'))
        else:
            res += ciphertext[x]
    return res

# Pemanggilan fungsi untuk dekripsi
decrypted_text = caesar_decrypt(ciphertext)
print("Teks terdekripsi:", decrypted_text)
