from .oxford_pets import OxfordPets
from .image import Image

dataset_list = {
                "oxford_pets": OxfordPets,
                "image": Image,
                }


def build_dataset(dataset, root_path, shots):
    return dataset_list[dataset](root_path, shots)