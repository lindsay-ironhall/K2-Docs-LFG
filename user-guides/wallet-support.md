---
description: Adding and viewing receipt tokens in your wallet
---

# Wallet Support

#### Viewing Receipt Tokens in Your Wallet

Receipt tokens (**aTokens**) are implemented as Soroban token contracts. Your balances are always recorded on-chain, but wallet support for displaying them varies.

**Freighter**

Freighter supports manually adding Soroban token contracts, so you can view your receipt token balances directly in your wallet.

To add a token:

1. Open Freighter.
2. Select **Add Token**.
3. Choose **Soroban Token**.
4. Paste the corresponding contract ID from the table above.
5. Confirm to add the token.

Once added, Freighter will display your balance for that token.

> **Note:** Adding a token to Freighter is a display preference only. It does not create a trustline, submit an on-chain transaction, or cost any XLM fees.

**LOBSTR**

LOBSTR does not currently support manually adding arbitrary Soroban token contracts, so aTokens may not appear in the wallet interface.

This has no effect on the functionality or security of your positions:

* Your balances and positions remain safely recorded on-chain.
* Deposits, borrowing, repayments, withdrawals, and liquidations work exactly the same.
* You can always view your balances in the K2 Lend app or verify them directly on-chain using the contract IDs above.

Current market and token contract addresses are listed at the link below.

{% content-ref url="../contracts.md" %}
[contracts.md](../contracts.md)
{% endcontent-ref %}
