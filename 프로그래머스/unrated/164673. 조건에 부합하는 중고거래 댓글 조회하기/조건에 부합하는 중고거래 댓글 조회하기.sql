SELECT BO.TITLE, BO.BOARD_ID, RE.REPLY_ID,
    RE.WRITER_ID, RE.CONTENTS, DATE_FORMAT(RE.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD BO, USED_GOODS_REPLY RE
WHERE BO.BOARD_ID = RE.BOARD_ID AND BO.CREATED_DATE LIKE '2022-10-%'
ORDER BY RE.CREATED_DATE ASC, BO.TITLE ASC;