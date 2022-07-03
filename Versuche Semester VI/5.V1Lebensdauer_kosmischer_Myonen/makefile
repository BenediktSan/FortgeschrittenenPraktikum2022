all: build/Protokoll_V1.pdf



#hier Python-Skripte


build/plots/plot1.pdf:	|build
	python python/V1.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V1.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plots/plot1.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V1.tex
	biber build/Protokoll_V1.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V1.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_.aux Protokoll_.bcf Protokoll_.log Protokoll_.pdf Protokoll_.run.xml Protokoll_.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean
