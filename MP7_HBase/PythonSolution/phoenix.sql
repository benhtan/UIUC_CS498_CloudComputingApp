DROP VIEW IF EXISTS "powers";
CREATE VIEW "powers" ( pk VARCHAR PRIMARY KEY, "professional"."name" VARCHAR,"personal"."power" VARCHAR, "personal"."hero" VARCHAR );
SELECT *
-- FROM "powers"
FROM "powers" AS p
-- INNER JOIN powers as p1
-- ON p.power = p1.power
;
-- WHERE p1."hero" = 'yes' AND p2."hero" = 'yes';