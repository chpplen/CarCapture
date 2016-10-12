from PIL import Image
import csv
import theano
import numpy
import theano.tensor as T

import random
import os

for response in os.walk("/python/demo/"):
    print response


def convert(): 
	seriesList = ['bmw1series','bmw2series','bmw3series','bmw4series','bmw5series','bmw6series','bmw7series']

	with open("BMW/data.csv", "wb") as csvfile: 
		# for number in range(400):
		for series in range(len(seriesList)):
			spamwriter = csv.writer(csvfile)
			for number in range(400):
				im = Image.open( "BMW/" + seriesList[series] + "/" + str(number)+".jpg" ).convert('L')

				width = 28
				height = 28

				nim = im.resize( (width, height), Image.BILINEAR )
				# nim.save( "resize2wide.jpg" )
				# print nim.size

				temp = [series]
				for i in range(nim.size[0]):
					for j in range(nim.size[1]):
						temp.append(nim.getpixel((i,j))/256.0)

				spamwriter.writerow(temp)

def load():
	print('... loading data')

	train_x = []
	train_y = []

	test_x = []
	test_y = []	

	# seriesList1 = ['bmw1series','bmw2series','bmw3series','bmw4series','bmw5series','bmw6series','bmw7series']
	# seriesList2 = ['bmwx1','bmwx3','bmwx4','bmwx5','bmwx6']
	# seriesList3 = ['bmwm2','bmwm3','bmwm4','bmwm5','bmwm6']
	seriesList1 = ['bmw']
	seriesList2 = ['benz']
	seriesList3 = ['lexus']
	seriesList4 = ['audi']

	thres = 0.3
	for series in range(len(seriesList1)):
		for response in os.walk("car/" + seriesList1[series] + "/"):
			# im = Image.open( "BMW/" + seriesList1[series] + "/" + str(response) ).convert('L')
			for name in response[2]:
				im = Image.open( "car/" + seriesList1[series] + "/" + str(name) )
				width = 32
				height = 32

				nim = im.resize( (width, height), Image.BILINEAR )

				R = []
				G = []
				B = []
				try:
					for i in range(nim.size[0]):
						r = []
						g = []
						b = []
						for j in range(nim.size[1]):
							r.append(nim.getpixel((i,j))[0])
							g.append(nim.getpixel((i,j))[1])
							b.append(nim.getpixel((i,j))[2])
						R.append(r)
						G.append(g)
						B.append(b)

					X = [R,G,B]
					if random.random() > thres: 
						train_x.append(X)
						train_y.append(0)
					else:
						test_x.append(X)
						test_y.append(0)
				except Exception:
					print "falied:" + name

				

	for series in range(len(seriesList2)):
		for response in os.walk("car/" + seriesList2[series] + "/"):
			# im = Image.open( "BMW/" + seriesList1[series] + "/" + str(response) ).convert('L')
			for name in response[2]:
				im = Image.open( "car/" + seriesList2[series] + "/" + str(name) )
				width = 32
				height = 32

				nim = im.resize( (width, height), Image.BILINEAR )

				R = []
				G = []
				B = []
				try:
					for i in range(nim.size[0]):
						r = []
						g = []
						b = []
						for j in range(nim.size[1]):
							r.append(nim.getpixel((i,j))[0])
							g.append(nim.getpixel((i,j))[1])
							b.append(nim.getpixel((i,j))[2])
						R.append(r)
						G.append(g)
						B.append(b)

					X = [R,G,B]
					if random.random() > thres: 
						train_x.append(X)
						train_y.append(1)
					else:
						test_x.append(X)
						test_y.append(1)
				except Exception:
					print "falied:" + name

	for series in range(len(seriesList3)):
		for response in os.walk("car/" + seriesList3[series] + "/"):
			# im = Image.open( "BMW/" + seriesList1[series] + "/" + str(response) ).convert('L')
			for name in response[2]:
				im = Image.open( "car/" + seriesList3[series] + "/" + str(name) )
				width = 32
				height = 32

				nim = im.resize( (width, height), Image.BILINEAR )

				R = []
				G = []
				B = []
				try:
					for i in range(nim.size[0]):
						r = []
						g = []
						b = []
						for j in range(nim.size[1]):
							r.append(nim.getpixel((i,j))[0])
							g.append(nim.getpixel((i,j))[1])
							b.append(nim.getpixel((i,j))[2])
						R.append(r)
						G.append(g)
						B.append(b)

					X = [R,G,B]
					if random.random() > thres: 
						train_x.append(X)
						train_y.append(2)
					else:
						test_x.append(X)
						test_y.append(2)
				except Exception:
					print "falied:" + name

	for series in range(len(seriesList4)):
		for response in os.walk("car/" + seriesList4[series] + "/"):
			# im = Image.open( "BMW/" + seriesList1[series] + "/" + str(response) ).convert('L')
			for name in response[2]:
				im = Image.open( "car/" + seriesList4[series] + "/" + str(name) )
				width = 32
				height = 32

				nim = im.resize( (width, height), Image.BILINEAR )

				R = []
				G = []
				B = []
				try:
					for i in range(nim.size[0]):
						r = []
						g = []
						b = []
						for j in range(nim.size[1]):
							r.append(nim.getpixel((i,j))[0])
							g.append(nim.getpixel((i,j))[1])
							b.append(nim.getpixel((i,j))[2])
						R.append(r)
						G.append(g)
						B.append(b)

					X = [R,G,B]
					if random.random() > thres: 
						train_x.append(X)
						train_y.append(3)
					else:
						test_x.append(X)
						test_y.append(3)
				except Exception:
					print "falied:" + name

	# for series in range(len(seriesList2)):
	# 	for response in os.walk("BMW/" + seriesList2[series] + "/"):
	# 		for name in response[2]:
	# 			im = Image.open( "BMW/" + seriesList2[series] + "/" + str(name) ).convert('L')
	# 			width = 28
	# 			height = 28

	# 			nim = im.resize( (width, height), Image.BILINEAR )

	# 			X = []
	# 			for i in range(nim.size[0]):
	# 				x = []
	# 				for j in range(nim.size[1]):
	# 					x.append(float(nim.getpixel((i,j))))
	# 				X.append(x)

	# 			if random.random() > thres: 
	# 				train_x.append(X)
	# 				train_y.append(1)
	# 			else:
	# 				test_x.append(X)
	# 				test_y.append(1)

	# for series in range(len(seriesList2)):
	# 	for response in os.walk("BMW/" + seriesList2[series] + "/"):
	# 		# im = Image.open( "BMW/" + seriesList1[series] + "/" + str(response) ).convert('L')
	# 		for name in response[2]:
	# 			im = Image.open( "BMW/" + seriesList2[series] + "/" + str(name) ).convert('L')
	# 			width = 28
	# 			height = 28

	# 			nim = im.resize( (width, height), Image.BILINEAR )

	# 			X = []
	# 			for i in range(nim.size[0]):
	# 				x = []
	# 				for j in range(nim.size[1]):
	# 					x.append(float(nim.getpixel((i,j))))
	# 				X.append(x)

	# 			if random.random() > thres: 
	# 				train_x.append(X)
	# 				train_y.append(2)
	# 			else:
	# 				test_x.append(X)
	# 				test_y.append(2)


	train_x = numpy.array(train_x)
	train_y = numpy.array(train_y)

	test_x = numpy.array(test_x)
	test_y = numpy.array(test_y)
	print train_x.shape
	print train_y.shape

	print test_x.shape
	print test_y.shape

	return [(train_x, train_y), (test_x, test_y)]

	# with open('../data/BMW/data.csv', 'rb') as csvfile:
	# #with open('test.csv', 'rb') as csvfile:
	# 	spamreader = csv.reader(csvfile)
	# 	count = 0
	# 	for row in spamreader:
	# 		x = []
	# 		for i in range(1,len(row)):
	# 			x.append(float(row[i]))

	# 		if random.random() > thres: 
	# 			train_y.append(row[0])
	# 			#print len(x)
	# 			train_x.append(x)
	# 		else :
	# 			test_y.append(row[0])
	# 			test_x.append(x)



