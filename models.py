import math

class Transfer:
    def __init__(self, r1, r2, vt, m1, m2):
        self.G = 6.67e-11
        
        self.r1 = r1
        self.r2 = r2
        self.vt = vt
        self.m1 = m1
        self.m2 = m2
                
        self.v1 = math.sqrt(self.G * self.m1 / self.r1)
        self.E1 = -self.G * self.m1 / (2 * self.r1)
        self.v2 = math.sqrt(self.G * self.m2 / self.r2)
        self.E2 = -self.G * self.m2 / (2 * self.r2)

    def transfer(self):
        self.a = (self.r1 + self.r2) / 2
        E = -self.G * (self.m1 + self.m2) / (2 * self.a)
        e = math.sqrt(1 + (2 * E * self.a**2) / (self.G * (self.m1 + self.m2)))
        theta_transfer = math.acos((self.a * (1 - (self.r1 / self.a))) / (self.r1 * e))

        v1_transfer = math.sqrt((2 * (self.E1 + (self.G * self.m1 / self.r1))) - (2 * self.G * self.m1 / (self.r1 + self.r2)))
        v2_transfer = math.sqrt((2 * (self.E2 + (self.G * self.m2 / self.r2))) - (2 * self.G * self.m2 / (self.r1 + self.r2)))

        deltaV = math.sqrt((v1_transfer**2) + (v2_transfer**2) - (2 * v1_transfer * v2_transfer * math.cos(theta_transfer)))

        # Perform the maneuver at the transfer point using deltaV
        # Adjust spacecraft's trajectory to match the new orbit

        return deltaV


# Example usage
r1 = 100000  # Initial radius (in meters)
r2 = 200000  # Final radius (in meters)
vt = 1000    # Velocity at transfer point (in meters per second)
m1 = 5.972e24  # Mass of primary body (e.g., Earth) (in kilograms)
m2 = 1000    # Mass of secondary body (e.g., spacecraft) (in kilograms)

transfer = Transfer(r1, r2, vt, m1, m2)
deltaV = transfer.transfer()

print("Delta V required for Hohmann transfer:", deltaV)
