#[macro_use]
extern crate diesel;

use std::convert::TryFrom;

use diesel::prelude::*; // Glob import DSL methods
use diesel::dsl::*; // any()
use diesel::result;

extern crate seasons_lib;
use seasons_lib::product::{Product, ProductCategory};

pub mod schema;
pub mod models;
use crate::models::CsaProduction;

pub fn get_csa_foods(conn: &diesel::PgConnection, query_id: i32) -> Result<Vec<Product>, result::Error> {
    use schema::produce::dsl::*;
    use schema::production;
    
    let query = produce.inner_join(
        production::table.on(
            production::csa_id.eq(query_id).and(produce_name.eq(production::produce_name))
        )
    ).select((produce_name, category, production::season));

    let result = query.load::<CsaProduction>(conn)?.iter()
        .map(|p| {
            let category = ProductCategory::try_from(p.season);
            Product::new(&p.produce_name, )
        })
        .collect::<Vec<Product>>();

    Ok(result)
}
