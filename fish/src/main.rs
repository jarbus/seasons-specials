use csv::Reader;
use serde::Deserialize;
use std::io;
use std::collections::HashSet;
use std::path::Path;

#[derive(Clone, Debug, Deserialize)]
struct LifeExpectancy {
    #[serde(rename = "location")]
    country: String,
    life_expectancy: Option<f32>,
}

fn main() -> io::Result<()> {
	println!("1");
    let mut reader = Reader::from_path(Path::new("./All_Regions.csv"))?;
	println!("2");
    let mut filter = HashSet::new();
    let mut count = 0;

    for record in reader.deserialize() {
        let record: LifeExpectancy = record?;
        if !filter.contains(&record.country) {
            println!("{:?}", record);
            filter.insert(record.country);
            count += 1;
        }
    }

    println!("{} countries", count);
    Ok(())
}