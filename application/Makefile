PDFLATEX=pdflatex

all: res.pdf tea.pdf cv.pdf

%.pdf : %.tex
	${PDFLATEX} $<

clean:
	rm -f *.pdf *.aux *.log