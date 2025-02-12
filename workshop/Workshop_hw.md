## Install dlt

https://dlthub.com/docs/reference/installation


On macOS, you can use Homebrew to install Python 3.10.
```ssh
brew update
brew install python@3.10
```

Create a new virtual environment in your working folder. This will create an ./env directory where your virtual environment will be stored:
```ssh
python -m venv ./en
```

Activate the virtual environment:
```ssh
source ./env/bin/activate
```
Install dlt library
You can now install dlt in your virtual environment by running:

```ssh
# install the newest dlt version or upgrade the existing version to the newest one
pip install "dlt[duckdb]"
```

install all the necessary dependencies
```ssh
pip install duckdb pandas numpy pyarrow
```

## Question 1. Check dlt version
I ran below code to check dlt version. And the version is **__main__.py 1.6.1**.
```ssh
python3 -m dlt --version
```

