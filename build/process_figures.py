import sys, os

references = ""

n=1
for fn in sys.argv[1:]:

    with open(fn, 'r') as f:
        text = str(f.read())

    for S in text.split("\%\% beginFigure \%\%")[1:]:

        fig = S.split('}')[0].split('{')[1]
        key = S.split('}')[0].split('/')[-1].replace('.png','').replace('.svg','') # png or svg

        S = "\%\% beginFigure \%\%"+S

        old_fig_string = S.split("\%\% endFigure \%\%")[0]+\
                                            "\%\% endFigure \%\%"

        new_fig_string = old_fig_string.replace(\
                "\%\% beginFigure \%\%", "\\begin{figure}\n")

        new_fig_string = new_fig_string.replace(\
                "\\textbf{", "\\textbf{\hypertarget{fig:%s}{Figure %i}. " % (key,n))

        new_fig_string = new_fig_string.replace(\
                "\%\% endFigure \%\%", "\end{figure}")

        # print(new_fig_string)
        text = text.replace("\href{%s}{Fig.}" % fig,
                            "\hyperlink{fig:%s}{Fig. %i}" % (key,n))

        new_fig_string = new_fig_string.replace("svg", "png") # force png figs

        text = text.replace(old_fig_string, new_fig_string)

        n+=1

    with open(fn, 'w') as f:
        f.write(text)
print()
print('  processed %i Figures' % (n-1))
print()

