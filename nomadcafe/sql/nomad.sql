# create database nomad;


drop table if exists cafe_info;

create table if not exists cafe_info(
  id int(11) primary key auto_increment,
  name varchar(255) not null,
  chain_id int(11) not null default '0',
  created_at datetime not null default current_timestamp,
  updated_at datetime not null default current_timestamp on update current_timestamp
);

insert into cafe_info (id, name, chain_id, created_at) values
  (30, 'マクドナルド南新宿店', 1,'2019-09-11 10:00:00'),
  (31, 'ドトール新宿南口店', 2, '2019-09-11 11:00:00'),
  (32, '但馬珈琲店新宿南口店', 3, '2019-09-11 11:30:00');
