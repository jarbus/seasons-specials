use rocket_contrib::databases::diesel;
use lib::product::Product;

use db::schema::{
    csa::dsl::*,
    region::dsl::*,
    produce::dsl::*,
    production::dsl::*,
    fish::dsl::*
};

#[database("postgres_db")]
pub struct DataDbConn(diesel::PgConnection);

// pub fn get_csa_foods(conn: &diesel::PgConnection, id: &str) -> Result<Vec<Product>> {
//     let results = csa.filter("")
// }
