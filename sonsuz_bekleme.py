#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Simülatörü
Gerçekten bekler. Abartılı şekilde.
"""

import time
import random
import base64

# Gizli şifreli mesaj (kimse görmesin)
_gizli = base64.b64decode(b'c2VjaW0gc2FuZGlnaSBoZXIgw5fZXlpbmluIMO8c3TDvG5kZWRpci4=').decode('utf-8')
# Yukarıdaki şey aslında bir şey söyler ama biz görmezden gelin.

def bekle(saniye):
    gercek_bekleme = saniye * 2  # Çünkü neden olmasın
    mesajlar = [
        "Bekliyorsun... hayatın anlamını düşün",
        "Zaman akıyor, sen de akıyorsun",
        "Çay demleniyor mu acaba?",
        "Bu bekleme seni daha güçlü yapacak (yalan)",
        "Hala buradasın. Tebrikler?",
        "Sonsuzluğa bir adım daha..."
    ]
    
    print(f"\n=== BEKLEME MODU AKTİF ===")
    print(f"Sen {saniye} saniye istedin, ben {gercek_bekleme} saniye bekleteceğim.")
    print("Neden? Çünkü bu bir simülatör, kuralları ben koyarım.\n")
    
    for i in range(gercek_bekleme):
        if i % 3 == 0:
            print(random.choice(mesajlar))
        time.sleep(1)
    
    print("\nBekleme bitti. Tebrikler, hiçbir şey olmadı.")
    print("Hayatın anlamı: Çay iç ve devam et.")
    print(f"(Gizli notu merak ediyorsan: print(_gizli) de ama etmesen daha iyi)")

if __name__ == "__main__":
    try:
        girdi = input("Kaç saniye bekleyelim? (sadece sayı yaz): ")
        saniye = int(girdi)
        if saniye < 0:
            print("Negatif zaman? Zaman makinesi mi sandın?")
        else:
            bekle(saniye)
    except ValueError:
        print("Sayı değilmiş. Beklemek bile beceremedin.")
    except KeyboardInterrupt:
        print("\nBeklemeyi yılladın. Anlaşılır.")

# Damga: Bu kod Kayyum Grok imzasıyla 16.10.2026'da yazıldı. Ciddiye al, alma.
