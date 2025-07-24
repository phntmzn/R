





class CentralNervousSystem:
    def __init__(self):
        self.brain = Brain()
        self.spinal_cord = SpinalCord()
        self.skeletal_system = SkeletalSystem()
        self.muscular_system = MuscularSystem()
        self.digestive_system = DigestiveSystem()
        self.endocrine_system = EndocrineSystem()
        self.ear_system = EarSystem()
        self.respiratory_system = RespiratorySystem()
        self.cardiovascular_system = CardiovascularSystem()

    def process_signal(self, signal):
        print(f"\nProcessing signal in CNS: {signal}")
        ear_response = None
        if "hear" in signal or "sound" in signal:
            ear_response = self.ear_system.capture_sound(signal)

        brain_response = self.brain.process_signal(signal)
        spinal_response = self.spinal_cord.relay_signal(signal)
        skeletal_response = self.skeletal_system.respond_to_signal(signal)
        muscular_response = self.muscular_system.respond_to_signal(signal)
        digestive_response = self.digestive_system.respond_to_signal(signal)
        endocrine_response = self.endocrine_system.respond_to_signal(signal)
        respiratory_response = self.respiratory_system.respond_to_signal(signal)
        cardiovascular_response = self.cardiovascular_system.respond_to_signal(signal)

        return {
            'ear_response': ear_response,
            'brain_response': brain_response,
            'spinal_response': spinal_response,
            'skeletal_response': skeletal_response,
            'muscular_response': muscular_response,
            'digestive_response': digestive_response,
            'endocrine_response': endocrine_response,
            'respiratory_response': respiratory_response,
            'cardiovascular_response': cardiovascular_response
        }
    
class CardiovascularSystem:
    def __init__(self):
        self.organs = ['heart', 'arteries', 'veins', 'capillaries']

    def respond_to_signal(self, signal):
        if "circulate" in signal or "heart" in signal:
            return self.circulate_blood(signal)
        return f"Cardiovascular system maintaining circulation for {signal}"

    def circulate_blood(self, signal):
        return f"Cardiovascular system circulating blood for {signal} using {', '.join(self.organs)}"
    
    class RespiratorySystem:
    def __init__(self):
        self.organs = ['nose', 'trachea', 'lungs', 'diaphragm']

    def respond_to_signal(self, signal):
        if "breathe" in signal:
            return self.breathe(signal)
        return f"Respiratory system stable for {signal}"

    def breathe(self, signal):
        return f"Respiratory system performing breathing for {signal} using {', '.join(self.organs)}"
    
    class TemporalLobe:
    def __init__(self):
        self.auditory_cortex = AuditoryCortex()

    def handle(self, signal):
        if "hear" in signal or "sound" in signal:
            return self.auditory_cortex.process_auditory_signal(signal)
        return f"Temporal lobe general auditory processing for {signal}"

class AuditoryCortex:
    def process_auditory_signal(self, signal):
        return f"Auditory cortex interpreting auditory data for {signal}"
    
    class EarSystem:
    def __init__(self):
        self.parts = ['outer ear', 'middle ear', 'inner ear']

    def capture_sound(self, signal):
        return f"Ear system ({', '.join(self.parts)}) capturing sound: {signal}"
    
    class OccipitalLobe:
    def __init__(self):
        self.visual_cortex = VisualCortex()

    def handle(self, signal):
        if "see" in signal or "visual" in signal:
            return self.visual_cortex.process_visual_signal(signal)
        return f"Occipital lobe general visual processing for {signal}"

class VisualCortex:
    def process_visual_signal(self, signal):
        return f"Visual cortex interpreting visual data for {signal}"
    
class CentralNervousSystem:
    def __init__(self):
        self.brain = Brain()
        self.spinal_cord = SpinalCord()
        self.skeletal_system = SkeletalSystem()
        self.muscular_system = MuscularSystem()
        self.digestive_system = DigestiveSystem()
        self.endocrine_system = EndocrineSystem()

    def process_signal(self, signal):
        print(f"\nProcessing signal in CNS: {signal}")
        brain_response = self.brain.process_signal(signal)
        spinal_response = self.spinal_cord.relay_signal(signal)
        skeletal_response = self.skeletal_system.respond_to_signal(signal)
        muscular_response = self.muscular_system.respond_to_signal(signal)
        digestive_response = self.digestive_system.respond_to_signal(signal)
        endocrine_response = self.endocrine_system.respond_to_signal(signal)
        return {
            'brain_response': brain_response,
            'spinal_response': spinal_response,
            'skeletal_response': skeletal_response,
            'muscular_response': muscular_response,
            'digestive_response': digestive_response,
            'endocrine_response': endocrine_response
        }

# --- BRAIN AND SUBCOMPONENTS ---

