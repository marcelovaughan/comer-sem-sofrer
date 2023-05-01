CREATE TABLE `nutricao`.`AGtaco3` ( `id` INT(3) NOT NULL AUTO_INCREMENT ,  
                              `categoria` VARCHAR(100) NOT NULL,
                              `numeroAlimento` VARCHAR(10) NOT NULL, 
                              `descricaoAlimento` VARCHAR(255) NOT NULL, 
                              `saturados` VARCHAR(20) NOT NULL, 
                              `monoinsaturados` VARCHAR(20) NOT NULL, 
                              `poliinsaturados` VARCHAR(20) NOT NULL, 
                              `12_0` VARCHAR(20) NOT NULL, 
                              `14_0` VARCHAR(20) NOT NULL,
                              `16_0` VARCHAR(20) NOT NULL,
                              `18_0` VARCHAR(20) NOT NULL, 
                              `20_0` VARCHAR(20) NOT NULL, 
                              `22_0` VARCHAR(20) NOT NULL, 
                              `24_0` VARCHAR(20) NOT NULL, 
                              `14_1` VARCHAR(20) NOT NULL, 
                              `16_1` VARCHAR(20) NOT NULL, 
                              `18_1` VARCHAR(20) NOT NULL, 
                              `20_1` VARCHAR(20) NOT NULL, 
                              `18_2N_6` VARCHAR(20) NOT NULL, 
                              `18_3N_3` VARCHAR(20) NOT NULL, 
                              `20_4` VARCHAR(20) NOT NULL, 
                              `20_5` VARCHAR(20) NOT NULL, 
                              `22_5` VARCHAR(20) NOT NULL, 
                              `22_6` VARCHAR(20) NOT NULL, 
                              `18_1t` VARCHAR(20) NOT NULL, 
                              `18_2t` VARCHAR(20) NOT NULL,
                              `created_at` VARCHAR(30) NOT NULL,
                              `updated_at` VARCHAR(30) NOT NULL,
                              PRIMARY KEY (`id`)) ENGINE = InnoDB;