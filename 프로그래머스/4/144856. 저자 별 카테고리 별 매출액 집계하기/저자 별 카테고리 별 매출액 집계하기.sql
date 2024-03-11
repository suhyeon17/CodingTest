-- 코드를 입력하세요
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SALES * PRICE) AS 'TOTAL_SALES'
FROM BOOK
JOIN AUTHOR USING (AUTHOR_ID)
JOIN BOOK_SALES USING (BOOK_ID)
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY AUTHOR_NAME, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC
