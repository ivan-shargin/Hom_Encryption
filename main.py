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
    def __init__(self, n, max_noise):
        self.n = n
        self.max_noise = max_noise
        
        self.key = np.random.randint(2, size=n)
        self.non_zero_key_ind = np.nonzero(self.key)[0] 
        if self.non_zero_key_ind.size == 0:
            i = np.random.randint(n, size=1)[0]
            self.key[i] = 1 
        self.non_zero_key_ind = np.nonzero(self.key)[0] 
        
        assert self.max_noise < 0.5

    def encode(self, open_message, debug=False) -> Message:
        ciphertext = np.random.uniform(low=-1.0, high=1.0, size=self.n)
        self.noise = np.random.uniform(low=0.0, high=self.max_noise)
        
        if debug:
            print("Key: {}".format(self.key))
        
        print("Noise: {}".format(self.noise))
        
        i = np.random.choice(self.non_zero_key_ind)
        
        if debug:
            print("Index of cipher element to compute: {}".format(i))        
        
        ciphertext[i] = 0
        ciphertext[i] = open_message + self.noise - np.dot(ciphertext, self.key)
        ciphertext[i] = ciphertext[i] % 2
        if ciphertext[i] >= 1:
            ciphertext[i] = ciphertext[i] - 2
        
        if debug:
            print("Ciphertext: {}".format(ciphertext))
            print("Dot product of ciphertext and key: {}".format(np.dot(ciphertext, self.key)))
            
        return Message(ciphertext)

    def decode(self, message):
        return int(np.rint(np.dot(message.value, self.key) % 2))


if __name__ == '__main__':
    encoder = Encoder(10, 0.1)
    m_1 = 0
    m_2 = 1
    cipher_1 = encoder.encode(m_1, debug=True)
    cipher_2 = encoder.encode(m_2)
    print("open message_1 is {}, was decoded as {}".format(m_1, encoder.decode(cipher_1)))
    print("open message_2 is {}, was decoded as {}".format(m_2, encoder.decode(cipher_2)))

    
    
