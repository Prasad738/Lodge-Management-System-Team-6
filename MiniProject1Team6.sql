
create database data4;
use data4;
create table checkin(
	checkin_id int auto_increment primary key,
	customer_Name varchar(50) not null,
    Moblie_number varchar(10) not null,
    id_proof varchar(30) not null,
    check_in_date date not null,
    room_type varchar(30) not null,
	rate int not null,
    num_of_guest int default(1)
    );
    
create table checkout(
	checkin_id int unique not null,
    check_out_date date not null,
    Total_bill int default(0)
    );
    
    
drop table checkout;

    
select * from checkin;
select * from checkout;
