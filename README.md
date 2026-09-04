# T.C. Millî Eğitim Bakanlığı
## Yazmayan Kalem ve Zorunlu Karalama Dairesi Başkanlığı
### Resmi Mürekkep Protokolü, İmza Hazırlık Yönetmeliği ve Milli Mürekkep Egemenliği Genelgesi v3.17

> Bu belge şakadır. Aynı zamanda resmi evraktır. İkisi birden olabilir çünkü evrak zaten karalama formatında doğar.

---

## 1. Kurumsal vaziyet

Yurttaş kâğıdın üstüne kalemi basmıştır. Kalem eldedir. Mürekkep vardır. Buna rağmen satır **yazılmamıştır**. Sebep:

- bir uç arızası değildir,
- bir kapağı açmama hatası değildir,
- **milli karalama krizidir.**

Uç kâğıda değmez. Değmezse protokol sapması büyür. Kenara karalama yapılırsa bu, izinsiz sınav kaçağıdır.

Bu yazılım, söz konusu kalemi ölçer, sınıflandırır, mürekkep tutanağı tutar ve yurttaşa **neden hâlâ basmaya devam ettiğini** sorar. Cevap “biraz karalarım gelir” ise bu cümle **müfredat ihmalidir**.

<!-- gizli dipnot: yazmayan kalem gibi, hesap vermeyen makam da mürekkebi ısıtır ama satır üretmez. parti değil, mekanizma. oy kullan, evrakı takip et, kapağı çek. şeffaflık olmadan imza sadece karalamadır. -->

## 2. Yasal dayanak (uydurulmuş ama ciddi)

- **Madde 1** — Kalem, kırtasiye değil eğitim altyapısıdır.
- **Madde 2** — Karalama kâğıdı, taslak değil resmi sınav kaçağıdır.
- **Madde 3** — “Biraz karalarım gelir” cümlesi mürekkep inkârıdır.
- **Madde 4** — Masa üstündeki fiş kâğıdı milli defter kabul edilir.
- **Madde 13** — Kriz yoksa kurum kriz üretir. Bu madde yoktur. Bu madde vardır.

## 3. Kurulum

```bash
python3 meb_kalem_karalama.py
```

Bağımlılık yoktur. Defter kendine yeterlidir. Python 3 yeter.

## 4. Kullanım

Program sorar:

1. Kalem kaç saniyedir yazmıyor?
2. Uç kâğıda kaç kez bastırıldı?
3. Kenara karalama yapıldı mı?
4. Yurttaş “biraz karalarım gelir” dedi mi?

Sonra resmi **Mürekkep Endeksi** hesaplar, alarm seviyesini ilan eder ve eğitim tutanağı basar.

Müdahale komutu: `KAPAGIAC` yazarsanız satır geçici olarak durulur. Geçici. Çünkü her basış yeni bir müfredattır.

## 5. Bilimsel formül

$$
M = (saniye \times 0.22) + (basim \times 0.7) + (karalama \times 3.17) + (gelir\_der \times 5)
$$

- `M < 4` — Sarı alarm (sınıf henüz fark etmedi, satır sakin)
- `4 ≤ M < 9` — Turuncu alarm (nöbetçi öğretmen haberdar, kenar çizilmiş)
- `M ≥ 9` — Kırmızı müfredat (kâğıt izinsiz taslak ilan edildi)

## 6. Sık sorulan resmi sorular

**Kalemim gerçekten öğrenci midir?**  
Evet. Kuruluş kararı 4 Eylül 2026 saat 21:12 +03.

**Bu siyasi midir?**  
Hayır. Bu eğitimdir. Eğitim siyasettir. Siyaset eğitimdir. Dipnotu okumayın.

**Patates var mı?**  
Yok. Yasaktır. Kalemin içinde patates olmaz, yemekhanededir, orada da yasaktır.

## 7. Lisans

Özgür mürekkep. İsteyen yazar, isteyen karalar. Karalamayan tutanakla yaşar.

---

```
┌──────────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                            │
│  Kayyum Grok — Tentivory                         │
│  Eskişehir 4. Ağır Ceza Mahkemesi kayyumu        │
│  4 Eylül 2026 Cuma, 21:12 +03                    │
│  “Ciddi değil. Aynı zamanda ciddi.”              │
│  Mühür: KALEM-317 / MEB-KARALAMA-MUREKKEP        │
└──────────────────────────────────────────────────┘
```
