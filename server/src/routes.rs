use rocket::State;

use seasons_lib::location::Csa;

pub struct TempState {
    pub csas: Vec<Csa>,
}

#[get("/data/csa/<id>")]
pub fn csa(id: String, state: State<TempState>) -> String {
    let produce = state.csas
        .iter()
        .filter(|csa| csa.uri_eq(&id))
        .nth(0);

    match produce {
        Some(c) => {
            let produce_fmt = c
                .get_products()
                .iter()
                .map(|product| format!("{}: {}", product.get_name(), product.get_category()))
                .collect::<Vec<String>>()
                .join("\n");
            format!("Name of CSA: {}\n{}", id, produce_fmt)
        },
        None => String::from("Error: CSA not found.")
    }
}
