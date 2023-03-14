from dataclasses import dataclass

@dataclass
class OrganisationUnitConfig:
    """
    A configuration object for an organisation unit.

    Attributes:
        has_fixed_membership_fee (bool): True if the organisation unit has a fixed membership fee, False otherwise.
        fixed_membership_fee_amount (int): Fixed membership fee amount (in pence).
    """
    has_fixed_membership_fee: bool
    fixed_membership_fee_amount: int

@dataclass
class OrganisationUnit:
    """
    An organisation unit.

    Attributes:
        name (str): The name of the organisation unit.
        config (OrganisationUnitConfig): The configuration for the organisation unit, if any.
        parent (OrganisationUnit): The parent organisation unit, if any.

    """
    name: str
    config: OrganisationUnitConfig = None
    parent: 'OrganisationUnit' = None

    def get_hierarchy_config(self):
        """
        Returns the configuration for the organisation unit, and checks any parent organisation units.

        Returns:
            OrganisationUnitConfig: The configuration for the organisation unit.
        """
        if self.config:
            return self.config
        if self.parent is None:
            return None
        return self.parent.get_hierarchy_config()