# def load_data():
# 	print('... loading data')

# 	train_x = []
# 	train_y = []

# 	valid_x = []
# 	valid_y = []

# 	test_x = []
# 	test_y = []	

# 	thres = 0.3
# 	thres2 = 0.5
# 	with open('../data/BMW/data.csv', 'rb') as csvfile:
# 	#with open('test.csv', 'rb') as csvfile:
# 		spamreader = csv.reader(csvfile)
# 		count = 0
# 		for row in spamreader:
# 			x = []
# 			for i in range(1,len(row)):
# 				x.append(float(row[i]))

# 			if random.random() > thres: 
# 				train_y.append(row[0])
# 				#print len(x)
# 				train_x.append(x)
# 			elif random.random() > thres2:
# 				valid_y.append(row[0])
# 				#print len(x)
# 				valid_x.append(x)
# 			else :
# 				test_y.append(row[0])
# 				test_x.append(x)

# 	# print train_x[0]
# 	# print len(train_x[0])

# 	# print len(train_y)
# 	# print len(valid_y)
# 	# print len(test_y)

# 	def shared_dataset(data_x, data_y, borrow=True):
# 		shared_x = theano.shared(numpy.asarray(data_x,
# 					dtype=theano.config.floatX),
# 					borrow=borrow)
# 		shared_y = theano.shared(numpy.asarray(data_y,
# 					dtype=theano.config.floatX),
# 					borrow=borrow)

# 		return shared_x, T.cast(shared_y, 'int32')

# 	test_set_x, test_set_y = shared_dataset(test_x,test_y)
# 	valid_set_x, valid_set_y = shared_dataset(valid_x,valid_y)
# 	train_set_x, train_set_y = shared_dataset(train_x,train_y)

# 	rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y),(test_set_x, test_set_y), (test_x, test_y)]

# 	return rval

if __name__ == '__main__':
	# convert()
	load()
	# datasets = load_data()
