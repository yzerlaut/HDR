import sys, os

references = ""

for fn in sys.argv[1:]:

    with open(fn, 'r') as f:
        text = str(f.read())

    # os.remove(fn)

    keys = []
    for k in text.split('\href{'):
        key = k.split('}')[0]
        if '.pdf' in key:
            keys.append(key)

    for k in keys:

        key = k.replace('.pdf','') # real key
        text = text.replace("href{%s}" % k, "hyperlink{%s}" % key)

        # ------------------------------- #
        # update the references code here #
        #  - fetch from biblio
        #  - alphabetical order
        #  - nice formatting
        # ------------------------------ #
        if len(references.split('\hypertarget{%s}' % key))<=1:
            references += """
        \hypertarget{%s}{%s} \\\\[.2cm]
        """ % (key, key)

    with open(fn, 'w') as f:
        print(fn)
        f.write(text)

with open('temp/pieces/references.tex', 'w') as f:
    f.write(references)

