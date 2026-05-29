"""Pipeline leakage taraması — make leakage ile çalıştırılır."""
import sys

CHECKS = [
    "scaler/imputer/encoder yalnızca train'de fit edildi",
    "OOF zamansal sıralı (shuffle=False)",
    "val_select != test (ayrı bölümler)",
    "future leakage yok (gap=24)",
    "daylight maskesi tüm modellerde aynı uygulanıyor",
    "holdout istasyonları hiçbir fit'e girmedi",
    "sample weight test metriğine sızmadı",
]

def main():
    print("=" * 60)
    print("Leakage kontrol listesi — tez-pv3")
    print("=" * 60)
    for i, check in enumerate(CHECKS, 1):
        print(f"  [{i}] {check}")
    print("\nDurum: STAGE-0 — kontrol edilecek pipeline yok.")
    print("=" * 60)

if __name__ == "__main__":
    main()
