# temporary folders for manuscript generation
mkdir -p temp
mkdir -p temp/Figures

fig_export() {
    # using inkscape
 /Applications/Inkscape.app/Contents/MacOS/Inkscape --export-area-page --export-filename=temp/$1 --export-type="png" --export-dpi=300 $1
 }

for filename in Figures/*.svg
do
    echo ""
    echo "-- exporting figure: " $filename
    fig_export $filename
done
