SELECT d.name, s.fullname
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id 
WHERE  s.id = 10
GROUP BY d.name;