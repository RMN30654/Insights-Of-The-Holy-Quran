import cv2
from pathlib import Path
import playsound
import tkinter

class al_Furqaan:
	
	def __init__(self,surah=1,ayah=0):
		BASE_DIR = str(Path(__file__).resolve().parent)+'/alQuran/'
		self.path = BASE_DIR
		self.surah = surah
		self.ayah = ayah
		self.format_ayah_audio()
		self.format_ayah_image()

	def format_ayah_image(self):
		self.ayah_image_name = str(self.surah)+'_'+str(self.ayah)+".png"

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
	def page_recite(self):
		pass
		


if __name__ == '__main__':
	al_Furqaan().ayah_recite_and_show()
	al_Furqaan(1,1).ayah_recite_and_show()
	a = al_Furqaan().serial_tracker()
	al_Furqaan(a.split(' ')[0].split(':')[1],a.split(' ')[1].split(':')[1]).ayah_recite_and_show()
else:
	surahayah = input('Input surah and ayah number : ')
	a = al_Furqaan(surahayah.split(' ')[0],surahayah.split(' ')[1])
	a.ayah_recite_and_show()
