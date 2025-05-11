import string

def is_palindrome(text:str)->bool:
    string.punctuation += " "
    clean_text = ''.join(ch for ch in text if ch not in string.punctuation)
    reversed = clean_text[::-1]
    return clean_text.lower() == reversed.lower()
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")