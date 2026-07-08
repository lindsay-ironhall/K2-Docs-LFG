# DEX Integration

K2 connects to Stellar's decentralized exchanges to power two features: collateral swaps and flash liquidations. You do not need to interact with any DEX directly. K2 handles it automatically as part of the transaction.

## Collateral Swap

A collateral swap lets you switch your collateral from one asset to another in a single transaction, without needing to manually withdraw, swap, and re-supply. For example, swapping your XLM collateral to USDC collateral happens in one step. Either the whole thing succeeds or nothing changes and your position is left untouched.

Things to know:

* You set a minimum amount you are willing to receive from the swap. If the DEX cannot meet that minimum due to price movement or low liquidity, the transaction fails and your position is unchanged. This protects you from unexpected losses on the swap.
* A small protocol fee is taken from the swap output before the new collateral is supplied on your behalf.
* Your health factor is checked after the swap. If the new collateral would leave your position at risk of liquidation, the transaction is rejected before anything changes.
* Both assets must be supported reserves in the protocol.

## Flash Liquidation

Flash liquidations are a tool for liquidators, not regular users. They allow a liquidator to repay your debt, seize your collateral, and swap it back to settle everything — all in one transaction with no upfront capital required on their part. From your perspective the outcome is the same as a standard liquidation: your debt is reduced and an equivalent value of collateral is taken, plus the liquidation bonus.

## Supported DEXes

K2 supports Soroswap, Sushi and Aquarius. Both are limited to direct asset pairs. There is no multi-hop routing. If a direct trading pair between your two assets does not exist on the chosen DEX, the swap will fail.
