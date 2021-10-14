import argparse
import os
import numpy as np

from lfw_dataset_util import LFWMaskedFaceDatasetCreator

def get_dataset_creator(base_folder, new_database_folder, dataset_name):
    dataset_creator = None
    if dataset_name == "lfw":
        dataset_path = f"{base_folder}/{dataset_name}"
        mask_unmask_dataset_path = f"{new_database_folder}/{dataset_name}"
        dataset_creator = LFWMaskedFaceDatasetCreator(dataset_path, mask_unmask_dataset_path)

    return dataset_creator

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(prog="Generate masked face dataset",
                                         description='Generate masked face dataset.', )
    arg_parser.add_argument("--base_folder", type=str, default="../dataset")
    arg_parser.add_argument("--new_dataset_folder", type=str, default="../new_dataset")

    args = arg_parser.parse_args()
    if not os.path.isdir(args.new_dataset_folder):
        os.mkdir(args.new_dataset_folder)

    mask_dataset_creator = get_dataset_creator(args.base_folder, args.new_dataset_folder, "lfw")
    mask_dataset_creator.generate()