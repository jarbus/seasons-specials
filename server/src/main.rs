#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use] extern crate rocket;

extern crate strum;
#[macro_use] extern crate strum_macros;

use rocket_contrib::serve::{StaticFiles};

// Binary Crate imports
pub mod product;
pub use crate::product::{ProductCategory, Product};

pub mod location;
pub use crate::location::{Location, City, Csa};

pub mod routes; // Imports routes
pub use crate::routes::TempState;

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
        .mount("/", StaticFiles::from(concat!(env!("CARGO_MANIFEST_DIR"), "/static")))
        .mount("/", routes![routes::csa])
        .launch();
}
