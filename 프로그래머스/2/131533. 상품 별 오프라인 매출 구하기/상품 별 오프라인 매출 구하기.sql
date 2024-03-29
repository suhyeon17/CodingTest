-- 코드를 입력하세요
SELECT PRODUCT_CODE, (SUM(SALES_AMOUNT) * PRICE) AS 'SALES'
FROM PRODUCT P, OFFLINE_SALE S
WHERE P.PRODUCT_ID = S.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE