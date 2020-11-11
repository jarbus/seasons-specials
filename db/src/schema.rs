table! {
    csa (id) {
        id -> Int4,
        csa_name -> Varchar,
        lat -> Nullable<Float8>,
        lon -> Nullable<Float8>,
        address -> Nullable<Text>,
        state_abbrev -> Nullable<Varchar>,
    }
}

table! {
    fish (species) {
        species -> Varchar,
        region_name -> Varchar,
        january -> Bool,
        february -> Bool,
        march -> Bool,
        april -> Bool,
        may -> Bool,
        june -> Bool,
        july -> Bool,
        august -> Bool,
        september -> Bool,
        october -> Bool,
        november -> Bool,
        december -> Bool,
    }
}

table! {
    produce (produce_name) {
        produce_name -> Varchar,
        category -> Int4,
    }
}

table! {
    production (csa_id, produce_name, season) {
        csa_id -> Int4,
        produce_name -> Varchar,
        season -> Int4,
    }
}

table! {
    region (region_name) {
        region_name -> Varchar,
        state_abbrev -> Varchar,
    }
}

allow_tables_to_appear_in_same_query!(
    csa,
    fish,
    produce,
    production,
    region,
);
