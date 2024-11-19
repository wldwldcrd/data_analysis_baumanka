select first_name from actor limit 5

select 
	title,
	length
from
	film
where length <> 100

select 
	rating,
	round(avg(length),2)
from 
	film
group by rating 


select
	f.title,
	l.name 
from film f
	join "language" l 
		on f.language_id = l.language_id 


select * from "language" l 

-- CRUD
--C - create
--R - read
-- U - update
-- D -- delete

select * from book b 

insert into book(title, pages) values('Преступление и наказание', 680)

update book set pages=680 where id = 2

delete from book where id=4



































