# HDR

*material for the fulfilment of the french Habilitation à Diriger les Recherches (HDR)*

## Compile and build the final pdf with:

```
bash build/figures.sh # for the figures
bash build/report.sh # for the manuscript
```

### Some synchronization snippets

- sync text to iCloud (from Notebook)
```
iCloudHDR=/Users/yann/Library/Mobile\ Documents/iCloud\~md\~obsidian/Documents/HDR
rsync -rvhP --exclude "temp" --exclude "build" --exclude "*.git" --include="*/" --include="*.md" --exclude="*" ~/Documents/Notebook/HDR/* $iCloudHDR
```

- sync from iCloud back 
```
iCloudHDR=/Users/yann/Library/Mobile\ Documents/iCloud\~md\~obsidian/Documents/HDR
rsync -rvhP --exclude "*.git" --include="*/" --include="*.md" --include="*.svg" --exclude="*" $iCloudHDR/* ~/Documents/Notebook/HDR
```
