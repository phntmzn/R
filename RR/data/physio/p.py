
physio.neurosystem = Neurosystem(
    brain=Brain(
        forebrain=Forebrain(
            cerebral_cortex=CerebralCortex(
                lobes=["Frontal", "Parietal", "Occipital", "Temporal"],
                functions={
                    "Frontal": "Motor control, planning, speech, decision-making",
                    "Parietal": "Sensory input, spatial orientation",
                    "Occipital": "Visual processing",
                    "Temporal": "Auditory processing, memory"
                }
            ),
            limbic_system=LimbicSystem(
                components=[
                    "Hippocampus", "Amygdala", "Septum", "Cingulate Gyrus",
                    "Hypothalamus", "Olfactory Bulb", "Anterior Thalamus"
                ],
                functions=[
                    "Emotion integration", "Drive regulation", "Memory processing",
                    "Instinctive motor patterns", "Autonomic nervous system regulation", "Hormonal responses"
                ]
            ),
            basal_ganglia=BasalGanglia(
                function="Motor control coordination",
                clinical_relevance="Lesions → movement disorders (e.g., Parkinson’s)"
            )
        ),
        brain_stem=BrainStem(
            structures=["Thalamus", "Hypothalamus", "Midbrain", "Pons", "Medulla"],
            functions={
                "Thalamus": "Relay sensory input",
                "Hypothalamus": "Homeostasis, endocrine control",
                "Midbrain": "Visual & auditory reflexes",
                "Pons": "Bridge cerebrum and cerebellum",
                "Medulla": "Vital functions (HR, breathing)"
            }
        ),
        cerebellum="Coordination and balance"
    )
)

physio.neurosystem = Neurosystem(
    brain=Brain(
        forebrain=Forebrain(
            cerebral_cortex=CerebralCortex(
                lobes=["Frontal", "Parietal", "Occipital", "Temporal"],
                functions={
                    "Frontal": "Motor control, planning, speech, decision-making",
                    "Parietal": "Sensory input, spatial orientation",
                    "Occipital": "Visual processing",
                    "Temporal": "Auditory processing, memory"
                }
            ),
            limbic_system=LimbicSystem(
                components=[
                    "Hippocampus", "Amygdala", "Septum", "Cingulate Gyrus",
                    "Hypothalamus", "Olfactory Bulb", "Anterior Thalamus"
                ],
                functions=[
                    "Emotion integration", "Drive regulation", "Memory processing",
                    "Instinctive motor patterns", "Autonomic nervous system regulation", "Hormonal responses"
                ]
            ),
            basal_ganglia=BasalGanglia(
                function="Motor control coordination",
                clinical_relevance="Lesions → movement disorders (e.g., Parkinson’s)"
            ),
            visual_system=VisualSystem(
                components=[
                    "Optic Nerve", "Optic Chiasm", "Optic Tract",
                    "Lateral Geniculate Body", "Optic Radiation",
                    "Primary Visual Cortex (V1)", "Visual Association Cortex (V2–V6)"
                ],
                functions={
                    "Primary Visual Cortex (V1)": "Basic visual processing (edges, motion)",
                    "Visual Association Cortex": "Higher-order analysis (shape, color, motion)",
                    "Orientation Columns": "Detect specific edge orientations",
                    "Ocular Dominance Columns": "Organize input by eye of origin"
                }
            )
        ),
        brain_stem=BrainStem(
            structures=["Thalamus", "Hypothalamus", "Midbrain", "Pons", "Medulla"],
            functions={
                "Thalamus": "Relay sensory input",
                "Hypothalamus": "Homeostasis, endocrine control",
                "Midbrain": "Visual & auditory reflexes",
                "Pons": "Bridge cerebrum and cerebellum",
                "Medulla": "Vital functions (HR, breathing)"
            }
        ),
        cerebellum="Coordination and balance"
    )
)

