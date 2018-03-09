#!/usr/bin/env python
# -*- coding: utf-8 -*- if __name__ == '__main__':

import os
import  sys
import shutil

#??????dict
# with open('E:/Games/fileurl.txt', 'r') as f:
# 	result = {}
# 	for line in f.readlines():
# 		line = line.strip()
# 		if not len(line):
# 			continue
# 		result[line.split(':')[0].strip()] = int(line.split(':')[1].strip())
# print(result)

filedict = {'Baskhead': 1, 'FruitNinjaVR': 2, 'A-10VR': 3, 'Enigmatic-CyberThreat': 4, 'Tank Heroes VR': 5, 'Wrath Of The Fire God': 6, 'Holopoint': 7, 'The Nest': 8, 'UltimateBooster(SteamVR)': 9, 'Titans of Space 2.0': 10, 'Armed Against the Undead': 11, 'IrreVRsible': 12, 'Meteor Crush VR': 13, 'Proton Pulse': 14, 'Eclipse --- Defending the motherland': 15, 'BellyBots': 16, 'Thirst': 17, 'The Path of Greatest Resistance': 18, 'Brookhaven': 19, 'VRzGame': 20, 'The Thrill of the Fight': 21, 'Stars': 22, 'Unbreakable Vr Runner': 23, 'Tilt Brush': 24, 'Island 359': 25, 'House of Alice': 26, 'VRporize': 27, "Acan's Call": 28, 'Everest VR': 29, 'Carpe Lucem - Seize The Light': 30, 'Mercenary': 31, 'theBlu': 32, 'BoxEnglish': 33, 'WarOfPlaneEnglish': 34, 'NetworkShooterEn': 35, 'Snow Fortress': 36, 'VRSports': 37, 'War of Castle VR': 38, 'bullet sorrow VR': 39, 'Space Fist VR': 40, 'Onward': 41, 'ArtofFight': 42, 'rawdata': 43, 'ArizonaSunshine': 44, 'OverkillVR': 45, 'The Walk': 46, 'VRKanojo': 47, 'Counter Fight': 48, 'Duck Force': 49, 'Sairento VR': 50, 'SUPERHOT VR': 51, 'Sweet Escape VR': 52, 'Sword Master VR': 53, 'Trickster VR': 54, 'Audioshield': 55, 'Zombie Kill': 56, 'Elven Assassin': 57, 'VR Coaster Extreme': 58, 'Fancy Skiing VR': 59, '2017 VR': 60, 'Carnival Games VR': 61, 'Fallout 4 VR': 62, 'FrontDefense': 63, 'RedCliffsVR': 64}

#path = 'C:\\Users\\test\\Desktop\\????????\\lua-5.3.4\\'
path = os.getcwd()
path += "\\"
print("当前路径为:",path)
dirs = os.listdir(path)
for dir in dirs:
	if os.path.isdir(path + dir):
		print (dir)
		if dir in filedict.keys():
			pathGame = path + dir
			print("    id:",filedict[dir])
			try:
				shutil.move(pathGame, pathGame + "_temp")
				pathGame = pathGame + "_temp"
				print("游戏文件夹重命名为临时名:",pathGame)
			
				pathID = path + str(filedict[dir])
				os.mkdir(pathID)  
				print("创建pathID文件夹:",pathID)
				
				shutil.move(pathGame,pathID)
				print("移动游戏文件夹:"+pathGame+"至新ID路径:"+pathID)
				
				newGamePath = pathID + "\\" + dir + "_temp"
				shutil.move(newGamePath, pathID +"\\"+ str(1))
				print("重命名游戏文件夹为版本号1","\n\n\n")
				#os.mkdir(os.path.join(path , str(filedict[dir])))
				
				#shutil.move(path + str(1),path + str(filedict[dir]))
			except Exception as e:
				print("错误:",e)
				os.system("pause")
		else:
			print("    不能识别的路径")
os.system("pause")