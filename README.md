# CrateDB connector for Tableau

[![CI status](https://github.com/crate/cratedb-tableau-connector/actions/workflows/main.yml/badge.svg?style=flat)](https://github.com/crate/cratedb-tableau-connector/actions/workflows/main.yml)
![TDVT compatibility](https://img.shields.io/badge/TDVT%20compatibility-96%25-brightgreen?style=flat)
![CrateDB version](https://img.shields.io/badge/CrateDB->=5.10.1-brightgreen?style=flat&logo=cratedb)
![pgJDBC version](https://img.shields.io/badge/PostgreSQL%20JDBC%20driver-<=42.7.4-brightgreen?style=flat&logo=postgresql)
![GitHub release](https://img.shields.io/github/v/release/crate/cratedb-tableau-connector?style=flat)

## About

[Tableau] is a visual business intelligence and analytics software platform.
It expresses data by translating drag-and-drop actions into data queries
through an intuitive interface.

[CrateDB] is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
PostgreSQL-compatible, and based on Lucene.

The [CrateDB connector for Tableau] provides optimal connectivity and usability
with Tableau's line of products. It is based on the [PostgreSQL JDBC driver].

## Install

You will need to acquire and install two software artefacts, the PostgreSQL
JDBC driver ([JAR file]), and the CrateDB connector ([TACO file]).

### PostgreSQL JDBC driver

Download the driver JAR file from the [pgJDBC page] into:

- Windows: `C:\Program Files\Tableau\Drivers`
- Mac: `~/Library/Tableau/Drivers`
- Linux: `/opt/tableau/tableau_driver/jdbc` 

The latest validated PostgreSQL JDBC driver version is `postgresql-42.7.4.jar`.
The latest validated CrateDB JDBC driver is `cratedb-jdbc-standalone-2.7.0`.

Note: The most recent release `postgresql-42.7.5.jar` is not compatible with CrateDB.
We are currently working with upstream authors on resolving this regression.

### CrateDB connector

You can find the connector artefacts within the "Assets" sections on the
[releases page]. Download the [TACO file], for example `cratedb_jdbc-v0.0.5.taco`,
into:

#### Tableau Desktop

- Windows: `C:\Users\[Windows User]\Documents\My Tableau Repository\Connectors`
- MacOS: `/Users/[user]/Documents/My Tableau Repository/Connectors`

#### Tableau Prep Builder

- Windows:  `C:\Users\[Windows User]\Documents\My Tableau Prep Repository\Connectors`
- MacOS: `/Users//Documents/My Tableau Prep Repository/Connectors`

#### Tableau Server
- Windows: `C:\Program Files\Tableau\Connectors`
- Linux: `/opt/tableau/connectors`

For older versions, see [Tableau Connector SDK legacy documentation].


## Usage

For development purposes, please read the [sandbox documentation](./DEVELOP.md).

### Configure data source

When it comes to configuring a data source in Tableau, a few fragments in the
[sandbox documentation](./DEVELOP.md) may also be applicable to a production setup.

Todo: Add a dedicated section about how to install and configure the connector
in non-development mode.

## Compatibility status

Compatibility is validated using Tableau's Connector SDK, specifically using its
[TDVT suite]. Compatibility progress is tracked in [TABLEAU-2].

```
CrateDB version: 5.10.1
Last update: 20/02/2024
Pass: 96%
```
```
Test Count: 848 tests
Passed tests: 807
Failed tests: 41
Tests run: 848
Disabled tests: 0
Skipped tests: 0
```


[CrateDB]: https://cratedb.com/database
[CrateDB connector for Tableau]: https://github.com/crate/cratedb-tableau-connector
[JAR file]: https://en.wikipedia.org/wiki/JAR_(file_format)
[pgJDBC page]: https://jdbc.postgresql.org/download/
[PostgreSQL JDBC driver]: https://jdbc.postgresql.org/
[releases page]: https://github.com/crate/cratedb-tableau-connector/releases
[TACO file]: https://help.tableau.com/current/pro/desktop/en-us/examples_connector_sdk.htm
[Tableau]: https://www.tableau.com/
[Tableau Connector SDK legacy documentation]: https://help.tableau.com/current/pro/desktop/en-us/examples_connector_sdk.htm
[TABLEAU-2]: https://github.com/crate/cratedb-tableau-connector/issues/2
[TDVT suite]: https://tableau.github.io/connector-plugin-sdk/docs/tdvt
