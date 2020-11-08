// pub mod product;
pub use crate::product::Product;

pub struct Location {
    state: State,
    address: Option<String>,
    coords: [f32;2]
}

impl Location {
    pub fn new(state: State, address: Option<&str>, coords: [f32;2]) -> Location {
        // Make a new copy of the properties
        Location {
            state,
            address: address.map_or(None, |a| Some(a.to_string())),
            coords
        }
    }
    pub fn get_coords(&self) -> &[f32; 2]{
        return &self.coords;
    }
}

pub struct State {
    name: String,
    uri: String
}

impl State {
    pub fn new(name: &str, uri: &str) -> State {
        State {
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

    pub fn get_location(&self) -> &Location {
        &self.location
    }
}
