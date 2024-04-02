-- 코드를 입력하세요
-- SELECT DR_NAME, DR_ID, MCDP_CD, to_char(HIRE_YMD, 'YYYY-MM-DD')
-- from DOCTOR
-- where MCDP_CD = 'CS' or MCDP_CD = 'GS'
-- order by HIRE_YMD desc, DR_ID asc;


SELECT  DR_NAME,
        DR_ID,  
        MCDP_CD,    
        TO_CHAR(HIRE_YMD,'YYYY-MM-DD') AS HIRE_YMD
FROM    DOCTOR
WHERE   MCDP_CD IN ('CS','GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC