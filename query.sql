SELECT coalesce(s.name, '') || ' ' || coalesce(s.surname, '') AS student, sc.math_score 
FROM students s
INNER JOIN scoring sc
USING(stud_id)
WHERE sc.reading_score > 80;

SELECT ge.gender, ROUND(AVG(sc.math_score), 2) AS average_math_score
FROM scoring sc
INNER JOIN gender ge
USING(stud_id)
GROUP BY ge.gender;

SELECT s.surname, sc.reading_score
FROM students s
INNER JOIN scoring sc
USING(stud_id);