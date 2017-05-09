CREATE TABLE tbl_device(
id int NOT NULL AUTO_INCREMENT,
device_name VARCHAR(30),
first_online timestamp not null default current_timestamp,
last_online timestamp not null default current_timestamp on update current_timestamp,
owner VARCHAR(30),
device_temp VARCHAR(3),
ambient_temp VARCHAR(3),
internal_temp VARCHAR(3),
lumens VARCHAR(3),
decibels VARCHAR(3),
status VARCHAR(3),
battery VARCHAR(3),
primary key (id)
);


CREATE TABLE tbl_readings(
id int NOT NULL AUTO_INCREMENT,
device_temp VARCHAR(3),
ambient_temp VARCHAR(3),
internal_temp VARCHAR(3),
lumens VARCHAR(3),
decibels VARCHAR(3),
status VARCHAR(3),
battery VARCHAR(3),
timestamp not null default current_timestamp,
primary key (id)
);
