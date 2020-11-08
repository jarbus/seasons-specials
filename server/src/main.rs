#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;

use rand::prelude::*;

use rocket_contrib::serve::{StaticFiles};

extern crate db;

extern crate lib;
use lib::product::{ProductCategory, Product};
use lib::location::{Location, State, Csa};
use lib::utils::{close_enough};
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead,BufReader};

// Binary Crate imports
pub mod routes;
pub use crate::routes::TempState;

<<<<<<< HEAD
pub mod db_interface;
pub use crate::db_interface::DataDbConn;
=======
fn add_file_to_map(file_name:&str, map: &mut HashMap<String,String>){
    let file = File::open(file_name).unwrap();
    let reader = BufReader::new(file);

    for item in reader.lines(){
        let item = item.unwrap().trim_end().to_string();
        map.insert(item,file_name[11..].to_string());
    }

}

// Categories of foods
const CATEGORIES: [&str; 13] = [
        "categories/dairy-eggs",
        "categories/fibers",
        "categories/flowers",
        "categories/fruits",
        "categories/gourds-squash",
        "categories/grains",
        "categories/herbs",
        "categories/meats",
        "categories/nuts-seeds",
        "categories/processed",
        "categories/specialty",
        "categories/sprouts",
        "categories/vegetables",
    ];

// We use REGIONS to construct a state -> body of water map
// to be used for finding fish seasonality
const REGIONS: [[&str; 2];23] = [["Alaska", "AK"],
    ["Atlantic", "MA"],
    ["Atlantic", "RI"],
    ["Atlantic", "CT"],
    ["Atlantic", "NY"],
    ["Atlantic", "NJ"],
    ["Atlantic", "DE"],
    ["Atlantic", "MD"],
    ["Atlantic", "VA"],
    ["Atlantic", "NC"],
    ["Atlantic", "SC"],
    ["Atlantic", "GA"],
    ["Atlantic", "FL"],
    ["Pacific", "WA"],
    ["Pacific", "OR"],
    ["Pacific", "CA"],
    ["Great_Lakes", "MN"],
    ["Great_Lakes", "WI"],
    ["Great_Lakes", "MI"],
    ["Great_Lakes", "IL"],
    ["Great_Lakes", "OH"],
    ["Great_Lakes", "PA"],
    ["Great_Lakes", "NY"]];


>>>>>>> 7f38ec5c4bed39eddd784a55dec764502fb2e1f6

fn main() {

    // Instantiate mapping of states to bodies of water
    let mut state_to_water: HashMap<String,String> = HashMap::new();
    for i in 0..REGIONS.len(){
        state_to_water.insert(REGIONS[i][0].to_string(),REGIONS[i][1].to_string());
    }

    // Instantiate mapping of food to category
    let mut food_map: HashMap<String,String> = HashMap::new();
    for file_name in 0..CATEGORIES.len(){
        add_file_to_map(CATEGORIES[file_name],&mut food_map);
    }

    for (key, value) in &food_map{
        println!("{} {}",key, value);
    }
    for (key, value) in &state_to_water{
        println!("{} {}",key, value);
    }


    // Create vector of face data
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
    // Compute distances
    let point: [f32; 2] = [1.0,1.0];
    let mut count: i16 = 0;
    for i in 0..1000{
        if close_enough(point[0],point[1],
                     data[i].get_location().get_coords()[0],
                     data[i].get_location().get_coords()[1], 0.5){

            count = count + 1;
        }
    }

    rocket::ignite()
        .manage(data)
        .attach(DataDbConn::fairing())
        .mount("/", StaticFiles::from(concat!(env!("CARGO_MANIFEST_DIR"), "/static")))
        .mount("/", routes![routes::csa])
}



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
