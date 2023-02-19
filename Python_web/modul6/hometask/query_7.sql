SELECT s.fullname, g.grade, gr.name 
FROM grades g
JOIN groups gr ON gr.id = s.group_id
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 1 AND gr.id = 2
ORDER BY s.fullname;