# Reverse words
def reverseWords(text:str):
    text_split = text.split()
    print("Split edilmiş hali: ", text_split)
    result = list()
    for i in text_split:
        result.append(i[::-1])
    
    return result

        

word = "double  spaces" # "elbuod  secaps"
print("Çıktı: ",reverseWords(word))
print("")
word2 = "This is an example!"
print("Çıktı: ",reverseWords(word2))


# CodeWars' ın kabul ettiği 
def reverse_words(text: str):
    words = text.split(' ')  # Boşluklara göre ayır ama boşlukları koru
    reversed_words = [word[::-1] for word in words]  # Her kelimeyi ters çevir
    return ' '.join(reversed_words)  # Tekrar boşlukla birleştir

print("----------------- CodeWars -----------------")
print(reverse_words("This is an example!"))  # "sihT si na !elpmaxe"
print(reverse_words("double  spaces"))       # "elbuod  secaps"



# List comprehension
""" reversed_words = [i[::-1] for i in words] """
# Aşağıdakinle aynı anlama gelir:
"""
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
"""

# Slicing Practices
name = "Ensar AKBAŞ"
print(name[0:5:]+" "+name[6:]+" "+name[::-1]+" "+name[2:8].replace(" ",""))

# join() Kullanım --> "ayırıcı".join(liste)
# "ayırıcı" → her iki elemanın arasına konacak şeydir (genelde boşluk " " ya da virgül ",").

harfler = ["H", "e", "l", "l", "o", "E", "n", "s", "a", "r"]
sonuc = " ".join(harfler).upper()
print(sonuc) 
