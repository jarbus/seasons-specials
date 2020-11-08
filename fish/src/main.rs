use csv::Reader;
use csv::Error;
use std::fs;
// use serde::Deserialize;
// use std::io;
// use std::collections::HashSet;
// use std::path::Path;

<<<<<<< Updated upstream

fn main() -> Result<(), Error> {

	// let jsn_file = fs::read_to_string("Locations_To_States.json");

	// let json: serde_json::Value = serde_json::from_str(jsn_file);

	let mut reader = Reader::from_path("All_Regions.csv")?;
	
    for record in reader.records() {
        let record = record?;
        println!(
            "{} is from {} and is {} available in july",
            &record[0],
            &record[1],
            &record[9]
        );
    }

    Ok(())
}
=======
fn example() -> Result<(), Box<dyn Error>> {
    // Build the CSV reader and iterate over each record.
    let mut rdr = Reader::from_reader("../../seafood/Alaska");
    for result in rdr.records() {
        // The iterator yields Result<StringRecord, Error>, so we check the
        // error here.
        let record = result?;
        println!("{:?}", record);
    }
    return "Goody"
}

fn main() -> io::Reader<()> {
    f let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
	Ok(());
}
>>>>>>> Stashed changes
