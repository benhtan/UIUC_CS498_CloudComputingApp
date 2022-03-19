DROP TABLE powers;
CREATE VIEW "powers" ( pk VARCHAR PRIMARY KEY, "personal".val VARCHAR, "professional".val VARCHAR, "custom".val VARCHAR);
SELECT * FROM powers;
-- WHERE p1."hero" = 'yes' AND p2."hero" = 'yes';