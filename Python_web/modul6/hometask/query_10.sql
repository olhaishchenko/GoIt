SELECT d.name, s.fullname, t.fullname 
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON t.id = d.teacher_id
JOIN students s ON s.id = g.student_id 
WHERE  s.id = 11 AND t.id =1
GROUP BY d.name; 