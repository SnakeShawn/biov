# Biological visualization

### Requirement
> **Python2.7**：numpy,matplotlib

> **R**:ggplot2
	

### Structure
Recommend you to organize your project like this tree.

```
.
├── README.md
├── __init__.py
├── biov.py
├── charts
│   ├── __init__.py
│   ├── python
│   │   ├── __init__.py
│   │   └── matplotlib
│   │       ├── __init__.py
│   │       ├── bar.py
│   │       ├── barh.py
│   └── r
│       ├── __init__.py
│       └── ggplot2
│           ├── __init__.py
│           ├── geom_dotplot.py
├── config
│   ├── __init__.py
│   ├── charts.csv
│   ├── config.py
├── data
│   ├── bar.csv
│   ├── mtcars.R
│   ├── mtcars.csv
│   └── output.eps
├── input.json
├── output
│   ├── picture.eps
│   └── picture.png
├── run.sh
└── sample_json
    ├── bar.json
    ├── barh.json
    └── rggplot2geomdot.json

```


