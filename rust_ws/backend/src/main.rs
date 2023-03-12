mod types;

use crate::types::{Vehicle, Vehicles};
use actix_files::Files;
use actix_web::http::StatusCode;
use actix_web::web::Json;
use actix_web::{delete, get, post, web, App, HttpServer, Responder};
use std::sync::{Arc, RwLock};

/// Updates vehicle status
#[post("/vehicle")]
async fn post_vehicle(
    data: web::Data<Arc<RwLock<Vehicles>>>,
    vehicle: web::Json<Vehicle>,
) -> impl Responder {
    let vehicles = data.into_inner();
    let vehicle = vehicle.0;

    let mut lk = vehicles.write().unwrap();

    println!("Updating {}", vehicle.vid);

    let res = lk.vehicle.iter_mut().find(|v| v.vid == vehicle.vid);

    match res {
        // New vehicle is connected
        None => {
            lk.vehicle.push(vehicle.clone());
            (Json(vehicle), StatusCode::CREATED)
        }
        // Update old vehicle
        Some(v) => {
            *v = vehicle;
            (Json(v.clone()), StatusCode::ACCEPTED)
        }
    }
}

/// Removes a vehicle
#[delete("/vehicle")]
async fn delete_vehicle(
    data: web::Data<Arc<RwLock<Vehicles>>>,
    vehicle: web::Json<Vehicle>,
) -> impl Responder {
    let vehicles = data.into_inner();
    let vehicle = vehicle.0;

    let mut lk = vehicles.write().unwrap();

    println!("Attempting to remove: {}", vehicle.vid);

    let pos = lk.vehicle.iter().position(|v| v.vid == vehicle.vid);

    if let Some(idx) = pos {
        lk.vehicle.remove(idx);
        ("Removed", StatusCode::OK)
    } else {
        ("No such car exists", StatusCode::NOT_FOUND)
    }
}

/// Returns all vehicles
#[get("/vehicles")]
async fn get_vehicles(data: web::Data<Arc<RwLock<Vehicles>>>) -> impl Responder {
    println!("hit /vehicles");
    let vehicles = data.into_inner();

    let vehicles = vehicles.write().unwrap().vehicle.clone();

    Json(vehicles)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let state = Arc::new(RwLock::new(Vehicles::default()));

    println!("Backend booted...");

    HttpServer::new(move || {
        //We don't need no security 😎
        let cors = actix_cors::Cors::permissive();

        App::new()
            .wrap(cors)
            .app_data(web::Data::new(state.clone()))
            .service(post_vehicle)
            .service(get_vehicles)
            .service(delete_vehicle)
            .service(Files::new("/", "/").index_file("index.html"))
    })
    .bind(("0.0.0.0", 80))?
    .run()
    .await
}
