import sys

outputhtmlfilename = 'out.html'

def writehtmlline(filename, linedata):
    with open(filename,'a+') as htmlfile:
        htmlfile.write(linedata+'\n')

with open(sys.argv[1], 'r') as mdfile:
    mdlines = mdfile.read().split('\n')

with open(outputhtmlfilename,'w') as htmlfile:
    htmlfile.write('')

for line in mdlines:
    # heading parsing
    if line[:7] == '###### ':
        html = f'<h6>{line.split('###### ')[1]}<h6>'
        writehtmlline(outputhtmlfilename, html)
    elif line[:6] == '##### ':
        html = f'<h5>{line.split('##### ')[1]}<h5>'
        writehtmlline(outputhtmlfilename, html)
    elif line[:5] == '#### ':
        html = f'<h4>{line.split('#### ')[1]}<h4>'
        writehtmlline(outputhtmlfilename, html)
    elif line[:4] == '### ':
        html = f'<h3>{line.split('### ')[1]}<h3>'
        writehtmlline(outputhtmlfilename, html)
    elif line[:3] == '## ':
        html = f'<h2>{line.split('## ')[1]}<h2>'
        writehtmlline(outputhtmlfilename, html)
    elif line[:2] == '# ':
        html = f'<h1>{line.split('# ')[1]}<h1>'
        writehtmlline(outputhtmlfilename, html)

    # ordered list parsing

    # unordered list parsing

    # images/links parsing

    # code parsing

    # escape chars