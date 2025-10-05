SELECT id, visit_date, people
FROM (
    SELECT 
        id,
        visit_date,
        people,
        -- Assign a group id for consecutive sequences
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
) temp
WHERE grp IN (
    SELECT grp
    FROM (
        SELECT 
            id - ROW_NUMBER() OVER (ORDER BY id) AS grp
        FROM Stadium
        WHERE people >= 100
    ) sub
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;
