use serde::{Deserialize, Serialize};

#[derive(Clone, Serialize, Deserialize)]
pub struct Vehicle {
    pub vid: String,
    pub charging_status: f32,
    pub model: String,
}

#[derive(Clone, Serialize, Deserialize)]
pub struct Vehicles {
    pub vehicle: Vec<Vehicle>,
}

impl Default for Vehicles {
    fn default() -> Self {
        Self {
            vehicle: Vec::new(),
        }
    }
}
