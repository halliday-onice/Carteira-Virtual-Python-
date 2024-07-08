EXCHANGES = {
      "USD": {
            "BRL": 5.4,
            "EUR": 0.92
      },
      "BRL": {
            "USD": 1/5.4,
            "EUR": 1/ 5.87
      },
      "EUR": {
            "USD": 0.92,
            "BRL": 5.87
      }
}

def get_exchange(fromcode, tocode):
      return EXCHANGES[fromcode][tocode]