SELECT s.fullname , ROUND(AVG(g.grade),2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
GROUP BY s.fullname 
ORDER BY  average_grade DESC 
LIMIT 5;

SELECT d.name, s.fullname , ROUND(AVG(g.grade),2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE  d.id = 3
GROUP BY s.fullname 
ORDER BY  average_grade DESC 
LIMIT 1;

SELECT d.name, gr.name, ROUND(AVG(g.grade),2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
JOIN groups gr ON gr.id = s.group_id 
WHERE  d.id = 3
GROUP BY gr.name, d.name 
ORDER BY  average_grade DESC;

SELECT d.name, ROUND(AVG(g.grade),2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
WHERE  d.id = 2;

SELECT d.name, t.fullname
FROM disciplines d
JOIN teachers t ON t.id = d.teacher_id
WHERE  t.id = 1;

SELECT s.fullname, gr.name 
FROM students s 
JOIN groups gr ON gr.id = s.group_id
WHERE gr.id = 3;

SELECT s.fullname, g.grade, gr.name 
FROM grades g
JOIN groups gr ON gr.id = s.group_id
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 1 AND gr.id = 2
ORDER BY s.fullname;

SELECT t.fullname, d.name, ROUND(AVG(g.grade),2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE  t.id = 1
GROUP BY t.fullname, d.name 
ORDER BY average_grade DESC;

SELECT d.name, s.fullname
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id 
WHERE  s.id = 10
GROUP BY d.name;

SELECT d.name, s.fullname, t.fullname 
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON t.id = d.teacher_id
JOIN students s ON s.id = g.student_id 
WHERE  s.id = 11 AND t.id =1
GROUP BY d.name; 

SELECT t.fullname, d.name, s.fullname, ROUND(AVG(g.grade),2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s ON s.id = g.student_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE  t.id = 1 AND s.id = 11
GROUP BY t.fullname, d.name; 

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


SELECT MAX(DATE(g2.date_of))
FROM (SELECT s.fullname, d.name, g.grade, g.date_of 
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN groups gr ON gr.id = s.group_id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE gr.id = 3 AND d.id = 8 
--AND g.date_of <= (SELECT MAX(DATE(g.date_of)) FROM grades g);
ORDER BY g.date_of DESC) g2;


--GROUP BY


