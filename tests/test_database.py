from data import TestDataBase
from conftest import data_base
import pytest


class TestDB:
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.TEST_BUN_FROM_DATABASE)
    def test_available_buns_db_success(self, data_base, index_bun, bun_name, bun_price):
        data_buns = data_base.available_buns()
        assert data_buns[index_bun].get_name() == bun_name and data_buns[index_bun].get_price() == bun_price

    @pytest.mark.parametrize('index_i, type_ingredient, name_ingredient, price_ingredient',
                             TestDataBase.TEST_DATABASE_INGREDIENTS)
    def test_available_ingredients_db_success(self, data_base, index_i, type_ingredient, name_ingredient, price_ingredient):
        data_ingredients = data_base.available_ingredients()
        assert data_ingredients[index_i].get_name() == name_ingredient
        assert data_ingredients[index_i].get_type() == type_ingredient
        assert data_ingredients[index_i].get_price() == price_ingredient



