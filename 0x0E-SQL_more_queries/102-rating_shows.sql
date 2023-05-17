--  lists all shows contained in hbtn_0d_tvshows without a genre linked
-- lists all rows of a database that don't have one column
SELECT tv_shows.title, SUM(ratings.rating) AS rating_sum
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
