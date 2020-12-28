import os
k = 6

if not os.path.exists('sample_data/deepsea/{:d}'.format(k)):
    os.makedirs('sample_data/deepsea/{:d}'.format(k))

# ftrain = open('sample_data/deepsea/{:d}/train.tsv'.format(k),'w')
# fdev = open('sample_data/deepsea/{:d}/dev.tsv'.format(k),'w')

with open('sample_data/deepsea/{:d}/train.tsv'.format(k), 'a') as ftrain:
    ftrain.writelines('sequence  label\n')
ftrain.close()
with open('sample_data/deepsea/{:d}/dev.tsv'.format(k), 'a') as fdev:
    fdev.writelines('sequence  label\n')
fdev.close()

with open('sample_data/deepsea/sample_output.csv','r') as orig:
    # Using readlines()
    Lines = orig.readlines()
    for j,line in enumerate(Lines[1:]):
        c =line.split(',')
        sequence = c[0]
        if c[0][0] =='N':
            continue
        kmers  = [sequence[i*k:(i+1)*k] for i in range(len(sequence)//k)]
        lables = [int('1' in i) for i in c[1:]]

        # write to new file
        if j < len(Lines[1:])*0.8:
            with open('sample_data/deepsea/{:d}/train.tsv'.format(k),'a') as ftrain:
                ftrain.writelines([i+' ' for i in kmers])
                ftrain.write(' ')
                ftrain.writelines([' '.join(str(i)) for i in lables])
                ftrain.write('\n')
        else:
            with open('sample_data/deepsea/{:d}/dev.tsv'.format(k),'a') as fdev:
                fdev.writelines([i+' ' for i in kmers])
                fdev.write(' ')
                fdev.writelines([' '.join(str(i)) for i in lables])
                fdev.write('\n')
