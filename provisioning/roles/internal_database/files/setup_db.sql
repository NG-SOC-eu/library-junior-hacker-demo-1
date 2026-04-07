CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password_hash VARCHAR(100),
    notes VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS infrastructure_config (
    service_name VARCHAR(50),
    service_value VARCHAR(100)
);

-- Insert the domain hint
INSERT INTO infrastructure_config (service_name, service_value) VALUES 
('internal_domain', 'ironvault.local'),
('domain_controller', '10.10.20.50'),
('active_directory_auth', 'ENABLED');

-- Flag 6 is hidden in this table
INSERT INTO users (username, password_hash, notes) VALUES 
('admin_backup', 'RkxBRzZ7c3FsX2R1bXBfc3VjY2Vzc30=', 'Legacy backup account. Use this b64 string as a hint for the ATM controller later.'),
('windows', '$2b$05$6SmxCW4Qt/MA8vqmEWlRXuk8k4rJHW4FJIY9v.hWAzlF1ILYDHL0K', 'Internal App Server User'); 
