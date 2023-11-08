# Source Code Folder

This is where all code files relating to analysis, data exploration etc go; they DO NOT go in the `quarto-paper` folder in order to keep that clean. This way, we can separate the coding work from the work that went into the actual writing of the paper.

## Files

- **`model_code/`**: Where the code from other repos for solving the NeurIPS challenge goes
- **`model_code/NeurIPS-Education-Challenge-2020`**: Best winner for Task 1, Task 3 (tie)
- **`model_code/TOP1-for-task-2-in-the-NeurIPS-2020-Education-Challenge`**: Best winner for Task 2
- **`model_code/NeurIPSEducation2020`**: Best winner for Task 4
- **`model_code/CRAFT-pytorch`**: Model for extracting the text from the Eedi Dataset question images, used for generating data for the winner from Task 3. To run, (although you don't need to run it if the `data/Eedi_dataset/images_text-segmentation/` folder exists):
  1. `cd` into `model_code/CRAFT-pytorch`
  2. run `pip install -r requirements.txt`
  3. run ``
