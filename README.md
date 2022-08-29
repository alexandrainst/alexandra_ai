<div align='center'>
<img src="https://raw.githubusercontent.com/alexandrainst/AIAI/main/gfx/aiai-logo.png" width="auto" height="224">
</div>

### A Python package for Danish data science.

______________________________________________________________________
[![Documentation](https://img.shields.io/badge/docs-passing-green)](https://alexandrainst.github.io/aiai/aiai.html)
[![License](https://img.shields.io/github/license/alexandrainst/aiai)](https://github.com/alexandrainst/aiai/blob/main/LICENSE)
[![LastCommit](https://img.shields.io/github/last-commit/alexandrainst/aiai)](https://github.com/alexandrainst/aiai/commits/main)
[![Code Coverage](https://img.shields.io/badge/Coverage-0%25-red.svg)](https://github.com/alexandrainst/aiai/tree/main/tests)


Developers:

- Dan Saattrup Nielsen (dan.nielsen@alexandra.dk)
- Anders Jess Pedersen (anders.j.pedersen@alexandra.dk)


## Installation
To install the package simply write the following command in your favorite terminal:
```
$ pip install aiai
```

## Quickstart
### Benchmarking from the Command Line
The easiest way to benchmark pretrained models is via the command line interface. After
having installed the package, you can benchmark your favorite model like so:
```
$ evaluate --model-id <model_id> --task <task>
```

Here `model_id` is the HuggingFace model ID, which can be found on the [HuggingFace
Hub](https://huggingface.co/models), and `task` is the task you want to benchmark the
model on, such as "ner" for named entity recognition. See all options by typing
```
$ evaluate --help
```

The specific model version to use can also be added after the suffix '@':
```
$ evaluate --model_id <model_id>@<commit>
```

It can be a branch name, a tag name, or a commit id. It defaults to 'main' for latest.

Multiple models and tasks can be specified by just attaching multiple arguments. Here
is an example with two models:
```
$ evaluate --model_id <model_id1> --model_id <model_id2> --task ner
```

See all the arguments and options available for the `evaluate` command by typing
```
$ evaluate --help
```

### Benchmarking from a Script
In a script, the syntax is similar to the command line interface. You simply initialise
an object of the `Evaluator` class, and call this evaluate object with your favorite
models and/or datasets:
```
>>> from aiai import Evaluator
>>> evaluator = Evaluator()
>>> evaluator('<model_id>', '<task>')
```


## Project structure
```
.
├── .flake8
├── .github
│   └── workflows
│       ├── ci.yaml
│       └── docs.yaml
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── config
│   ├── __init__.py
│   ├── config.yaml
│   ├── model
│   │   └── model1.yaml
│   └── process
│       └── process1.yaml
├── data
│   ├── final
│   ├── processed
│   └── raw
├── makefile
├── models
├── notebooks
├── poetry.toml
├── pyproject.toml
├── src
│   ├── scripts
│   │   ├── fix_dot_env_file.py
│   │   └── versioning.py
│   └── aiai
│       ├── __init__.py
│       └── demo.py
└── tests
    └── __init__.py
```
