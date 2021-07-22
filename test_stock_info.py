from stock_info import stock_info
import unittest


class TestStockInfo(unittest.TestCase):

    def test_valores_validos(self):
        self.assertEqual(stock_info('aapl', start='2000-01-01', end='2000-01-05'),
                         {'Open': {'2000-01-03': 0.9363840222358704, '2000-01-04': 0.966517984867096},
                          'High': {'2000-01-03': 1.004464030265808, '2000-01-04': 0.9877229928970337},
                          'Low': {'2000-01-03': 0.9079239964485168, '2000-01-04': 0.9034600257873535},
                          'Close': {'2000-01-03': 0.9994419813156128, '2000-01-04': 0.9151790142059326},
                          'Adj Close': {'2000-01-03': 0.859423041343689, '2000-01-04': 0.786965012550354},
                          'Volume': {'2000-01-03': 535796800, '2000-01-04': 512377600}})
        self.assertEqual(stock_info('mmm', start='2000-01-01', end='2000-01-05', only='open'),
                         {'Open': {'2000-01-03': 48.03125, '2000-01-04': 46.4375}})
        self.assertEqual(stock_info('v', start='2010-01-01', end='2010-01-05', only='close'),
                         {'Close': {'2010-01-04': 22.03499984741211}})

    def test_acciones_inexistentes(self):
        self.assertEqual(stock_info('asdasdas', start='2000-01-01', end='2000-01-05'),
                         {'Open': {}, 'High': {}, 'Low': {}, 'Close': {}, 'Adj Close': {}, 'Volume': {}})
        self.assertEqual(stock_info('asdasdas', start='2000-01-01', end='2000-01-05'),
                         {'Open': {}, 'High': {}, 'Low': {}, 'Close': {}, 'Adj Close': {}, 'Volume': {}})

    def test_acciones_fecha_sin_info(self):
        self.assertFalse(bool(stock_info('v', start='2000-01-01', end='2000-01-05', only='close')['Close']))


if __name__ == '__main__':
    unittest.main()
