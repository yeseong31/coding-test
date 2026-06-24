SELECT
    hd.dept_id,
    hd.dept_name_en,
    ROUND(AVG(he.sal)) AS avg_sal
FROM hr_department hd
JOIN hr_employees he ON hd.dept_id = he.dept_id
GROUP BY hd.dept_id, hd.dept_name_en
ORDER BY avg_sal DESC;