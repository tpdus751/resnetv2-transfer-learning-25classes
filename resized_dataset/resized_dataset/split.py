import os
import shutil
import random

SRC_DIR = './train'  # 현재 100장씩 있는 폴더
DEST_TRAIN = './train_split'
DEST_VAL = './validation_split'

os.makedirs(DEST_TRAIN, exist_ok=True)
os.makedirs(DEST_VAL, exist_ok=True)

for class_name in os.listdir(SRC_DIR):
    class_path = os.path.join(SRC_DIR, class_name)
    if not os.path.isdir(class_path):
        continue

    images = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)

    train_imgs = images[:80]
    val_imgs = images[80:]

    # 클래스별 폴더 생성
    train_class_dir = os.path.join(DEST_TRAIN, class_name)
    val_class_dir = os.path.join(DEST_VAL, class_name)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)

    # 복사
    for img_name in train_imgs:
        shutil.copy(os.path.join(class_path, img_name), os.path.join(train_class_dir, img_name))

    for img_name in val_imgs:
        shutil.copy(os.path.join(class_path, img_name), os.path.join(val_class_dir, img_name))

print("✅ 8:2 비율로 train/validation 재분할 완료")
