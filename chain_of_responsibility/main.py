import objects as obj


if __name__ == '__main__':

    director = obj.Director()
    lider = obj.Leader()
    gerente = obj.Manager()
    ejecutivo = obj.Executive()

    director.set_successor(lider).set_successor(gerente).set_successor(ejecutivo)

    obj.main(director)
