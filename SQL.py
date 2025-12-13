# main.py yoki models.py faylida
create_table_query = """
CREATE TABLE teacher (
    id SERIAL PRIMARY KEY,
    ismi VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age INTEGER CHECK (age > 0),
    tugilgan_kuni DATE,
    tel VARCHAR(20),
    adres TEXT
);
"""

insert_data_query = """
INSERT INTO teacher(ismi, surname, email, age, tugilgan_kuni, tel, adres)
VALUES
('user', 'userov', 'userov@gmail.com', 20, '1990-01-01', '998901234567', 'Toshkent');
"""

# ... keyin bu o'zgaruvchilarni (queries) bazaga ulanish orqali yuborasiz.