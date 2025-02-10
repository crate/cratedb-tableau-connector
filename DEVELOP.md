# How to set up tests.

# Setting up the environment:

## 1. Install tableau desktop.
Tableau test sdk needs a valid Tableau desktop installation (either Windows or MacOs) https://www.tableau.com/support/releases, and
hence a valid Tableau license. Without a license tests cannot be run.

Once Tableau Desktop is installed, log in selecting 'tableau cloud'.

## 2. Install dependencies.

MacOS
```shell
python3 -m pip install -r requirements.txt
```

Windows
```shell
py -m pip install -r requirements
```

Alternatively, with `uv`

```shell
uv venv
```
```shell
uv pip install -r requirements.txt
```

You should be able to now use `tdvt`, we'll use that quite a lot.

```
python -m tdvt.tdvt
```

## 3. Clone ``cratedb-tableau-connector``
```shell
git clone git@github.com:crate/cratedb-tableau-connector.git
```

# Setting up the testing workspace:

Now that the environment is set up, we need to also set up the Tableau test files and data.

Tdvt workflow is documented here: https://tableau.github.io/connector-plugin-sdk/docs/tdvt, it is pretty lengthy, you
can follow the official `tdvt` docs or continue reading and do step by step.

Note: There is also a [50 minute video by the tableau team](https://www.youtube.com/watch?v=rAgnnByJIJA).
## Set up CrateDB.

The quickest way to set up CrateDB is by [using Docker](https://cratedb.com/docs/guide/install/container/).
```shell
docker run --publish=4200:4200 --publish=5432:5432 --env CRATE_HEAP_SIZE=1g --pull=always crate
```

## Set up ``tdvt`` execution profile.

1. Go to `./tests/config/tdvt/tdvt_override.ini` and put the path of your installation's `tabquerytool.exe`, for example
on a Windows machine it is: `C:\Program Files\Tableau\Tableau 2024.3\bin\tabquerytool.exe`
2. [Download datasets](https://github.com/tableau/connector-plugin-sdk/tree/master/tests/datasets/TestV1) and load both 
`calcs` and `staples` tables into the CrateDB instance. The script in `./data/setup_data.py` can be used to
automatically create the tables and load the data.

MacOs
```shell
python ./data/setup_data.py
```

Windows
```shell
py ./data/setup_data.py
```