use std::fs::File;
use std::io::{BufRead,BufReader};
use std::collections::HashMap;

fn add_file_to_map(file_name:&str, map: &mut HashMap<String,String>){
    let file = File::open(file_name).unwrap();
    let reader = BufReader::new(file);

    for item in reader.lines(){
        let item = item.unwrap().trim_end().to_string();
        map.insert(item,"test".to_string());
    }

}

const CATEGORIES: [&str; 13] = [
        "dairy-eggs",
        "fibers",
        "flowers",
        "fruits",
        "gourds-squash",
        "grains",
        "herbs",
        "meats",
        "nuts-seeds",
        "processed",
        "specialty",
        "sprouts",
        "vegetables",
    ];




fn main() -> std::io::Result<()> {
    let mut food_map: HashMap<String,String> = HashMap::new();
    for file_name in 0..CATEGORIES.len(){
        add_file_to_map(CATEGORIES[file_name],&mut food_map)
    }
    for (key, value) in &food_map{
        println!("{} {}",key, value);
    }
    Ok(())
}
