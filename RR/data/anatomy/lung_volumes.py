# Lung Volumes (in mL)
lung_volumes = {
    "tidal_volume": 500,
    "inspiratory_reserve_volume": 2500,  # can range 2500–3500
    "expiratory_reserve_volume": 1000,
    "residual_volume": 1000,
    "anatomic_dead_space": 150
}

# Derived Capacities
def vital_capacity():
    return (lung_volumes["tidal_volume"] +
            lung_volumes["inspiratory_reserve_volume"] +
            lung_volumes["expiratory_reserve_volume"])  # VC

def total_lung_capacity():
    return vital_capacity() + lung_volumes["residual_volume"]  # TLC

def inspiratory_capacity():
    return lung_volumes["tidal_volume"] + lung_volumes["inspiratory_reserve_volume"]

def functional_residual_capacity():
    return lung_volumes["expiratory_reserve_volume"] + lung_volumes["residual_volume"]

# Alveolar Ventilation (per breath and per minute)
def alveolar_air_per_breath():
    return lung_volumes["tidal_volume"] - lung_volumes["anatomic_dead_space"]

def alveolar_ventilation_per_minute(breaths_per_minute=12):
    return alveolar_air_per_breath() * breaths_per_minute