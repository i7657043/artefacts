CREATE TABLE tbl_device(
device_name VARCHAR(30),
first_online DATETIME,
last_online DATETIME,
owner VARCHAR(30),
device_temp VARCHAR(3),
ambient_temp VARCHAR(3),
internal_temp VARCHAR(3),
lumens VARCHAR(3),
decibels VARCHAR(3),
status VARCHAR(3),
battery VARCHAR(3)
);

CREATE TABLE tbl_readings(
device_temp VARCHAR(3),
ambient_temp VARCHAR(3),
internal_temp VARCHAR(3),
lumens VARCHAR(3),
decibels VARCHAR(3),
status VARCHAR(3),
battery VARCHAR(3),
timestamp DATETIME
);