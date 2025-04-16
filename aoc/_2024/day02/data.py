import os


def load_data(file_name: str) -> str:
    """
    Load data from a file in the same directory as this script.
    :param file_name:
    :return:
    """
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, file_name)
    with open(full_path) as f:
        return f.read()


data = load_data("data.txt")
sample_data = load_data("data_sample.txt")
