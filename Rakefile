require 'rake/clean'

#CLOBBER.include()
CLEAN.include(['*.log', '*.out', '*_files', '*.aux', '*.tex', '*.tex-e'])


rule '.pdf' => ['.ipynb'] do |t|
    # I'll leave this as an example of how to use a template to remove the code cells.
    # #`jupyter nbconvert --template=/Users/tim/Projects/jupyternbcode/hidecode.tplx --to latex --execute "#{t.source}"`
    `jupyter nbconvert --to latex --execute "#{t.source}"`
    #texfn = t.name.sub('.pdf', '.nbconvert.tex')
    texfn = t.name.sub('.pdf', '.tex')
    `sed -i -e 's/Out.*]:}/}/'  "#{texfn}"`
#    `sed -i -e 's/\documentclass\\[11pt\\]\{article\}/\documentclass[10pt,a3paper,landscape]{article}/'  "#{texfn}"`
    `xelatex "#{texfn}"`
end
