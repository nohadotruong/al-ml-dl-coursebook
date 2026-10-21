```
ai-ml-dl-be/
│
├── data/
│   ├── housing/
│   │   ├── raw/
│   │   └── processed/
│   │
│   └── titanic/
│       ├── raw/
│       └── processed/
│
├── models/
│   ├── housing/
│   │   └── model.pkl
│   │
│   └── titanic/
│       └── model.pkl
│
├── src/
│   ├── __init__.py
│   │
│   ├── common/
│   │   ├── cleaner.py      # fill/drop missing values, remove duplicate values, clip outliers
│   │   ├── encoder.py      # encode categorical col, merge rare value
│   │   ├── loader.py       # load data
│   │   ├── overview.py     # overview, visualization data
│   │   ├── saver.py        # save data
│   │   ├── scaler.py       # scaler values
│   │   └── spliter.py      # split dataset
│   │
│   ├── housing/
│   │   ├── preprocessing.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── config.py
│   │   └── run_pipeline.py
│   │
│   └── titanic/
│       ├── preprocessing.py
│       ├── train.py
│       ├── predict.py
│       ├── config.py
│       └── run_pipeline.py
│
├── notebooks/
├── configs/
├── requirements.txt
└── README.md

```
