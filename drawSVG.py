from fileinput import filename
import os
import argparse

parser = argparse.ArgumentParser(description='Process some parameters')
parser.add_argument('--folder', type=str, 
                    help='please add foldername')
parser.add_argument('--file', type=str, 
                    help='please add filename')
parser.add_argument('--number', type=int, default=20,
                    help="please input number of cases")

args = parser.parse_args()



id = args.number




for i in range(1, id+1):
    if i < 10:
        id = '00' + str(i)
    if i >= 10:
        id = '0' + str(i)
    command = "lqn2svg projectCode/"+ args.folder +"/" + args.file + ".d/" + args.file + "-" + id + ".lqxo"
    os.system(command)
