(TeX-add-style-hook
 "project2"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "report"
    "rep10"
    "comment"
    "fancyhdr"
    "listings"
    "titlesec"
    "tikz"))
 :latex)

