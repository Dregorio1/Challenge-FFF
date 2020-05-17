import sys
import re
import argparse


def main():
    parser = argparse.ArgumentParser(description='Strings but better')
    
    parser.add_argument('path', type=str,
                        help='path to file')
    parser.add_argument('-n', type=int, default=4,
                        help='least [n] characters (default 4)')

    args = parser.parse_args()

    with open(args.path, 'br') as f:
        lines = [re.split(r'\\x[0-9a-fA-F]{2}', str(line)) for line in f.readlines()]
        for line in lines:
            for word in line:
                if len(word) >= args.n:
                    print(word)



if __name__ == '__main__':
    main()
