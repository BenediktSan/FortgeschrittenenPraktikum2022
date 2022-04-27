all: build/Protokoll_V70.pdf



#hier Python-Skripte


build/plots/dreh_04mbar.pdf:	|build
	python python/V70.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V70.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plots/dreh_04mbar.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V70.tex
	biber build/Protokoll_V70.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V70.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V70.aux Protokoll_V70.bcf Protokoll_V70.log Protokoll_V70.pdf Protokoll_V70.run.xml Protokoll_V70.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean
