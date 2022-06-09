all: build/Protokoll_V14.pdf



#hier Python-Skripte


build/plots/spektrum.pdf:	|build
	python python/V14.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V14.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex  build/plots/spektrum.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V14.tex
	biber build/Protokoll_V14.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V14.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V14.aux Protokoll_V14.bcf Protokoll_V14.log Protokoll_V14.pdf Protokoll_V14.run.xml Protokoll_V14.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean
