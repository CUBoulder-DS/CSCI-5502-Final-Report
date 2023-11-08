# Source Code Folder

This is where all code files relating to analysis, data exploration etc go; they DO NOT go in the `quarto-paper` folder in order to keep that clean. This way, we can separate the coding work from the work that went into the actual writing of the paper.

## Files

- **`model_code/`**: Where the code from other repos for solving the NeurIPS challenge goes
- **`model_code/NeurIPS-Education-Challenge-2020`**: Best winner for Task 1, Task 3 (tie)
  - [Repo link](https://github.com/haradai1262/NeurIPS-Education-Challenge-2020)
- **`model_code/TOP1-for-task-2-in-the-NeurIPS-2020-Education-Challenge`**: Best winner for Task 2
  - [Repo link](https://github.com/shshen-closer/TOP1-for-task-2-in-the-NeurIPS-2020-Education-Challenge)
- **`model_code/NeurIPSEducation2020`**: Best winner for Task 4
  - [Repo link](https://github.com/arghosh/NeurIPSEducation2020)
- **`model_code/CRAFT-pytorch`**: Model for extracting the text from the Eedi Dataset question images, used for generating data for the winner from Task 3. To run, (although you don't need to run it if the `data/Eedi_dataset/images_text-segmentation/` folder exists):
  1. `cd` into `model_code/CRAFT-pytorch`
  2. run `pip install -r requirements.txt`
  3. Make sure Bhav's changes to the `CRAFT-pytorch` repo are there (to get code working with newer torch/torchvision packages)
  4. Download the model [from this link](https://drive.google.com/open?id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ) and put into base dir at `CRAFT-pytorch`
  5. run `python test.py --trained_model=craft_mlt_25k.pth --test_folder="../../../data/Eedi_dataset/images/"`
  6. Copy `result` folder to `data/Eedi_dataset/images_text-segmentation/` folder (make new if needed)
  - [Repo link](https://github.com/clovaai/CRAFT-pytorch)
