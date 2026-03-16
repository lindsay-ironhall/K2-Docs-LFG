# Flash Loans

Flash loans let you borrow assets without any collateral, as long as you return the borrowed amount plus a small fee within the same transaction. If you do not repay, the entire transaction is reversed as if it never happened. No funds are at risk.

## How It Works

1. Borrow any available asset from K2 with no collateral needed.
2. Execute your logic (arbitrage, liquidation, collateral swap, etc.).
3. Repay the borrowed amount plus a premium (default: 0.09%).
4. If repayment does not happen, the entire transaction is rolled back.

> **Example:** You flash borrow 100,000 USDC, use it to perform an arbitrage trade that nets 500 USDC profit, then repay 100,090 USDC (the 100,000 principal plus 90 USDC premium). You keep 410 USDC profit.

## Who Are Flash Loans For?

Flash loans are primarily a tool for developers and sophisticated users running automated strategies. Common use cases:

- **Arbitrage.** Exploit price differences across DEXes.
- **Liquidation.** Borrow the debt asset to liquidate an undercollateralized position without having capital upfront.
- **Collateral swaps.** Change your collateral type in a single transaction.

## Flash Loan Availability

Flash loans are not available for every asset. Each reserve has flash loans independently enabled or disabled. The protocol also has a global switch that can disable all flash loans at once. Currently all configured reserves have flash loans enabled.
