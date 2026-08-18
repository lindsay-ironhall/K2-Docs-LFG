# Contract Addresses

Contract addresses for the K2 Earn Market (earnUSDC/USDC) on mainnet.

### Earn Market Contracts

Contracts deployed for the earn market only.

| Name                        | Address                                                    |
| --------------------------- | ---------------------------------------------------------- |
| `router`                    | `CDWPVHKB2O4D2SX42EQMX7YFHZHOART4LZUNNE5XZE72L7BUKTPF6TZE` |
| `configurator`              | `CDAZUO5AHUSP7ENGHBNXIQFLTDSF4CJN2V3AOOB2LVED43QF3FHVQXW6` |
| `incentives`                | `CCRDMPUFJPXYPR24JN6DRAP4FICYDUNI74V6N4P62ZXJX35WQG4ZDXH6` |
| `interest_rate`             | `CCMYQHC3IMROZKFD2KSW6XRQVST7OAI3OW7IQLTUFHMNTORUOKDFHEZO` |
| `earnusdc_composite_oracle` | `CD5HZWK6UQEVRKXKYYTWGT3ADIYVSZ4ZJNK6EFMNT2FADGCVTEZZHS2Y` |

The `earnusdc_composite_oracle` prices earnUSDC/USD as RedStone USDC/USD multiplied by the vault NAV (`convert_to_assets`).

### Reserve Token Contracts

| Market     | Underlying                                                 | aToken                                                     | Debt Ledger                                                |
| ---------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `USDC`     | `CCW67TSZV3SSS2HXMBQ5JFGCKJNXKZM7UQUWUZPUTHXSTZLEO7SJMI75` | `CBUXPT7VJO2NABYDL5Q5NSHG2KNAVS5OCZQS7PXNSVTDXO5JSYB5IS7X` | `CDVYJRIAHEZWYOQUG4FDU7HZ7UU3RGRLPZ7NXQ54UBAURYXFC72KA44F` |
| `earnUSDC` | `CCL3WITWFFXIHV2I52ECV5DPIEOFSTU3PBPR53ILPLF2IP5KHECXRUTY` | TBA                                                        | TBA                                                        |

The keEarnUSDC aToken and its debt ledger will be added once deployed.

### Shared Contracts

These are the same instances used by the main and isolated markets.

| Name                     | Address                                                    |
| ------------------------ | ---------------------------------------------------------- |
| `price_oracle`           | `CCHRZE2K5TCERZLDO5IXDUWUKLRPVE72DI3TDF2RP6EQKEW6BNOMQRMU` |
| `redstone_batch_adapter` | `CA526Y2NQWGWVVQ7RFFPGAZMU66PSYJ3UC2MTVAV4ZU7OM5BOPHDXUSG` |
| `treasury`               | `CCQ4J5VLQHM2ORP4K7GBVAJJPK5SGG23DH4RD7QEHAZDHTN7JNESNXKZ` |
| `soroswap_router`        | `CAG5LRYQ5JVEUI5TEID72EYOVX44TTUJT5BQR2J6J77FH65PCCFAJDDH` |
| `soroswap_factory`       | `CA4HEQTL2WPEUYKYKCDOHCDNIV4QHNJ7EL4J4NQ6VADP7SYHVRYZ7AW2` |
| `volta_vault`            | `CC4UQND4XSP5MBHYOKGGJZQRONSTSJ3OF2EPEGA5QMCDCCZFLAE43BWJ` |
| `emergency_admin`        | `GBHSESA2MPRDVJ5UMGU2Q4SQKBMEQKIGABRMA2ARWNKTUAQRVZCUH7L2` |

### External Contracts

The earnUSDC vault is operated by Gami/Upshift, a third party. It serves as both the token contract and the NAV source, with 13 decimals.

| Name             | Address                                                    |
| ---------------- | ---------------------------------------------------------- |
| `earnusdc_vault` | `CCL3WITWFFXIHV2I52ECV5DPIEOFSTU3PBPR53ILPLF2IP5KHECXRUTY` |
