<div align='center'>
 <img src="https://raw.githubusercontent.com/alexandrainst/AlexandraAI/docs/add-logo/gfx/alexandra-ai-logo-dark.svg">
</div>

### A Toolkit for Machine Learning Practitioners

______________________________________________________________________
[![PyPI Status](https://badge.fury.io/py/alexandra_ai.svg)](https://pypi.org/project/alexandra_ai/)
[![Documentation](https://img.shields.io/badge/docs-passing-green)](https://alexandrainst.github.io/AlexandraAI/alexandra_ai.html)
[![License](https://img.shields.io/github/license/alexandrainst/AlexandraAI)](https://github.com/alexandrainst/AlexandraAI/blob/main/LICENSE)
[![LastCommit](https://img.shields.io/github/last-commit/alexandrainst/AlexandraAI)](https://github.com/alexandrainst/AlexandraAI/commits/main)
[![Code Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](https://github.com/alexandrainst/AlexandraAI/tree/main/tests)

## Installation

To install the package simply write the following command in your favorite terminal:

```
pip install alexandra-ai
```

If you're on MacOS and get an error saying something along the lines of "fatal error:
'lzma.h' file not found" then try the following:

```
export CPPFLAGS="-I$(brew --prefix)/include"
pip install alexandra-ai-eval
```

## Quickstart

### Benchmarking from the Command Line

The easiest way to benchmark pretrained models is via the command line interface. After
having installed the package, you can benchmark your favorite model like so:

```
evaluate --model-id <model_id> --task <task>
```

Here `model_id` is the HuggingFace model ID, which can be found on the [HuggingFace
Hub](https://huggingface.co/models), and `task` is the task you want to benchmark the
model on, such as "ner" for named entity recognition. See all options by typing

```
evaluate --help
```

The specific model version to use can also be added after the suffix '@':

```
evaluate --model_id <model_id>@<commit>
```

It can be a branch name, a tag name, or a commit id. It defaults to 'main' for latest.

Multiple models and tasks can be specified by just attaching multiple arguments. Here
is an example with two models:

```
evaluate --model_id <model_id1> --model_id <model_id2> --task ner
```

See all the arguments and options available for the `evaluate` command by typing

```
evaluate --help
```

### Benchmarking from a Script

In a script, the syntax is similar to the command line interface. You simply initialise
an object of the `Evaluator` class, and call this evaluate object with your favorite
models and/or datasets:

```
>>> from alexandra_ai import Evaluator
>>> evaluator = Evaluator()
>>> evaluator('<model_id>', '<task>')
```

## Contributors

If you feel like this package is missing a crucial feature, if you encounter a bug or
if you just want to correct a typo in this readme file, then we urge you to join the
community! Have a look at the [CONTRIBUTING.md](./CONTRIBUTING.md) file, where you can
check out all the ways you can contribute to this package. :sparkles:

- _Your name here?_ :tada:

## Maintainers

The following are the core maintainers of the `alexandra_ai` package:

- [@saattrupdan](https://github.com/saattrupdan) (Dan Saattrup Nielsen; dan.nielsen@alexandra.dk)
- [@AJDERS](https://github.com/AJDERS) (Anders Jess Pedersen; anders.j.pedersen@alexandra.dk)

## The AlexandraAI ecosystem

This package is a wrapper around other AlexandraAI packages, each of which is standalone:

- [AlexandraAI-eval](https://github.com/alexandrainst/AlexandraAI-eval): Evaluation of finetuned models.

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
├── gfx
├── makefile
├── notebooks
├── poetry.toml
├── pyproject.toml
├── src
│   ├── alexandra_ai
│   │   └── __init__.py
│   └── scripts
│       ├── fix_dot_env_file.py
│       └── versioning.py
└── tests
    └── __init__.py
```
