-- CREATE DATABASE fifa_world_cup;
USE fifa_world_cup;
-- Query 1 : Total Matches Played
/* SELECT COUNT(*) AS Total_Matches
FROM matches;

-- Query 2 : Total Goals Scored
SELECT SUM(total_goals) AS Total_Goals
FROM matches;

-- Query 3 : Average Goals Per Match
SELECT ROUND(AVG(total_goals),2) AS Avg_Goals_Per_Match
FROM matches;

-- Query 4 : Home vs Away Wins
SELECT
match_result,
COUNT(*) AS Matches
FROM matches
GROUP BY match_result;

-- Query 5 : Highest Attendance Match
SELECT
home_team,
away_team,
stadium,
attendance
FROM matches
ORDER BY attendance DESC
LIMIT 1; */

-- Query 6 : Team with Most Goals

/* SELECT
team,
SUM(goals) AS Total_Goals

FROM
(
SELECT home_team AS team,
home_goals AS goals
FROM matches

UNION ALL

SELECT away_team,
away_goals
FROM matches
) t

GROUP BY team

ORDER BY Total_Goals DESC;


-- Query 7 : Team with Most Wins

SELECT
winner,
COUNT(*) AS Wins

FROM matches

WHERE winner<>'Draw'

GROUP BY winner

ORDER BY Wins DESC;


-- Query 8 : Team with Highest Average Possession

SELECT
team,
ROUND(AVG(possession),2) AS Avg_Possession

FROM
(
SELECT
home_team AS team,
home_possession AS possession
FROM matches

UNION ALL

SELECT
away_team,
away_possession
FROM matches
) t

GROUP BY team

ORDER BY Avg_Possession DESC;


-- Query 9 : Team with Most Shots

SELECT
team,
SUM(shots) AS Total_Shots

FROM
(
SELECT
home_team AS team,
home_shots AS shots
FROM matches

UNION ALL

SELECT
away_team,
away_shots
FROM matches
) t

GROUP BY team

ORDER BY Total_Shots DESC;


-- Query 10 : Team with Most Corners

SELECT
team,
SUM(corners) AS Total_Corners

FROM
(
SELECT
home_team AS team,
home_corners AS corners
FROM matches

UNION ALL

SELECT
away_team,
away_corners
FROM matches
) t

GROUP BY team

ORDER BY Total_Corners DESC; */

-- Query 11 : Highest Scoring Matches

/* SELECT
home_team,
away_team,
total_goals,
stadium

FROM matches

ORDER BY total_goals DESC
LIMIT 10;


-- Query 12 : Biggest Winning Margin

SELECT
home_team,
away_team,
goal_difference

FROM matches

ORDER BY goal_difference DESC
LIMIT 10;


-- Query 13 : Stage-wise Goal Analysis

SELECT
stage,
SUM(total_goals) AS Goals

FROM matches

GROUP BY stage

ORDER BY Goals DESC;


-- Query 14 : Stadium Attendance Analysis

SELECT
stadium,
SUM(attendance) AS Total_Attendance

FROM matches

GROUP BY stadium

ORDER BY Total_Attendance DESC;


-- Query 15 : Most Entertaining Matches
-- (Based on Total Shots)

SELECT
home_team,
away_team,
total_shots,
total_goals

FROM matches

ORDER BY total_shots DESC
LIMIT 10;*/