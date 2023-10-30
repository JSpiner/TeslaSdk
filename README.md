# TeslaSdk
[![PyPI version](https://badge.fury.io/py/teslasdk.svg)](https://badge.fury.io/py/teslasdk)

This is an unofficial project that implements the official Tesla SDK into multiple languages/platforms.

| Language/Platform | http api | ble api | docs |
| -- | -- | -- | -- |
| python | ✅ | ❌ | [docs](./python/README.md) |
| js | planning | ❌ | |
| kotlin / Android | planning | planning | |
| swift / iOS | need contribute | need contribute | |

# Authentication
### Create partner authentication key pair
This requires a key that satisfies the PEM-encoded EC public key using the secp256r1 curve (prime256v1) specification.

1. create private key

```bash
$ openssl ecparam -name prime256v1 -genkey -noout -out com.tesla.3p.private-key.pem
```

2. create public key from private key
```bash
$ openssl ec -in com.tesla.3p.private-key.pem -pubout -out com.tesla.3p.public-key.pem
```

3. serve your public key to `https://<your domain>/.well-known/appspecific/com.tesla.3p.public-key.pem`

