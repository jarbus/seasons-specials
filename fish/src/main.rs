static PATH: &str = "../../seafood/Alaska";

use csv::Reader;
use serde::Deserialize;
use std::error::Error;
use std::io;
use std::process;

fn example() -> Result<(), Box<dyn Error>> {
    // Build the CSV reader and iterate over each record.
    let mut rdr = csv::Reader::from_reader("../../seafood/Alaska");
    for result in rdr.records() {
        // The iterator yields Result<StringRecord, Error>, so we check the
        // error here.
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() -> io::Reader<()> {
	Ok(())
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}