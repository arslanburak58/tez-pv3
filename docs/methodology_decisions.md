# Methodology Decisions — tez-pv3

Her karar: gerekçe + alternatif + atıf + tez paragrafı.

---

## Karar 10 — İstasyon dengeleme (ters-frekans sample weight)

**Karar:** Ters-frekans örneklem ağırlıklandırması, yalnızca eğitimde uygulanır.  
**Alternatif:** Veri budama (daha az istasyon); sabit ağırlıklar.  
**Gerekçe:** Tüm veriyi eğitimde tutarken hiçbir istasyonun gradient katkısını baskın kılmaz.  
**Kritik kural:** Sample weight test metriğine SIZMAZ — test metrikleri ağırlıksız hesaplanır.

**Tez paragrafı:**
> İstasyonlar arası veri hacmi dengesizliği, ters-frekans örneklem ağırlıklandırmasıyla giderilmiştir. Her gözlem, ait olduğu istasyonun satır sayısının tersiyle ağırlıklandırılmış ve ağırlıklar ortalama 1 olacak şekilde normalize edilmiştir. Bu yaklaşım tüm veriyi eğitimde tutarken hiçbir istasyonun gradient katkısını baskın kılmaz. Ağırlıklar yalnızca eğitim aşamasında uygulanmış; test metrikleri, gerçek dünya dağılımını yansıtması için ağırlıksız hesaplanmıştır.

---

## Karar 11 — Çözünürlük hizalama (DKASC 5-dk → 15-dk)

**Karar:** DKASC verisi ardışık 3 gözlemin ortalaması alınarak 15-dakikalık çözünürlüğe downsample edilir.  
**Alternatif:** PVOD'u 5-dk'ya upsample etmek (gürültü ekler); karışık çözünürlükle çalışmak (lag bozulur).  
**Gerekçe:** Lag ve rolling öznitelikleri tutarlı zaman adımları ister; güç eğrisinin yumuşak yapısı nedeniyle bilgi kaybı ihmal edilebilir.

**Tez paragrafı:**
> Farklı zaman çözünürlükleri (DKASC 5-dk, PVOD 15-dk) ortak 15-dakikalık çözünürlüğe hizalanmıştır. DKASC verisi ardışık üç gözlemin ortalaması alınarak yeniden örneklenmiş, güç eğrisinin yumuşak yapısı nedeniyle bilgi kaybı ihmal edilebilir düzeyde tutulmuştur.

---

## Karar 12 — Holdout genelleme protokolü

**Karar:** station02 (Mono-Si) ve station09 (Poly-Si) eğitim/val/test'e hiç girmez; zero-shot değerlendirme için ayrılır.  
**Metrik:** Pearson r (q50 vs actual) şekil yakalama tanısı; coverage; noon_ratio (sıfır-bölme guard ile).  
**Eşik:** Coverage %70+ güçlü, %60–70 kabul edilebilir, <%60 tanı playbook devreye girer.

**Tez paragrafı:**
> Modelin genelleme yetisi, eğitime hiç dahil edilmeyen iki holdout santralinde (station02, Mono-Si; station09, Poly-Si) ayrıca test edilmiştir.

---

## Karar 1 — Meta-öğrenici: QuantileLinear (Ridge değil)

**Karar:** Ridge MSE yerine QuantileLinear (pinball + L2, scipy L-BFGS-B) kullanılır.  
**Gerekçe:** v1/v2'de Ridge üç quantile'da coverage=0 üretti — quantile dönüşümü olmayan MSE minimizasyonu çöküyor.

---

## Karar 3 — CQR k seçimi val_select'te

**Karar:** CQR ölçekleme faktörü k, val_select'te seçilir.  
**Gerekçe:** v1'de test üzerinde grid search = leakage. val_fit/val_select ayrımı bu soruyu kökten çözer.

---

## Karar 5 — Quantile crossing: post-hoc np.sort

**Karar:** q01 ≤ q05 ≤ ... ≤ q09 garantisi için post-hoc `np.sort` uygulanır.

---

## Karar 7 — Robustness hipotezi iki yönlü

**Karar:** H1 iki yönlü test. Asıl katkı coverage stability.  
**Gerekçe:** v1'de H1 doğrulanmadı (ΔCRPS +%1.44); gerçek katkı coverage stability çıktı.
