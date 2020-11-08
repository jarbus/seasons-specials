#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;

use rocket_contrib::serve::{StaticFiles};

extern crate db;

extern crate lib;
use lib::product::{ProductCategory, Product};
use lib::location::{Location, City, Csa};

// Binary Crate imports
pub mod routes;
pub use crate::routes::TempState;

pub mod db_interface;
pub use crate::db_interface::DataDbConn;

fn main() {
    let data = TempState {
        csas: vec![
            Csa::new(
                "Denison Farm",
                "denison_farm",
                Location::new(
                    City::new(
                        "New York",
                        "new_york"
                    ),
                    None
                )
            ).add_product(Product::new(
                "cheese",
                ProductCategory::Dairy
            ))
        ]
    };
    
    rocket::ignite()
        .manage(data)
        .attach(DataDbConn::fairing())
        .mount("/", StaticFiles::from(concat!(env!("CARGO_MANIFEST_DIR"), "/static")))
        .mount("/", routes![routes::csa])
        .launch();
}
