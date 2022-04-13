from fileinput import filename
import os
import argparse

parser = argparse.ArgumentParser(description='Process some parameters')
parser.add_argument('--fd', type=str, 
                    help='please add foldername')
parser.add_argument('--fn', type=str, 
                    help='please add filename')

args = parser.parse_args()



id = 1

folderName = "1-4PCMSensitvity"
fileName = "template_1_pcm0.9"



for i in range(1, 21):
    if i < 10:
        id = '00' + str(i)
    if i >= 10:
        id = '0' + str(i)
    command = "lqn2svg projectCode/"+ args.fd +"/" + args.fn + ".d/" + args.fn + "-" + id + ".lqxo"
    os.system(command)
