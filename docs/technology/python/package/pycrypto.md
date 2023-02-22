# crypto

## 背景知识

- （1）**AES** 是高级加密标准(**Advanced Encryption Standard**)的缩写，**AES** 是最常见的对称加密算法。

    > **对称加密算法** 也就是`加密`和`解密`用相同的密钥，同一个秘钥即用来加密，也用来解密。

    关于加密解密的原理可以搜索一下相关的文章。

    > **RSA** 是一种典型的`非对称密钥密码`体制，从`加密密钥`和`解密密钥`中的任何一个推导出另一个在计算上是不可行的。`RSA`的安全性建立在 **“大数分解和素性检测”** 这一著名数论难题的基础上。
    >
    > 公钥对可以完全公开，不需要进行保密，但必须提供完整性检测机制以保证不受篡改；
    >
    > 私钥由用户自己保存。通信双方无需实现交换密钥就可以进行保密通信。

- （2）RSA密码体制算法如下：

    由用户选择两个互异并且距离较远的大素数`p`和`q`；

    计算`n=p×q`和`f(n)=(p-1)×(q-1)`；

    选择正整数`e`，使其与`f(n)`的最大公约数为`1`；

    然后计算正整数`d`，使得`e × d`对`f(n)`的余数为`1`，即`e×d≡1 mod f(n)`，最后销毁`p`和`q`。

    经过以上步骤，得出公钥对`(n,e)`和私钥对`(n,d)`。

    设`M`为明文，`C`为对应的密文，

    则加密变换为：`C=M^e mod n`；

    解密变换为：`M=C^d mod n`。

## PyCrypto - Python 密码学工具包

> **Python 密码学工具包 (pycrypto)**
>
> **注意**: 该软件不再维护。参考:  <https://www.pycrypto.org/>
>
> **pycrypto** 历史链接
>
> ⚠️ PyCrypto 2.x 未维护。已过时且包含安全漏洞。以下内容仅供参考。
>
> - [API 文档](https://www.pycrypto.org/api/)（epydoc 输出）
> - [PyCrypto 概述](https://www.pycrypto.org/doc/)（从[Doc/pycrypto.rst 构建](https://github.com/pycrypto/pycrypto/blob/master/Doc/pycrypt.rst)）
> - [源代码存储库](https://github.com/pycrypto/pycrypto) (GitHub)
> - [发布压缩包](https://www.pycrypto.org/pub/dlitz/crypto/pycrypto/)
> - [邮件列表存档](https://lists.dlitz.net/pipermail/pycrypto/)（[本地快照](https://www.pycrypto.org/pipermail/pycrypto/)）
> - [Pypi](https://pypi.org/project/pycrypto/)
>
> 这是安全散列函数（如 SHA256 和 RIPEMD160）和各种加密算法（AES、DES、RSA、ElGamal 等）的集合。
>
> **请选择以下选项之一**：
>
> - Cryptography: <https://cryptography.io/>
>   - 推荐用于新应用
>   - 较新的 API，陷阱较少。
>   - [API 文档](https://cryptography.io/)
>   - [GitHub](https://github.com/pyca/cryptography)
>   - [Pypi](https://pypi.org/project/cryptography)
> - PyCryptodome: <https://www.pycryptodome.org/>
>   - 推荐用于依赖 PyCrypto 的现有软件。
>   - PyCrypto 的分叉。大多数应用程序应该在未经修改的情况下运行。
>   - [API 文档](https://www.pycryptodome.org/)
>   - [GitHub](https://github.com/Legrandin/pycryptodome)
>   - [Pypi](https://pypi.org/project/pycryptodome)

## 老版本AES的ECB模型加密示例

```python
import base64
from Crypto.Cipher import AES

class AesEncry(object):
    key = "U%56#o#u$jk0ffds".encode('utf-8')  # aes秘钥
    mode = AES.MODE_ECB
    cryptos = AES.new(key, mode)

    def decrypt(self, text):
        decode_base64 = base64.decodebytes(text.encode("utf-8"))
        plain_text = self.cryptos.decrypt(decode_base64)
        return self.uncode_chars(plain_text.decode("utf-8"))

    @staticmethod
    def uncode_chars(data):
        nCount = ord(data[-1])
        for i in data[-nCount:]:
            if ord(i) != nCount:
                return data
        return data[:-nCount]

    def encrypt(self, data):
        BLOCK_SIZE = 16
        pad = lambda s: (
            s
            + (BLOCK_SIZE - len(s) % BLOCK_SIZE)
            * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
        )
        text = pad(str(data))
        cipher_text = self.cryptos.encrypt(text.encode("utf-8"))
        # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为base64进制字符串
        return base64.encodebytes(cipher_text).decode("utf-8")


## 对应的较新的使用 PyCryptodome 的加密方式

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
BLOCK_SIZE = 32 # Bytes
 
key = 'abcdefghijklmnop'
cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
msg = cipher.encrypt(pad(b'hello', BLOCK_SIZE))
print(msg.hex())

decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
msg_dec = decipher.decrypt(msg)
print(unpad(msg_dec, BLOCK_SIZE))

```

## 使用cryptography进行AES-256-ECB加密

原文: <https://gist.github.com/tcitry/df5ee377ad112d7637fe7b9211e6bc83>

```python
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from django.utils.encoding import force_bytes, force_text

SECRET_KEY = "hellomotherfucker"
value = force_bytes("12345678901234567890")

backend = default_backend()
key = force_bytes(base64.urlsafe_b64encode(force_bytes(SECRET_KEY))[:32])


class Crypto:

    def __init__(self):
        self.encryptor = Cipher(algorithms.AES(key), modes.ECB(), backend).encryptor()
        self.decryptor = Cipher(algorithms.AES(key), modes.ECB(), backend).decryptor()

    def encrypt(self):
        padder = padding.PKCS7(algorithms.AES(key).block_size).padder()
        padded_data = padder.update(value) + padder.finalize()
        encrypted_text = self.encryptor.update(padded_data) + self.encryptor.finalize()
        return encrypted_text

    def decrypt(self, value):
        padder = padding.PKCS7(algorithms.AES(key).block_size).unpadder()
        decrypted_data = self.decryptor.update(value)
        unpadded = padder.update(decrypted_data) + padder.finalize()
        return unpadded


if __name__ == '__main__':
    print('>>>>>>>>>>>')
    crypto = Crypto()
    text = force_text(base64.urlsafe_b64encode(crypto.encrypt()))
    print(text)
    print('<<<<<<<<<<<<<')
    text = force_text(crypto.decrypt(base64.urlsafe_b64decode(text)))
    print(text)
```
