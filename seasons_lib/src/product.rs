use std::convert::TryFrom;
use strum::IntoEnumIterator;

#[derive(EnumString, Display, EnumIter)]
#[strum(serialize_all = "lowercase")]
pub enum ProductCategory {
    Vegetable,
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
}

impl TryFrom<usize> for ProductCategory {
    type Error = String;

    fn try_from(v: usize) -> Result<Self, Self::Error> {
        use ProductCategory::*;
        match v {
            0 => Ok(Vegetable),
            1 => Ok(Fruit),
            2 => Ok(Meat),
            3 => Ok(Seed),
            4 => Ok(Grain),
            5 => Ok(Processed),
            6 => Ok(Dairy),
            7 => Ok(Gourd),
            8 => Ok(Flower),
            9 => Ok(Herb),
            10 => Ok(Fiber),
            11 => Ok(Sprout),
            12 => Ok(Specialty),
            _ => Err("Invalid category".to_string())
        }
    }
}

pub struct Product {
    name: String,
    category: ProductCategory,
}

pub struct Fish {
    name: String,
    region: String,
    month_availability: [i8;12]
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
