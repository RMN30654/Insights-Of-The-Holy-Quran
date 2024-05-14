import sys
import time
import cv2
import numpy as np
import os
from pathlib import Path
import playsound
import tkinter

class al_Furqaan:
	
	def __init__(self,surah=1,ayah=0):
		BASE_DIR = str(Path(__file__).resolve().parent)+'/alQuran/'
		self.path = BASE_DIR #+self.ayah_image_name
		#print(self.path)
		self.surah = surah
		self.ayah = ayah
		self.format_ayah_audio()
		self.format_ayah_image()

	def format_ayah_image(self):
		self.ayah_image_name = str(self.surah)+'_'+str(self.ayah)+".png"
		#print(self.ayah_image_name)

	def format_ayah_audio(self):
		self.ayah_audio_name = str(self.surah).zfill(3)+str(self.ayah).zfill(3)+".mp3"

	def ayah_show(self):
		img = cv2.imread(self.path+'000_images/'+self.ayah_image_name)
		cv2.imshow(self.ayah_image_name,img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def ayah_recite(self,reciter='Sudais'):
		self.reciter = reciter
		playsound.playsound(self.path+'000_versebyverse/'+self.reciter+'/'+self.ayah_audio_name)
		
	def ayah_recite_and_show(self,reciter='Sudais'):
		img = cv2.imread(self.path+'000_images/'+self.ayah_image_name)
		app = tkinter.Tk()
		width = app.winfo_screenwidth()
		height = app.winfo_screenheight()
		cv2.imshow(self.ayah_image_name,img)
		cv2.moveWindow(self.ayah_image_name,width-1750,200)
		self.reciter = reciter
		playsound.playsound(self.path+'000_versebyverse/'+self.reciter+'/'+self.ayah_audio_name)
		cv2.destroyAllWindows()
		
	def serial_tracker(self):
		ff = open(self.path+"surahayahNumber.txt",'r')
		tff = ff.readlines()
		ff.close()
		tff = [x.strip('\n') for x in tff]
		p = open(self.path+"/tracker.txt",'r')
		a = int(p.read()) #current ayah number
		self.current_ayah_number = a
		p.close()
		p = open(self.path+"/tracker.txt",'w')
		p.write(str(a+1)) #update ayah number
		p.close()
		return tff[int(a)-1]
		


if __name__ == '__main__':
	al_Furqaan().ayah_recite_and_show()
	al_Furqaan(1,1).ayah_recite_and_show()
	a = al_Furqaan().serial_tracker()
	al_Furqaan(a.split(' ')[0].split(':')[1],a.split(' ')[1].split(':')[1]).ayah_recite_and_show()
else:
	surahayah = input('Input surah and ayah number : ')
	a = al_Furqaan(surahayah.split(' ')[0],surahayah.split(' ')[1])
	a.ayah_recite_and_show()
	print(__name__)






















'''

def ayatReciteAndShow():
	BASE_DIR = Path(__file__).resolve().parent
	print(BASE_DIR)
	BASE_DIR = str(BASE_DIR)
	subprocess.Popen(["/usr/bin/amixer","-D","pulse","sset","Master","30%"])
	time.sleep(1)
	#pa = subprocess.Popen(["cvlc",BASE_DIR+"/alQuran/000_versebyverse/001000.mp3",'--volume=100'])
	#time.sleep(4)
	#pa.kill()
	playsound.playsound(BASE_DIR+"/alQuran/000_versebyverse/001000.mp3")
	#pa = subprocess.Popen(["cvlc",BASE_DIR+"/alQuran/000_versebyverse/001001.mp3"])
	#time.sleep(4)
	#pa.kill()
	playsound.playsound(BASE_DIR+"/alQuran/000_versebyverse/001001.mp3")
	ff = open(BASE_DIR+"/alQuran/ayahFinal.txt",'r')
	tff = ff.readlines()
	ff.close()
	tff = [x.strip('\n') for x in tff]
	p = open(BASE_DIR+"/tempfile.txt",'r')
	a = int(p.read())
	p.close()
	p = open(BASE_DIR+"/tempfile.txt",'w')
	p.write(str(a+1))
	p.close()
	print(BASE_DIR+"/alQuran/000_images/"+tff[int(a)-1].split(' ')[4].split(':')[1])
	os.environ['DISPLAY'] = ':0.0'
	print(os.environ['DISPLAY'])
    #cv2.imshow('window on %s'%display, a)
	img = cv2.imread(BASE_DIR+"/alQuran/000_images/"+tff[int(a)-1].split(' ')[4].split(':')[1] )
	#pa = subprocess.Popen(["cvlc",BASE_DIR+"/alQuran/000_versebyverse/"+tff[int(a)-1].split(' ')[2].split(':')[1]])
	
	cv2.imshow(tff[int(a)-1].split(' ')[4].split(':')[1],img)
	cv2.moveWindow(tff[int(a)-1].split(' ')[4].split(':')[1], 950, 500)
	playsound.playsound(BASE_DIR+"/alQuran/000_versebyverse/"+tff[int(a)-1].split(' ')[2].split(':')[1])
	#cv2.waitKey(int(tff[int(a)-1].split(' ')[3].split(':')[1])*1000)
	cv2.destroyAllWindows()
	#pa.kill()
	
	p = subprocess.Popen(["/usr/bin/amixer",
					  "-D","pulse","sset",
					  "Master","50%"])
	time.sleep(0.1)
	p.kill()

#-------------------------------------------------------------------


ayatReciteAndShow()
'''