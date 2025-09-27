s = input()

s = ''.join(ch.lower() for ch in s if ch.isalnum())

if s == s[::-1]:
    print(True)
else:
    print(False)


'''for ch in s → har ek character (letter ya symbol) nikalte hain.

if ch.isalnum() → sirf letters aur digits rakhte hain (spaces, commas, punctuation hata dete hain).

ch.lower() → sabko chhote (lowercase) letters me badal dete hain, taaki case ka farq na ho.

''.join(...) → in saaf characters ko jod ke ek nayi string bana dete hain.'''