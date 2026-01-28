# first separate text into dict with keys and values

nodes = {}

def get_lines(source):
    text = open(source, 'r')
    list_lines = text.readlines() # list of lines
    return list_lines

def make_dict(text):
    count=0
    for i in text:
        i = i.replace("\n","")
        i = i.replace(">", "")
        count +=1
        if count % 2 == 1:
            key = i
        else:
            value = i
            nodes[key] =value
    return nodes

def fasta2dict(fil):
    """
    Read fasta-format file fil, return dict of form scaffold:sequence.
    Note: Uses only the unique identifier of each sequence, rather than the
    entire header, for dict keys.
    """
    dic = {}
    cur_scaf = ''
    cur_seq = []
    for line in open(fil):
        if line.startswith(">") and cur_scaf == '':
            cur_scaf = line.split(' ')[0]
            cur_scaf = cur_scaf.replace(">", "")
            #print ('cur-scaf 1 ', cur_scaf)
        elif line.startswith(">") and cur_scaf != '':
            dic[cur_scaf] = ''.join(cur_seq)
            cur_scaf = line.split(' ')[0]
            cur_scaf = cur_scaf.replace(">", "")
            #print('cur-scaf', cur_scaf)
            cur_seq = []
        else:
            cur_seq.append(line.rstrip())
    #print(cur_scaf)
    cur_scaf = cur_scaf.replace(">", "")
    dic[cur_scaf] = ''.join(cur_seq)
    return dic

if __name__ == '__main__':
    make_dict(get_lines('rosalind_grph.txt'))
    dic = fasta2dict('rosalind_grph.txt')
    #print(dic)

#define some variables
"""
k = int (3)
for key in nodes:
    value = nodes[key]
    sufix = value [(len(value)-k):len(value)]
    for i in nodes:
        value = nodes[i]
        prefix = value[0:k]
        if i != key:
            if sufix == prefix:
                print(key, i)
"""
k = int (3)
for key in dic:
    value = dic[key]
    sufix = value [(len(value)-k):len(value)]
    #print(key,"s", sufix)
    for i in dic:
        value = dic[i]
        prefix = value[0:k]
        #print (i,"p",prefix)
        if i != key:
            if sufix == prefix:
                print(key.strip(), i.strip())
