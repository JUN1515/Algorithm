-- 코드를 입력하세요
SELECT book_id, to_char(published_date, 'YYYY-MM-DD')
from book
where to_char(published_date, 'YYYY') = '2021' and category in ('인문')
order by published_date;