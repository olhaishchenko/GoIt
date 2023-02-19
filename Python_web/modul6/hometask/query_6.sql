SELECT s.fullname, gr.name 
FROM students s 
JOIN groups gr ON gr.id = s.group_id
WHERE gr.id = 3;