create database labemp;
use labemp;
create table department(did varchar(20)primary key ,dname varchar(20));
create table salgrade(grade varchar(5)primary key,minsal int,maxsal int);
create table employee(ssn varchar(10)primary key,ename varchar(20),address varchar(27),desig varchar(12),hire date,commi int,
salary int,hssn varchar(20),did varchar(20),grade varchar(10),
foreign key(grade)references salgrade(grade)on update 
cascade on delete cascade,foreign key(did)references department(did)on update cascade on delete cascade);

insert into department values('ml101','machine');
insert into department values('ml102','machanical');
insert into department values('ml103','maths');
insert into department values('ml104','english');

insert into salgrade values('a',10000,20000);
insert into salgrade values('b',15000,25000);
insert into salgrade values('c',15050,18000);
insert into salgrade values('d',11000,22000);

insert into employee values('head01','akask','mumbai','head',"1-1-13",12000,260000,'null','ml101','a');
insert into employee values('emp02','bhavya','mumbai','emphead',"1-1-12",2000,200000,'head01','ml101','b');
insert into employee values('emp03','tarun','mumbai','emp',"3-3-13",12000,250000,'head01','ml101','c');
1
select ename,salary,concat("$",salary*1.25) as dollersalary from employee;
2
select desig,avg(salary)from employee where desig="emp";
3
select e.* from employee as e, department as d where e.did=d.did and dname!="english"; 
5
select ename,salary,commi from employee where (select max(salary+commi)from employee)>=any(select salary from employee);
6
select d.*,e.* from department as d left join employee as e on e.did=d.did where e.did is null;