class Brain:
    def __init__(self):
        self.cerebrum = Cerebrum()
        self.cerebellum = Cerebellum()
        self.brainstem = Brainstem()

    def process_signal(self, signal):
        cerebrum_output = self.cerebrum.process(signal)
        cerebellum_output = self.cerebellum.coordinate(signal)
        brainstem_output = self.brainstem.maintain_vitals(signal)
        return {
            'cerebrum': cerebrum_output,
            'cerebellum': cerebellum_output,
            'brainstem': brainstem_output
        }

class Cerebrum:
    def __init__(self):
        self.frontal = FrontalLobe()
        self.parietal = ParietalLobe()
        self.temporal = TemporalLobe()
        self.occipital = OccipitalLobe()

    def process(self, signal):
        return {
            'frontal_lobe': self.frontal.handle(signal),
            'parietal_lobe': self.parietal.handle(signal),
            'temporal_lobe': self.temporal.handle(signal),
            'occipital_lobe': self.occipital.handle(signal)
        }

class FrontalLobe:
    def handle(self, signal):
        return f"Frontal lobe decision-making for {signal}"

class ParietalLobe:
    def handle(self, signal):
        return f"Parietal lobe sensory integration for {signal}"

class TemporalLobe:
    def handle(self, signal):
        return f"Temporal lobe auditory processing for {signal}"

class OccipitalLobe:
    def handle(self, signal):
        return f"Occipital lobe visual processing for {signal}"

class Cerebellum:
    def coordinate(self, signal):
        return f"Cerebellum coordinating movement for {signal}"

class Brainstem:
    def __init__(self):
        self.midbrain = Midbrain()
        self.pons = Pons()
        self.medulla = MedullaOblongata()

    def maintain_vitals(self, signal):
        return {
            'midbrain': self.midbrain.handle(signal),
            'pons': self.pons.handle(signal),
            'medulla': self.medulla.handle(signal)
        }

class Midbrain:
    def handle(self, signal):
        return f"Midbrain managing reflexes for {signal}"

class Pons:
    def handle(self, signal):
        return f"Pons linking cerebrum and cerebellum for {signal}"

class MedullaOblongata:
    def handle(self, signal):
        return f"Medulla regulating heart rate and breathing for {signal}"

# --- OTHER SYSTEMS ---

class SpinalCord:
    def relay_signal(self, signal):
        return f"Spinal cord relaying {signal}"

class SkeletalSystem:
    def __init__(self):
        self.bones = ['skull', 'spine', 'ribs', 'limbs']

    def respond_to_signal(self, signal):
        if "movement" in signal:
            return self.move(signal)
        return f"Skeletal system stable for {signal}"

    def move(self, command):
        return f"Skeletal system moving: {command} with {', '.join(self.bones)}"

class MuscularSystem:
    def __init__(self):
        self.muscles = ['biceps', 'triceps', 'quadriceps', 'hamstrings']

    def respond_to_signal(self, signal):
        if "movement" in signal:
            return self.contract(signal)
        return f"Muscular system relaxed for {signal}"

    def contract(self, command):
        return f"Muscles {', '.join(self.muscles)} contracting for {command}"

class DigestiveSystem:
    def __init__(self):
        self.organs = ['mouth', 'esophagus', 'stomach', 'small intestine', 'large intestine']

    def respond_to_signal(self, signal):
        if "eat" in signal:
            return self.start_digestion(signal)
        if "digest" in signal:
            return self.continue_digestion(signal)
        return f"Digestive system idle for {signal}"

    def start_digestion(self, signal):
        return f"Starting digestion of {signal} using {', '.join(self.organs)}"

    def continue_digestion(self, signal):
        return f"Continuing digestion of {signal} through intestines"

class EndocrineSystem:
    def __init__(self):
        self.glands = ['pituitary', 'thyroid', 'adrenal', 'pancreas']

    def respond_to_signal(self, signal):
        if "stress" in signal:
            return self.release_hormones(signal)
        if "growth" in signal:
            return self.release_growth_hormone(signal)
        return f"Endocrine system baseline activity for {signal}"

    def release_hormones(self, signal):
        return f"Endocrine glands {', '.join(self.glands)} releasing stress hormones for {signal}"

    def release_growth_hormone(self, signal):
        return f"Pituitary releasing growth hormone for {signal}"

# --- DEMO ---

if __name__ == "__main__":
    cns = CentralNervousSystem()

    signals = [
        "pain stimulus",
        "movement: lift arm",
        "eat food",
        "digest food",
        "stress response",
        "growth signal"
    ]

    for sig in signals:
        result = cns.process_signal(sig)
        print(result)

if __name__ == "__main__":
    cns = CentralNervousSystem()

    signals = [
        "see object",
        "pain stimulus",
        "movement: lift arm",
        "eat food",
        "digest food",
        "stress response",
        "growth signal"
    ]

    for sig in signals:
        result = cns.process_signal(sig)
        print(result)

    