physio.neurosystem = Neurosystem(
    brain=Brain(
        forebrain=Forebrain(
            cerebral_cortex=CerebralCortex(
                lobes=["Frontal", "Parietal", "Occipital", "Temporal"],
                functions={
                    "Frontal": "Motor control, planning, speech, decision-making",
                    "Parietal": "Sensory input, spatial orientation",
                    "Occipital": "Visual processing",
                    "Temporal": "Auditory processing, memory"
                }
            ),
            limbic_system=LimbicSystem(
                components=[
                    "Hippocampus", "Amygdala", "Septum", "Cingulate Gyrus",
                    "Hypothalamus", "Olfactory Bulb", "Anterior Thalamus"
                ],
                functions=[
                    "Emotion integration", "Drive regulation", "Memory processing",
                    "Instinctive motor patterns", "Autonomic nervous system regulation", "Hormonal responses"
                ]
            ),
            basal_ganglia=BasalGanglia(
                function="Motor control coordination",
                clinical_relevance="Lesions → movement disorders (e.g., Parkinson’s)"
            ),
            visual_system=VisualSystem(
                components=[
                    "Optic Nerve", "Optic Chiasm", "Optic Tract",
                    "Lateral Geniculate Body", "Optic Radiation",
                    "Primary Visual Cortex (V1)", "Visual Association Cortex (V2–V6)"
                ],
                functions={
                    "Primary Visual Cortex (V1)": "Basic visual processing (edges, motion)",
                    "Visual Association Cortex": "Higher-order analysis (shape, color, motion)",
                    "Orientation Columns": "Detect specific edge orientations",
                    "Ocular Dominance Columns": "Organize input by eye of origin"
                }
            ),
            auditory_system=AuditorySystem(
                components=[
                    "Cochlea", "Tectorial Membrane", "Hair Cells", "Auditory Nerve",
                    "Basilar Membrane", "Organ of Corti",
                    "Medulla", "Midbrain", "Medial Geniculate Body",
                    "Primary Auditory Cortex", "Association Cortex"
                ],
                functions={
                    "Cochlea": "Transduces sound wave vibration into neural signals",
                    "Basilar Membrane": "Frequency tuning via vibration location",
                    "Hair Cells": "Mechanoreceptors for auditory transduction",
                    "Primary Auditory Cortex": "Processes frequency and intensity",
                    "Association Cortex": "Language, speech, and high-order auditory integration"
                },
                cochlear_map={
                    "Base": "High-frequency discrimination",
                    "Apex": "Low-frequency discrimination"
                },
                clinical_notes="Presbycusis causes high-frequency hearing loss with age"
            )
        ),
        brain_stem=BrainStem(
            structures=["Thalamus", "Hypothalamus", "Midbrain", "Pons", "Medulla"],
            functions={
                "Thalamus": "Relay sensory input",
                "Hypothalamus": "Homeostasis, endocrine control",
                "Midbrain": "Visual & auditory reflexes",
                "Pons": "Bridge cerebrum and cerebellum",
                "Medulla": "Vital functions (HR, breathing)"
            }
        ),
        cerebellum="Coordination and balance"
    )
)

physio.neurosystem = Neurosystem(
    brain=Brain(
        forebrain=Forebrain(
            ...
            learning_memory_system=LearningMemorySystem(
                stages=[
                    "Instantaneous Learning",
                    "Short-term Memory",
                    "Memory Consolidation",
                    "Long-term Memory"
                ],
                mechanisms=[
                    "Neural reverberation",
                    "Synaptic facilitation",
                    "Protein synthesis",
                    "Synapse growth"
                ],
                brain_regions=[
                    "Hippocampus",
                    "Temporal Lobe",
                    "Limbic System",
                    "Prefrontal Cortex"
                ],
                disorders={
                    "Senile Amnesia": "Loss of recent memories due to degeneration",
                    "Alzheimer's": "Degeneration of hippocampus, cortex, nucleus basalis",
                    "Trauma": "Retrograde amnesia linked to hippocampal injury"
                },
                enhancement_methods=[
                    "Electrical stimulation of temporal lobe",
                    "Reinforcement learning",
                    "Memory recall via cue exposure"
                ]
            )
        ),
        ...
    )
)

