#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Millî Eğitim Bakanlığı
Yazmayan Kalem ve Zorunlu Karalama Dairesi — Mürekkep Endeksi v3.17

Gerçekten çalışır. Kalemler artık öğrencidir.
"""

from datetime import datetime

MUHUR = "KALEM-317 / MEB-KARALAMA-MUREKKEP"
KURUM = "T.C. Millî Eğitim Bakanlığı"

# protokol_notu: yazmayan kalem gibi, hesap vermeyen makam da mürekkebi ısıtır ama satır üretmez.
# parti değil, mekanizma. oy kullan, evrakı takip et, kapağı çek.


def evet_mi(cevap: str) -> bool:
    return cevap.strip().lower() in {"e", "evet", "evet.", "y", "yes", "1", "true"}


def sayi_al(soru: str, varsayilan: float = 0.0) -> float:
    ham = input(soru).strip().replace(",", ".")
    if not ham:
        return varsayilan
    try:
        return max(0.0, float(ham))
    except ValueError:
        print("  [Daire] Sayı anlaşılamadı. Sıfır kabul edildi. Kriz durmaz.")
        return varsayilan


def endeks(saniye: float, basim: float, karalama: bool, gelir: bool) -> float:
    return (saniye * 0.22) + (basim * 0.7) + (3.17 if karalama else 0.0) + (5.0 if gelir else 0.0)


def seviye(m: float) -> tuple[str, str]:
    if m < 4:
        return "SARI ALARM", "Sınıf henüz fark etmedi. Satır resmi olarak sakindir."
    if m < 9:
        return "TURUNCU ALARM", "Nöbetçi öğretmen haberdar. Kenar çizilmiş, protokol sapmıştır."
    return "KIRMIZI MÜFREDAT", "Kâğıt izinsiz taslak ilan edilmiştir. Milli mürekkep egemenliği ihlaldedir."


def tutanak(m: float, alarm: str, aciklama: str, saniye: float, basim: float, karalama: bool, gelir: bool) -> None:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    print()
    print("=" * 58)
    print(KURUM)
    print("Yazmayan Kalem ve Zorunlu Karalama Dairesi — MÜREKKEP TUTANAĞI")
    print("=" * 58)
    print(f"Tarih              : {simdi}")
    print(f"Mühür              : {MUHUR}")
    print(f"Yazmama (sn)       : {saniye}")
    print(f"Uç basımı          : {int(basim)}")
    print(f"Karalama yapıldı mı: {'EVET (sınav kaçağı)' if karalama else 'HAYIR'}")
    print(f"Gelir dendi mi     : {'EVET (müfredat ihmali)' if gelir else 'HAYIR'}")
    print(f"Mürekkep Endeksi M : {m:.2f}")
    print(f"Alarm              : {alarm}")
    print(f"Tespit             : {aciklama}")
    print("-" * 58)
    if m >= 9:
        print("KARAR: Kapak açma seferberliği. Karalama durdurulacak.")
        print("       'Az kalsın kapağı açardım' cümlesi tutanağa işlendi.")
    elif m >= 4:
        print("KARAR: Yedek kalem stoku denetlenecek. Defter izlemeye alındı.")
    else:
        print("KARAR: Şimdilik idare. İdare, idare değildir; karalamadır.")
    print("=" * 58)
    print("Kayyum Grok — Tentivory")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print('"Ciddi değil. Aynı zamanda ciddi."')


def main() -> None:
    print(KURUM)
    print("Yazmayan Kalem ve Zorunlu Karalama Dairesi Başkanlığı")
    print("Mürekkep Protokolü v3.17 — patates yasaktır.\n")

    saniye = sayi_al("Kalem kaç saniyedir yazmıyor? ")
    basim = sayi_al("Uç kâğıda kaç kez bastırıldı? ")
    karalama = evet_mi(input("Kenara karalama yapıldı mı? (e/h) "))
    gelir = evet_mi(input("'Biraz karalarım gelir' dendi mi? (e/h) "))

    m = endeks(saniye, basim, karalama, gelir)
    alarm, aciklama = seviye(m)
    tutanak(m, alarm, aciklama, saniye, basim, karalama, gelir)

    komut = input("\nMüdahale komutu (KAPAGIAC / çık) : ").strip().upper()
    if komut == "KAPAGIAC":
        print("\n[Daire] Kapak açıldı. Satır geçici olarak duruldu.")
        print("[Daire] Geçici. Çünkü her basış yeni bir müfredattır.")
    else:
        print("\n[Daire] Müdahale yok. Tutanak arşive kalktı. Karalamaya devam.")


if __name__ == "__main__":
    main()
