# способ 1
#import sys

#print(sys.argv)

#способ 2

# import getopt
#
# argv = sys.argv[1::]
#
# try:
#     opts, args = getopt(argv, "f:l:", ["first_name=", "last_name="])
# except:
#     print('ERROR')
#
# for opt, arg in opts:
#     print(opt, arg)


# 3 способ

import argparse
parser = argparse.ArgumentParser(
    prog='Prog name',
    description='This prog does this and that',
    epilog='Footer'
)
parser.add_argument('filename') # позиционный аргумент
parser.add_argument('-c', '--count') # именованный аргумент
parser.add_argument('-v', '--verbose', action='store_true') # принимает булево значение

args = parser.parse_args()
print(args)