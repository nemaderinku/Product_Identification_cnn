from shutil import copyfile
import csv
import numpy
#copyfile(src, dst)
items = []
img = []
with open('train.csv','rb') as csvfile:
	r = csv.reader(csvfile, delimiter = ',')
	for row in r:
		s = list(row)
		i = ""
		i = s[0]+'.png'
		img.append(i)
		items.append(s[1])

u = numpy.unique(items)
u = numpy.ndarray.tolist(u)
csvfile.close()
for i in range (1 , (len(img) - 1)):
	index = u.index(items[i])
	src = "/home/rinku/dataset/train_img/" + str(img[i])
	dest = "/home/rinku/dataset/img/"+ str(index)+"/"+str(img[i])
	print "copying "+ src +"to" + dest
	copyfile(src, dest)
