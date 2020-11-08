#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use] extern crate rocket;

use rand::prelude::*;

use rocket_contrib::serve::{StaticFiles};

extern crate lib;
use lib::product::{ProductCategory, Product};
use lib::location::{Location, State, Csa};
use lib::utils::{close_enough};

// Binary Crate imports
pub mod routes;
pub use crate::routes::TempState;

fn main() {
    //let data = TempState {
    //    csas: vec![
    //        Csa::new( "Farm1","farm1",
    //            Location::new(
    //                State::new( "City1", "city1"),
    //                        None, [10.4,13.2])
    //        ).add_product(Product::new(
    //            "cheese", ProductCategory::Dairy))
    //    ]
    //};
    let mut data = Vec::new();
    for i in 0..1000{
        data.push(
            Csa::new( "Farm1","farm1",
                Location::new(
                    State::new( "City1", "city1"),
                            None, [random(),random()])
            ).add_product(Product::new(
                "cheese", ProductCategory::Dairy))
        )
    }
    let point: [f32; 2] = [1.0,1.0];
    let mut count: i16 = 0;
    for i in 0..1000{
        if close_enough(point[0],point[1],
                     data[i].get_location().get_coords()[0],
                     data[i].get_location().get_coords()[1], 0.5){

            count = count + 1;
        }
    }
}


//rocket::ignite()
//    .manage(data)
//    .mount("/", StaticFiles::from(concat!(env!  ("CARGO_MANIFEST_DIR"), "/static")))
//    .mount("/", routes![routes::csa])
