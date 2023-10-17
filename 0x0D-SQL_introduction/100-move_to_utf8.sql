-- Change the character set and collation for the entire 'hbtn_0c_0' database to UTF-8
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation for the 'first_table' to UTF-8
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
