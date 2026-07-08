# Reserves and Interest Rates

## What is a Reserve?

A reserve is a liquidity pool for a single asset. When users supply USDC, it goes into the USDC reserve. When someone borrows USDC, it comes from that same reserve. Each reserve independently tracks its supply, debt, interest rates, and configuration. K2 supports up to 64 reserves simultaneously.

## How Interest Rates Work

K2 uses a variable rate model where rates change automatically based on supply and demand. There are no fixed-rate loans.

The core mechanism is simple: the more an asset is borrowed, the higher the rates go. This is driven by the utilization rate, which is the percentage of the reserve that is currently lent out.

> **Utilization Rate = Total Borrowed / Total Supplied**

## The Rate Curve

Interest rates follow a two-slope curve with a kink point at the optimal utilization (typically 80%):

**Below optimal utilization.** Rates rise gently. The protocol encourages borrowing to improve capital efficiency.

**Above optimal utilization.** Rates rise steeply. The protocol discourages excess borrowing and encourages repayment to maintain liquidity for withdrawals.

## Supply Rate vs. Borrow Rate

Borrowers pay the variable borrow rate on their debt.

Suppliers earn a fraction of what borrowers pay. The supply rate is calculated as:

> **Supply Rate = Borrow Rate x Utilization x (1 minus Reserve Factor)**

> **Example:** Borrow rate is 10%, utilization is 80%, reserve factor is 20%. Supply rate = 10% x 80% x 80% = 6.4% APY for suppliers.

## How Interest Accrues

Interest does not update every second. Instead, K2 uses an index-based system:

* Each reserve has a liquidity index (for suppliers) and a borrow index (for borrowers). Both indices grow over time and produce a compounding effect. The difference is in the math used per update: the liquidity index applies a linear approximation per interval, while the borrow index uses the full compound formula. In practice the difference is negligible for most users over typical holding periods. What matters is that both your supply balance and your debt grow over time, and neither requires any manual action.
* When you check your balance, it is calculated as your scaled balance multiplied by the current index.
* The index is updated on the first interaction with a reserve in any given ledger. If multiple transactions hit the same reserve in the same ledger, only the first one triggers an index update. Subsequent ones use the already-current index.

This is more efficient than updating every user's balance individually. One index update effectively updates everyone's balance at once.
