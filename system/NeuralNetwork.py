import os
import glob
import numpy as np
import cv2
from sklearn.utils import shuffle

NeuralNetwork:
    def load_train(train_path, image_size, classes):
        images = []
        labels = []
        ids = []
        cls = []
        print('Loading {} files (Index: {})'.format(fld, index))
        path = os.path.join(train_path, fld, '*.' + dataType + '.png')
        files = glob.glob(path)
        for fl in files:
            image = cv2.imread(fl)
            image = cv2.resize(image, (image_size, image_size), cv2.INTER_LINEAR)
            images.append(image)
            label = np.zeros(len(classes))
            label[index] = 1.0
            labels.append(label)
            flbase = os.path.basename(fl).splt('.')
            ids.append(flbase[0])
        images = np.array(images)
        labels = np.array(labels)
        ids = np.array(ids)

        return images, labels, ids


    def load_test(test_path, image_size):
        path = os.path.join(test_path, '*g')
        files = sorted(glob.glob(path))

        X_test = []
        X_test_id = []
        print("Reading test images")
        for fl in files:
            flbase = os.path.basename(fl)
            img = cv2.imread(fl)
            img = cv2.resize(img, (image_size, image_size), cv2.INTER_LINEAR)
            X_test.append(img)
            X_test_id.append(flbase)

        ### because we're not creating a DataSet object for the test images, normalization happens here
        X_test = np.array(X_test, dtype=np.uint8)
        X_test = X_test.astype('float32')
        X_test = X_test / 255

        return X_test, X_test_id

    def read_train_sets(train_path, image_size, classes, validation_size=0):
        class DataSets(object):
            pass

        data_sets = DataSets()

        images, labels, ids = load_train(train_path, image_size, classes)
        images, labels, ids = shuffle(images, labels, ids)  # shuffle the data

        if isinstance(validation_size, float):
            validation_size = int(validation_size * images.shape[0])

        validation_images = images[:validation_size]
        validation_labels = labels[:validation_size]
        validation_ids = ids[:validation_size]

        train_images = images[validation_size:]
        train_labels = labels[validation_size:]
        train_ids = ids[validation_size:]

        data_sets.train = DataSet(train_images, train_labels, train_ids)
        data_sets.valid = DataSet(validation_images, validation_labels, validation_ids)

        return data_sets


    def read_test_set(test_path, image_size):
        images, ids = load_test(test_path, image_size)
        return images, ids