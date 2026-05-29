"""Deterministik dataset üretimi."""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    print(f"make_dataset.py — seed={args.seed}")
    print("Pipeline henüz kurulmadı (STAGE-0).")

if __name__ == "__main__":
    main()
