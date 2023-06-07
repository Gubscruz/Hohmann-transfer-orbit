import math

class DeltaVs:
    def __init__(self):
        self.R1 = 1496 * 1e8
        self.R2 = 2279 * 1e8
        self.GM = 1.327 * 1e20
        self.P1 = 365.25 * 86400
        self.P2 = 686.68 * 86400
        self.a_transf = (self.R1 + self.R2) / 2
        self.p_transf = math.sqrt(4 * math.pi**2 * self.a_transf**3 / self.GM)

    def transfer_velocity(self):
        v1 = 2 * math.pi * self.R1 / self.P1
        v2 = 2 * math.pi * self.R2 / self.P2
        vpi = (((2 * math.pi * self.a_transf) / self.p_transf) *
                math.sqrt((2*self.a_transf/self.R1) - 1))
        vap = (((2 * math.pi * self.a_transf) / self.p_transf) *
                math.sqrt((2*self.a_transf/self.R2) - 1))
        impulse1 = vpi - v1
        impulse2 = v2 - vap
        return impulse1, impulse2
    
    def transfer_time(self):
        return 0.5*self.p_transf/86400
delta_vs = DeltaVs()
print(delta_vs.transfer_velocity())
print(delta_vs.transfer_time())
