CREATE DATABASE lol;
use lol;

DROP TABLE IF EXISTS champions;
DROP TABLE IF EXISTS classes;
DROP TABLE if exists champions_stats;
drop table if exists champions_abilities;
drop table if exists itemss;
drop table if exists runes;
drop function if exists get_nr_champs;
drop procedure if exists get_all_items;
drop function if exists get_nr_items;
drop table if exists itemss_archive;

CREATE TABLE champions (
  name VARCHAR(20),
  class VARCHAR(20),
  description VARCHAR(50)
);

create table classes (
	typee varchar(20),
	description varchar(200),
	num int
);

create table champions_stats(
	name VARCHAR(20),
	health int,
	armour int,
	magic_resist int,
	adaptive_damage int
);

create table champions_abilities(
	name varchar(20),
	passive varchar(20),
	qbility varchar(20),
	wbility varchar(20),
	ebility varchar(20),
	rbility varchar(20)
);

create table itemss(
	name varchar(20),
	cost int,
	components_number varchar(20)
);

create table itemss_archive(
	name varchar(20),
	cost int,
	components_number varchar(20)
);


create table runes(
	description varchar(20), /*---precision*/
	keystone varchar(20),
	slot1 varchar(20),
	slot2 varchar(20),
	slot3 varchar(20)
);

/* procedure to get all items */
DELIMITER $$
 
CREATE PROCEDURE get_all_items()
BEGIN
    select * from itemss;
END $$
 
DELIMITER ;

/* function to get number of items */
DELIMITER $$ 
CREATE FUNCTION get_nr_items() 
RETURNS int
BEGIN
    DECLARE num int;
 
    select count(*) into num from itemss;
    RETURN (num);
END$$
DELIMITER ;

/* function to get number of champions*/
DELIMITER $$ 
CREATE FUNCTION get_nr_champs() 
RETURNS int
BEGIN
    DECLARE num int;
 
    select count(*) into num from champions;
    RETURN (num);
END$$
DELIMITER ;

/*    TRIGGER    */
DELIMITER $$
 
CREATE TRIGGER before_itemss_delete
BEFORE DELETE
ON itemss FOR EACH ROW
BEGIN
    INSERT INTO itemss_archive(name, cost, components_number)
    VALUES(OLD.name, OLD.cost, OLD.components_number);
END$$    
 
DELIMITER ;


insert into classes 
(typee, description, num)
values
('mage', 'Mages are champions who typically possess great reach, ability-based area of effect damage and crowd control', 27),
('assassin', 'Assassins specialize in infiltrating enemy lines with their unrivaled mobility to quickly dispatch high-priority targets', 18),
('support', 'Supports specialize in locking down opponents or, creating intense zones of threat that only foolish enemies would dare wade through', 10),
('tank', 'Tanks are tough melee champions who sacrifice damage in exchange for powerful crowd control', 9);

insert into itemss
(name, cost, components_number)
values
('Bloodthirster', 3500, 4),
('Frostfang', 500, 0),
('Guardian Angel', 2800, 3),
('Iceborn gauntlet', 2700, 2);

insert into champions
(name, class, description)
values
('Azir', 'Mage', 'Emperor of the sands'),
('Anivia', 'Mage', 'The Cryopheonix'),
('Akali', 'Assassin', 'The rogue assassin'),
('Bard', 'Support', 'The wandering caretaker'),
('Evelynn', 'Assassin', 'Agony\'s embrace'),
('Irelia', 'Fighter', 'The blade dancer'),
('Jhin', 'Marksman', 'The virtuoso'),
('Maokai', 'Tank', 'The twisted treant');

insert into champions_stats
(name, health, armour, magic_resist, adaptive_damage)
values
('Azir', 100, 20, 30, 40),
('Anivia', 120, 15, 25, 40),
('Akali', 110, 17, 35, 45),
('Bard', 99, 20, 22, 40),
('Evelynn', 8, 20, 20, 50),
('Irelia', 120, 25, 25, 45),
('Jhin', 75, 15, 22, 55),
('Maokai', 130, 45, 45, 20);
