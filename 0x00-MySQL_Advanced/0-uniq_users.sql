--Create users table
--With id, email and name
CREATE TABLE IF NOT EXISTS `users` (
	PRIMARY KEY(`id`),
	`id` INT	NOT NULL AUTO_INCREMENT,
	`email` VARCHAR(255)	NOT NULL UNIQUE,
	`name` VARCHAR(255)
);
