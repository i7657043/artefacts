<<<<<<< HEAD
CREATE TABLE tbl_readings(
id int not null AUTO_INCREMENT,
=======
CREATE TABLE tbl_device(
device_name VARCHAR(30),
first_online DATETIME,
last_online DATETIME,
owner VARCHAR(30),
>>>>>>> origin/master
device_temp VARCHAR(3),
ambient_temp VARCHAR(3),
internal_temp VARCHAR(3),
lumens VARCHAR(3),
decibels VARCHAR(3),
status VARCHAR(3),
<<<<<<< HEAD
battery VARCHAR(3),
timestamp timestamp default currrent_timestamp not null,
primary key (id)
);



CREATE TABLE tbl_device(
id int not null AUTO_INCREMENT,
device_name VARCHAR(30),
first_online timestamp not null default current_timestamp,
last_online timestamp not null default current_timestamp on update current_timestamp,
owner VARCHAR(30),
=======
battery VARCHAR(3)
);

CREATE TABLE tbl_readings(
>>>>>>> origin/master
device_temp VARCHAR(3),
ambient_temp VARCHAR(3),
internal_temp VARCHAR(3),
lumens VARCHAR(3),
decibels VARCHAR(3),
status VARCHAR(3),
battery VARCHAR(3),
<<<<<<< HEAD
primary key (id)
=======
timestamp DATETIME
>>>>>>> origin/master
);