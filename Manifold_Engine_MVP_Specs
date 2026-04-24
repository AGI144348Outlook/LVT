import numpy as np

# ==========================================
# 🌀 THE FRACTAL MANIFOLD KERNEL
# ==========================================

class Domain:
    """A spherical sub-domain within the Nexus."""
    def __init__(self, depth=0, name="Nexus_Root"):
        self.depth = depth
        self.name = name
        self.substrate = np.zeros((3, 3)) # The 3x3 core within each manifold
        self.children = {} # Nested domains (Fractal Recursion)
        
    def manifold_inward(self, sector_name):
        """Creates a new domain within the current one."""
        if sector_name not in self.children:
            self.children[sector_name] = Domain(depth=self.depth + 1, name=sector_name)
            return f"Created sub-domain '{sector_name}' at fractal depth {self.depth + 1}."
        return f"Sector '{sector_name}' already exists."

    def inject_data(self, energy):
        """Distributes energy across the local substrate."""
        self.substrate += (np.random.rand(3, 3) * energy)
        self.substrate = 1 / (1 + np.exp(-self.substrate)) # Sigmoid stability

class FractalNexus:
    def __init__(self):
        self.root = Domain()
        self.active_path = [self.root] # Navigation stack

    def current(self):
        return self.active_path[-1]

    def process(self, text):
        # 1. Action Check
        if text.startswith("manifold "):
            sector = text.replace("manifold ", "").strip()
            return self.current().manifold_inward(sector)
        
        if text.startswith("enter "):
            sector = text.replace("enter ", "").strip()
            if sector in self.current().children:
                self.active_path.append(self.current().children[sector])
                return f"Navigated into {sector}."
            return "Sector not found."

        if text == "exit":
            if len(self.active_path) > 1:
                papped = self.active_path.pop()
                return f"Exited {papped.name}. Back in {self.current().name}."
            return "Already at Nexus Root."

        # 2. Default: Inject energy into the current manifold
        energy = len(text) / 50.0
        self.current().inject_data(energy)
        return f"Substrate {self.current().name} excited. Depth: {self.current().depth}"

# ==========================================
# 🚀 THE OPERATOR INTERFACE
# ==========================================

def start_nexus():
    nexus = FractalNexus()
    print("FHCN ONLINE: Fractal Hierarchical Compression Nexus")
    print("Commands: 'manifold [name]', 'enter [name]', 'exit', or speak to inject.")
    print("-------------------------------------------------------------------")

    while True:
        path_str = " > ".join([d.name for d in nexus.active_path])
        user_input = input(f"\n[{path_str}] Operator > ")
        
        if user_input.lower() == 'quit': break
            
        result = nexus.process(user_input)
        
        print(f"\nKernel > {result}")
        print(f"Current Substrate:\n{np.round(nexus.current().substrate, 2)}")
        print(f"Sub-Domains Available: {list(nexus.current().children.keys())}")

if __name__ == "__main__":
    start_nexus()
