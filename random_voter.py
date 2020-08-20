from random import randint
from os import system

def vote():
    ad_num = str(randint(1000000000000000, 9999999999999999))
    system("echo '"+ad_num+" 1900' >> ./reg_data.txt")
    system("echo '"+str(randint(1, 5))+' '+ad_num+"' >> ./vote_data.txt")

for i in range(5):
    vote()

system("python3 ./result.py")