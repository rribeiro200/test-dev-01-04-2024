import unittest
from calculator_python import (
    ResidentialTariff,
    CommercialTariff,
    IndustrialTariff,
    DiscountContext,
)

class TestTariffStrategies(unittest.TestCase):
    def test_residential_tariff_discount(self):
        residential_strategy = ResidentialTariff()
        self.assertAlmostEqual(residential_strategy.calculate_discount(5000), 0.18)
        self.assertAlmostEqual(residential_strategy.calculate_discount(15000), 0.22)
        self.assertAlmostEqual(residential_strategy.calculate_discount(25000), 0.25)

    def test_residential_tariff_coverage(self):
        residential_strategy = ResidentialTariff()
        self.assertAlmostEqual(residential_strategy.calculate_coverage(5000), 0.9)
        self.assertAlmostEqual(residential_strategy.calculate_coverage(15000), 0.95)
        self.assertAlmostEqual(residential_strategy.calculate_coverage(25000), 0.99)

    def test_commercial_tariff_discount(self):
        commercial_strategy = CommercialTariff()
        self.assertAlmostEqual(commercial_strategy.calculate_discount(5000), 0.16)
        self.assertAlmostEqual(commercial_strategy.calculate_discount(15000), 0.18)
        self.assertAlmostEqual(commercial_strategy.calculate_discount(25000), 0.22)

    def test_commercial_tariff_coverage(self):
        commercial_strategy = CommercialTariff()
        self.assertAlmostEqual(commercial_strategy.calculate_coverage(5000), 0.9)
        self.assertAlmostEqual(commercial_strategy.calculate_coverage(15000), 0.95)
        self.assertAlmostEqual(commercial_strategy.calculate_coverage(25000), 0.99)

    def test_industrial_tariff_discount(self):
        industrial_strategy = IndustrialTariff()
        self.assertAlmostEqual(industrial_strategy.calculate_discount(5000), 0.12)
        self.assertAlmostEqual(industrial_strategy.calculate_discount(15000), 0.15)
        self.assertAlmostEqual(industrial_strategy.calculate_discount(25000), 0.18)

    def test_industrial_tariff_coverage(self):
        industrial_strategy = IndustrialTariff()
        self.assertAlmostEqual(industrial_strategy.calculate_coverage(5000), 0.9)
        self.assertAlmostEqual(industrial_strategy.calculate_coverage(15000), 0.95)
        self.assertAlmostEqual(industrial_strategy.calculate_coverage(25000), 0.99)

if __name__ == '__main__':
    unittest.main()
