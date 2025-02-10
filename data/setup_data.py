import pathlib
import logging

import polars
import requests

CRATE_DB = 'HOST:PORT'  # Examples: localhost:4200, 192.168.88.21:4200
CRATEDB_HTTP = f'http://{CRATE_DB}/_sql'
CRATEDB_SQLALCHEMY = f'crate://{CRATE_DB}'
DATA_URL = pathlib.Path(__file__).parent.parent / 'data'

FILES_URL = [
    {'name': 'Calcs',
     'url': 'https://raw.githubusercontent.com/tableau/connector-plugin-sdk/'
            'refs/heads/master/tests/datasets/TestV1/Calcs_headers.csv'},
    {'name': 'Staples',
     'url': 'https://raw.githubusercontent.com/tableau/connector-plugin-sdk/'
            'refs/heads/master/tests/datasets/TestV1/Staples_utf8_headers.csv'}
]

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Create tables.
    for file in DATA_URL.iterdir():
        if file.suffix == '.sql':
            statement = file.read_text()
            response = requests.post(CRATEDB_HTTP,
                                     json={'stmt': statement})
            logging.info(f'Tried creating {file.name}, response from CrateDB: {response.text}')

    # Download data and load it to CrateDB.
    for file in FILES_URL:
        result = requests.get(file.get('url'))
        logging.info(f'Downloading {file.get('url')}')

        df = polars.read_csv(result.content, use_pyarrow=True)

        # There is a bug where an empty space is added to 'Market Segment' column name.
        # Easiest solution is just to try to rename it if it exists.
        try:
            df.get_column('Market Segment ')
            df = df.rename({'Market Segment ': 'Market Segment'})
        except polars.exceptions.ColumnNotFoundError:
            pass

        logging.info(f'Loading to CrateDB {file.get('name')!r}')
        df.write_database(file.get('name'),
                          connection=CRATEDB_SQLALCHEMY,
                          if_table_exists='append')
