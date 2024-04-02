-- 코드를 입력하세요
SELECT count(*) 
from user_info
where to_char(joined, 'YYYY') = '2021' and
      age is not null and
      age between 20 and 29;