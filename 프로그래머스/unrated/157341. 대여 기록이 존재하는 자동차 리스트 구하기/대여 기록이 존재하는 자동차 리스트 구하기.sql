SELECT DISTINCT(C.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR C, CAR_RENTAL_COMPANY_RENTAL_HISTORY H
WHERE C.CAR_ID = H.CAR_ID AND C.CAR_TYPE = '세단'
    AND DATE_FORMAT(START_DATE, '%m') = '10'
ORDER BY C.CAR_ID DESC;