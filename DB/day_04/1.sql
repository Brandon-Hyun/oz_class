CREATE TABLE guardian(
    id_guardian INTEGER PRIMARY KEY AUTO_INCREMENT,
    name_guardian TEXT,
    phone_number VARCHAR(45),
    email TEXT,
    address TEXT
);

CREATE TABLE pet (
    id_pet INTEGER PRIMARY KEY AUTO_INCREMENT,
    pet_name VARCHAR(45),
    age_pet INTEGER,
    animal_type TEXT,
    species TEXT,
    FOREIGN KEY (id_guardian) references guardian(id_guardian)
);

CREATE TABLE order (
    id_order PRIMARY KEY AUTO_INCREMENT,
    quantity INTEGER
);

CREATE TABLE item (
    id_item INTEGER PRIMARY KEY AUTO_INCREMENT,
    name_item VARCHAR(45),
    price_item INTEGER,
    stock_item INTEGER
);

CREATE TABLE order_item (
    id_order_item PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (id_item) references item(id_item),
    FOREIGN KEY (id_order) references order(id_order),
);

CREATE TABLE vet (
    id_vet PRIMARY KEY AUTO_INCREMENT,
    name_vet TEXT,
    id_license TEXT,
    phone_number TEXT
);

CREATE TABLE medical_record (
    id_medical_record PRIMARY KEY AUTO_INCREMENT,
    date_visit date,
    note TEXT,
    FOREIGN KEY (id_pet) references pet(id_pet),
    FOREIGN KEY (id_vet) references vet(id_vet)
);