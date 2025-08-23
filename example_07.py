"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""
#[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
#[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)



def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return evens[0] if len(evens) == 1 else odds[0]


def FindOutlier(integers):
    sample = integers[:3]
    even_count = sum(1 for x in sample if x % 2 == 0)
    majority_even = even_count >= 2  # True ise dizi çoğunlukla çift

    for x in integers:
        if (x % 2 == 0) != majority_even:
            return x



first_list = [2, 4, 0, 100, 4, 11, 2602, 36]
seconde_list = [160, 3, 1719, 19, 11, 13, -21]

print(find_outlier(first_list))
print(find_outlier(seconde_list))
print("******************************************")
print(FindOutlier(first_list))
print(FindOutlier(seconde_list))



# Another Solution:
"""
def find_outlier(integers):
	evens = []
	odds = []
	for each in integers:
		if each%2==0:
			evens.append(each)
		else:
			odds.append(each)
		if len(evens)>1 and len(odds)==1:
			return odds[0]
		elif len(odds)>1 and len(evens)==1:
			return evens[0]
"""


"""
Problem ve çözüm — detaylı anlatım
Özet: elimizde en az 3 tamsayı içeren bir dizi var. Dizide bütün sayılar aynı parite (hepsi tek veya hepsi çift) olağanüstü tek bir tane istisna (outlier) içeriyor. Görev: bu tek istisnayı (outlier) döndürmek.

Temel fikir / sezgi
Parite (tek/çift) basit bir özelliktir — bir sayı ya çifttir ya tektir. Problem koşuluna göre dizideki elemanların çoğunluğu tek veya çifttir, ve yalnızca bir tane farklı paritede eleman vardır. Dolayısıyla:

Önce dizinin çoğunluk paritesini bul (çoğu tek mi yoksa çoğu çift mi),

sonra çoğunluğa uymayan ilk (ve tek) elemanı döndür.

Bu iki adım hem mantıklı hem hızlıdır.

Yöntemler, avantaj / dezavantaj, zaman/alan karmaşıklığı
1) Basit — tüm diziyi tarayıp evens ve odds listelerini oluşturmak (iki geçiş değil, tek geçiş ama ekstra alan)
Mantık: tüm elemanları dolaş, çiftleri evens listesine, tekleri odds listesine ekle. Döngü bitince hangi listede 1 eleman kaldıysa onu döndür.

Özellikler:

Zaman: O(n) (tek geçiş)

Alan: O(n) (çünkü iki liste potansiyel olarak n büyüklüğünde olur)

Basit, kolay anlaşılır, güvenli.

Kullanım durumu: küçük/orta boy listelerde, kod açıklığı isteniyorsa.

2) En verimli: ilk 3 elemanı kullanarak çoğunluğu belirle, sonra tek geçişte outlier'ı bul (önerilen)
Neden 3 eleman? problem garantisi: dizide yalnızca bir outlier var. Dolayısıyla ilk 3 elemanda çoğunluk kesinlikle gerçek çoğunluğu yansıtacaktır (örnek: çoğunluk çift ise en az 2 tane çift ilk 3 içinde olacaktır; outlier tek ise en fazla 1 tek olur). Bu yüzden:

sample = arr[:3]

even_count = sum(1 for x in sample if x % 2 == 0)

majority_even = (even_count >= 2)

Tüm diziyi dolaş, majority_even ile eşleşmeyen ilk elemanı döndür.

Özellikler:

Zaman: O(n)

Alan: O(1) ek alan (sabit)

Çok büyük diziler için daha idealdir (daha az hafıza, erken karar mantığı).

Basit doğrulama: outlier ilk 3 içinde olsa bile sample içindeki çoğunluk doğruyu verecektir çünkü outlier yalnızca 1 eleman; diğer iki eleman çoğunluğa aittir.

3) Alternatif — tek geçişte erken tespit (ilk üçe bakmadan)
Mantık: döngü sırasında even_count ve odd_count ile say; her yeni elemanda eğer bir tarafta 2 veya daha fazla, diğer tarafta 1 ise outlier'ı geri döndürebilirsin. Pratikte ilk-3 yaklaşımı daha net ve güvenlidır, ama bu da çalışır.

Dikkat edilmesi gereken küçük noktalar / tuzaklar
Python’da i % 2 negatif sayılar için de güvenilir: -3 % 2 == 1 olur; yine de bazı dillerde modulo davranışı farklı olabilir. Genel ve dil-bağımsız kontrol istersen (i & 1) (bitwise) veya i % 2 != 0 kullanabilirsin.

Problemde uzunluk >= 3 olduğu açıklandığı için “ilk 3” yaklaşımı güvenlidir. Eğer uzunluk garantisi olmasaydı ek kontroller gerekirdi.

Tek/çift kontrolü için x % 2 == 0 (çift) ve x % 2 != 0 (tek) yeterli ve anlaşılır.

Örneklerle adım adım (ilk-3 yaklaşımı)
Dizi: [2, 4, 0, 100, 4, 11, 2602, 36]

sample = [2,4,0] → even_count = 3 → majority_even = True

Tüm diziyi tara, if (x % 2 == 0) != majority_even koşulunu kontrol et: bu koşul, elemanın majority ile eşleşmediğini kontrol eder. İlk uyumsuz: 11 → döndür.

Dizi: [160, 3, 1719, 19, 11, 13, -21]

sample = [160,3,1719] → even_count = 1 → majority_even = False (çoğunluk tektir)

Tara, majority ile eşleşmeyen ilk eleman: 160 → döndür.
"""