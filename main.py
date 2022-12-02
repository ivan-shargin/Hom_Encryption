import numpy as np


class Message:
    """
    Encrypted message class
    """

    def __init__(self, ciphertext):
        self.value = ciphertext

    def hom_add(self, mes_2):
        assert isinstance(mes_2, Message)
        return self.value + mes_2.value

    def hom_mult(self, mes_2, encrypts_x):
        pass


class Encoder:
    def __init__(self, key, noise):
        self.key = key
        assert noise < 0.5
        self.noise = noise

    def encode(self, open_message) -> Message:
        ciphertext = 1
        return Message(ciphertext)

    def decode(self, ciphertext):
        return 1


if __name__ == '__main__':
    encoder = Encoder(1, 2)
    m_1 = 1
    m_2 = 0
    message_1 = encoder.encode(m_1)
    message_2 = encoder.encode(m_2)

    print(encoder.decode(message_1.hom_add(message_2)))
