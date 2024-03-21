# CrateDB tableau's connector.

For simple queries and graphs you can use the default PostgresSQL connector,
but for more advance usage SQL compatibility issues and nuanced SQL functionalities get into play,
we circumvent/fix those limitations with our custom connector.

## How to use.

You will need two things:

The `postgresql jdbc driver` and the `cratedb_jdbc`

### Get the Postgresql jdbc driver.
Download the driver from [here](https://jdbc.postgresql.org/download/) and put it in `$PATH TO DRIVER`
the latest tested one is `postgresql-42.7.3.jar`

### Get the connector.
Clone the repository `git clone https://github.com/crate/tableau-connector.git` or manually
download `cratedb_jdbc`.

Put it in: `/PATH`

## State of the driver.
This custom connector aims to offer the best Tableau experience possible, this is a work in progress since 
PostgresSQL compatibility is not 100% and is bound to change over time.

We test compatibility issues with Tableau's connector sdk (TDVT), it is tracked in `PATH TO pinned MAIN ISSUE`