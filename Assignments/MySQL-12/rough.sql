DROP database IF EXISTS doc;
create database doc;
use doc;
DROP TABLE IF EXISTS doctor;
CREATE TABLE DOCTOR (
  No decimal(2,0) PRIMARY KEY,
  Name varchar(10) default NULL,
  Age decimal(2,0) default NULL,
  Department varchar(20) default Orthopedic,  
  DateofAdmn date default NULL,
  Charges decimal(3) default 300,
  Sex char(1) default F
);


INSERT INTO DOCTOR VALUES ('1','Sandeep','65','Surgery','23/02/07','M');
INSERT INTO DOCTOR VALUES ('2','Ravina','24','20/01/07',200);
INSERT INTO DOCTOR VALUES ('3','Karan','45','19/02/07',200,'M');
INSERT INTO DOCTOR VALUES ('4','Tarun','12','Surgery','01/01/07','M');
INSERT INTO DOCTOR VALUES ('5','Zubin','36','ENT','12/01/07',250,'M');
INSERT INTO DOCTOR VALUES ('6','Ketaki','16','ENT','24/02/07');
INSERT INTO DOCTOR VALUES ('7','Ankita','29','Cardiology','20/02/07',800);
INSERT INTO DOCTOR VALUES ('8','Zareen','45','Gynecology','22/02/07');
INSERT INTO DOCTOR VALUES ('9','Kush','19','Cardiology','13/01/07',800,'M');
INSERT INTO DOCTOR VALUES ('10','Shailya','31','Nuclear Medicine','19/02/07',400);

