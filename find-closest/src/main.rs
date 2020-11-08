
const CATEGORIES: [[f32;2]; 4] =[
    [1.0,1.0],
    [2.0,2.0],
    [3.0,3.0],
    [4.0,4.0]];








fn main() {
    const POINT: [f32; 2] = [2.5,2.5];
    let threshold: f32 = 1.0;
    for i in 0..CATEGORIES.len(){
        println!("{}",close_enough(
            CATEGORIES[i][0],
            CATEGORIES[i][1],
            POINT[0],
            POINT[1],threshold));
    }
}
