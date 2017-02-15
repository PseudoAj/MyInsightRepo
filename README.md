![cover](misc/images/cover.png)

> AUTH: Analytics of Utility Things is a platform for ingesting, processing and extracting insights from next billion connected Internet of Things (IoT).

<hr/>

| [![Build Status](https://travis-ci.org/PseudoAj/MyInsightRepo.svg?branch=master)](https://travis-ci.org/PseudoAj/MyInsightRepo) | Presentation: [slides](http://authslides.pseudoaj.com)  | Demo: [auth.pseudoaj.com](http://auth.pseudoaj.com) | Contact: [linkedin](https://www.linkedin.com/in/pseudoaj) |
|----------|----------------|--------|-----------|

## About

With the advent of Internet of Things (IoT), traditional systems are being replaced with smart systems that can speak with cloud in real-time but there is a engineering problem: How can I **ingest** this information with high **velocity** from **variety** of sensors and extract **accurate** insights at **scale** with **fault tolerance**? This project attempts to solve this problem.

### Wouldn't it be nice if you can see your home utilization like this?

![Demo1](misc/images/demo1.gif)

### Or wouldn't it be cool to monitor your country utilization like this?

![Demo2](misc/images/demo2.gif)

## Data Pipeline

![pipeline](misc/images/pipeline.jpg)

## Technical Stack

| **#**| **Technology**   | **Language** | **Purpose**              |
|---|--------------|----------|----------------------|
| 1 | `Apache Kafka` | Python   | Ingestion            |
| 2 | `Apache Flink` | Java     | Stream Processing    |
| 3 | `Redis`        | Java/PHP | Key/Value Cache      |
| 4 | `Amazon S3`    | N/A      | Distributed Storage  |
| 5 | `Apache Spark` | Python   | Batch Processing     |
| 6 | `MySQL`        | SQL      | Application Database |
| 7 | `Laravel`      | PHP      | Web Framework        |
| 8 | `Amazon AWS`   | BASH     | Devops               |

## Directory Structure

+ data
  + batch
  + examples
  + output
  + S3
    + tmp
  + src
  + stream
+ flink

## 1. Simulating Data

The idea is to create as realistic dataset as possible; hence the dataset is inspired from real world frameworks and smart meters. Data consists of `8 Miliion` users including residential and business utility installations, this data is saved as `dictionaries` using `pickle` files along with meta data. Each user is assigned with a random starting time for sending information and data is generated every

## 2. Data Ingestion

## 3. Batch Processing

## 4. Stream Processing

## 5. Web Application
