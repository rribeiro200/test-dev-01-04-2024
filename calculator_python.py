from abc import ABC, abstractmethod

class TariffStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, consumption: float) -> float:
        pass

    @abstractmethod
    def calculate_coverage(self, consumption: float) -> float:
        pass

class ResidentialTariff(TariffStrategy):
    def calculate_discount(self, consumption: float) -> float:
        if consumption < 10000:
            return 0.18
        elif 10000 <= consumption <= 20000:
            return 0.22
        else:
            return 0.25

    def calculate_coverage(self, consumption: float) -> float:
        if consumption < 10000:
            return 0.9
        elif 10000 <= consumption <= 20000:
            return 0.95
        else:
            return 0.99

class CommercialTariff(TariffStrategy):
    def calculate_discount(self, consumption: float) -> float:
        if consumption < 10000:
            return 0.16
        elif 10000 <= consumption <= 20000:
            return 0.18
        else:
            return 0.22

    def calculate_coverage(self, consumption: float) -> float:
        if consumption < 10000:
            return 0.9
        elif 10000 <= consumption <= 20000:
            return 0.95
        else:
            return 0.99

class IndustrialTariff(TariffStrategy):
    def calculate_discount(self, consumption: float) -> float:
        if consumption < 10000:
            return 0.12
        elif 10000 <= consumption <= 20000:
            return 0.15
        else:
            return 0.18

    def calculate_coverage(self, consumption: float) -> float:
        if consumption < 10000:
            return 0.9
        elif 10000 <= consumption <= 20000:
            return 0.95
        else:
            return 0.99

class DiscountContext:
    def __init__(self, strategy: TariffStrategy):
        self._strategy = strategy

    def apply_discount(self, consumption: float) -> float:
        return self._strategy.calculate_discount(consumption)

    def calculate_coverage(self, consumption: float) -> float:
        return self._strategy.calculate_coverage(consumption)
