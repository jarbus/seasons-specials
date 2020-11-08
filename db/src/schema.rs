table! {
    csa (id) {
        id -> Int4,
        csaname -> Varchar,
        lat -> Nullable<Float8>,
        lon -> Nullable<Float8>,
        address -> Nullable<Text>,
        stateabbrev -> Nullable<Varchar>,
    }
}

table! {
    fish (species) {
        species -> Varchar,
        regionname -> Varchar,
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
    produce (producename) {
        producename -> Varchar,
        category -> Int4,
    }
}

table! {
    production (csaid, producename, season) {
        csaid -> Int4,
        producename -> Varchar,
        season -> Int4,
    }
}

table! {
    region (regionname) {
        regionname -> Varchar,
        stateabbrev -> Varchar,
    }
}

allow_tables_to_appear_in_same_query!(
    csa,
    fish,
    produce,
    production,
    region,
);
