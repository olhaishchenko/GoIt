SELECT s.fullname, d.name, g.grade, g.date_of 
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN groups gr ON gr.id = s.group_id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE g.date_of = (SELECT MAX(DATE(g2.date_of))
FROM (SELECT g.grade, g.date_of 
FROM grades g 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE gr.id = 1 AND d.id = 1) g2);