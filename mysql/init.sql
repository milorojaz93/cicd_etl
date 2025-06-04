-- Crear tabla clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

-- Crear tabla ventas
CREATE TABLE ventas (
    id INT PRIMARY KEY,
    cliente_id INT,
    producto VARCHAR(100),
    fecha DATE,
    monto DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Insertar datos en clientes
INSERT INTO clientes (id, nombre, apellido) VALUES
(1, 'Juan', 'Pérez'),
(2, 'Ana', 'Gómez'),
(3, 'Luis', 'Martínez'),
(4, 'Carla', 'Rodríguez'),
(5, 'Pedro', 'López');

-- Insertar datos en ventas (fechas recientes)
INSERT INTO ventas (id, cliente_id, producto, fecha, monto) VALUES
(1, 1, 'Laptop',       CURDATE() - INTERVAL 30 DAY, 1200.00),
(2, 2, 'Smartphone',   CURDATE() - INTERVAL 15 DAY, 800.00),
(3, 1, 'Teclado',      CURDATE() - INTERVAL 10 DAY, 50.00),
(4, 3, 'Monitor',      CURDATE() - INTERVAL 45 DAY, 300.00),
(5, 4, 'Tablet',       CURDATE() - INTERVAL 5 DAY, 400.00);
