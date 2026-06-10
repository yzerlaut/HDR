import sys, os

references = ""

n=1
for fn in sys.argv[1:]:

    with open(fn, 'r') as f:
        text = str(f.read())

    for S in text.split("\%\%beginFigure\%\%")[1:]:

        old_fig = S.split('}')[0].split('{')[1]
        key = S.split('}')[0].split('/')[-1].replace('.png','').replace('.svg','') # png or svg
        print('Figure %i.' % n, key, old_fig)

        S = "\%\%beginFigure\%\%"+S

        old_fig_string = S.split("\%\%endFigure\%\%")[0]+\
                                    "\%\%endFigure\%\%"

        # print(old_fig_string)
        new_fig_string = old_fig_string.replace(\
                "\%\%beginFigure\%\%", "\\begin{figure}\n")

        new_fig_string = new_fig_string.replace(\
                "\\textbf{", "\\textbf{\hypertarget{fig:%s}{Figure %i}. " % (key,n))

        new_fig_string = new_fig_string.replace(\
                "\%\%endFigure\%\%", "\end{figure}")

        # new_fig_string = new_fig_string.replace(\
                # "../Figures", "./temp/Figures")

        new_fig_string = new_fig_string.replace(\
                "includesvg", "includegraphics")

        new_fig_string = new_fig_string.replace(\
                ".svg", ".png")

        text = text.replace("\href{%s}{Fig.}" % old_fig,
                            "\hyperlink{fig:%s}{Fig. %i}" % (key,n))

        text = text.replace(old_fig_string, new_fig_string)

        n+=1

    with open(fn, 'w') as f:
        f.write(text)
print()
print('  processed %i Figures' % (n-1))
print()

