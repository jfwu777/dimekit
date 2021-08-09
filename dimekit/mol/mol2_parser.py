def _mol2_parser(file):
    with open(file, 'r') as fp:
        is_started = False
        xmax = None
        xmin = None
        ymax = None
        ymin = None
        zmax = None
        zmin = None
        xsum = 0
        ysum = 0
        zsum = 0
        cnt = 0
        
        for line in fp:
            if is_started and line.startswith('@<TRIPOS>'):
                break
            if is_started:
                x = float(line[17:27])
                y = float(line[27:37])
                z = float(line[37:47])

                if xmax is None:
                    xmax = x
                    xmin = x
                else:
                    xmax = max(x, xmax)
                    xmin = min(x, xmin)

                if ymax is None:
                    ymax = y
                    ymin = y
                else:
                    ymax = max(y, ymax)
                    ymin = min(y, ymin)

                if zmax is None:
                    zmax = z
                    zmin = z
                else:
                    zmax = max(z, zmax)
                    zmin = min(z, zmin)

                xsum += x
                ysum += y
                zsum += z
                cnt += 1
            if line.startswith('@<TRIPOS>ATOM'):
                is_started = True
        center = (xsum/cnt, ysum/cnt, zsum/cnt)
        span = (xmax-xmin, ymax-ymin, zmax-zmin)
    return center, span

def str_parser(file, type=None):
    """
    A structure parser that supports: pdb / pdbqt / mol2
    """
    assert type is None, "Please specify the file type"
    
    if type == "mol2":
        _mol2_parser(file)
    else:
        raise Exception("File type not supported")
