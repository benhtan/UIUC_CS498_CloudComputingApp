DROP VIEW "powers";
CREATE VIEW "powers" ( pk VARCHAR PRIMARY KEY, "personal".val VARCHAR, "professional".val VARCHAR, "custom".val VARCHAR);
SELECT p.name, p.power
-- FROM "powers"
FROM "powers" AS p
-- INNER JOIN powers as p1
-- ON p.power = p1.power
;
-- WHERE p1."hero" = 'yes' AND p2."hero" = 'yes';