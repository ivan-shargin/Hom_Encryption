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
        assert isinstance(mes_2, Message)
        pass


class Encoder:
    def __init__(self, n, noise):
        self.n = n
        self.key = np.random.randint(2, size=n)
        assert noise < 0.5
        self.noise = noise

    def encode(self, open_message) -> Message:
        ciphertext = np.random.uniform(low=-1.0, high=1.0, size=self.n)
        i = np.random.randint(self.n)
        ciphertext[i] = 0
        print(ciphertext)
        print(i)
        print(self.key)
        print(np.dot(ciphertext, self.key))
        ciphertext[i] = 2 + open_message + self.noise - np.dot(ciphertext, self.key)
        print(ciphertext)
        return Message(ciphertext)

    def decode(self, message):
        print(np.dot(message.value, self.key))
        print(np.dot(message.value, self.key) % 2)
        return np.rint(np.dot(message.value, self.key) % 2)


if __name__ == '__main__':
    encoder = Encoder(5, 0.1)
    m_1 = 1
    m_2 = 0
    message_1 = encoder.encode(m_1)
    print(encoder.decode(message_1))
    #message_2 = encoder.encode(m_2)

    #print(encoder.decode(message_1.hom_add(message_2)))
