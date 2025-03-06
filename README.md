# CrateDB connector for Tableau

[![CI status](https://github.com/crate/cratedb-tableau-connector/actions/workflows/main.yml/badge.svg)](https://github.com/crate/cratedb-tableau-connector/actions/workflows/main.yml)
![GitHub Release](https://img.shields.io/github/v/release/crate/cratedb-tableau-connector)
![Static Badge](https://img.shields.io/badge/tdvt_compatibility-95%25-brightgreen?style=flat&logo=cratedb)
![Static Badge](https://img.shields.io/badge/CrateDB-5.10.1-brightgreen?style=flat&logo=cratedb)

## About

[Tableau] is a visual business intelligence and analytics software platform.
It expresses data by translating drag-and-drop actions into data queries
through an intuitive interface.

[CrateDB] is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
PostgreSQL-compatible, and based on Lucene.

## Install

You will need to acquire and install two software artefacts,
the PostgreSQL JDBC driver, and the CrateDB connector.

### PostgreSQL JDBC driver

Download the driver from the [pgJDBC page] and put it into:

- Windows: `C:\Program Files\Tableau\Drivers`
- Mac: `~/Library/Tableau/Drivers`
- Linux: `/opt/tableau/tableau_driver/jdbc` 

The latest validated PostgreSQL JDBC driver version is `postgresql-42.7.4.jar`.
The latest validated CrateDB JDBC driver is `cratedb-jdbc-standalone-2.7.0`.

Note: The most recent release `postgresql-42.7.5.jar` is not compatible with CrateDB.
We are currently working with upstream authors on resolving this regression.

### CrateDB connector

You can find the connector on the [releases page]. Put it into:

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

### Configure data source

Todo: Add a few words how to actually establish the connection to CrateDB
after installing the driver and connector?


### Signature verification

The current release of the connector is not signed. This issue is being addressed,
but in the meantime, signature verification can be disabled.

* On _Tableau Desktop_, please use this command-line argument: `-DDisableVerifyConnectorPluginSignature=true`

* On _Tableau Server_, you can disable signature verification by setting `native_api.disable_verify_connector_plugin_signature` to `true` via TSM.

More information can be found on the [Tableau Connector SDK `run-taco` documentation].


## Status

The native CrateDB connector for Tableau aims to offer excellent compatibility
with Tableau's line of products, providing optimal user experience.
While it does not offer 100% compatibility yet, the connector is pretty close to
cover Tableau's test suite successfully and completely.

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

Compatibility is validated using Tableau's Connector SDK, specifically using its [TDVT suite].
Compatibility progress is tracked in [TABLEAU-2].


[CrateDB]: https://cratedb.com/database
[pgJDBC page]: https://jdbc.postgresql.org/download/
[releases page]: https://github.com/crate/cratedb-tableau-connector/releases
[Tableau]: https://www.tableau.com/
[Tableau Connector SDK legacy documentation]: https://help.tableau.com/current/pro/desktop/en-us/examples_connector_sdk.htm
[Tableau Connector SDK `run-taco` documentation]: https://tableau.github.io/connector-plugin-sdk/docs/run-taco
[TABLEAU-2]: https://github.com/crate/cratedb-tableau-connector/issues/2
[TDVT suite]: https://tableau.github.io/connector-plugin-sdk/docs/tdvt
