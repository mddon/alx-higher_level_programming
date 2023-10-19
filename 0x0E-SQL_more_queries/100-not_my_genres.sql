-- List all genres not linked to the show 'Dexter' from the 'hbtn_0d_tvshows' database


SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
LEFT JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
LEFT JOIN `tv_shows` AS t ON s.`show_id` = t.`id` AND t.`title` = "Dexter"
WHERE t.`id` IS NULL
ORDER BY g.`name`;
