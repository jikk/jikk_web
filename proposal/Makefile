FILES = proposal.aux proposal.blg proposal.dvi proposal.log proposal.ps proposal.pdf

all: proposal

proposal: bbl
	dvipdf proposal.dvi
	dvips -o proposal.ps -t letter proposal.dvi

bbl: proposal.tex proposal.bib
	rm -rf proposal.bbl
	latex proposal
	bibtex proposal
	latex proposal
	latex proposal

clean:
	rm -f $(FILES)
