from dataclasses import dataclass
import constant
from organisationunit import OrganisationUnit, OrganisationUnitConfig

def calculate_membership_fee(rent_amount: int, rent_period: str, organisation_unit: OrganisationUnit) -> int:
    """
    Calculates the membership fee based on the rent amount, rent period, and organisation unit.

    Args:
        rent_amount (int): The rent amount in pence.
        rent_period (str): The rent period, which should be 'week' or 'month'.
        organisation_unit (OrganisationUnit): The organisation unit.

    Returns:
        int: The membership fee which has been calculated in pence.

    Raises:
        ValueError: If the rent period is invalid, or if the rent amount is outside the valid range for the rent period.
    """
    if rent_period == 'week':
        if rent_amount < constant.MIN_RENT_PER_WEEK or rent_amount > constant.MAX_RENT_PER_WEEK:
            raise ValueError("Rent amount must be between £25 and £2,000.")
    elif rent_period == 'month':
        if rent_amount < constant.MIN_RENT_PER_MONTH or rent_amount > constant.MAX_RENT_PER_MONTH:
            raise ValueError("Rent amount must be between £110 and £8,660.")
        rent_amount = rent_amount / 4
    else:           # if the rent period is not 'week' or 'month', then it is invalid
        raise ValueError("Invalid rent period.")
    rent_amount = max(rent_amount, constant.MIN_MEMBERSHIP_FEE)
    vat = constant.VAT_PERCENTAGE * rent_amount
    membership_fee = rent_amount + vat

    config = organisation_unit.get_hierarchy_config()
    if config is not None and config.has_fixed_membership_fee:
        membership_fee = config.fixed_membership_fee_amount

    return membership_fee






















