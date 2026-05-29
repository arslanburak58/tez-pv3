# Tez Workflow — 14 Aşama (tez-pv3)

v1/v2 dersleri baked-in. Her aşamada tamamlandı ölçütü karşılanmadan geçilmez.

---

## STAGE-0: Setup
**Hedef:** Proje iskeleti, ortam, repo hazır.  
**Tamamlandı ölçütü:** `make help` + `make test` çalışıyor; ilk commit+push yapıldı.

## STAGE-1: Literatür
**Hedef:** PV güç tahmini, olasılıksal tahmin, sensör dayanıklılığı literatürü.  
**Araç:** NotebookLM atıf defterleri + köprü prompt.

## STAGE-2: Veri
**Hedef:** DKASC + PVOD yükleme, doğrulama, `data_provenance.md` doldurma.  
**v1/v2 dersi:** wind_speed çıkar; DKASC 5-dk → 15-dk downsample (Karar 11).

## STAGE-3: Fizik Öznitelik
**Hedef:** pvlib cos(θ_z), k_t, air mass, T_cell (Ross NOCT=46), daylight maskesi.  
**KRİTİK:** Daylight maskesi (cos θ_z > 0.087) bu aşamada baştan kurulur.

## STAGE-4: Bölme
**Hedef:** Kronolojik 70/15/15; val → val_fit + val_select ayrımı; Walk-Forward gap=24.

## STAGE-5: Taban Modeller
**Hedef:** 9 taban model (LightGBM, CatBoost, XGBoost native quantile; diğerleri).

## STAGE-6: Meta-Öğrenici
**Hedef:** QuantileLinear stacking (pinball + L2, scipy L-BFGS-B).  
**KRİTİK:** Ridge KULLANMA (coverage=0 riski — Karar 1).

## STAGE-7: Optuna
**Hedef:** TPE + MedianPruner, objective = ortalama pinball. 50–100 trial.

## STAGE-8: Robustness (Sensör Kaybı)
**Hedef:** Augmentation ile sensör kaybı dayanıklılığı.  
**KRİTİK:** H1 iki yönlü test; coverage stability asıl metrik (Karar 7).

## STAGE-9: Baseline'lar + Smoke Holdout
**Hedef:** k-NN, SVM, LSTM, hafif TFT kıyası. Erken holdout smoke testi.

## STAGE-10: Analiz + Holdout
**Hedef:** Master tablo, DM testi + Holm-Bonferroni; holdout genelleme testi.

## STAGE-11: Streamlit Demo
## STAGE-12: Tez Yazımı
## STAGE-13: Makale

---

## Champion-Challenger protokolü
Promosyon kapısı: metrik+eşik · guardrail · leakage temiz · 2-3 seed doğrulama.
