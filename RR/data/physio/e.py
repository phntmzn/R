

# Definitions of charged particles and voltage effects
electrical_forces = {
    "positive_charge": ["Na⁺", "K⁺"],
    "negative_charge": ["Cl⁻", "A⁻"],
    "flow_direction": {
        "low_to_high_voltage": "opposed",
        "high_to_low_voltage": "favored",
    },
    "examples": {
        "Na⁺": "flows toward lower voltage",
        "Cl⁻": "flows toward higher voltage",
    }
}

# Membrane potential and gradients
membrane_potential = {
    "structure": "phospholipid bilayer with embedded proteins",
    "components": ["K⁺ channel", "Na⁺ channel", "Cl⁻ channel"],
    "forces": {
        "concentration_gradient": "drives ions from high to low concentration",
        "voltage_gradient": "drives ions according to electrical charge",
    },
    "key_terms": ["equilibrium_potential", "resting_membrane_potential"]
}

# Sodium-Potassium Pump system
sodium_potassium_pump = {
    "name": "Na⁺/K⁺-ATPase",
    "function": {
        "Na⁺": "pumps 3 Na⁺ out",
        "K⁺": "pumps 2 K⁺ in",
        "ATP": "required to drive pump"
    },
    "result": {
        "maintains_negative_resting_potential": True,
        "maintains_ion_gradients": True
    }
}

# Equilibrium dynamics
equilibrium_potential_example = {
    "K⁺_diffusion": {
        "initial": "K⁺ diffuses out",
        "builds_voltage": "inside becomes more negative",
        "eventual": "electrical force pulls K⁺ back in",
        "equilibrium_potential": "when concentration and voltage forces balance"
    }
}

# Example snapshot of intracellular vs extracellular environment
cell_environment_snapshot = {
    "intracellular": {"K⁺": "high", "Na⁺": "low", "Cl⁻": "low", "A⁻": "high"},
    "extracellular": {"K⁺": "low", "Na⁺": "high", "Cl⁻": "high"},
    "channels": ["K⁺ leak channel", "Na⁺ channel", "Cl⁻ channel"],
    "active_transport": ["Na⁺/K⁺ pump"]
}

# Brain vs Total Body
brain_vs_body = {
    "weight_percentage": 2,            # % of total body weight
    "blood_flow_percentage": 15,       # % of cardiac output
    "oxygen_consumption_percentage": 20
}

# Brain energy sources
brain_food = {
    "glucose": "primary energy source",
    "oxygen": "required for aerobic metabolism"
}

# Metabolic rates of brain regions
brain_metabolism = {
    "very_high": ["gray matter", "cerebral cortex", "basal ganglia"],
    "medium": ["thalamus", "hypothalamus", "reticular formation", "cerebellum"],
    "low": ["spinal cord", "white matter"]
}

# Functional brain activation maps
brain_activities = {
    "thoughtless_speech": ["frontal cortex"],
    "reading": ["visual cortex", "Wernicke's area", "premotor cortex"],
    "creative_speech": ["Broca’s area", "prefrontal cortex", "auditory cortex"],
    "hand_clenching": ["motor cortex", "sensory cortex"],
    "hand_stimulation": ["sensory cortex"],
    "visual_spatial": ["visual cortex", "parietal lobe"],
    "anxiety_pain": ["limbic system", "prefrontal cortex"],
    "contemplation": ["prefrontal cortex", "Broca’s area", "Wernicke’s area"]
}

# Endocrine communication model
hormonal_communication = {
    "endocrine": {
        "origin": "endocrine cell",
        "path": ["hormone", "blood circulation", "target cell", "receptor"],
        "note": "Hormones travel through blood to distant cells."
    },
    "neuroendocrine": {
        "origin": "neurosecretory neuron",
        "path": ["neurohormone", "blood", "target cell", "receptor"],
        "note": "Neurons release hormones into circulation."
    },
    "neuroendocrine_portal": {
        "origin": "neurosecretory neuron",
        "path": ["neurohormone", "portal vessel", "target cell", "receptor"],
        "note": "Hormones use a local portal circulation (e.g., hypothalamus → anterior pituitary)."
    },
    "neural_autonomic": {
        "origin": "brain",
        "path": ["autonomic neuron", "target tissue", "neurotransmitter", "receptor"],
        "note": "Direct autonomic innervation by neurons to target organs."
    },
    "paracrine": {
        "origin": "local tissue cell",
        "path": ["local hormone", "adjacent target cell"],
        "note": "Hormones diffuse locally within tissue."
    },
    "autocrine": {
        "origin": "self-signaling cell",
        "path": ["local hormone", "same cell receptor"],
        "note": "Cell responds to the hormone it secretes."
    }
}

