# temporary folders for manuscript generation
mkdir -p temp
mkdir -p temp/pieces
mkdir -p temp/manuscript

if true; then
    for f in Career-Overview Academic-degrees Training Publications
    do
        pandoc -i CV/$f.md -o temp/pieces/$f.tex
    done
fi

if true; then

    cp ./Introduction.md temp/pieces/Introduction.md
    pandoc -i temp/pieces/Introduction.md -o temp/pieces/Introduction.tex

    cat $(ls Past-Research/*.md) > temp/pieces/Past-Research.md
    pandoc -i temp/pieces/Past-Research.md -o temp/pieces/Past-Research.tex

    cat $(ls Research-Projects/*.md) > temp/pieces/Research-Projects.md
    pandoc -i temp/pieces/Research-Projects.md -o temp/pieces/Research-Projects.tex

    cat $(ls Supervision/*.md) > temp/pieces/Supervision.md
    pandoc -i temp/pieces/Supervision.md -o temp/pieces/Supervision.tex

    # process references (this builds temp/pieces/references.tex)
    python build/process_references.py temp/pieces/Introduction.tex temp/pieces/Past-Research.tex temp/pieces/Research-Projects.tex temp/pieces/Supervision.tex

    pandoc -i Summaries/Summary.md -o temp/pieces/Summary.tex
    pandoc -i Summaries/Resume.md -o temp/pieces/Resume.tex

    # figures:
    mkdir -p temp/manuscript
    cp build/titlepage.pdf temp/pieces/titlepage.pdf
    cp build/Funding.tex temp/pieces/Funding.tex
    cp build/full.tex temp/manuscript/full.tex
fi

if true; then
    python build/process_figures.py temp/pieces/Introduction.tex temp/pieces/Past-Research.tex temp/pieces/Research-Projects.tex temp/pieces/Supervision.tex
fi

# Copy PDFs 
#cp ~/Documents/Research/my_papers/2_Zerlaut-et-al_JPhysiol2016.pdf temp/pieces/1.pdf

if true; then
    cd temp/manuscript
    pdflatex full.tex # uses the different "pieces"
    pdflatex full.tex # redo for cross referencing
    mv full.pdf ../../HDR.pdf
    cd ../..
fi

if true; then
    #rm -rf temp
    open HDR.pdf
fi

