def caesar_cipher_encrypt(text, shift):
  encrypted_text = ""
  for char in text:
    if char.isalpha():
      if char.isupper():
        encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
      else:
        encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
      encrypted_text += char
  return encrypted_text

def caesar_cipher_decrypt(text, shift):
  decrypted_text = ""
  for char in text:
    if char.isalpha():
      if char.isupper():
        decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
      else:
        decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    else:
      decrypted_text += char
  return decrypted_text

def main():
  message = input("Enter the message to encrypt/ decrypt: ")
  shift = int(input("Enter the shift value for encryption/decryption (a number between 1 and 25): "))

  encrypted_message = caesar_cipher_encrypt(message, shift)
  print("Encrypted message:", encrypted_message)

  decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
  print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
  main()
