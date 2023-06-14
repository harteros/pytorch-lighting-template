## Getting Started

This project provides a starting point for structuring your machine learning project in a scalable and extensible way.

You can find more information about the project structure in my blog
post: [Scalable Project Structure for Machine Learning Projects with PyTorch and PyTorch Lightning](https://medium.com/@l.charteros/scalable-project-structure-for-machine-learning-projects-with-pytorch-and-pytorch-lightning-d5f1408d203e).

## Project Structure

The directory structure of the project looks as follows:

```
.
├── .data
│   ├── processed
│   │   ├── test.csv
│   │   └── train.csv
│   └── raw
│       └── data.csv
|
├── .experiments
│   └── model1
│       ├── version_0
|       |   └── ...
|       └── ...
└── src
    |
    └── ml
        ├── data
        │   ├── make_dataset.py
        │   └── preprocessing.py
        |
        ├── datasets
        │   ├── dataset1
        │   |   ├── datamodule.py
        │   |   └── dataset.py
        |   └── ...
        |
        ├── engines
        │   └── system.py
        |
        ├── models
        │   ├── model1.py
        │   └── model2.py
        |
        ├── scripts
        │   ├── predict.py
        │   ├── test.py
        │   └── train.py
        |
        └── utils
            ├── constants.py
            └── helpers.py
```

*Note 1*: The `.data` directory is not tracked by Git. For your data you should
download your dataset and place it in the `.data/raw` directory or use the `make_dataset.py` script to write your
logic for downloading the dataset. The processed data should be saved in the `.data/processed` directory.

*Note 2*: The `.experiments` is not tracked by Git but will be created automatically when you run your training scripts
if you logger is configured correctly to use the `.experiments` directory. (See `src/ml/utils/constants.py`)