# Hormone action mechanisms
steroid_thyroid_hormones = {
    "type": "lipid-soluble",
    "receptor_location": "nucleus (or cytoplasm → nucleus)",
    "steps": [
        "Hormone diffuses into cell",
        "Binds to nuclear receptor",
        "Hormone-receptor complex binds DNA",
        "Initiates mRNA transcription",
        "mRNA translated to protein in cytoplasm",
        "Protein causes physiological response"
    ],
    "time_course": "hours",
    "examples": ["cortisol", "estrogen", "testosterone", "thyroxine (T4)", "triiodothyronine (T3)"],
    "termination": ["excretion (kidney)", "degradation (liver)"]
}

# 
peptide_catecholamine_hormones = {
    "type": "water-soluble",
    "receptor_location": "cell membrane",
    "signal_transduction": [
        "Hormone binds membrane receptor",
        "Activates G protein",
        "Stimulates adenylate cyclase",
        "Produces cAMP from ATP",
        "cAMP activates protein kinase",
        "Protein kinase phosphorylates target proteins",
        "Triggers physiological response"
    ],
    "time_course": "seconds to minutes",
    "examples": ["epinephrine", "norepinephrine", "insulin", "glucagon", "ADH"],
    "termination": ["phosphodiesterase breaks down cAMP", "hormone degradation"]
}

# 
calcium_calmodulin_pathway = {
    "trigger": "Hormone activates G protein → opens Ca²⁺ channels",
    "second_messenger": "Ca²⁺",
    "binding_protein": "Calmodulin",
    "effect": "Activates kinases → phosphorylates proteins",
    "time_course": "seconds"
}

# General feedback control model
feedback_control = {
    "input": "stimulus or signal",
    "system": "endocrine or physiological mechanism",
    "output": "response (hormone or effect)",
    "feedback": "modifies input (via inhibition or stimulation)"
}

# Types of Feedback
feedback_types = {
    "negative_feedback": {
        "function": "maintains equilibrium (homeostasis)",
        "examples": ["thyroid hormone inhibiting TSH", "cortisol inhibiting ACTH"],
        "outcome": "stable, regulated output"
    },
    "positive_feedback": {
        "function": "amplifies response until interruption",
        "examples": ["oxytocin during childbirth", "LH surge in ovulation"],
        "outcome": "escalating output (vicious cycle)"
    }
}

# 1. Simple Hormonal Regulation
simple_hormonal = {
    "level": 1,
    "steps": [
        "Endocrine gland secretes hormone",
        "Hormone acts on target organ cell",
        "Effect modifies further secretion (feedback)"
    ],
    "example": "parathyroid hormone"
}

# 2. Complex Hormonal Regulation
complex_hormonal = {
    "level": 2,
    "steps": [
        "Pituitary gland cell releases tropic hormone",
        "Stimulates endocrine gland",
        "Endocrine gland secretes hormone to act on target organ"
    ],
    "example": "pituitary → adrenal cortex → cortisol"
}

# 3. Complex Neurohormonal Regulation
complex_neurohormonal = {
    "level": 3,
    "steps": [
        "Environmental input processed by brain",
        "Hypothalamus secretes releasing hormone",
        "Pituitary releases tropic hormone",
        "Stimulates endocrine gland to release hormone"
    ],
    "example": "hypothalamus → CRH → pituitary → ACTH → adrenal cortex → cortisol"
}

# Core Structures
posterior_pituitary_pathway = {
    "brain_regions": {
        "hypothalamus": ["supraoptic nucleus", "paraventricular nucleus"],
        "pituitary": {
            "posterior": "neurohypophysis",
            "tract": "hypothalamo-hypophyseal tract"
        }
    },
    "stimuli": {
        "ADH": ["high blood osmolality", "low blood volume"],
        "oxytocin": ["cervical/uterine stretch", "nipple stimulation"]
    },
    "neural_input": [
        "baroreceptors", "osmoreceptors", "cervical stretch receptors"
    ]
}

