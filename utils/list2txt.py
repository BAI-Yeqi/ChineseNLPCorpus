'''
This module define the function to output elements in a list to a txt
'''


def list2txt(input_list, txt_path):
    '''
    Save list to text file
    Arguments:
        input_list (list): list to convert
        txt_path (str): path to save the text file
    '''
    with open(txt_path, 'w') as out_file:
        for element in input_list:
            out_file.write('{}\n'.format(str(element)))

    print('{} saved.'.format(txt_path))


def txt2list(txt_path):
    '''
    Read a txt file and return a list
    Arguments:
        txt_path (str): path to save the text file
    '''
    output = []
    f = open(txt_path, 'r')
    for line in f.readlines():
        output.append(line.replace('\n', ''))
    f.close()
    print('{} loaded.'.format(txt_path))

    return output
