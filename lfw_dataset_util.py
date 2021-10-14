import os
import shutil

import cv2
import numpy as np
import random
from tqdm import tqdm

from masked_face_creater import MaskedFaceCreator

class LFWMaskedFaceDatasetCreator:
    def __init__(self, dataset_path, new_dataset_folder_path, mask_type="c"):
        self.dataset_path = dataset_path
        self.new_dataset_folder_path = new_dataset_folder_path
        self.mask_type = mask_type
        self.mask_color = random.choice([(252, 166, 146),(255, 255, 255),(42,40,40)])
        self.masked_face_creator = MaskedFaceCreator('shape_predictor_68_face_landmarks.dat')

    def generate(self):
        if not os.path.isdir(self.new_dataset_folder_path):
            os.mkdir(self.new_dataset_folder_path)

        for person in tqdm(os.listdir(self.dataset_path)):
            person_folder_path = f"{self.dataset_path}/{person}"
            files = os.listdir(person_folder_path)
            if len(files) > 1:
                for image_file in files:
                    if image_file.startswith("masked_"):
                        image_path = f"{self.dataset_path}/{person}/{image_file}"
                        os.remove(image_path)
                        continue
                    image_path = f"{self.dataset_path}/{person}/{image_file}"
                    image = cv2.imread(image_path)
                    if image is None:
                        os.remove(image_path)
                        continue

                    image_with_mask = self.masked_face_creator.simulateMask(np.array(image, dtype=np.uint8),
                                                                            mask_type=self.mask_type,
                                                                            color=self.mask_color,
                                                                            draw_landmarks=False)
                    if image_with_mask is None:
                        continue

                    new_image_folder = f"{self.new_dataset_folder_path}/{person}"
                    if not os.path.isdir(new_image_folder):
                        os.mkdir(new_image_folder)
                    new_image_path = f"{self.new_dataset_folder_path}/{person}/masked_{image_file}"
                    unmask_image_path = f"{self.new_dataset_folder_path}/{person}/{image_file}"

                    shutil.copy(image_path, unmask_image_path)
                    cv2.imwrite(new_image_path, image_with_mask)