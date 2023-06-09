SELECT BOOK.BOOK_ID, AUTHOR.AUTHOR_NAME,
    DATE_FORMAT(BOOK.PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK JOIN AUTHOR on BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE CATEGORY IN ('경제')
ORDER BY PUBLISHED_DATE
