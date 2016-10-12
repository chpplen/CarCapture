import csv
import theano
import numpy
import theano.tensor as T

import random


import gzip
import os
import six.moves.cPickle as pickle

def loadData():
	print('... loading data')

	train_x = []
	train_y = []

	valid_x = []
	valid_y = []

	test_x = []
	test_y = []	

	thres = 0.3
	thres2 = 0.5
	with open('../data/BMW/data.csv', 'rb') as csvfile:
	#with open('test.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
		count = 0
		for row in spamreader:
			x = []
			for i in range(1,len(row)):
				x.append(float(row[i]))

			if random.random() > thres: 
				train_y.append(int(row[0]))
				#print len(x)
				train_x.append(x)
			elif random.random() > thres2:
				valid_y.append(int(row[0]))
				#print len(x)
				valid_x.append(x)
			else :
				test_y.append(int(row[0]))
				test_x.append(x)

	# print train_x[0]
	# print len(train_x[0])

	print 'train size: ' + str(len(train_y))
	print 'valid size: ' + str(len(valid_y))
	print 'test size: ' + str(len(test_y))

	train_x = numpy.array(train_x, dtype=numpy.float32)
	valid_x = numpy.array(valid_x, dtype=numpy.float32)
	test_x = numpy.array(test_x, dtype=numpy.float32)

	train_y = numpy.array(train_y, dtype=numpy.int64)
	valid_y = numpy.array(valid_y, dtype=numpy.int64)
	test_y = numpy.array(test_y, dtype=numpy.int64)

	# print (train_x,train_y)

	def shared_dataset(data_x, data_y, borrow=True):
		shared_x = theano.shared(numpy.asarray(data_x,
					dtype=theano.config.floatX),
					borrow=borrow)
		shared_y = theano.shared(numpy.asarray(data_y,
					dtype=theano.config.floatX),
					borrow=borrow)

		return shared_x, T.cast(shared_y, 'int32')

	test_set_x, test_set_y = shared_dataset(test_x,test_y)
	valid_set_x, valid_set_y = shared_dataset(valid_x,valid_y)
	train_set_x, train_set_y = shared_dataset(train_x,train_y)

	rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y),(test_set_x, test_set_y), (test_x, test_y)]

	return rval

def load_data(dataset):
    ''' Loads the dataset

    :type dataset: string
    :param dataset: the path to the dataset (here MNIST)
    '''

    #############
    # LOAD DATA #
    #############

    # Download the MNIST dataset if it is not present
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # Check if dataset is in the data directory.
        new_path = os.path.join(
            os.path.split(__file__)[0],
            "..",
            "data",
            dataset
        )
        if os.path.isfile(new_path) or data_file == 'mnist.pkl.gz':
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == 'mnist.pkl.gz':
        from six.moves import urllib
        origin = (
            'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'
        )
        print('Downloading data from %s' % origin)
        urllib.request.urlretrieve(origin, dataset)

    print('... loading data')

    # Load the dataset
    with gzip.open(dataset, 'rb') as f:
        try:
            train_set, valid_set, test_set = pickle.load(f, encoding='latin1')
        except:
            train_set, valid_set, test_set = pickle.load(f)
    # train_set, valid_set, test_set format: tuple(input, target)
    # input is a numpy.ndarray of 2 dimensions (a matrix)
    # where each row corresponds to an example. target is a
    # numpy.ndarray of 1 dimension (vector) that has the same length as
    # the number of rows in the input. It should give the target
    # to the example with the same index in the input.

    def shared_dataset(data_xy, borrow=True):
        """ Function that loads the dataset into shared variables

        The reason we store our dataset in shared variables is to allow
        Theano to copy it into the GPU memory (when code is run on GPU).
        Since copying data into the GPU is slow, copying a minibatch everytime
        is needed (the default behaviour if the data is not in a shared
        variable) would lead to a large decrease in performance.
        """
        data_x, data_y = data_xy
        shared_x = theano.shared(numpy.asarray(data_x,
                                               dtype=theano.config.floatX),
                                 borrow=borrow)
        shared_y = theano.shared(numpy.asarray(data_y,
                                               dtype=theano.config.floatX),
                                 borrow=borrow)
        # When storing data on the GPU it has to be stored as floats
        # therefore we will store the labels as ``floatX`` as well
        # (``shared_y`` does exactly that). But during our computations
        # we need them as ints (we use labels as index, and if they are
        # floats it doesn't make sense) therefore instead of returning
        # ``shared_y`` we will have to cast it to int. This little hack
        # lets ous get around this issue
        return shared_x, T.cast(shared_y, 'int32')

    X = test_set[0]
    with open('testX.csv','wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        for x in X:
            spamwriter.writerow(x)
    Y = test_set[1]
    with open('testY.csv','wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(Y)

    test_set_x, test_set_y = shared_dataset(test_set)
    valid_set_x, valid_set_y = shared_dataset(valid_set)
    train_set_x, train_set_y = shared_dataset(train_set)

    rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y),
            (test_set_x, test_set_y)]
    return rval

if __name__ == '__main__':
	# datasets = loadData()
	datasets = load_data('mnist.pkl.gz')
