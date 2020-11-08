#[derive(EnumString, Display, EnumIter)]
#[strum(serialize_all = "lowercase")]
pub enum ProductCategory {
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
    Seafood,
}

pub struct Product {
    name: String,
    category: ProductCategory,
}


// pub implied
impl Product {
    pub fn new(name: &str, category: ProductCategory) -> Product {
        Product {
            name: name.to_string(),
            category
        }
    }

    pub fn get_name(&self) -> &str {
        &self.name
    }

    pub fn get_category(&self) -> &ProductCategory {
        &self.category
    }
}
