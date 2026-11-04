USE bd_mi_cuentika;

-- =========================================
-- DATOS DE PRUEBA PARA MI CUENTIKA
-- =========================================

-- 1. Insertar categorías si todavía no existen
INSERT IGNORE INTO TBL_CATEGORIA (cat_nombre)
VALUES
('Bebidas'),
('Lácteos'),
('Golosinas'),
('Limpieza'),
('Granos básicos');


-- 2. Insertar productos solamente si no existen

-- Producto 1: Coca-Cola
INSERT INTO TBL_PRODUCTO
(prod_nombre, prod_unidad, prod_precio_compra, prod_precio_venta,
 prod_stock, prod_stock_minimo, prod_activo, cat_id)
SELECT 'Coca-Cola', 'Unidad', 35.00, 45.00, 24, 5, TRUE, cat_id
FROM TBL_CATEGORIA
WHERE cat_nombre = 'Bebidas'
AND NOT EXISTS (
    SELECT 1 FROM TBL_PRODUCTO
    WHERE prod_nombre = 'Coca-Cola'
);

-- Producto 2: Leche
INSERT INTO TBL_PRODUCTO
(prod_nombre, prod_unidad, prod_precio_compra, prod_precio_venta,
 prod_stock, prod_stock_minimo, prod_activo, cat_id)
SELECT 'Leche', 'Litro', 40.00, 50.00, 12, 3, TRUE, cat_id
FROM TBL_CATEGORIA
WHERE cat_nombre = 'Lácteos'
AND NOT EXISTS (
    SELECT 1 FROM TBL_PRODUCTO
    WHERE prod_nombre = 'Leche'
);

-- Producto 3: Galletas
INSERT INTO TBL_PRODUCTO
(prod_nombre, prod_unidad, prod_precio_compra, prod_precio_venta,
 prod_stock, prod_stock_minimo, prod_activo, cat_id)
SELECT 'Galletas', 'Paquete', 12.00, 15.00, 30, 5, TRUE, cat_id
FROM TBL_CATEGORIA
WHERE cat_nombre = 'Golosinas'
AND NOT EXISTS (
    SELECT 1 FROM TBL_PRODUCTO
    WHERE prod_nombre = 'Galletas'
);

-- Producto 4: Detergente
INSERT INTO TBL_PRODUCTO
(prod_nombre, prod_unidad, prod_precio_compra, prod_precio_venta,
 prod_stock, prod_stock_minimo, prod_activo, cat_id)
SELECT 'Detergente', 'Unidad', 30.00, 40.00, 15, 3, TRUE, cat_id
FROM TBL_CATEGORIA
WHERE cat_nombre = 'Limpieza'
AND NOT EXISTS (
    SELECT 1 FROM TBL_PRODUCTO
    WHERE prod_nombre = 'Detergente'
);

-- Producto 5: Arroz
INSERT INTO TBL_PRODUCTO
(prod_nombre, prod_unidad, prod_precio_compra, prod_precio_venta,
 prod_stock, prod_stock_minimo, prod_activo, cat_id)
SELECT 'Arroz', 'Libra', 18.00, 22.00, 40, 10, TRUE, cat_id
FROM TBL_CATEGORIA
WHERE cat_nombre = 'Granos básicos'
AND NOT EXISTS (
    SELECT 1 FROM TBL_PRODUCTO
    WHERE prod_nombre = 'Arroz'
);

-- Producto 6: Jugo de naranja
INSERT INTO TBL_PRODUCTO
(prod_nombre, prod_unidad, prod_precio_compra, prod_precio_venta,
 prod_stock, prod_stock_minimo, prod_activo, cat_id)
SELECT 'Jugo de naranja', 'Unidad', 15.00, 20.00, 10, 2, TRUE, cat_id
FROM TBL_CATEGORIA
WHERE cat_nombre = 'Bebidas'
AND NOT EXISTS (
    SELECT 1 FROM TBL_PRODUCTO
    WHERE prod_nombre = 'Jugo de naranja'
);

-- Producto 7: Agua natural
INSERT INTO TBL_PRODUCTO
(prod_nombre, prod_unidad, prod_precio_compra, prod_precio_venta,
 prod_stock, prod_stock_minimo, prod_activo, cat_id)
SELECT 'Agua natural', 'Unidad', 10.00, 15.00, 20, 5, TRUE, cat_id
FROM TBL_CATEGORIA
WHERE cat_nombre = 'Bebidas'
AND NOT EXISTS (
    SELECT 1 FROM TBL_PRODUCTO
    WHERE prod_nombre = 'Agua natural'
);


-- 3. Consultar los productos registrados
SELECT
    p.prod_id,
    p.prod_nombre,
    p.prod_unidad,
    p.prod_precio_compra,
    p.prod_precio_venta,
    p.prod_stock,
    p.prod_stock_minimo,
    c.cat_nombre
FROM TBL_PRODUCTO p
INNER JOIN TBL_CATEGORIA c
    ON p.cat_id = c.cat_id
ORDER BY p.prod_id ASC;