# Hormones
posterior_pituitary_hormones = {
    "ADH": {
        "produced_by": "supraoptic nucleus",
        "target": ["kidney collecting ducts", "arterioles"],
        "action": [
            "water reabsorption", 
            "vasoconstriction"
        ],
        "net_effect": "increase blood volume and pressure"
    },
    "oxytocin": {
        "produced_by": "paraventricular nucleus",
        "target": ["uterus", "mammary glands"],
        "action": [
            "uterine contraction", 
            "milk ejection (let-down reflex)"
        ],
        "net_effect": "facilitates labor and breastfeeding"
    }
}

# Hormone Transport
neurosecretion_mechanism = {
    "cell_type": "neurosecretory cell",
    "parts": ["cell body", "axon", "axon terminal"],
    "mechanism": "Hormones synthesized in hypothalamus travel down axons to posterior pituitary and are released into capillary blood."
}

posterior_peptides = {
    "oxytocin": "Cys-Tyr-Ile-Gln-Asn-Cys-Pro-Leu-Gly-NH₂",
    "ADH": "Cys-Tyr-Phe-Gln-Asn-Cys-Pro-Arg-Gly-NH₂"
}

# Hypothalamic-Pituitary Regulation of GH
gh_regulation = {
    "hypothalamus": {
        "stimulatory": "GHRH (Growth Hormone Releasing Hormone)",
        "inhibitory": "Somatostatin (GHIH)"
    },
    "pituitary": {
        "cell": "somatotrope",
        "hormone": "Growth Hormone (GH)"
    },
    "secretion_pattern": "episodic, every ~4 hours, with peak during deep sleep"
}

gh_effects = {
    "metabolic": {
        "muscle": "↑ amino acid uptake, protein synthesis",
        "liver": "↑ gluconeogenesis, IGF-1 secretion",
        "adipose": "↑ lipolysis → ↑ free fatty acids",
        "carbohydrate": "↓ glucose uptake in tissues → hyperglycemia"
    },
    "growth": {
        "via_igf1": True,
        "targets": ["epiphyseal plates", "bone", "cartilage", "muscle", "organs"],
        "cellular_effects": ["↑ protein synthesis", "↑ cell proliferation"]
    },
    "amino_acids_glucose": {
        "glucose_sparing": True,
        "net_effect": "protein synthesis preserved during fasting"
    }
}

gh_disorders = {
    "children": {
        "deficiency": "dwarfism",
        "excess": "gigantism"
    },
    "adults": {
        "excess_after_epiphyseal_closure": "acromegaly"
    }
}

# HPT Axis Regulation
thyroid_axis = {
    "hypothalamus": {
        "hormone": "TRH (Thyrotropin-Releasing Hormone)",
        "target": "anterior pituitary"
    },
    "anterior_pituitary": {
        "cell": "thyrotroph",
        "hormone": "TSH (Thyroid-Stimulating Hormone)",
        "target": "thyroid gland"
    },
    "thyroid_gland": {
        "hormones": ["T3 (triiodothyronine)", "T4 (thyroxine)"],
        "conversion": "T4 converted to T3 in target tissues",
        "target": "multiple tissues for metabolic effects"
    },
    "feedback": {
        "T3_T4": "inhibit TRH and TSH via negative feedback"
    }
}

thyroid_hormone_synthesis = {
    "steps": [
        "Iodide uptake into follicular cell",
        "Transport to colloid and oxidation to iodine",
        "Iodine binds tyrosine residues on thyroglobulin",
        "Forms MIT and DIT → T3 (MIT + DIT), T4 (DIT + DIT)",
        "Thyroglobulin endocytosed back into follicular cell",
        "Proteolysis releases T3/T4 into bloodstream"
    ],
    "storage_form": "colloid (thyroglobulin-bound)",
    "stimulated_by": "TSH"
}

thyroid_hormone_effects = {
    "metabolism": "↑ basal metabolic rate (BMR)",
    "oxygen_use": "↑ O2 consumption (calorigenic effect)",
    "nervous_system": "↑ growth and development, especially in children",
    "cardiovascular": "↑ heart rate and contractility",
    "sympathetic": "↑ sensitivity to catecholamines"
}

