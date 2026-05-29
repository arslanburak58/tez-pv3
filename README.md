# tez-pv3

**Fotovoltaik Sistemlerde Sensör Kayıplarına Dayanıklı Olasılıksal Güç Tahmini**

Burak Arslan · Doç. Dr. Kenan Altun  
Sivas Cumhuriyet Üniversitesi · FBE · YZ ve Veri Bilimi ABD

## Kurulum

```bash
python -m venv tez-env
source tez-env/bin/activate
pip install -r requirements.txt
```

## Çalıştırma

```bash
make help        # tüm komutlar
make leakage     # leakage taraması
make test        # testler
make repro       # reproduksiyon doğrulama
```

## Veri

Ham veri `.gitignore`'da — commit edilmez.  
Kaynak: DKASC (Alice Springs, Avustralya) + PVOD (Hebei, Çin).  
Detay: `docs/data_provenance.md`

## Yapı

```
docs/        → günce, karar defteri, deney logu
features/    → fizik + zamansal öznitelikler
models/      → taban + meta öğrenici + baselines
evaluation/  → metrikler, DM testi
experiments/ → challenger deneyleri (izole)
scripts/     → leakage, compare, dataset üretimi
```

## Açık Bilim

Seed=42, tüm bağımlılıklar `requirements.txt`'te sabitlenmiş.  
Ham veri lisansları: `docs/data_provenance.md`
