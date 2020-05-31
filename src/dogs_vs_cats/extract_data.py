import os, zipfile

DATA_PATH = "./dataset"
TRAIN_DATA_PATH = os.path.join(DATA_PATH, "train")
DOG_TRAIN_DATA_PATH = os.path.join(TRAIN_DATA_PATH, "dog")
CAT_TRAIN_DATA_PATH = os.path.join(TRAIN_DATA_PATH, "cat")

VAL_DATA_PATH = os.path.join(DATA_PATH, "validation")
DOG_VAL_DATA_PATH = os.path.join(VAL_DATA_PATH, "dog")
CAT_VAL_DATA_PATH = os.path.join(VAL_DATA_PATH, "cat")

TEST_DATA_PATH = os.path.join(DATA_PATH, "test")
DOG_TEST_DATA_PATH = os.path.join(TEST_DATA_PATH, "dog")
CAT_TEST_DATA_PATH = os.path.join(TEST_DATA_PATH, "cat")

CLASS_TRAIN_SAMPLES = 9000
CLASS_VAL_SAMPLES = 1000
CLASS_TEST_SAMPLES = 2500

def make_dir(path: str)->None:
    '''Creates new folder if it does not exist.

        Parameters:
        path (str): new folder path.
    '''
    if not os.path.exists(path):
        os.makedirs(path)

def compose_folder_structure()->None:
    '''Creates folder structure to divide dataset.'''

    make_dir(DOG_TRAIN_DATA_PATH)
    make_dir(CAT_TRAIN_DATA_PATH)
    make_dir(DOG_VAL_DATA_PATH)
    make_dir(CAT_VAL_DATA_PATH)
    make_dir(DOG_TEST_DATA_PATH)
    make_dir(CAT_TEST_DATA_PATH)
    
def extract_images()->None:
    '''Extracts images from a zip file.'''

    DATA_ZIP_PATH = "./dogs-vs-cats.zip"

    with zipfile.ZipFile(DATA_ZIP_PATH) as zfile:
        TRAIN_ZIP_NAME = "train.zip"
        
        zfile.extract(TRAIN_ZIP_NAME)
        with zipfile.ZipFile(TRAIN_ZIP_NAME) as data_zfile:  
            data_zfile.extractall(DATA_PATH)
                
        os.remove(TRAIN_ZIP_NAME)

def move_data(cat_dst: str, dog_dst: str, start_index: int, end_index: int)->None:
    '''Moves images to a proper destination folder.
        Parameters:
        cat_dst (str): cat images destination folder.
        dog_dst (str): dog images destination folder.
        start_index (int): starting image index which will be moved.
        end_index (int): ending image index which will be moved.
    '''
    for img_index in range(start_index, end_index):
        cat_img = f"cat.{img_index}.jpg"
        src_cat = os.path.join(TRAIN_DATA_PATH, cat_img)
        dst_cat = os.path.join(cat_dst, cat_img)

        dog_img = f"dog.{img_index}.jpg"
        src_dog = os.path.join(TRAIN_DATA_PATH, dog_img)
        dst_dog = os.path.join(dog_dst, dog_img)

        # moves images
        os.rename(src_cat, dst_cat)
        os.rename(src_dog, dst_dog)

def main():
    compose_folder_structure()
    extract_images()

    move_data(CAT_TRAIN_DATA_PATH,
              DOG_TRAIN_DATA_PATH,
              start_index=0,
              end_index=CLASS_TRAIN_SAMPLES)

    val_start_idx = CLASS_TRAIN_SAMPLES
    val_end_idx = CLASS_TRAIN_SAMPLES + CLASS_VAL_SAMPLES

    move_data(CAT_VAL_DATA_PATH,
              DOG_VAL_DATA_PATH,
              start_index=val_start_idx,
              end_index=val_end_idx)

    test_start_idx = val_end_idx
    test_end_idx = val_end_idx + CLASS_TEST_SAMPLES                 
    
    move_data(CAT_TEST_DATA_PATH,
              DOG_TEST_DATA_PATH,
              start_index=test_start_idx,
              end_index=test_end_idx)   

if __name__ == '__main__':
    main()