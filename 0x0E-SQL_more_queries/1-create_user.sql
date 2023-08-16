-- creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGE ON *.* TO 'user_0d_1'@'localhost'
