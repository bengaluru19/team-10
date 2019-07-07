create database anthill
use anthill

 create table client(cid int primary key, name varchar(100), email varchar(100), phone varchar(100));

create table project (pid int primary key,location varchar(1000), snakeprone boolean, numberOfChildren varchar(100), minAge varchar(2), maxAge varchar(2), siteArea varchar(10), publicPlace boolean, Vandalism boolean, soilCondition varchar(10), trafficRoads boolean, waterBodies boolean, speciallyAbledChildren boolean, requireMaintainance boolean, cid int, budget int, FOREIGN key (cid) REFERENCES client(cid), designType varchar(1));

create table projectDashboard(pid int PRIMARY KEY, cid int, progress varchar(20), location varchar(1000), FOREIGN KEY (cid) REFERENCES client(cid), FOREIGN key (pid) REFERENCES project(pid));

insert into client values (1,'Anagha','anagha@gmail.com','9343434112');
insert into client values (2,'Sanjitha','sanj@gmail.com','9343474112');
insert into client values (3,'Kaushik','kaush@gmail.com','9343434562');
insert into client values (4,'Deepak','deep@gmail.com','9342134112');

insert into project values (1,'Vijayanagar',0,440,5,5,900,0,0,'Rocky',1,0,0,0,2,210000,NULL);
insert into project values (2,'Marathalli',1,100,3,3,1400,1,1,'Soft',1,0,0,1,4,175000,NULL);
insert into project values (3,'Mathikere',0,200,2,2,2000,0,1,'Wet',1,1,0,1,1,150000,NULL);
insert into project values (4,'Hebbal',1,300,4,4,1700,1,0,'Dry',0,0,1,0,3,300000,NULL);


insert into projectDashboard values (1,2,NULL,'Vijayanagar');
insert into projectDashboard values (2,4,'Construction in Progress','Marathalli');
insert into projectDashboard values (3,1,Design Accepted,'Mathikere');
insert into projectDashboard values (4,3,Survey Complete,'Hebbal');

