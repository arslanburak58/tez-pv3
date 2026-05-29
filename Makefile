.PHONY: help leakage repro compare test freeze

help:  ## Komutları listele
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

leakage:  ## Pipeline leakage taraması
	python scripts/check_leakage.py

repro:  ## seed=42 ile dataset+model yeniden üret, hash karşılaştır
	python scripts/make_dataset.py --seed 42 --verify

compare:  ## Challenger vs champion kıyasla (CH=<dal-adı>)
	@[ "${CH}" ] || ( echo "Kullanım: make compare CH=<dal-adı>"; exit 1 )
	python scripts/compare.py --challenger ${CH}

test:  ## Tüm testleri çalıştır
	pytest -q

freeze:  ## Bağımlılıkları sabitle
	pip freeze > requirements.txt && echo "requirements.txt güncellendi."
