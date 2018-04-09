import skimage
import os
from skimage import data, io, filters, color
from skimage import feature
from skimage import measure
from skimage.color import rgb2gray

class Ski:
	
	def __init__(self, sigma):
		self.sigma = sigma

	def give_Aver (self, srt, name):
		filename = os.path.join(skimage.data_dir, srt + name)
		image = io.imread(filename)
		image_g = rgb2gray(image)
		edges = feature.canny(image_g, sigma=self.sigma)
		aver = measure.perimeter(edges)
		return aver

	def learn (self):
		files = os.listdir('apple/')
		aver_sum = 0
		num = 0
		minn = 1000
		maxx = 100
		for name in files:
			aver = self.give_Aver(srt = 'apple/', name = name)
			aver_sum += aver
			num += 1
			if(minn > aver):
				minn = aver
			if(maxx < aver):
				maxx = aver

		print("aver_sum: ", aver_sum)
		print("num: ", num)
		print("average: ", aver_sum/num)
		print("min:", minn)
		print("max: ", maxx)
		self.apple = aver_sum/num
		self.applemin = minn
		self.applemax = maxx
		
		files = os.listdir('avokado/')
		aver_sum = 0
		num = 0
		minn = 1000
		maxx = 100
		for name in files:
			aver = self.give_Aver(srt = 'avokado/', name = name)
			aver_sum += aver
			num += 1
			if(minn > aver):
				minn = aver
			if(maxx < aver):
				maxx = aver

		print("aver_sum: ", aver_sum)
		print("num: ", num)
		print("average: ", aver_sum/num)
		print("min:", minn)
		print("max: ", maxx)
		self.avokado = aver_sum/num
		self.avokadomin = minn
		self.avokadomax = maxx

	def start(self, step):
		files = os.listdir('testing/apple/')
		ok = 0
		fail = 0
		num = 0

		for name in files:
			aver = self.give_Aver(srt = 'testing/apple/', name = name)
			num += 1
			if(self.apple - step < aver and self.apple + step > aver):
				ok += 1
			elif(self.avokado - step < aver and self.avokado + step > aver):
				fail += 1

		print("APPLE:")
		print("ok: ", ok)
		print("%: ", ok/num*100)
		print("fail: ", fail)
		print("%: ", fail/num*100)

		files = os.listdir('testing/avokado/')
		ok = 0
		fail = 0
		num = 0

		for name in files:
			aver = self.give_Aver(srt = 'testing/avokado/', name = name)
			num += 1
			if(self.avokado - step < aver and self.avokado + step > aver):
				ok += 1
			elif(self.apple - step < aver and self.apple + step > aver):
				fail += 1

		print("AVOKADO")
		print("ok: ", ok)
		print("%: ", ok/num*100)
		print("fail: ", fail)
		print("%: ", fail/num*100)