# Logs Analysis Project

This project is designed to use SQL and the python DB-API to create readable reports in plain english. It answers three key questions which real world management teams might ask:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Dependencies

`psycopg2` ,
`vagrant`

In order to run the source code 'SRB-Logs-Analysis.py' you will need to have psycopg2 imported. This can be done in OSX by opening a terminal and running the command `$pip3 install psycopg2`

After installing vagrant on your machine, you will need to use the command `vagrant up` to bring the VM online. Then use the command `vagrant ssh` to log in. After that you should be all set to
navigate the virtual machine through the terminal and run the source code.

## How to run on your machine

To run the source code, you will need access to the database 'news' which will contain three tables - all of which are queried in the code. This database can be downloaded from Udacity as a zipped file and must be unzipped and stored in the same vagrant directory which holds all of the other project files.

The source code was written in python version 2.7.12, so to run it from the command line simply cd into the directory containing the file and the database (vagrant), and use the command `$python Logs-Analysis-SRB.py`

The result should be the report showing the solution to the three questions.

## Views

Two views are used to answer question 3. I think there are several ways that this question could be answered including self joins and views, but I think that using two views was the easiest, so that's what I did.

Before running the source code for this project, you will need to create the two below views.

### View #1

```
create view All_results as
  select count(status) as All_Results, CAST(time AS DATE) as date
  from log
  group by date
  order by date desc;
  ```
### View #2

```
create view Error_results as
  select count(status) as ERRORS, CAST(time AS DATE) as date
  from log
  where status like '%404%'
  group by date
  order by date desc;
  ```
