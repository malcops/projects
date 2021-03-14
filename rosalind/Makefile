CXX=g++
GTEST_FLAGS=-lgtest -lpthread

.PHONY: dna rna revc gc hamm prot prtm

all: dna rna revc gc hamm prot prtm

dna:
	$(CXX) DNA/DNA.cpp -o DNA/dna

rna:
	$(CXX) RNA/RNA.cpp -o RNA/rna

revc:
	$(CXX) REVC/REVC.cpp -o REVC/revc

gc:
	$(CXX) GC/GC.cpp -o GC/gc

hamm:
	$(CXX) HAMM/HAMM.cpp -o HAMM/hamm

prot:
	$(CXX) PROT/PROT.cpp -o PROT/prot

prtm:
	$(CXX) PRTM/PRTM.cpp -o PRTM/prtm
