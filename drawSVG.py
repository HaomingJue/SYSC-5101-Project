from fileinput import filename
import os

id = 1

folderName = "1-4PCMSensitvity"
fileName = "template_1_pcm0.9"



for i in range(1, 21):
    if i < 10:
        id = '00' + str(i)
    if i >= 10:
        id = '0' + str(i)
    command = "lqn2svg projectCode/"+ folderName +"/" + fileName + ".d/" + fileName + "-" + id + ".lqxo"
    os.system(command)
