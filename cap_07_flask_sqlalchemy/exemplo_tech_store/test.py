from TechApp import db, models
from TechApp.models import Loja
import unittest

class TechAppTestCase(unittest.TestCase):

    def setUp(self):
    	# create the database
    	db.drop_all()
    	db.create_all()

    def test_obter_lojas(self):
    	db.session.add(Loja('Macavi'))
    	db.session.add(Loja('Casas Bahia'))
    	db.session.commit()
    	lojas = models.obter_lojas()
    	self.assertEqual(len(lojas),2)
    	self.assertEqual(lojas, Loja.query.all())

    def test_inserir_loja(self):
        db.drop_all()
        db.create_all()
        count1 = len(Loja.query.filter_by(titulo = 'Leleo').all())
        models.inserir_loja(titulo = 'Leleo')
        count2 = len(Loja.query.filter_by(titulo = 'Leleo').all())
        loja = Loja.query.filter_by(titulo = 'zxc').first()
        self.assertEqual(loja, None)
        loja = Loja.query.filter_by(titulo = 'Leleo').first()
        self.assertEqual(loja.titulo, 'Leleo')
        self.assertNotEqual(count1, count2)
        self.assertEqual(count1 + 1, count2)

    def test_atualizar_loja(self):
        loja = Loja('Loja X')
        db.session.add(loja)
        db.session.commit()
        models.atualizar_loja(loja.id, 'novo nome')
        self.assertEqual(loja.titulo, 'novo nome')

    def test_remover_loja(self):
        loja = Loja('Loja X')
        db.session.add(loja)
        db.session.commit()       
        models.remover_loja(id = loja.id)
        self.assertEqual(Loja.query.get(loja.id), None)


if __name__ == '__main__':
	unittest.main()