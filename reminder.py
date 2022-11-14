# program for remainders about relaxing, drink water, eyes exercise,etc...
import time
from pygame import mixer

# initialize sound
mixer.init()
mixer.music.load("bell.wav")
mixer.music.set_volume(1)

# some decoration
print("Started --> " + time.strftime("%H") + ':' + time.strftime("%M") + ':' +time.strftime("%S"))

#functions...
def time_now():     #returns current "hour + min" in minutes
    hour, mint = int(time.strftime("%H")),int(time.strftime("%M"))
    return (hour*60 + mint)
    
timestamp = [time_now(),time_now(),time_now()] # index '0' = water , index '1' = eyes exercise, index '2' = physical exercise

def music_start():    # play sound on loop as arg is '-1'
    mixer.music.play(-1)
def music_stop():   # stop playing music
    mixer.music.stop()

# exercises to be used
def water():
    # 100 ml water every 30 minutes
    music_start()
    input("Time to drink water (100 ml) ...")
    hour = time.strftime("%H")
    mint = time.strftime("%M")
    scnd = time.strftime("%S")
    time_write = hour + ":" + mint + ":" + scnd
    str_write = f"[{time_write}] : Drank Water \n"
    with open("data.txt","a") as file:
        file.write(str_write)
    timestamp[0] = time_now()
    music_stop()
    return

def eyes():
    # relax eyes every hour
    music_start()
    input("Time to relax your eyes ...")
    hour = time.strftime("%H")
    mint = time.strftime("%M")
    scnd = time.strftime("%S")
    time_write = hour + ":" + mint + ":" + scnd
    str_write = f"[{time_write}] : Relaxed Eyes \n"
    with open("data.txt","a") as file:
        file.write(str_write)
    timestamp[1] = time_now()
    music_stop()
    return
    
def strech():
    # body streching every 100 minutes
    music_start()
    input("Time for some streching ...")
    hour = time.strftime("%H")
    mint = time.strftime("%M")
    scnd = time.strftime("%S")
    time_write = hour + ":" + mint + ":" + scnd
    str_write = f"[{time_write}] : Streched Up Body \n"
    with open("data.txt","a") as file:
        file.write(str_write)
    timestamp[2] = time_now()
    music_stop()
    return
    
# intervals
water_interval = 30     # minutes b/w intervals
eyes_interval = 50     # minutes b/w intervals
streching_interval = 40     # minutes b/w intervals

# checks timing and call repective functions
while (True):
    if ((time_now() - timestamp[0]) > water_interval):     #check for water timing
        water()
    if ((time_now() - timestamp[1]) > eyes_interval):     # check for eyes timing
        eyes()
    if ((time_now() - timestamp[2]) > streching_interval):     # check for physic training
        strech()
# end