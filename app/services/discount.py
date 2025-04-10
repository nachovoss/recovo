from app.models.discount import Discount
from app.repositories import DiscountRepository


class DiscountService:
    def __init__(self, db):
        self.repo = DiscountRepository(db)

    def get_all_active_discounts(self):
        return self.repo.get_active_discounts()

    def get_all_discounts(self):
        return self.repo.get_all()

    def get_discount_by_id(self, discount_id: int):
        return self.repo.get_by_id(discount_id)

    def create_discount(self, discount_data: dict):
        new_discount = Discount(**discount_data)
        return self.repo.create(new_discount)

    def update_discount(self, discount_id: int, update_data: dict):
        discount = self.get_discount_by_id(discount_id)
        if not discount:
            return None
        return self.repo.update(discount, update_data)

    def delete_discount(self, discount_id: int):
        discount = self.get_discount_by_id(discount_id)
        if not discount:
            return False
        self.repo.delete(discount)
        return True

    def deactivate_discount(self, discount_id: int):
        discount = self.get_discount_by_id(discount_id)
        if not discount:
            return False
        self.repo.update(discount, {"active": False})
        return True
