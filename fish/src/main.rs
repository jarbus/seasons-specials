use csv::Reader;
use csv::Error;
// use serde::Deserialize;
// use std::io;
// use std::collections::HashSet;
// use std::path::Path;


fn main() -> Result<(), Error> {
	let mut reader = Reader::from_path("All_Regions.csv")?;
	
    for record in reader.records() {
        let record = record?;
        println!(
            "In {}, {} built the {} model. It is a {}.",
            &record[0],
            &record[1],
            &record[2],
            &record[3]
        );
    }

    Ok(())
}