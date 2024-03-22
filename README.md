# CrateDB tableau's connector.

For simple queries and graphs, you can use the default PostgresSQL connector,
but for more advance usage SQL compatibility issues and nuanced SQL functionalities get into play,
we circumvent/fix those limitations with our custom connector.

## How to use.

You will need two things:

The `postgresql jdbc driver` and the `cratedb_jdbc`

### Get the Postgresql jdbc driver.

Download the driver from [here](https://jdbc.postgresql.org/download/) and put it in:

- Windows - C:\Program Files\Tableau\Drivers
- Mac - ~/Library/Tableau/Drivers
- Linux -  /opt/tableau/tableau_driver/jdbc 

The latest tested one is `postgresql-42.7.3.jar`

### Get the connector.

Clone the repository `git clone https://github.com/crate/tableau-connector.git` or manually
download `cratedb_jdbc`.

Put it in: 

#### Tableau Desktop

- Windows - C:\Users\[Windows User]\Documents\My Tableau Repository\Connectors 
- MacOS - /Users/[user]/Documents/My Tableau Repository/Connectors

#### Tableau Prep Builder

- Windows -  C:\Users\[Windows User]\Documents\My Tableau Prep Repository\Connectors
- MacOS - /Users//Documents/My Tableau Prep Repository/Connectors

#### Tableau Server
- Windows - C:\Program Files\Tableau\Connectors
- Linux - /opt/tableau/connectors

For older versions see https://help.tableau.com/current/pro/desktop/en-us/examples_connector_sdk.htm


## State of the driver.

This custom connector aims to offer the best Tableau experience possible, this is a work in progress since 
PostgresSQL compatibility is not 100% and is bound to change over time.

We test compatibility issues with Tableau's connector sdk (TDVT),
it is tracked in https://github.com/crate/tableau-connector/issues/2