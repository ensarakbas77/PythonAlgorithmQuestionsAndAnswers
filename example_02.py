def to_camel_case(text):
    if text == "":
        return ""  # boşsa boş döndür
    
    # '-' veya '_' ile böl
    words = text.replace('-', '_').split('_')

    # İlk kelime aynı kalsın
    first = words[0]

    # Diğer kelimelerin ilk harfi büyük olsun
    others = [word.capitalize() for word in words[1:]]

    # Hepsini birleştir
    return first + ''.join(others)

text1 = "the-stealth-warrior"
text2 = "The_Stealth_Warrior"
text3 = "The_Stealth-Warrior"
result = to_camel_case(text1), to_camel_case(text2), to_camel_case(text3)

print(result[0])  
print(result[1])  
print(result[2])


"""
Açıklama
replace('-', '_'): önce tüm - işaretlerini _ yapıyoruz (çünkü ikisi de olabilir).

split('_'): sonra _ karakterine göre parçalayarak kelimelere ayırıyoruz.

word.capitalize(): kelimenin ilk harfini büyük yapar.

first + ''.join(others): ilk kelime + diğerlerini birleştir.

Daha iyi bir çözüm için:
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

text = "the-stealth-warrior"

text[:1]                          # "t"
text.title()                     # "The-Stealth-Warrior"
text.title()[1:]                 # "he-Stealth-Warrior"
.replace('_', '').replace('-', '')  # "heStealthWarrior"

Sonuç = "t" + "heStealthWarrior" = "theStealthWarrior"


"""