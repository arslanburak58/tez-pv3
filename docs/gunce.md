# Günce — tez-pv3

**Son güncelleme:** 2026-05-29
**Aktif aşama:** STAGE-1 (Literatür)
**Durum:** S1 kapsam taraması yapıldı, boşluklar belirlendi

## Bekleyen görev
- [ ] CQR / conformal prediction kaynaklarını ekle (Romano ve ark., 2019 vd.) — eksen-2 boşluğu
- [ ] PV'de sensör-kaybı robustness + cross-site/zero-shot domain generalization kaynakları ekle — eksen-3 boşluğu
- [ ] Yanlış etiketli "Robust Probabilistic..." defterini düzelt / PV kaynaklarını doğru deftere taşı (NotebookLM tarafı)
- [ ] skill_lit_synth.md'yi Claude Project'e yükle (Project tarafı)
- [ ] docs/literatur_ozeti.md: tematik sentez + araştırma boşluğu cümlesi (Opus + ET oturumu)
- [ ] Atiea (2025) + Ali ve ark. (2026) fark konumlandırması (Opus oturumu)

## Tıkanıklık
Yok.

## Son oturum özeti
S1 literatür kapsam taraması yapıldı. PV tabanı tek defterde: "TEZ — PV Olasılıksal Tahmin" (28 kaynak). Eksen-1 (base/ensemble: XGBoost, LightGBM, CatBoost/Dorogush 2018, stacking, Transformer/TFT) tam. Eksen-2 quantile temeli var (Koenker & Bassett 1978; Gneiting & Raftery 2007 CRPS) ama CQR/conformal boşluk. Eksen-3 (PV sensör-kaybı robustness + zero-shot domain generalization) boşluk = asıl katkı alanı. İki doğrudan öncül teyit: Atiea ve ark. (2025, Results in Engineering) ve Ali ve ark. (2026, Energies/HybrEnNet, PVOD v1.0); ikisi de deterministik, robustness/zero-shot test etmiyor. 43 kaynaklık defter yanlış etiketli (deep-research-agents içeriği), S1'de kullanılmadı.
