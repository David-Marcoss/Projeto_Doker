
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

CREATE TABLE IF NOT EXISTS `mydb`.`enderecos` (
  `idenderecos` INT NOT NULL,
  `cep` VARCHAR(45) NOT NULL,
  `rua` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(45) NOT NULL,
  `estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idenderecos`),
  UNIQUE INDEX `cep_UNIQUE` (`cep` ASC) VISIBLE)
ENGINE = InnoDB;
