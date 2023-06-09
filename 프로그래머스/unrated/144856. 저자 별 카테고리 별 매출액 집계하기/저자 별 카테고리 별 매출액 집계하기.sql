SELECT AB.AUTHOR_ID, C.AUTHOR_NAME, AB.CATEGORY, SUM(SALES*PRICE) AS TOTAL_SALES
FROM (SELECT *
       FROM BOOK_SALES AS A
       NATURAL JOIN BOOK AS B
       WHERE DATE_FORMAT(SALES_DATE, '%m') = '01') AS AB
INNER JOIN AUTHOR AS C
ON AB.AUTHOR_ID = C.AUTHOR_ID
GROUP BY AB.AUTHOR_ID, C.AUTHOR_NAME, AB.CATEGORY
ORDER BY AB.AUTHOR_ID ASC, AB.CATEGORY DESC;