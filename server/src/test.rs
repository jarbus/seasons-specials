 let mut data = Vec::new();
    for i in 0..1000{
        data.push(
            Csa::new( "Farm1","farm1",
                Location::new(
                    State::new( "City1", "city1"),
                            None, [random(),random()])
            ).add_product(Product::new(
                "cheese", ProductCategory::Dairy))
        )
    }
    let point: [f32; 2] = [1.0,1.0];
    let mut count: i16 = 0;
    for i in 0..1000{
        if close_enough(point[0],point[1],
                     data[i].get_location().get_coords()[0],
                     data[i].get_location().get_coords()[1], 0.5){

            count = count + 1;
        }
    }
