--List all shows without the comedy genre from the 'hbtn_0d_tvshows' database

CREATE TEMPORARY TABLE tmp_comedy_shows AS
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
JOIN `tv_genres` AS g ON s.`genre_id` = g.`id`
WHERE g.`name` = "Comedy";

SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
LEFT JOIN tmp_comedy_shows AS c ON t.`title` = c.`title`
WHERE c.`title` IS NULL
ORDER BY t.`title`;

DROP TEMPORARY TABLE IF EXISTS tmp_comedy_shows;
