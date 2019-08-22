
--Trying to get all these queries to work out...

-- Query 1
SELECT title as aritcle_title, count(title) as article_count
FROM articles,log
WHERE articles.slug = SUBSTR(log.path, 10)
GROUP BY articles.title
ORDER BY article_count desc
LIMIT 3;


-- Query 2
SELECT name as author_name, count(name) as view_count
FROM articles, authors, log --join three tables!
WHERE articles.slug = SUBSTR(log.path, 10) --<-- First join from earlier function
AND articles.author = authors.id --<-- Second join from udacity help section
GROUP BY author_name
ORDER BY view_count DESC;


-- Query 3 ...still in progress...
select count(status) as ERRORS, CAST(time AS DATE) as date
from log
where status like '%404%'
group by date
order by date desc;

select count(status) as All_Results, CAST(time AS DATE) as date
from log
group by date
order by date desc;

--creating views!

create view All_results as
  select count(status) as All_Results, CAST(time AS DATE) as date
  from log
  group by date
  order by date desc;

create view Error_results as
  select count(status) as ERRORS, CAST(time AS DATE) as date
  from log
  where status like '%404%'
  group by date
  order by date desc;

--And now the query which will be used to combine data stored in each view
select * from All_Results;
select * from Error_Results;

--final query!
select percent_error, date from
  (select (CAST(errors as FLOAT) / CAST(all_results as FLOAT)) as percent_error, date from
      (select All_results.all_results, Error_results.ERRORS, Error_results.date
      from All_Results, Error_Results
      where All_Results.date = Error_Results.date) as x
    ) as answer
    where percent_error > 0.01;


  # REFERENCES
  """
  Through this project I used several sites including stack exchange, stack overflow, and github.
  By far the largest source of input that I used for this project was the Udacity message board.
  I'm not sure who Christopher C is, but his answers to questions were very helpful!
  I also figured out many of the problems by simply rewatching the videos on SQL from this course!
  They were very helpful!
  """











--end
