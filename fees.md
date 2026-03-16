# Fees

## Reserve Factor (Interest Fee)

A percentage of all interest earned by suppliers is directed to the protocol treasury.

- **Typical value:** 10 to 20%
- **Who pays:** Effectively shared between borrowers and suppliers. Borrowers pay the full rate; suppliers receive the rate minus the reserve factor.
- **When charged:** Continuously, as interest accrues.

> **Example:** Borrow rate is 10%, reserve factor is 10%. Suppliers receive 9% APY and 1% goes to the protocol.

## Flash Loan Premium

A flat fee charged on every flash loan.

- **Default:** 9 basis points (0.09%)
- **Who pays:** The flash loan borrower.
- **When charged:** At repayment, added to the required repayment amount.

> **Example:** Flash borrow 1,000,000 USDC. Premium = 900 USDC. You must repay 1,000,900 USDC.

## Liquidation Protocol Fee

A portion of the liquidation bonus is claimed by the protocol.

- **Default:** 0.3%
- **Who pays:** Deducted from the collateral before transfer to the liquidator.
- **When charged:** During each liquidation event.

## What K2 Does Not Charge

- No deposit fees. Supplying assets is free.
- No withdrawal fees. Withdrawing your assets costs nothing beyond the standard Stellar transaction fee.
- No repayment fees. Repaying debt has no additional charge.
- No lock-up penalties. No fees for early repayment or withdrawal.

## Stellar Network Fees

Every transaction on Stellar requires a small fee paid to the network, not to K2. These fees cover the computational cost of processing your transaction on-chain, similar to gas fees on other blockchains. In practice they are tiny, typically fractions of a cent, and are paid automatically from your wallet when you initiate any action such as supplying, borrowing, repaying, or withdrawing.

## Where Do Fees Go?

All protocol fees are collected in the Treasury contract. The treasury address is configured by the pool admin and can be a multisig account for added security. Treasury funds can be used for protocol development, security, and maintenance.
