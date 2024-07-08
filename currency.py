from exchanges import get_exchange
from utils import get_name



def make_dolar(value):
      return Currency(value, "USD")

class Currency:
      #atributos: valor, codigo (ex BRL, USD)
      def __init__(self, value: float, code: str) -> None:
            self.value = float(value)
            self.code = code.upper()
      
      def __str__(self)-> str:
            return f"{self.value: .2f} {self.code}"
      
      @property
      def name(self):
            return get_name(self.code)
      
      def convert(self, to_code):
            factor = get_exchange(self.code, to_code.upper())
            res = Currency(self.value * factor, to_code)
            return res
      
      def __add__(self, rhs):
            if self.code == rhs.code:
                  value = self.value + rhs.value
                  return Currency(value, self.code)
            #se precisar converter
            convertion = rhs.convert(self.code)
            return self + convertion
      
      def __sub__(self, rhs):
            other = -rhs
            return self + other
      
      def __neg__(self):
            return Currency(-self.value, self.code)
      
      def __mul__(self, rhs):
            return Currency(self.value * rhs, self.code)
      
      def __rmul__(self, lhs):
            return self * lhs
      
      def dolar(value):
            return Currency(value, "USD")


def test_conversion():
      moeada = Currency(250, "usd")
      euro = moeada.convert("eur")
      print(moeada)
      print(euro)


if __name__ == "__main__":
      dolar_test = Currency.dolar(1223.65)
      print(dolar_test)
      euro_coverted = dolar_test.convert("eur")
      print(euro_coverted)
