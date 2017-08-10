-- SELECT * FROM meals LIMIT 5;


-- SELECT
--   type,
--   ROUND(AVG(price),2) as avg_price,
--   MIN(price) AS min_price,
--   MAX(price) AS max_price
-- FROM meals
-- GROUP BY type;


-- SELECT
--   type,
--   ROUND(AVG(price),2) as avg_price,
--   MIN(price) AS min_price,
--   MAX(price) AS max_price
-- FROM meals
-- WHERE
--   date_part('year', dt) = 2013 AND
--   date_part('month', dt) <= 3
-- GROUP BY type;


-- SELECT
--   type,
--   date_part('month', dt) AS month,
--   ROUND(AVG(price),2) AS avg_price,
--   MIN(price) AS min_price,
--   MAX(price) AS max_price
-- FROM meals
-- WHERE
--   date_part('year', dt) = 2013 AND
--   date_part('month', dt) <= 3
-- GROUP BY type, month
-- ORDER BY month;

-- SELECT * FROM events LIMIT 5;

-- From the events table, write a query that gets the total number of buys, likes and shares for each meal id.

-- SELECT
--   meal_id,
--   event,
--   COUNT(event)
-- FROM events
-- GROUP BY meal_id, event
-- ORDER BY meal_id
-- LIMIT 25;
--
-- SELECT
--   meal_id,
--   SUM(CASE WHEN event='bought' THEN 1 ELSE 0 END) AS bought,
--   SUM(CASE WHEN event='like' THEN 1 ELSE 0 END) AS likes,
--   SUM(CASE WHEN event='share' THEN 1 ELSE 0 END) AS shares
-- FROM events
-- GROUP BY meal_id
-- ORDER BY meal_id
-- LIMIT 25;

-- SELECT * FROM meals LIMIT 5;
--
-- SELECT
--   type,
--   ROUND(AVG(price), 2) AS avg_price
-- FROM meals
-- GROUP BY type;
--
-- SELECT
--   type,
--   ROUND(AVG(price), 2) AS avg_price
-- FROM meals
-- GROUP BY type
-- ORDER BY type;
--
-- SELECT
--   type,
--   ROUND(AVG(price), 2) AS avg_price
-- FROM meals
-- GROUP BY type
-- ORDER BY avg_price DESC;

-- SELECT * FROM users LIMIT 1;
-- SELECT * FROM events LIMIT 1;
-- SELECT * FROM meals LIMIT 1;

-- SELECT
--   u.userid,
--   u.dt,
--   u.campaign_id,
--   e.meal_id,
--   e.event,
--   m.price,
--   m.type
-- FROM users AS u
-- JOIN events AS e
-- ON u.userid = e.userid AND
--   e.event='bought'
-- JOIN meals AS m
-- ON m.meal_id = e.meal_id
-- LIMIT 10;
--
-- SELECT
--   meal_id,
--   SUM(CASE WHEN event='bought' THEN 1 ELSE 0 END) AS num_meals_bought
-- FROM events
-- GROUP BY meal_id
-- ORDER BY meal_id
-- LIMIT 10;

-- SELECT
--   type,
--   COUNT(type)
-- FROM meals
-- JOIN events
-- ON meals.meal_id = events.meal_id AND
--   events.event = 'bought'
-- GROUP BY type;

-- SELECT m.type, COUNT(m.type)
-- FROM meals AS m
-- JOIN (
--   SELECT type, AVG(price) AS avg_price
--   FROM meals
--   GROUP BY type) AS avgs
-- ON m.type = avgs.type AND
--   m.price > avgs.avg_price
-- GROUP BY m.type;

-- SELECT COUNT(users) FROM users;
--
-- SELECT
--   campaign_id,
--   COUNT(users),
--   CAST(COUNT(users) AS REAL) / (SELECT COUNT(users) FROM users) AS percent
-- FROM users
-- GROUP BY campaign_id;

-- Answer the question, "What user from each campaign bought the most items?"


WITH user_campaign_count AS
(
  SELECT campaign_id, users.userid, COUNT(1) AS cnt
FROM users
JOIN events
ON users.userid=events.userid AND
events.event = 'bought'
GROUP BY campaign_id, users.userid
ORDER BY users.userid, campaign_id
  )

SELECT u.campaign_id, u.userid, u.cnt
FROM user_campaign_count AS u
JOIN(
  SELECT campaign_id, MAX(cnt) AS cnt
  FROM user_campaign_count
  GROUP BY campaign_id) AS m
ON u.campaign_id=m.campaign_id AND u.cnt=m.cnt
ORDER BY u.campaign_id, u.userid;



-- WITH user_campaign_count AS(
--   campaign_id, users.userid, COUNT(1) AS cnt
--   FROM users
--   JOIN events
--   ON users.userid=events.userid AND
--   events.event = 'bought'
--   GROUP BY campaign_id, users.userid
-- )
--
-- SELECT userid, campaign_id
-- FROM users AS u
-- JOIN(
--   SELECT
--     userid,
--     SUM(CASE WHEN event='bought' THEN 1 ELSE 0 END) as counts
--   FROM events
--   GROUP BY userid) AS counts
-- ON
