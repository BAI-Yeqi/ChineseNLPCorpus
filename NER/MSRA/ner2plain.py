'''
Convert NER data to plain texts.
'''


import os
import sys
sys.path.append('../../')
import argparse
from utils.list2txt import list2txt, txt2list


ner_labels = ['/o ', '/nr ', '/nt ', '/ns ']


def parse_args():
    parser = argparse.ArgumentParser()
    # arguments:
    parser.add_argument('--input_txt',
        help='path to input txt file, which will be processed',
        required=True, type=str)
    parser.add_argument('--output_txt',
        help='path to output txt file',
        required=True, type=str)
    args = parser.parse_args()
    return args


def process_ner_line(line):
    '''
    process a single line of NER data
    '''
    for label in ner_labels:
        line = line.replace(label, '')
    return line


def main(args):
    '''
    Load NER data, convert to plain txt format, save plain txt
    '''
    ner_list = txt2list(args.input_txt)
    plain_list = []
    for line in ner_list:
        plain_line = process_ner_line(line)
        plain_list.append(plain_line)
    list2txt(plain_list, args.output_txt)


if __name__ == '__main__':
    args = parse_args()
    main(args)
