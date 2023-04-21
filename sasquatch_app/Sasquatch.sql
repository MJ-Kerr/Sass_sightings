-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Sassquatch_sightings
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Sassquatch_sightings` ;

-- -----------------------------------------------------
-- Schema Sassquatch_sightings
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Sassquatch_sightings` DEFAULT CHARACTER SET utf8 ;
USE `Sassquatch_sightings` ;

-- -----------------------------------------------------
-- Table `Sassquatch_sightings`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sassquatch_sightings`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(250) NOT NULL,
  `last_name` VARCHAR(250) NOT NULL,
  `email` VARCHAR(250) NOT NULL,
  `password` VARCHAR(60) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sassquatch_sightings`.`sightings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sassquatch_sightings`.`sightings` (
  `sight_id` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(200) NOT NULL,
  `what_happened` TEXT NOT NULL,
  `sight_date` DATE NOT NULL,
  `how_many` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() on UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`sight_id`),
  INDEX `fk_sightings_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_sightings_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `Sassquatch_sightings`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
