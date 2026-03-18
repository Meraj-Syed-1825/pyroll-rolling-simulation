
import numpy as np
import logging
from pyroll.core import SymmetricRollPass, Hook

VERSION = "0.1.0"

# New hooks — quantities our plugin computes
SymmetricRollPass.hitchcock_constant = Hook[float]()
SymmetricRollPass.flattened_roll_radius = Hook[float]()
SymmetricRollPass.flattening_ratio = Hook[float]()


@SymmetricRollPass.hitchcock_constant
def hitchcock_constant(self: SymmetricRollPass):
    E_roll  = 210e9
    nu_roll = 0.3
    return 16 * (1 - nu_roll**2) / (np.pi * E_roll)


@SymmetricRollPass.flattened_roll_radius
def flattened_roll_radius(self: SymmetricRollPass):
    R  = self.roll.nominal_radius
    F  = self.roll_force
    b  = self.in_profile.width
    dh = self.in_profile.height - self.gap

    if dh <= 0:
        logging.getLogger(__name__).warning(
            f"Non-positive draft in {self.label} — returning nominal radius."
        )
        return R

    return R * (1 + self.hitchcock_constant * F / (b * dh))


@SymmetricRollPass.flattening_ratio
def flattening_ratio(self: SymmetricRollPass):
    R_prime = self.flattened_roll_radius
    R       = self.roll.nominal_radius
    h       = self.in_profile.height
    return (R_prime - R) / h
