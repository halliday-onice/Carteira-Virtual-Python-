from currency import Currency

class NotEnoughFundsError(Exception):
      pass


class Wallet:
      # a classe currency tem como atributo da nova classe wallet
      # a lista vazia em currencies eh pra poder não passar nada na hora de chamar a funcao
      def __init__(self, currencies = [])->None:
            self.balance = {}
            for c in currencies:
                  self.balance[c.code] = c
                  

      def __str__(self)-> str:
            if self.balance: #se o objeto
                  s = "Saldo em moeda:\n"
                  """ for c in self.balance.values():
                        s += f"{c}\n" """
                  return s + "\n".join([str(c) for c in self.balance.values()])
            return "Carteira vazia!"

      def add_to_wallet(self, value, code):
            currency = Currency(value, code)
            #eu quero adicionar em quem eu ja tenho
            
            try:
                  self.balance[code] += currency

            except KeyError:
                  #se der key error eh pq não tinha nada antes
                  self.balance[code] = currency #to criando no dicionario a chave

      def balance_in(self, code):
            balance= Currency(0, code) # crio uma novo objeto com valor zero e vou iterando, adicionando
            
            for c in self.balance.values():
                  balance += c 
            return balance
      
      def withdraw(self, value,code):
            currency = Currency(value, code)
            try:
                  aux = self.balance[code] - currency
                  if aux.value >= 0:
                        self.balance[code] = aux
                  else:
                        raise NotEnoughFundsError(f"tentando tirar  {currency}, mas tem apenas {self.balance[code]}")
            except KeyError:
                  print("{code} não disponível")

if __name__ == "__main__":
      currencies = [Currency(234, "BRL"),
                    Currency(76, "USD")]
      
      wallet = Wallet()# se eu nao colocar nada no __init__ vou ter que chamar o argumento Wallet(currencies)
      print(wallet)
      wallet.add_to_wallet(50, "BRL")
      wallet.add_to_wallet(70, "BRL")
      print(wallet)
      wallet.add_to_wallet(129.35, "USD")
      print(wallet)
      print('-' * 20)
      print(wallet.balance_in("USD"))
      

      wallet.withdraw(10, "BRL")
      print(wallet)

      wallet.withdraw(19999, "BRL")