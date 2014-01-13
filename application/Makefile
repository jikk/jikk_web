BIBTEX=bibtex
PDFLATEX=pdflatex

all: res.pdf tea.pdf cv.pdf

#%.pdf : %.tex
#	${PDFLATEX} $<

res.pdf: res.tex res.bib
	${PDFLATEX} $<
	${BIBTEX} res
	${PDFLATEX} $<

tea.pdf: tea.tex
	${PDFLATEX} $<

cv.pdf: cv.tex
	${PDFLATEX} $<

clean:
	rm -f *.pdf *.aux *.log *.blg