thyroid_disorders = {
    "hypothyroidism": {
        "children": {
            "condition": "cretinism",
            "symptoms": ["stunted growth", "intellectual disability", "coarse features"]
        },
        "adults": {
            "condition": "myxedema",
            "symptoms": ["fatigue", "weight gain", "cold intolerance", "puffy face"]
        },
        "histology": "large follicles with scant colloid",
        "state": "hypoactive"
    },
    "hyperthyroidism": {
        "condition": "e.g., Graves' disease",
        "symptoms": ["high BMR", "weight loss", "sweating", "heat intolerance", "exophthalmos"],
        "histology": "small follicles with scant colloid",
        "state": "hyperactive"
    }
}

# Distribution of Blood at Rest vs Exercise
blood_distribution = {
    "rest": {
        "veins_and_venules": "63%",
        "lungs": "11%",
        "arteries": "10%"
    },
    "exercise": {
        "veins_and_venules": "35%",
        "lungs": "11%",
        "arteries": "16%",
        "skeletal_muscle": "↑ blood redirection"
    }
}

vascular_compliance = {
    "veins": {
        "property": "high compliance",
        "function": "volume reservoir",
        "pressure_vs_volume": "large volume change with small pressure increase"
    },
    "arteries": {
        "property": "low compliance",
        "function": "pressure reservoir",
        "pressure_vs_volume": "small volume change with large pressure increase"
    }
}

venous_pressure_gradient = {
    "aortic_pressure": 100,  # mmHg
    "capillary_pressure": 35,
    "venous_pressure": 15,
    "right_atrium": 0,
    "note": "Venous return is driven by pressure gradient from veins → heart"
}

venous_pumps = {
    "skeletal_muscle_pump": {
        "mechanism": "muscle contraction compresses veins",
        "valves": "prevent backflow",
        "effect": "propels blood toward heart"
    },
    "respiratory_pump": {
        "mechanism": "inspiration ↓ thoracic pressure, ↑ abdominal pressure",
        "effect": "sucks blood toward chest and heart"
    },
    "venous_valves": {
        "role": "ensure unidirectional flow",
        "found_in": "limb veins"
    }
}

# Local Chemical Control of Blood Vessels
local_chemical_control = {
    "trigger": "increased cell metabolism",
    "released_metabolites": ["↑ CO₂", "↑ H⁺", "↑ adenosine", "↑ K⁺", "↓ O₂"],
    "effect": "vasodilation of arterioles and precapillary sphincters",
    "purpose": "increase nutrient/waste exchange in active tissues"
}

# Nitric Oxide (NO) Mechanism
nitric_oxide_action = {
    "produced_by": "endothelial cells (via ↑ intracellular Ca²⁺)",
    "acts_on": "smooth muscle cells (paracrine action)",
    "mechanism": [
        "NO diffuses into smooth muscle",
        "Activates guanylate cyclase",
        "↑ cGMP → ↓ Ca²⁺",
        "Smooth muscle relaxation"
    ],
    "effect": "vasodilation"
}

# Sympathetic Nervous Control of Vascular Tone
systemic_neural_control = {
    "neurotransmitter": "norepinephrine (NE)",
    "receptor": "adrenergic receptor on smooth muscle",
    "neural_firing_frequency_effects": {
        "high_frequency": "vasoconstriction",
        "low_frequency": "vasodilation"
    },
    "reflex_control": True,
    "override_by_local_metabolites": True  # local overrides central
}

heart_rate_control = {
    "parasympathetic": {
        "origin": "vagus nerve",
        "effect": "↓ heart rate (slows SA node firing)"
    },
    "sympathetic": {
        "origin": "spinal cord + adrenal medulla",
        "neurotransmitters": ["norepinephrine", "epinephrine"],
        "effect": "↑ heart rate and contractility"
    }
}

stroke_volume_control = {
    "mechanisms": {
        "preload": "↑ venous return → ↑ ventricular filling → ↑ stretch",
        "contractility": "↑ sympathetic stimulation → ↑ contraction strength"
    },
    "graph_notes": {
        "curve_1": "baseline",
        "curve_2": "enhanced with sympathetic input"
    }
}

