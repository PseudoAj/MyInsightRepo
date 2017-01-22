# Utility of Things

## Motivation

The current utility systems are outdated and this is engineered data pipeline to accommodate the next generation of devices.

## Requirements

* [pegasus](https://github.com/InsightDataScience/pegasus)
* python
  * [Faker](https://faker.readthedocs.io/en/latest/index.html)

## Data format

### Idea

The idea is to create as realistic dataset as possible; hence the dataset is inspired from multiple sources including:

1. [Utility API](https://utilityapi.com/docs#data-formats)

### Considerations

1. Based on [census](http://www.census.gov/quickfacts/table/PST045216/36) it is evident that there `536,890` business establishments and `8,206,739` households in in NYC; thats about `6.14%`. The same ratio is replicated while generating data.

### Schema

The schema for the data:

* user
  * name
  * address
