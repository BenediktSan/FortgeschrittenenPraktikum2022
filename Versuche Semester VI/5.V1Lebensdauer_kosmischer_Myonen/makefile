all: build/Protokoll_V01.pdf



#hier Python-Skripte


build/plots/lebensdauer.pdf:	|plots
	



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V01.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plots/lebensdauer.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V01.tex
	biber build/Protokoll_V01.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V01.tex

plots:
	python python/justage_10.py
	python python/justage_20.py
	python python/kalibration.py
	python python/untergrund.py
	python python/lebensdauer.py


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V01.aux Protokoll_V01.bcf Protokoll_V01.log Protokoll_V01.pdf Protokoll_V01.run.xml Protokoll_V01.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean
