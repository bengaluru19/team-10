create DATABASE anthills;
use anthills;
create table client(cid int primary key, name varchar(100), email varchar(100), phone varchar(100));
create table project (pid int primary key,location varchar(1000), snakeprone varchar(1000), schoolTtype varchar(100), numberOfChildren varchar(100), minAge varchar(2), maxAge varchar(2), siteArea varchar(10), publicPlace boolean, Vandalism boolean, soilCondition varchar(10), trafficRoads varchar(10), waterBodies varchar(100), speciallyAbledChildren boolean, requireMaintainance varchar(10), cid int, budget int, FOREIGN key (cid) REFERENCES client(cid), designType varchar(100), designerName varchar(20) );
create table projectDashboard(pid int PRIMARY KEY, cid int, progress varchar(20), location varchar(1000), FOREIGN KEY (cid) REFERENCES client(cid), FOREIGN key (pid) REFERENCES project(pid));
