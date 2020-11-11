
#[derive(Queryable)]
pub struct CsaProduction {
    pub produce_name: String,
    pub category: i32,
    pub season: i32
}

#[derive(Queryable)]
pub struct Csa {
    pub id: i32,
    pub csa_name: String,
    pub lat: Option<f64>,
    pub lon: Option<f64>,
    pub address: Option<String>,
    pub state_abbrev: Option<String>
}

#[derive(Queryable)]
pub struct Region {
    pub region_name: String,
    pub state_abbrev: String
}

#[derive(Queryable)]
pub struct Produce {
    pub produce_name: String,
    pub category: i32,
}

#[derive(Queryable)]
pub struct Production {
    pub csa_id: i32,
    pub produce_name: String,
    pub season: i32
}

#[derive(Queryable)]
pub struct Fish {
    pub species: String,
    pub region_name: String,
    pub january: bool,
    pub february: bool,
    pub march: bool,
    pub april: bool,
    pub may: bool,
    pub june: bool,
    pub july: bool,
    pub august: bool,
    pub septebmer: bool,
    pub october: bool,
    pub november: bool,
    pub december: bool
}
