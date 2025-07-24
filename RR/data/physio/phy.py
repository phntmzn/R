from dataclasses import dataclass, field
from typing import List, Dict, Union

@dataclass
class CardiacOutput:
    formula: str
    typical_values: Dict[str, str]
    regulation: Dict[str, Dict[str, Union[str, bool]]]
    measurement: Dict[str, str]

@dataclass
class BloodPressure:
    MAP_formula: str
    short_term: Dict[str, Union[str, List[str]]]
    intermediate: List[str]
    long_term: List[str]

@dataclass
class CardiovascularSystem:
    cardiac_output: CardiacOutput
    blood_pressure: BloodPressure

@dataclass
class LungMechanics:
    inspiration: Dict[str, str]
    expiration: Dict[str, str]

@dataclass
class RespiratorySystem:
    airways: List[str]
    lung_mechanics: LungMechanics
    volumes: Dict[str, str]
    spirometry: Dict[str, str]
    gas_exchange: Dict[str, str]

@dataclass
class HemoglobinStructure:
    subunits: str
    heme_groups: int
    iron_atoms: int

@dataclass
class BindingMechanism:
    tense_state: str
    relaxed_state: str

@dataclass
class OxygenTransport:
    in_plasma: str
    as_hemoglobin: str
    structure: HemoglobinStructure
    binding: BindingMechanism

@dataclass
class CO2Conversion:
    in_tissue: str
    in_lung: str

@dataclass
class CarbonDioxideTransport:
    as_bicarbonate: str
    as_carbamino: str
    dissolved: str
    conversion: CO2Conversion

@dataclass
class GasTransport:
    oxygen: OxygenTransport
    carbon_dioxide: CarbonDioxideTransport

@dataclass
class Nephron:
    components: List[str]
    types: List[str]

@dataclass
class Kidney:
    blood_flow: Dict[str, str]
    structures: List[str]
    nephron: Nephron
    vasculature: List[str]

@dataclass
class RenalSystem:
    kidney: Kidney

@dataclass
class Physiology:
    cardiovascular: CardiovascularSystem
    respiratory: RespiratorySystem
    gas_transport: GasTransport
    renal: RenalSystem

