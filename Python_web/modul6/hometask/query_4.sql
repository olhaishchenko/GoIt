SELECT d.name, ROUND(AVG(g.grade),2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
WHERE  d.id = 2;