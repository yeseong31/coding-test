WITH EMP_EVALUATION AS (
    SELECT
        E.EMP_NO,
        E.EMP_NAME,
        E.SAL,
        AVG(G.SCORE) AS AVG_SCORE
    FROM HR_EMPLOYEES E
    JOIN HR_GRADE G
      ON G.EMP_NO = E.EMP_NO
    GROUP BY E.EMP_NO, E.EMP_NAME, E.SAL
),
EMP_GRADE AS (
    SELECT
        EMP_NO,
        EMP_NAME,
        SAL,
        CASE
            WHEN AVG_SCORE >= 96 THEN 'S'
            WHEN AVG_SCORE >= 90 THEN 'A'
            WHEN AVG_SCORE >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE,
        CASE
            WHEN AVG_SCORE >= 96 THEN 0.20
            WHEN AVG_SCORE >= 90 THEN 0.15
            WHEN AVG_SCORE >= 80 THEN 0.10
            ELSE 0
        END AS BONUS_RATE
    FROM EMP_EVALUATION
)
SELECT
    EMP_NO,
    EMP_NAME,
    GRADE,
    SAL * BONUS_RATE AS BONUS
FROM EMP_GRADE
ORDER BY EMP_NO;