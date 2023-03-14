import unittest
from organisationunit import OrganisationUnit, OrganisationUnitConfig

class TestOrganisationUnit(unittest.TestCase):
    def test_get_hierarchy_config_with_no_parent(self):
        org_unit = OrganisationUnit(name='Test Org Unit')
        config = org_unit.get_hierarchy_config()
        self.assertIsNone(config)

    def test_get_hierarchy_config_with_parent(self):
        parent_config = OrganisationUnitConfig(has_fixed_membership_fee=True, fixed_membership_fee_amount=5000)
        parent_unit = OrganisationUnit(name='Parent Org Unit', config=parent_config)
        org_unit = OrganisationUnit(name='Test Org Unit', parent=parent_unit)
        config = org_unit.get_hierarchy_config()
        self.assertIsNotNone(config)
        self.assertEqual(config, parent_config)

if __name__ == '__main__':
    unittest.main()
