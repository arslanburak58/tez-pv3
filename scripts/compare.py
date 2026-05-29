"""Challenger vs champion kıyaslama."""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--challenger", required=True)
    args = parser.parse_args()
    print(f"compare.py — challenger: {args.challenger}")
    print("Pipeline henüz kurulmadı (STAGE-0).")

if __name__ == "__main__":
    main()
