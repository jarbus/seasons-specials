// pub mod product;
pub use crate::product::Product;

pub struct Location {
    city: City,
    address: Option<String>
}

impl Location {
    pub fn new(city: City, address: Option<&str>) -> Location {
        // Make a new copy of the properties
        Location {
            city,
            address: address.map_or(None, |a| Some(a.to_string()))
        }
    }
}

pub struct City {
    name: String,
    uri: String
}

impl City {
    pub fn new(name: &str, uri: &str) -> City {
        City {
            name: String::from(name),
            uri: String::from(uri)
        }
    }
}

// Communicated Supported Agriculture
pub struct Csa {
    name: String,
    uri: String,
    produces: Vec<Product>,
    location: Location,
}

impl Csa {
    pub fn new(name: &str, uri: &str, location: Location) -> Csa {
        Csa {
            name: String::from(name),
            uri: String::from(uri),
            produces: Vec::new(),
            location,
        }
    }

    pub fn add_product(mut self, product: Product) -> Csa {
        self.produces.push(product);
        self
    }

    pub fn uri_eq(&self, uri: &str) -> bool {
        self.uri.eq(uri)
    }

    pub fn get_products(&self) -> &Vec<Product> {
        &self.produces
    }
}
