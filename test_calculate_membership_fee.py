import unittest
from organisationunit import OrganisationUnit, OrganisationUnitConfig
from calculate_membership_fee import calculate_membership_fee

class TestCalculateMembershipFee(unittest.TestCase):
    def test_calculate_membership_fee_with_weekly_rent_within_range(self):
        rent_amount = 100000
        rent_period = 'week'
        organisation_unit = OrganisationUnit(name='Test Organisation')
        membership_fee = calculate_membership_fee(rent_amount, rent_period, organisation_unit)
        self.assertEqual(membership_fee, 120000.0)

    def test_calculate_membership_fee_with_weekly_rent_below_range(self):
        rent_amount = 2000
        rent_period = 'week'
        organisation_unit = OrganisationUnit(name='Test Organisation')
        with self.assertRaises(ValueError):
            calculate_membership_fee(rent_amount, rent_period, organisation_unit)

    def test_calculate_membership_fee_with_weekly_rent_above_range(self):
        rent_amount = 250000
        rent_period = 'week'
        organisation_unit = OrganisationUnit(name='Test Organisation')
        with self.assertRaises(ValueError):
            calculate_membership_fee(rent_amount, rent_period, organisation_unit)

    def test_calculate_membership_fee_with_monthly_rent_within_range(self):
        rent_amount = 800000
        rent_period = 'month'
        organisation_unit = OrganisationUnit(name='Test Organisation')
        membership_fee = calculate_membership_fee(rent_amount, rent_period, organisation_unit)
        self.assertEqual(membership_fee, 240000.0)

    def test_calculate_membership_fee_with_monthly_rent_below_range(self):
        rent_amount = 10000
        rent_period = 'month'
        organisation_unit = OrganisationUnit(name='Test Organisation')
        with self.assertRaises(ValueError):
            calculate_membership_fee(rent_amount, rent_period, organisation_unit)

    def test_calculate_membership_fee_with_monthly_rent_above_range(self):
        rent_amount = 1000000
        rent_period = 'month'
        organisation_unit = OrganisationUnit(name='Test Organisation')
        with self.assertRaises(ValueError):
            calculate_membership_fee(rent_amount, rent_period, organisation_unit)

    def test_calculate_membership_fee_with_invalid_rent_period(self):
        rent_amount = 50000
        rent_period = 'year'
        organisation_unit = OrganisationUnit(name='Test Organisation')
        with self.assertRaises(ValueError):
            calculate_membership_fee(rent_amount, rent_period, organisation_unit)

    def test_calculate_membership_fee_with_fixed_membership_fee(self):
        rent_amount = 50000
        rent_period = 'month'
        config = OrganisationUnitConfig(has_fixed_membership_fee=True, fixed_membership_fee_amount=20000)
        parent_unit = OrganisationUnit(name='Parent Organisation', config=config)
        organisation_unit = OrganisationUnit(name='Test Organisation', parent=parent_unit)
        membership_fee = calculate_membership_fee(rent_amount, rent_period, organisation_unit)
        self.assertEqual(membership_fee, 20000)

if __name__ == '__main__':
    unittest.main()
