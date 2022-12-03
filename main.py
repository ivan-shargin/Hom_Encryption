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
        print(self.key)
        non_zero_key_ind = np.nonzero(self.key) 
        i = np.random.choice(non_zero_key_ind[0])
        print(i)        
        
        ciphertext[i] = 0
        ciphertext[i] = open_message + self.noise - np.dot(ciphertext, self.key)
        ciphertext[i] = ciphertext[i] % 2
        if ciphertext[i] >= 1:
            ciphertext[i] = ciphertext[i] - 2
        
        
        print(ciphertext)
        print(np.dot(ciphertext, self.key))
        return Message(ciphertext)

    def decode(self, message):
        # print(np.dot(message.value, self.key))

        # print(np.dot(message.value, self.key) % 2)
        return np.rint(np.dot(message.value, self.key) % 2)


if __name__ == '__main__':
    encoder = Encoder(5, 0.1)
    m_1 = 0
    m_2 = 0
    message_1 = encoder.encode(m_1)
    print("decode-open message")

    print(encoder.decode(message_1))
    #message_2 = encoder.encode(m_2)

    #print(encoder.decode(message_1.hom_add(message_2)))
