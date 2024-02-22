(TeX-add-style-hook
 "project1"
 (lambda ()
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

