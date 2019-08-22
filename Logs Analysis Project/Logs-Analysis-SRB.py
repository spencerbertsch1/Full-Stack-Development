#!/usr/bin/env python
# python2 - version 2.7.12

# Package Imports
import psycopg2

print("... Logs Analysis Project - Spencer Bertsch ...")
print(" ")

# Use psycopg2 to connect to the news database
db = psycopg2.connect("dbname=news")
DBNAME = 'news'

# Thank you to https://www.geeksforgeeks.org/sql-string-functions/ for teaching me the SUBSTR function!
# Create function for first task:
Query1 = """
SELECT title as aritcle_title, count(title) as article_count
FROM articles,log
WHERE articles.slug = SUBSTR(log.path, 10)
GROUP BY articles.title
ORDER BY article_count desc
LIMIT 3;
"""
def QUERY1():
    #Use SQL to query the necessary data to answer the question
    db = psycopg2.connect(database = DBNAME)
    cursor = db.cursor() #create a cursor object
    cursor.execute(Query1)
    articles = cursor.fetchall()
    db.close()
    #retrieve that data from a list format - tuples are stored in the list
    A1 = articles[0][0]
    A2 = articles[1][0]
    A3 = articles[2][0]
    count1 = articles[0][1]
    count2 = articles[1][1]
    count3 = articles[2][1]
    #Print the answer the the initial question.
    print("The most popular article is " + str(A1) + " with a view count of " + str(count1) + " views.")
    print("The second most popular article is " + str(A2) + " with a view count of " + str(count2) + " views.")
    print("The third most popular article is " + str(A3) + " with a view count of " + str(count3) + " views.")
    return articles


# Create function for second task:
Query2 = """
SELECT name as author_name, count(name) as view_count
FROM articles, authors, log --join three tables!
WHERE articles.slug = SUBSTR(log.path, 10) --<-- First join from earlier function
AND articles.author = authors.id --<-- Second join from udacity help section
GROUP BY author_name
ORDER BY view_count DESC;
"""
def QUERY2():
    #Use SQL to query the necessary data to answer the question
    db = psycopg2.connect(database = DBNAME)
    cursor = db.cursor() #create a cursor object
    cursor.execute(Query2)
    author_data = cursor.fetchall()
    db.close()
    #retrieve that data from a list format - tuples are stored in the list
    author1 = author_data[0][0]
    author2 = author_data[1][0]
    author3 = author_data[2][0]
    author4 = author_data[3][0]
    view1 = author_data[0][1]
    view2 = author_data[1][1]
    view3 = author_data[2][1]
    view4 = author_data[3][1]
    #Print the answer the the initial question.
    print("The most popular author is " + str(author1) + " with " + str(view1) + " views.")
    print("The second most popular author is " + str(author2) + " with " + str(view2) + " views.")
    print("The third most popular author is " + str(author3) + " with a count of " + str(view3) + " views.")
    print("The fourth most popular author is " + str(author4) + " with a count of " + str(view4) + " views.")
    return author_data


# Create function for third task: #TWO VIEWS USED HERE - SEE README FOR VIEWS
Query3 = """
SELECT percent_error, date from
  (SELECT (CAST(errors as FLOAT) / CAST(all_results as FLOAT)) as percent_error, date from
      (SELECT All_results.all_results, Error_results.ERRORS, Error_results.date
      FROM All_Results, Error_Results
      WHERE All_Results.date = Error_Results.date) as x
    ) AS answer
    WHERE percent_error > 0.01;
"""

def QUERY3():
    #Use SQL to query the necessary data to answer the question
    db = psycopg2.connect(database = DBNAME)
    cursor = db.cursor() #create a cursor object
    cursor.execute(Query3)
    error_data = cursor.fetchall()
    db.close()
    #retrieve that data from a list format - tuples are stored in the list
    error_rate = error_data[0][0]
    date = error_data[0][1]
    #Print the answer the the initial question.
    print("On " + str(date) + " roughly " + str(100*round(error_rate,3)) + "% of requests lead to errors.")
    return error_data


if __name__ == '__main__':
    print("1. What are the most popular three articles of all time?")
    QUERY1()

    print(" ")
    print("2. Who are the most popular article authors of all time?")
    QUERY2()

    print(" ")
    print("3. On which days did more than 1% of requests lead to errors?")
    QUERY3()
