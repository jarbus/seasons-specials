#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}

extern crate strum;
#[macro_use] extern crate strum_macros;

pub mod location;
pub mod product;
pub mod utils;
