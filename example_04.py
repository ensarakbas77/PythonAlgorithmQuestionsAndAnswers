"""Bir pangram, alfabenin her bir harfini en az bir kez içeren bir cümledir. Örneğin, "Hızlı kahverengi tilki tembel köpeğin üzerinden atlar" cümlesi bir pangramdır, çünkü A-Z harflerini en az bir kez kullanır (büyük/küçük harf fark etmez).

Bir dize verildiğinde, bunun bir pangram olup olmadığını tespit edin. Eğer öyleyse True, değilse False döndürün. Sayıları ve noktalama işaretlerini dikkate almayın."""


def is_pangram(s):
    s = s.lower()  
    letters = set()

    for char in s:
        if char.isalpha():  
            letters.add(char)

    return len(letters) == 26  


print(is_pangram("The quick brown fox jumps over the lazy dog")) 
print(is_pangram("Hello world"))  