baroreceptor_reflex = {
    "stimulus": "↑ blood pressure (MAP)",
    "receptors": {
        "carotid_sinus": "sinus nerve",
        "aortic_arch": "depressor nerve"
    },
    "afferent_signals": "↑ firing rate from baroreceptors to medulla",
    "medulla_response": {
        "parasympathetic_output": "↑ vagus nerve activity → ↓ HR",
        "sympathetic_output": {
            "to_heart": "↓ HR and ↓ contractility",
            "to_arterioles": "↓ vasoconstriction → ↓ TPR",
            "to_veins": "↓ venous tone → ↓ preload"
        }
    },
    "result": "↓ cardiac output, ↓ resistance, ↓ MAP → negative feedback"
}

baroreceptor_sequence = [
    "blood_pressure_rise",
    "baroreceptor_stretch",
    "increased_afferent_firing",
    "medulla_activation",
    "↑ parasympathetic (vagus), ↓ sympathetic",
    "↓ heart rate, ↓ stroke volume",
    "↓ cardiac output",
    "↓ peripheral resistance",
    "↓ venous return",
    "↓ MAP (compensated)"
]

higher_brain_influences = {
    "hypothalamus": "modulates autonomic tone based on temperature, emotion",
    "cerebral_cortex": "can override reflex via stress, fear, or voluntary control",
    "medulla_oblongata": "executive center for cardiovascular homeostasis"
}

# Short-Term (Neural)
short_term_regulators = {
    "mechanism": "baroreceptor reflex",
    "sensors": ["carotid sinus", "aortic arch"],
    "effector_pathways": {
        "parasympathetic": "↓ heart rate",
        "sympathetic": ["↑ heart rate", "↑ vasoconstriction", "↑ contractility"]
    },
    "response_time": "seconds to minutes",
    "function": "buffer acute changes in BP"
}

intermediate_regulators = {
    "trans_capillary_shift": {
        "mechanism": "fluid shifts from capillaries to interstitium or plasma",
        "trigger": "sudden BP change",
        "effect": "buffers volume and pressure over minutes to hours"
    },
    "vascular_stress_relaxation": {
        "mechanism": "slow relaxation of smooth muscle under pressure",
        "location": "venous system",
        "effect": "accommodates changes in volume and pressure"
    },
    "renin_angiotensin_pathway": {
        "trigger": "↓ renal perfusion",
        "sequence": ["Renin → Angiotensin I → ACE → Angiotensin II"],
        "angiotensin_II_effects": ["↑ vasoconstriction", "↑ aldosterone release", "↑ thirst"]
    }
}

long_term_regulators = {
    "fluid_volume_control": {
        "mechanism": "water and sodium retention or excretion",
        "hormones": ["ADH", "aldosterone", "ANP"],
        "systems": [
            "hypothalamus → thirst/ADH",
            "renin-angiotensin-aldosterone system (RAAS)",
            "atrial natriuretic peptide (ANP) from heart"
        ],
        "effect": "regulates extracellular volume → long-term BP"
    },
    "aldosterone_effects": {
        "site": "distal tubule of kidney",
        "action": "↑ Na⁺ reabsorption, ↑ K⁺/H⁺ excretion",
        "net_effect": "↑ water retention → ↑ BP"
    },
    "ANP_effects": {
        "trigger": "↑ atrial stretch",
        "action": "↑ Na⁺ excretion (natriuresis), ↓ renin/ADH/aldosterone",
        "net_effect": "↓ BP and volume"
    }
}

# Respiratory Tract Anatomy
respiratory_tract = {
    "upper_airway": [
        "nasal cavity",
        "oral cavity",
        "pharynx",
        "epiglottis"
    ],
    "lower_airway": [
        "larynx",
        "trachea",
        "bronchi",
        "bronchiole",
        "alveolar duct",
        "alveolus"
    ],
    "muscles": ["diaphragm", "intercostals"],
    "function": "conduct air and exchange gases"
}

gas_exchange = {
    "location": "alveolar-capillary interface",
    "structure": {
        "alveolar_epithelium": "Type I and II pneumocytes",
        "capillary_endothelium": "thin-walled for diffusion"
    },
    "process": {
        "O2": "diffuses from alveolus to blood",
        "CO2": "diffuses from blood to alveolus"
    },
    "factors_affecting_exchange": [
        "surface area (~88 m²)",
        "membrane thickness",
        "partial pressure gradient"
    ],
    "note": "rapid exchange due to short diffusion distance"
}

blood_flow_states = {
    "deoxygenated": {
        "path": "pulmonary artery → capillary bed of alveoli",
        "contains": "high CO₂, low O₂"
    },
    "oxygenated": {
        "path": "pulmonary vein → left atrium",
        "contains": "high O₂, low CO₂"
    }
}

