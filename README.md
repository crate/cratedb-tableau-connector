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

You will need to download the PostgreSQL JDBC driver ([JAR file]), and the CrateDB connector ([TACO file]).

### PostgreSQL JDBC driver

Warning: PostgreSQL JDBC driver versions `>=postgresql-42.7.5.jar` are not compatible with CrateDB. 
The latest validated version is `postgresql-42.7.4.jar`.

Download the driver JAR file from the [pgJDBC page] into:

- Windows: `C:\Program Files\Tableau\Drivers`
- Mac: `~/Library/Tableau/Drivers`
- Linux: `/opt/tableau/tableau_driver/jdbc` 

### CrateDB connector

You can find the connector within the "Assets" sections on the
[releases page]. Download the [TACO file], for example `cratedb_jdbc-v0.0.5.taco`,
into:

#### Tableau Desktop

- Windows: `C:\Users\[Windows User]\Documents\My Tableau Repository\Connectors`
- MacOS: `/Users/[user]/Documents/My Tableau Repository/Connectors`

#### Tableau Prep Builder

- Windows: `C:\Users\[Windows User]\Documents\My Tableau Prep Repository\Connectors`
- MacOS: `/Users//Documents/My Tableau Prep Repository/Connectors`

#### Tableau Server
- Windows: `C:\Program Files\Tableau\Connectors`
- Linux: `/opt/tableau/connectors`

For older versions, see [Tableau Connector SDK legacy documentation].

Important: For Tableau Server, in multi node setups, the connector has to be installed in every node.

## Usage

For development purposes, please read the [sandbox documentation](./DEVELOP.md).

## Compatibility status

Compatibility is validated using Tableau's Connector SDK, using its
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
