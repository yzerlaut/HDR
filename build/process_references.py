import sys, os
import numpy as np

references = ""

for fn in sys.argv[1:]:

    with open(fn, 'r') as f:
        text = str(f.read())

    # os.remove(fn)

    # 1) grab from main document:
    keys = []
    for k in text.split('\href{'):
        key = k.split('}')[0]
        if '.pdf' in key:
            keys.append(key)

    # 2) sort in alphabetical order
    keys = np.sort(keys)


    for k in keys:

        key = k.replace('.pdf','') # real key
        text = text.replace("href{%s}" % k, "hyperlink{%s}" % key)

        # 3) grab in reference biblio.bib file


        # 4)
        # ------------------------------- #
        # update the references code here #
        #  - fetch from biblio
        #  - nice formatting
        # ------------------------------ #
        if len(references.split('\hypertarget{%s}' % key))<=1:
            print(key)
            references += """
        \hypertarget{%s}{%s} \\\\[.2cm]
        """ % (key, key)

    with open(fn, 'w') as f:
        print(fn)
        f.write(text)

with open('temp/pieces/references.tex', 'w') as f:
    f.write(references)

