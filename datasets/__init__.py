from .oxford_pets import OxfordPets
from .image import Image
from .gender import Gender
dataset_list = {
                "oxford_pets": OxfordPets,
                "image": Image,
                "gender": Gender,
                }


def build_dataset(dataset, root_path, shots):
    return dataset_list[dataset](root_path, shots)