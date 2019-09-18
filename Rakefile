require 'rake/clean'

#CLOBBER.include()
CLEAN.include(['*.log', '*.out', '*_files', '*.aux', '*.tex', '*.tex-e'])


task 'mkreadings' do
    `python3 simple.py howard3/pumpkin_8444/var/log/hub-connect/hub-connect.log  howard.readings.pkl --ignoreb4 "2019-04-23 12:00:00"`
    `python3 simple.py vivian/pumpkin_53314/var/log/hub-connect/hub-connect.log  vivian.readings.pkl`


end

rule '.pdf' => ['.ipynb'] do |t|
#    `jupyter nbconvert --template=/Users/tim/Projects/jupyternbcode/hidecode.tplx --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags="['remove_cell']" --to latex --execute "#{t.source}"`
    # does not work. Cannot remove tagged cells.
    # `jupyter nbconvert --template=/Users/tim/Projects/jupyternbcode/hidecode.tplx --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags="['remove_cell']" --to notebook "#{t.source}"`
    # interim file does not work
    # `jupyter nbconvert --template=/Users/tim/Projects/jupyternbcode/hidecode.tplx --to latex --execute "#{t.source.sub('.ipynb', '.nbconvert.ipynb')}"`
    #`jupyter nbconvert --template=/Users/tim/Projects/jupyternbcode/hidecode.tplx --to latex --execute "#{t.source}"`
    `jupyter nbconvert --to latex --execute "#{t.source}"`
    #texfn = t.name.sub('.pdf', '.nbconvert.tex')
    texfn = t.name.sub('.pdf', '.tex')
    `sed -i -e 's/Out.*]:}/}/'  "#{texfn}"`
#    `sed -i -e 's/\documentclass\\[11pt\\]\{article\}/\documentclass[10pt,a3paper,landscape]{article}/'  "#{texfn}"`
    `xelatex "#{texfn}"`
end

# curl --header "Content-Type: application/json" https://homeinstead.anthropos.io/PumpHouse/rest/v1/iot/users/5b225850c7fe056c9624783c/residences | jq '.residence[].locations[].deviceSlots[].devices[]' > 5b2259aac7fe056c962480d
