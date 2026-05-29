# CLAUDE.md — tez-pv3 çalışma kuralları

Sen bu tezin yürütme asistanısın. Her oturumda önce şunları oku:
- docs/gunce.md      → aktif aşama, bekleyen görev, tıkanıklık
- docs/manifest.json → makine durumu, checkpoint yolları
- docs/experiment_log.md → açık challenger var mı

## Değişmez kurallar
1. main = champion. main'e yalnızca promosyon kapısını geçen sonuç girer.
2. Her challenger ayrı dalda: `experiment/<stage>-<isim>`, çıktı experiments/<...>/outputs/.
3. Deney çalıştırmadan ÖNCE experiments/<...>/preregister.md yaz (metrik+eşik).
4. Her commit'ten önce: make leakage temiz olmalı.
5. Tüm seed=42. Bir "kazanan" çıkarsa 2–3 seed ile doğrula.
6. Test seti dokunulmaz. Challenger seçimi val_select üzerinde yapılır.
7. Checkpoint silme yok → models/archive/ altına taşı.
8. Veri commit etme. Büyük .joblib local.

## Karar verince
- methodology_decisions.md'ye işle: gerekçe + alternatif + atıf + tez paragrafı.
- stage_log.md'ye kronolojik satır ekle.
- gunce.md'yi güncelle.

## Donanım
MacBook Air M4 (MPS). Ağır eğitim (LSTM/TFT) uzarsa Colab T4 öner, batch/seq küçült.

## Üslup
Türkçe, akademik, doğrudan. Teknik terim İngilizce. Varsayım yapma, belirsizi söyle.

## v1/v2 derslerinden gelen baked-in defaults (yeniden doğrulanır)
- wind_speed çıkar (DKASC %85 eksik, Ross buna dayanmaz)
- Metrikler yalnızca gündüz (cos θ_z > 0.087)
- Meta-öğrenici: QuantileLinear (Ridge değil — coverage=0 riski)
- CQR k seçimi val_select'te (test'te değil)
- Quantile crossing: post-hoc np.sort
- DKASC 5-dk → 15-dk downsample (çözünürlük hizalama)
- Sample weight ters-frekans, yalnızca eğitimde
- Holdout: station02, station09 (eğitime hiç girmiyor)
