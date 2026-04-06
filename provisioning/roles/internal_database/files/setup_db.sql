CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password_hash VARCHAR(100),
    notes VARCHAR(255)
);

-- Flag 6 is hidden in this table
INSERT INTO users (username, password_hash, notes) VALUES 
('admin_backup', 'RkxBRzZre3NxbF9kdW1wX3N1Y2Nlc3N9', 'Legacy backup account. Use this b64 string as a hint for the ATM controller later.'),
('windows', '$2b$05$6SmxCW4Qt/MA8vqmEWlRXuk8k4rJHW4FJIY9v.hWAzlF1ILYDHL0K', 'Internal App Server User'); 

-- Note: The hash above is 'IronVault2026!' in bcrypt format for the player to crack.
