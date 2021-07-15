from __future__ import annotations

from pydantic import BaseModel


class Outlets(BaseModel):
    count_n: int


class TotalItemsQuantity(BaseModel):
    hot_water: int
    hot_milk: int
    ginger_syrup: int
    sugar_syrup: int
    tea_leaves_syrup: int


class HotTea(BaseModel):
    hot_water: int
    hot_milk: int
    ginger_syrup: int
    sugar_syrup: int
    tea_leaves_syrup: int


class HotCoffee(BaseModel):
    hot_water: int
    ginger_syrup: int
    hot_milk: int
    sugar_syrup: int
    tea_leaves_syrup: int


class BlackTea(BaseModel):
    hot_water: int
    ginger_syrup: int
    sugar_syrup: int
    tea_leaves_syrup: int


class GreenTea(BaseModel):
    hot_water: int
    ginger_syrup: int
    sugar_syrup: int
    green_mixture: int


class Beverages(BaseModel):
    hot_tea: HotTea
    hot_coffee: HotCoffee
    black_tea: BlackTea
    green_tea: GreenTea


class Machine(BaseModel):
    outlets: Outlets
    total_items_quantity: TotalItemsQuantity
    beverages: Beverages


class DispenserConfig(BaseModel):
    machine: Machine
