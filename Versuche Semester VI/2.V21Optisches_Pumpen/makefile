all: build/Protokoll_V21.pdf



#hier Python-Skripte


build/Magnetfeld.png:	|build
	python python/V21.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V21.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/Magnetfeld.png | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V21.tex
	biber build/Protokoll_V21.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V21.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V21.aux Protokoll_V21.bcf Protokoll_V21.log Protokoll_V21.pdf Protokoll_V21.run.xml Protokoll_V21.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean