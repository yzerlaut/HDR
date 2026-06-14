import sys, os
import numpy as np
import bibtexparser # pip install bibtexparser==1.4.3

references = ""

bibfile = os.path.expanduser(\
        '~/Documents/Notebook/Library/biblio.bib')

def reshape(author):
    # author is a string of type "Zerlaut, Yann Thomas"
    s = author.split(', ')[0]+' '
    for ss in author.split(', ')[1].split(' '):
        if len(ss)>0:
            s += ss[0]
    return s

if not os.path.isfile(bibfile):
    print()
    print(20*'-')
    print('  [!!] bibfile not found [!!]')
    print(20*'-')
    db = None

else:

    parser = bibtexparser.bparser.BibTexParser(\
            common_strings = True, interpolate_strings=False)
    with open(bibfile) as bfile:
        db = bibtexparser.load(bfile, parser=parser)

    # list of entries
    entries = np.array(\
        [ent['ID'] for ent in db.entries])

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


    for i, k in enumerate(keys):

        key = k.replace('.pdf','') # real key
        text = text.replace("href{%s}" % k, "hyperlink{%s}" % key)

        if len(references.split('\hypertarget{%s}' % key))<=1:

            if db is not None:

                i0  = np.flatnonzero(key==entries)

                if len(i0)==1:
                    entry = db.entries[i0[0]]
                    full_authors = ''
                    authors = entry['author'].split('and') 
                    nMax = min([len(authors),15])
                    for author in authors[:nMax-1]:
                        # 15 authors max
                        full_authors += reshape(author)+','
                    if len(authors)>15:
                        full_authors = full_authors[:-1]+' et al'
                    elif len(authors)>1:
                        full_authors = full_authors[:-1]+\
                                ' and'+reshape(authors[-1])
                    journal = entry['journal']
                    if 'volume' in entry and entry['volume']!='':
                        journal += ' (%s)' % entry['volume'] 
                    num_pages = ''
                    if 'number' in entry and entry['number']!='':
                        num_pages += entry['number'] 
                    num_pages += '. '
                    if 'pages' in entry and entry['pages']!='':
                        num_pages += entry['pages']+'.'

                    # first_author = entry['author'].split(',')[0] 
                    formatted_ref = \
                            ' %s (%s) %s. \\textit{%s}%s' %\
                            (full_authors,
                             entry['year'],
                             entry['title'],
                             journal, num_pages)
                    # print(formatted_ref)
                    if 'doi' in entry and entry['doi']!='':
                        references += """\hypertarget{%s}{%s} \href{%s}{doi:%s} \\\\[.2cm]
                    """ % (key, formatted_ref, 
                           'https://doi.org/'+entry['doi'],
                           entry['doi'])
                else:
                    print()
                    print(' --- reference key: %s' % key )
                    print(' ------          not found in bib file !')
                    print()

            else:
                print(key)

                references += """
            \hypertarget{%s}{%s} \\\\[.2cm]
            """ % (key, key)

    with open(fn, 'w') as f:
        print(fn)
        f.write(text)

with open('temp/pieces/references.tex', 'w') as f:
    f.write(references)