physio.neurosystem = Neurosystem(
    brain=Brain(
        forebrain=Forebrain(
            ...
            neurochemical_system=NeurochemicalSystem(
                neurotransmitters={
                    "Norepinephrine": {
                        "synthesis": "Tyrosine → Dopa → Dopamine → Norepinephrine",
                        "function": "Mood, alertness, arousal",
                        "clinical_notes": "Deficiency linked to depression"
                    },
                    "Serotonin": {
                        "synthesis": "Tryptophan → Serotonin (5-HT)",
                        "function": "Mood regulation, sleep, appetite",
                        "clinical_notes": "Deficiency linked to depression"
                    },
                    "Dopamine": {
                        "synthesis": "Tyrosine → Dopa → Dopamine",
                        "function": "Motivation, reward, movement",
                        "clinical_notes": "Excess linked to schizophrenia"
                    }
                },
                brain_regions_involved={
                    "Locus Coeruleus": "Norepinephrine production and projection",
                    "Raphe Nuclei": "Serotonin production",
                    "Midbrain (VTA, substantia nigra)": "Dopamine pathways to cortex, limbic system, basal ganglia"
                },
                clinical_disorders={
                    "Depression": {
                        "neurochemistry": "Deficiency of NE and/or 5-HT",
                        "drug_targets": ["Reuptake inhibitors", "MAO inhibitors"]
                    },
                    "Schizophrenia": {
                        "neurochemistry": "Excess dopamine in mesolimbic pathway",
                        "drug_targets": ["D2 receptor blockers"]
                    }
                }
            )
        )
    )
)

cerebral_cortex=CerebralCortex(
    lobes=["Frontal", "Parietal", "Occipital", "Temporal"],
    functions={
        "Frontal": "Motor control, planning, speech, decision-making",
        "Parietal": "Sensory input, spatial orientation",
        "Occipital": "Visual processing",
        "Temporal": "Auditory processing, memory"
    },
    hemispheres={
        "Left": {
            "functions": [
                "Speech (Broca's area)",
                "Language comprehension (Wernicke's area)",
                "Logical reasoning",
                "Sequential analysis",
                "Motor control for right body"
            ],
            "dominance_in": "90% right-handed individuals"
        },
        "Right": {
            "functions": [
                "Spatial skills",
                "Emotion recognition",
                "Musical processing",
                "Holistic perception",
                "Visual imagery",
                "Motor control for left body"
            ],
            "dominance_in": "31% left-handed individuals"
        }
    },
    language_functions={
        "Broca's Area": {
            "location": "Frontal lobe, left hemisphere",
            "role": "Speech production",
            "disorder": "Motor aphasia"
        },
        "Wernicke's Area": {
            "location": "Temporal lobe, left hemisphere",
            "role": "Language comprehension",
            "disorder": "Sensory aphasia"
        },
        "Angular Gyrus": {
            "location": "Parietal-temporal junction",
            "role": "Reading and writing integration"
        }
    }
),

metabolic_system=MetabolicSystem(
    brain_weight_ratio=0.021,  # 2.1% of body weight
    blood_flow_ratio=0.15,     # 15% of cardiac output
    oxygen_consumption=0.20,   # 20% of body oxygen
    fuel_sources=["Glucose", "Oxygen"],
    regional_rates={
        "Gray Matter": "Very High",
        "White Matter": "Medium",
        "Cerebral Cortex": "High",
        "Basal Ganglia": "Very High",
        "Spinal Cord": "Low",
        "Cerebellum": "Medium",
        "Brainstem": "Variable"
    },
    functional_activations={
        "Reading": ["Visual Cortex", "Wernicke's Area", "Broca’s Area", "Auditory Cortex"],
        "Creative Speech": ["Broca’s Area", "Motor Cortex"],
        "Hand Clenching": ["Motor Cortex - Hand Area"],
        "Anxiety/Pain": ["Frontal Lobe", "Limbic System"],
        "Contemplation": ["Prefrontal Cortex", "Parietal Association Areas"],
        "Visual/Spatial": ["Occipital Lobe", "Parietal Association Cortex"]
    },
    clinical_notes=[
        "Hypoglycemia causes confusion, loss of consciousness",
        "Hypoxia leads to irreversible brain damage in minutes"
    ]
)

