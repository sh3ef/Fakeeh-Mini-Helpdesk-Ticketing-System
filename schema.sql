CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(20) DEFAULT 'Staff' NOT NULL
);

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Open' NOT NULL,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE replies (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    ticket_id INTEGER REFERENCES tickets(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (email, password, name, role) VALUES
('admin@fakeeh.edu.sa', '$2b$12$rI84TuGEv.UlgrPUoqOryO36zMFgcGCys6qime8ONnrPZvqYC.n5e', 'Admin User', 'Admin'),
('user1@fakeeh.edu.sa', '$2b$12$Uz5LGZx1APm9UcBrRFJ5uejI55hLf8bffjiWahYTl0FDHJsien5TG', 'Saleh Abdullah', 'Staff'),
('user2@fakeeh.edu.sa', '$2b$12$Uz5LGZx1APm9UcBrRFJ5uejI55hLf8bffjiWahYTl0FDHJsien5TG', 'Fatima Ali', 'Staff'),
('user3@fakeeh.edu.sa', '$2b$12$Uz5LGZx1APm9UcBrRFJ5uejI55hLf8bffjiWahYTl0FDHJsien5TG', 'Khalid Mohammed', 'Staff'),
('user4@fakeeh.edu.sa', '$2b$12$Uz5LGZx1APm9UcBrRFJ5uejI55hLf8bffjiWahYTl0FDHJsien5TG', 'Noura Saad', 'Staff'),
('user5@fakeeh.edu.sa', '$2b$12$Uz5LGZx1APm9UcBrRFJ5uejI55hLf8bffjiWahYTl0FDHJsien5TG', 'Yasser Ahmed', 'Staff');

INSERT INTO tickets (title, description, user_id) VALUES
('Printer Not Working', 'The printer on the 2nd floor is out of ink.', 2),
('Slow Computer', 'My computer has become very slow and needs a check-up.', 3),
('Network Issues', 'The internet connection in my office keeps dropping.', 4),
('Software Request', 'I need to install Adobe Photoshop on my machine.', 5),
('Login Problem', 'I cannot log in to the HR system.', 6);
