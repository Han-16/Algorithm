SELECT FH.FLAVOR
FROM FIRST_HALF FH, ICECREAM_INFO II
WHERE FH.FLAVOR = II.FLAVOR AND II.INGREDIENT_TYPE = 'FRUIT_BASED'
    AND TOTAL_ORDER >= 3000
ORDER BY FH.TOTAL_ORDER DESC;