# Respiratory Structures
respiratory_muscles = {
    "inspiration": {
        "primary": ["diaphragm", "external intercostal muscles"],
        "movement": "diaphragm flattens, rib cage lifts outward"
    },
    "expiration": {
        "passive": True,
        "muscles": ["internal intercostal muscles (forced)", "abdominals (forced)"],
        "movement": "diaphragm relaxes, ribs recoil inward"
    },
    "static_support": ["sternum", "spinal column", "pleural membranes", "intrapleural fluid"]
}

# Pressure values in mmHg (relative to atmospheric = 0 mmHg)
respiratory_pressures = {
    "at_rest": {
        "intrapulmonary_pressure": 0,
        "intrapleural_pressure": -5,
        "lung_volume": "functional residual capacity"
    },
    "inspiration": {
        "intrapulmonary_pressure": -1,
        "intrapleural_pressure": -6,
        "volume_change": "+0.5L"
    },
    "expiration": {
        "intrapulmonary_pressure": +1,
        "intrapleural_pressure": -3,
        "volume_change": "-0.5L"
    }
}

# Oxygen Transport in Blood
oxygen_transport = {
    "dissolved_in_plasma": 0.3,       # mL O₂ / 100 mL blood
    "bound_to_Hb": 20.0,              # mL O₂ / 100 mL blood
    "percent_distribution": {
        "oxyhemoglobin": 99,
        "dissolved": 1
    },
    "reaction": "HHb + O₂ ⇌ HbO₂ + H⁺"
}

co2_transport = {
    "as_bicarbonate": 67,      # %
    "as_carbamino_hemoglobin": 25,   # %
    "dissolved": 8,            # %
    "mechanism": {
        "carbonic_anhydrase": "CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻",
        "carbamino_binding": "CO₂ + Hb ⇌ HbCO₂ (in RBCs)"
    }
}

hemoglobin_structure = {
    "chains": {
        "alpha": 2,
        "beta": 2
    },
    "hemes": 4,
    "porphyrins": 4,
    "iron_atoms": 4,
    "binding_sites": 4
}

hemoglobin_binding_dynamics = {
    "tense_state": {
        "description": "low O₂ affinity (T state)",
        "initial_state": True,
        "mechanism": "first O₂ binding breaks salt bridges"
    },
    "relaxed_state": {
        "description": "high O₂ affinity (R state)",
        "cooperative_binding": "each O₂ increases affinity for the next"
    },
    "effect": "sigmoidal oxygen dissociation curve"
}

# Key enzymes and reactions in tissues (internal respiration)
internal_respiration = {
    "tissue_cell": {
        "O2_consumption": "HbO2 → Hb + O2 (used by mitochondria)",
        "CO2_production": "CO2 + H2O ⇌ H2CO3 ⇌ HCO3⁻ + H⁺",
        "enzyme": "carbonic anhydrase (in RBCs)"
    },
    "RBC_buffering": {
        "H⁺_buffering": "H⁺ + Hb → HHb (buffered hemoglobin)",
        "HCO3_exit": True,
        "Cl_shift": "Cl⁻ enters to maintain charge (chloride shift)"
    }
}

# Alveolar gas exchange (external respiration)
external_respiration = {
    "alveolus": {
        "O2_diffuses": "O2 → plasma → RBC → binds to Hb",
        "Hb_reaction": "Hb + O2 → HbO2",
        "H⁺_release": "HbO2 displaces H⁺ from HHb",
        "CO2_exhalation": {
            "HCO3⁻ + H⁺ → H2CO3 → CO2 + H2O",
            "CO2 → diffuses to alveoli → exhaled"
        }
    },
    "enzyme": "carbonic anhydrase (reversible catalyst)"
}

reaction_chain_internal = [
    "CO2 + H2O → H2CO3",
    "H2CO3 → H⁺ + HCO3⁻",
    "H⁺ + Hb → HHb (buffering)",
    "HCO3⁻ → plasma (Cl⁻ in)"
]

reaction_chain_external = [
    "HCO3⁻ + H⁺ → H2CO3",
    "H2CO3 → CO2 + H2O",
    "CO2 diffuses to alveolus → exhaled",
    "Hb + O2 → HbO2"
]


