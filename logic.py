from main import *

Base.metadata.create_all(engine)


def create_icecream(name, cone, taste_id):
    taste_ice = s.query(Tastes).filter_by(id=taste_id).first()
    if taste_ice:
        if taste_ice.weight > 0:
            ice_cream = IceCream(name=name, cone=cone, taste_id=taste_id)
            s.add(ice_cream)
            taste_ice.weight -= 0.1
            s.commit()
            return ice_cream
        else:
            raise TypeError("недостаточно начинки")
    else:
        raise TypeError("Вкус не найден")


if __name__ == '__main__':
    taste = Tastes(id=5, name="черника", weight=0)
    s.add(taste)
    s.commit()
    ice = create_icecream("сигмабой", "Маленький", 5)
