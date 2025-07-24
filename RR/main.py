from data.physio.phy import *
from data.anatomy import *
from unsupervised.density_est import *
from supervised.learning.sgd import *
from supervised.learning.classification import *


physio = Physiology(
    cardiovascular=CardiovascularSystem(
        cardiac_output=CardiacOutput(
            formula="CO = HR × SV",
            typical_values={"Resting": "5 L/min", "Exercise": "30 L/min"},
            regulation={
                "HeartRate": {"Parasympathetic": "↓ HR", "Sympathetic": "↑ HR via adrenal medulla"},
                "StrokeVolume": {"IncreasedFilling": True, "SympatheticStimulation": True}
            },
            measurement={"Method": "Fick Principle", "Formula": "CO = O2 uptake / (A-V O2 difference)"}
        ),
        blood_pressure=BloodPressure(
            MAP_formula="CO × TPR",
            short_term={"Sensor": "Baroreceptors", "Effectors": ["HR", "Vasoconstriction"]},
            intermediate=["Capillary fluid shift", "Vascular stress relaxation", "RAAS"],
            long_term=["Thirst (hypothalamus)", "ADH", "Aldosterone", "ANP"]
        )
    ),
    respiratory=RespiratorySystem(
        airways=["Nasal cavity", "Pharynx", "Larynx", "Trachea", "Bronchi", "Bronchioles", "Alveoli"],
        lung_mechanics=LungMechanics(
            inspiration={
                "Diaphragm": "Contracts and flattens",
                "PressureChange": "↓ intrapulmonary pressure",
                "VolumeChange": "↑ lung volume"
            },
            expiration={
                "Diaphragm": "Relaxes",
                "PressureChange": "↑ intrapulmonary pressure",
                "VolumeChange": "↓ lung volume"
            }
        ),
        volumes={
            "TidalVolume": "500 mL",
            "InspiratoryReserve": "2500–3500 mL",
            "ExpiratoryReserve": "1000 mL",
            "ResidualVolume": "1000 mL",
            "DeadSpace": "150 mL"
        },
        spirometry={
            "Device": "Bell + water tank spirometer",
            "Function": "Measures lung volume via bell displacement"
        },
        gas_exchange={
            "Location": "Alveolar-capillary membrane",
            "O2Direction": "Alveoli → Blood",
            "CO2Direction": "Blood → Alveoli"
        }
    ),
    gas_transport=GasTransport(
        oxygen=OxygenTransport(
            in_plasma="1%",
            as_hemoglobin="99%",
            structure=HemoglobinStructure(subunits="2 alpha, 2 beta", heme_groups=4, iron_atoms=4),
            binding=BindingMechanism(
                tense_state="Low O2 affinity",
                relaxed_state="High O2 affinity"
            )
        ),
        carbon_dioxide=CarbonDioxideTransport(
            as_bicarbonate="67%",
            as_carbamino="25%",
            dissolved="8%",
            conversion=CO2Conversion(
                in_tissue="CO2 + H2O → H2CO3 → H+ + HCO3⁻",
                in_lung="HCO3⁻ + H+ → H2CO3 → CO2 + H2O"
            )
        )
    ),
    renal=RenalSystem(
        kidney=Kidney(
            blood_flow={"Input": "1300 mL/min", "Output": "1299 mL/min", "Urine": "1 mL/min"},
            structures=["Renal artery", "Renal vein", "Cortex", "Medulla", "Pelvis"],
            nephron=Nephron(
                components=[
                    "Bowman's capsule", "Proximal tubule", "Loop of Henle",
                    "Distal tubule", "Collecting duct"
                ],
                types=["Cortical", "Juxtamedullary"]
            ),
            vasculature=[
                "Afferent arteriole", "Glomerulus", "Efferent arteriole",
                "Peritubular capillaries", "Vasa recta"
            ]
        )
    )
)