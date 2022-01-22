import numpy as np
from random import randint, choices, choice, sample


class Generator:
    def __init__(self, msg="", debug=False):
        self.__msg = msg
        self.__symbols = None
        self.__debug = debug

    @staticmethod
    def guide(msg):

        start = randint(0, 4)
        jump = randint(2, len(msg) // 2)
        index = np.arange(len(msg))[start::jump].tolist()

        return {"Start": start, "Jump": jump, "Index": index}

    @staticmethod
    def table():
        rng = {"Fancy": sample(["!", "@", "#", "$", "%", "&", "*", "~", "+", "_", "?",
                                "=", ";", ">", "<"], 15),

               "Small": sample(["!", "@", "#", "$", "%", "&", "*", "~", "^", ".", ","], 11),

               "Medium": sample(["!", "@", "#", "$", "%", "&", "*", "~", "^", ".", ",",
                                 "(", ")", "[", "]", "{", "}", ":", ";", "+", "-", "_",
                                 "?", "="], 24),

               "Big": sample(["!", "@", "#", "$", "%", "&", "*", "~", "^", ".", ",",
                              "(", ")", "[", "]", "{", "}", ":", ";", "+", "-", "_",
                              "?", "=", ">", "<", "∆", "π", "∑", "μ", "λ", "β", "δ",
                              "φ", "ω"], 35)
               }

        return rng

    def phrase(self):
        self.__symbols = self.table()
        symbol_list = choice(list(self.__symbols))

        upper_index = self.guide(self.__msg)  # Uppercase
        symbol_index = self.guide(self.__msg)  # Special characters

        rng_upper = randint(9, 9945)
        rng_symbol = randint(9, 9945)

        upper_msg = ""
        new_msg = ""

        for pos in range(len(self.__msg)):

            if pos in upper_index["Index"]:
                upper_msg += str(self.__msg)[pos].upper()

            else:
                upper_msg += str(self.__msg)[pos]

        for pos in range(len(self.__msg)):

            if pos in symbol_index["Index"]:
                new_msg += str(upper_msg)[pos] + "".join((choices(self.__symbols[symbol_list], k=randint(1, 3))))
            else:
                new_msg += str(upper_msg)[pos]

        num_upper = str(sum(upper_index["Index"]) + rng_upper)
        num_symbol = str(sum(symbol_index["Index"]) + rng_symbol)
        password = num_upper + new_msg + num_symbol

        if self.__debug:
            return f"""
| >-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O>
|Frase:{self.__msg}
|Senha:{password}
|Tamanho:{len(password)}
| >-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O> 

|Tabela:{symbol_list}

|Sequência de letras minusculas
|Começa na posição:{upper_index["Start"]}
|Pulos:{upper_index["Jump"]}
|Todas posições:{upper_index["Index"]}
|Numero aleatório:{rng_upper}

|Sequência de símbolos
|Começa na posição:{symbol_index["Start"]}
|Pulos:{symbol_index["Jump"]}
|Todas posições:{symbol_index["Index"]}
|Numero aleatório:{rng_symbol}
"""
        else:
            return f"""
>-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O>
Frase:{self.__msg}
Senha:|| {password} ||
Tamanho:{len(password)}
>-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O> >-|-|-O> 
"""


if __name__ == '__main__':
    gen = Generator("batata")
    for loop in range(5):
        print(gen.phrase())
