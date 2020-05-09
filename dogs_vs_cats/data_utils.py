from .extract_data import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data(image_dim: tuple)->tuple:
    '''Loads train and test data.

        Parameters:
        image_dim (tuple): tuple containing image width and height.

        Returns:
        tuple: (X_train, y_train), (X_test, y_test)
    '''
    train_samples = 2 * CLASS_TRAIN_SAMPLES
    test_samples = 2 * CLASS_TEST_SAMPLES
    channels = 3

    train_datagen = ImageDataGenerator()
    train_gen = train_datagen.flow_from_directory(TRAIN_DATA_PATH,
                                                  target_size=image_dim,
                                                  batch_size=train_samples,
                                                  class_mode='binary')
    test_datagen = ImageDataGenerator()
    test_gen = train_datagen.flow_from_directory(TEST_DATA_PATH,
                                                  target_size=image_dim,
                                                  batch_size=test_samples,
                                                  class_mode='binary')
    X_train, y_train = train_gen.next()
    X_test, y_test = test_gen.next()
    
    return (X_train, y_train), (X_test, y_test)