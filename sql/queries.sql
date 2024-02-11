select * from "products";
select * from "products" where id = $1;
select * from "product_information" where "product_id" = $1;

INSERT INTO "products" (name, description, price, created) VALUES ($1, $2, $3, $4)
update "products" set name = $2, description = $3, price = $4 where id = $1
delete from "products" where "id" = $1

INSERT INTO "product_information" (product_id, sku, inventory_levels) VALUES ($1, $2, $3)
UPDATE "product_information" SET sku = $2, inventory_levels = $3 WHERE id = $1
delete from "product_information" where "id" = $1