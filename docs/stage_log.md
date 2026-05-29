# Stage Log — tez-pv3

Kronolojik olay günlüğü. Her satır: tarih · olay · sonuç.

---

**2026-05-29** · STAGE-0 Bootstrap başlatıldı. Dizin ağacı + CLAUDE.md + Makefile + README.md + docs/ iskeleti oluşturuldu. Repo push edildi, champion-stage0 tag'i atıldı.

**2026-05-29** · STAGE-0 kapatıldı. Tamamlandı ölçütü doğrulandı (venv, core+torch/MPS import, make help/leakage, pytest 4/4, champion-stage0 tag, requirements 44 paket, git temiz). STAGE-1 Literatür'e geçildi. Proje yeri ~/anaconda_projects/tez-pv3.

**2026-05-29** · S1 literatür kapsam taraması. PV tabanı: "TEZ — PV Olasılıksal Tahmin" (28 kaynak). Eksen-1 (base/ensemble) tam; Eksen-2 quantile temeli var ama CQR/conformal boşluk; Eksen-3 (PV sensör-kaybı robustness + zero-shot domain generalization) boşluk = asıl katkı alanı. İki doğrudan öncül teyit: Atiea ve ark. (2025, Results in Eng.) ve Ali ve ark. (2026, Energies/HybrEnNet, PVOD v1.0). 43 kaynaklık defter yanlış etiketli (deep-research-agents içeriği), S1'de kullanılmadı.
