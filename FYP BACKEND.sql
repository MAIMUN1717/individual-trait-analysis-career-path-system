-- CREATION OF DATABASE
CREATE DATABASE FYP;

-- USE OF DATABASE
USE FYP;



-- Users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    degree VARCHAR(50),
    branch VARCHAR(50),
    year INT,
    college VARCHAR(100)
);

-- Interests (from form + psychometric)
CREATE TABLE user_interests (
    user_id INT,
    domain VARCHAR(100),
    interest_score INT,  -- 0–100
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Questions
CREATE TABLE questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT,
    test_type VARCHAR(50)
);

-- Options mapped to traits
CREATE TABLE question_options (
    option_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT,
    option_text TEXT,
    trait VARCHAR(50),
    trait_weight INT,  -- can be + or -
    FOREIGN KEY (question_id) REFERENCES questions(question_id)
);

-- User answers
CREATE TABLE user_answers (
    user_id INT,
    question_id INT,
    option_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Final user traits
CREATE TABLE user_traits (
    user_id INT,
    trait VARCHAR(50),
    score INT,          -- 0–100
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Roles
CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(100)
);

-- Role requirements
CREATE TABLE role_requirements (
    role_id INT,
    trait VARCHAR(50),
    required_level INT,  -- 0–100
    weight FLOAT,
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

-- Results
CREATE TABLE role_results (
    user_id INT,
    role_id INT,
    fit_score FLOAT,
    interest_score FLOAT,
    final_score FLOAT
);

SHOW TABLES;


INSERT INTO roles (role_name) VALUES
('Backend Developer'),
('Frontend Developer'),
('Data Analyst'),
('Machine Learning Engineer'),
('QA Engineer'),
('DevOps Engineer');


-- Backend Developer = role_id 1 (check with SELECT * FROM roles)

INSERT INTO role_requirements (role_id, trait, required_level, weight) VALUES
(1, 'logical_thinking', 70, 0.30),
(1, 'problem_solving', 75, 0.25),
(1, 'critical_thinking', 65, 0.15),
(1, 'decision_making', 60, 0.15),
(1, 'people_orientation', 40, 0.05),
(1, 'ambiguity_tolerance', 55, 0.10);


INSERT INTO questions (question_text, test_type) VALUES
('When a problem is unclear, what do you do first?', 'logical'),
('How do you react when your solution fails?', 'critical'),
('How do you usually make decisions under pressure?', 'decision');


-- Assume question_id = 1

INSERT INTO question_options (question_id, option_text, trait, trait_weight) VALUES
(1, 'Break the problem and start working', 'logical_thinking', 15),
(1, 'Wait for clearer instructions', 'structure_preference', 10),
(1, 'Ask others immediately', 'people_orientation', 8),
(1, 'Avoid the task', 'ambiguity_tolerance', -10);


INSERT INTO users (degree, branch, year, college)
VALUES ('B.Tech', 'CSE', 3, 'ABC Engineering College');

INSERT INTO user_interests (user_id, domain, interest_score) VALUES
(1, 'Backend Developer', 80),
(1, 'Data Analyst', 60),
(1, 'Machine Learning Engineer', 40);


INSERT INTO user_answers (user_id, question_id, option_id) VALUES
(1, 1, 1),
(1, 2, 3),
(1, 3, 2);

SHOW TABLES;

SELECT * FROM ROLE_RESULTS;

SELECT * FROM USER_ANSWERS;



