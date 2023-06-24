CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`enderecos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`enderecos` (
  `idenderecos` INT NOT NULL AUTO_INCREMENT,
  `cep` VARCHAR(45) NOT NULL,
  `rua` VARCHAR(45) NULL,
  `bairro` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  PRIMARY KEY (`idenderecos`),
  UNIQUE INDEX `cep_UNIQUE` (`cep` ASC) VISIBLE)
ENGINE = InnoDB;