endocrine_system = EndocrineSystem(
    glands=[
        "Pineal", "Pituitary", "Thyroid", "Parathyroid",
        "Pancreas", "Adrenal", "Ovary", "Testis"
    ],
    partial_function_organs=[
        "Hypothalamus", "Liver", "Thymus", "Heart",
        "Kidney", "Stomach", "Duodenum"
    ],
    communication_forms={
        "Endocrine": "Hormones travel via blood to distant target cells",
        "Neuroendocrine": "Neurons release hormones into blood or portal vessels to target glands",
        "Paracrine": "Local diffusion to nearby tissue cells",
        "Autocrine": "Hormones act on the same cell that secreted them"
    },
    pathways=[
        {
            "name": "Classic Endocrine Pathway",
            "mechanism": "Endocrine cell → Hormone → Bloodstream → Distant Target Cell"
        },
        {
            "name": "Neuroendocrine Direct",
            "mechanism": "Neurocell → Neurohormone → Blood → Target Receptor"
        },
        {
            "name": "Hypothalamic Portal",
            "mechanism": "Brain (Hypothalamus) → Portal Vessel → Pituitary → Target"
        },
        {
            "name": "Paracrine Signaling",
            "mechanism": "Paracrine cell → Local diffusion → Neighboring tissue cell"
        },
        {
            "name": "Autocrine Signaling",
            "mechanism": "Cell releases hormone → Receptors on same cell"
        }
    ]
)

physio.endocrine_system = endocrine_system

hormone_mechanisms = {
    "Steroid_Thyroid": {
        "receptor_type": "Nuclear",
        "location": "Intracellular (nucleus)",
        "mechanism": [
            "Hormone enters cell",
            "Binds nuclear receptor",
            "Activates transcription",
            "mRNA → Protein synthesis"
        ],
        "response_time": "Hours to days",
        "examples": ["Cortisol", "Estrogen", "Thyroid Hormones (T3, T4)"]
    },
    "Peptide_Catecholamine": {
        "receptor_type": "Membrane-bound",
        "location": "Cell membrane",
        "mechanism": [
            "Hormone binds membrane receptor",
            "Activates G protein",
            "Stimulates adenylate cyclase → cAMP",
            "Activates Protein Kinase → Protein phosphorylation"
        ],
        "response_time": "Seconds to minutes",
        "examples": ["Epinephrine", "Glucagon", "Insulin"]
    },
    "Calcium_Calmodulin": {
        "receptor_type": "Membrane-bound",
        "location": "Cell membrane",
        "mechanism": [
            "Hormone binding causes Ca²⁺ influx",
            "Ca²⁺ binds calmodulin",
            "Activates enzymes"
        ],
        "response_time": "Seconds",
        "examples": ["ADH", "Oxytocin"]
    }
}

posterior_pituitary = PosteriorPituitary(
    hormones={
        "ADH": {
            "origin": "Supraoptic Nucleus",
            "trigger": ["High plasma osmolarity", "Low blood volume/pressure"],
            "targets": ["Kidney (nephron)", "Blood vessels"],
            "functions": [
                "Water retention in collecting ducts",
                "Vasoconstriction to increase BP"
            ]
        },
        "Oxytocin": {
            "origin": "Paraventricular Nucleus",
            "trigger": ["Nipple stimulation", "Cervical stretch"],
            "targets": ["Mammary glands", "Uterus"],
            "functions": [
                "Milk ejection",
                "Uterine contraction during labor"
            ]
        }
    },
    transport_path="Hypothalamo-hypophyseal tract",
    storage_site="Posterior Pituitary (Herring bodies)",
    release_mode="Neurosecretory via axon terminals into bloodstream"
)

physio.hormonal_regulation.posterior_pituitary = posterior_pituitary


