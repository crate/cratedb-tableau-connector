# How to set up tests.

# Setting up the environment:

## 1. Install tableau desktop.
Tableau test sdk need a valid Tableau desktop installation (either Windows or mac) https://www.tableau.com/support/releases, and
hence a valid tableau license. Without a license tests cannot be run.

Login in tableau selecting 'tableau cloud', 

## 2. Clone the repository
```sh
git clone git@github.com:crate/cratedb-tableau-connector.git
```

## 3. Install poetry.
It is expected that you have a valid python installation.

mac
```sh
pipx install poetry
```

windows
```sh
python3 -m pip install poetry
```

Check that poetry is properly installed by running

mac
```sh
poetry
```

windows
```shell
python3 -m poetry
```

## 4. Clone tdvt

```shell
https://github.com/tableau/connector-plugin-sdk.git
```


## 5. Install tdvt
```shell
python3 -m poetry add --editable .\connector-plugin-sdk\tdvt\
```

In windows, you might need to specify the full path, for example

```shell
python3 -m poetry add -e C:\Users\surister\PycharmProjects\cratedb-tableau-connector\connector-plugin-sdk\tdvt
```

Check that the installation was done correctly by running:

```
python3 -m poetry run python -m tdvt.tdv
```

# Setting up the database and connector:

Now that the environment is set up, we need to also set up the tableau test files and data.