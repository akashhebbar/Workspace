create database labmovie;
use labmovie;
create table movie(mid int primary key,title varchar(20),yor date,duration time,language varchar(20),start date);
create table actor(aid int primary key,name varchar(20),gender varchar(20));
create table director(did int primary key,fname varchar(20),lname varchar(20));
create table genere(gid int primary key,gtype varchar(20));
drop table reviewer;
create table reviewer(rid int primary key,rname varchar(20));
create table actsin(mid int,aid int,role varchar(20),foreign key(mid)references 
movie(mid)on update cascade on delete cascade,foreign key(aid)references actor(aid)on update cascade on delete cascade);
create table review(rid int,mid int,rate int,foreign key(rid)references
reviewer(rid)on update cascade on delete cascade,foreign key (mid)references movie(mid)on update cascade on delete cascade);
create table directs(did int,mid int,foreign key(did)references
director(did)on update cascade on delete cascade,foreign key (mid)references movie(mid)on update cascade on delete cascade);
create table belongs(mid int,gid int,foreign key(gid)references
genere(gid)on update cascade on delete cascade,foreign key (mid)references movie(mid)on update cascade on delete cascade);


insert into movie values(101,'newday','1-1-19',12.00,'english','1-1-18');
insert into movie values(102,'oldday','2-2-19',11.00,'english','4-4-18');

insert into actor values(101,'arun','male');
insert into actor values(102,'Trun','male');
insert into actor values(103,'Karun','male');

insert into director values(101,'tarun','raj');
insert into director values(102,'Karun','ram');
insert into director values(103,'Varun','ravi');


insert into genere values(101,'love');
insert into genere values(102,'horror');
insert into genere values(103,'romantic');



1
select * from movie where yor>"1-1-19";
2
