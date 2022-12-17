SELECT COUNT(*)
FROM tweet_userhist;

SELECT id_str, favorite_count
FROM tweets;

SELECT id_str, retweet_count
FROM tweets;

SELECT id_str, text, id, max(created_at)
FROM tweets
GROUP BY id_str, text, id, created_at;

SELECT id_str, text, COUNT(*)id
FROM tweets
GROUP BY id_str;

SELECT COUNT(*) 
FROM tweet_users;

SELECT COUNT(*) 
FROM tweets 
WHERE TEXT LIKE '%crime%';

SELECT * 
FROM tweet_users
WHERE screen_name LIKE '%pd';

SELECT city, count(id_str)
FROM tweets
GROUP BY city;

SELECT * 
FROM tweets 
WHERE date(created_at) = current_date();

SELECT * 
FROM tweets 
WHERE hour(created_at) = hour(current_time());

SELECT created_at, id
FROM tweets 
GROUP BY created_at
ORDER BY created_at DESC;

SELECT city, count(city)
FROM tweets
GROUP BY city
ORDER BY city DESC;

SELECT state, count(state)
FROM tweets
GROUP BY state
ORDER BY state DESC;

SELECT country, count(country)
FROM tweets
GROUP BY country
ORDER BY country DESC;

SELECT * 
FROM tweets
WHERE created_at >= '2022-11-12 18:00:00.000' 
AND   created_at <= '2022-11-13 06:00:00.000';

SELECT *
FROM tweets
WHERE created_at >= '2022-11-12 06:00:00.000' 
AND   created_at <= '2022-11-12 18:00:00.000';

SELECT * 
FROM tweet_userhist
WHERE user_id = 1591246553771311104;

SELECT COUNT(*) 
FROM tweet_userhist 
WHERE user_id = 1572665185319403525;

SELECT id 
FROM tweets 
WHERE id_str = 1590902258098900992;

SELECT created_at 
FROM tweets 
WHERE id_str = 1590902258098900992;






















