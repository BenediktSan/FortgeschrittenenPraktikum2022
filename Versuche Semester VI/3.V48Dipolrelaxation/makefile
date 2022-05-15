all: build/Protokoll_V48.pdf



#hier Python-Skripte


#build/plots/dreh_04mbar.pdf:	|build
#	python python/V70.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V48.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V48.tex
	biber build/Protokoll_V48.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V48.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V48.aux Protokoll_V48.bcf Protokoll_V48.log Protokoll_V48.pdf Protokoll_V48.run.xml Protokoll_V48.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean
