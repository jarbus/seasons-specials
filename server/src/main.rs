#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use] extern crate rocket;

extern crate strum;
#[macro_use] extern crate strum_macros;

use std::io;
use std::path::Path;

use rocket::State;
use rocket::response::NamedFile;
use rocket_contrib::serve::{StaticFiles, Options};

#[derive(EnumString, Display, EnumIter)]
#[strum(serialize_all = "lowercase")]
enum ProductCategory {
    Vegtable,
    Fruit,
    Meat,
    Seed,
    Grain,
    Processed,
    Dairy,
    Gourd,
    Flower,
    Herb,
    Fiber,
    Sprout,
    Specialty,
    Seafood
}

struct Product {
    name: String,
    category: ProductCategory
}

struct Location {
    city: City,
    address: Option<String>
}

struct City {
    name: String,
    uri: String
}

// Communicated Supported Agriculture
struct Csa {
    name: String,
    uri: String,
    produces: Vec<Product>,
    location: Location,
}

struct TempState {
    csas: Vec<Csa>,
}

#[get("/", format = "text/html")]
fn homepage() -> Option<NamedFile> {
    NamedFile::open(Path::new("static/index.html")).ok()
}

// #[get("/", format = "text/plain", rank = 2)]
// fn homepage_txt() -> &'static str {
//     "Welcome to our app!"
// }

#[get("/csa/<id>", rank = 0)]
fn city(id: String, state: State<TempState>) -> String {
    let produce = state.csas
        .iter()
        .filter(|csa| csa.uri.eq(&id))
        .map(|csa| &csa.produces)
        .nth(0);

    match produce {
        Some(lst) => {
            let produce_fmt = lst
                .iter()
                .map(|product| format!("{}: {}", product.name, product.category))
                .collect::<Vec<String>>()
                .join("\n");
            format!("Name of CSA: {}\n{}", id, produce_fmt)
        },
        None => String::from("Error: CSA not found.")
    }
}

fn main() {
    let data = TempState {
        csas: vec![
            Csa {
                uri: String::from("denison_farm"),
                name: String::from("Denison Farm"),
                produces: vec![
                    Product {
                        name: String::from("cheese"),
                        category: ProductCategory::Dairy,
                    }
                ],
                location: Location {
                    city: City {
                        uri: String::from("new_york"),
                        name: String::from("New York")
                    },
                    address: None
                    
                }
            }
        ]
    };
    
    rocket::ignite()
        .manage(data)
        .mount("/public", StaticFiles::from("/static"))
        .mount("/", routes![homepage])
        .mount("/data", routes![city])
        .launch();
}
