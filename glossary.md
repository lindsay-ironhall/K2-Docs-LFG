# Glossary

### Annual Percentage Yield (APY)

The effective yearly return on your supplied assets, accounting for interest compounding over time. Supply APY is what you earn as a lender. Borrow APY is what you pay as a borrower. Both rates are variable and change based on how much of a reserve is currently being borrowed.

### Basis Points (bps)

A unit used to express percentages precisely. 1 basis point equals 0.01%. So 500 basis points equals 5%, and 10,000 basis points equals 100%. You will see this used when describing liquidation bonuses, reserve factors, and interest rates.

### Borrow Cap

The maximum total amount of an asset that can be borrowed across the entire protocol at any one time. If the cap is reached, no further borrowing of that asset is possible until existing loans are repaid.

### Circuit Breaker

A safety mechanism on the price oracle. If an asset's price moves by more than 20% from the last recorded value in a single update, the new price is rejected and the last known good price is retained. This protects against oracle failures and price manipulation.

### Close Factor

The maximum percentage of a borrower's debt that can be repaid in a single liquidation. The default is 50%, meaning a liquidator can repay at most half of your outstanding debt in one transaction. This rises to 100% if your health factor falls below 0.5, or if your position is below $2,000 in value.

### Collateral

Assets you supply to K2 that back your borrowing. If your health factor drops below 1.0, your collateral can be seized by a liquidator to repay your debt.

### Collateral Swap

A feature that lets you switch your collateral from one asset to another in a single transaction, without needing to manually withdraw, swap, and re-supply. Your position stays open throughout.

### Debt Token

An internal token that tracks how much you owe. When you borrow an asset, a corresponding debt token is created to record your balance. It cannot be transferred. When you repay, the debt token is burned. You do not interact with debt tokens directly. They exist behind the scenes.

### Flash Liquidation

A type of liquidation where the liquidator uses a flash loan to fund the repayment, seizes the collateral, and swaps it back to repay the flash loan, all within a single transaction. This means liquidators need no upfront capital.

### Flash Loan

A loan that is borrowed and repaid within a single transaction. If the loan is not repaid by the end of the transaction, the whole thing is reversed as if it never happened. Flash loans require no collateral and are primarily used by developers and liquidators.

### Freeze

An asset state where no new supplying or borrowing is allowed, but existing positions can still be repaid and withdrawn. A frozen asset is being wound down rather than immediately shut off.

### Health Factor (HF)

A number that represents how safe your borrowing position is. It is calculated from the value of your collateral, the liquidation thresholds of your collateral assets, and the value of your debt. A health factor above 1.0 means your position is safe. Below 1.0, it becomes eligible for liquidation. The closer to 1.0 you are, the more at risk you are.

### Hypernative

The real-time on-chain monitoring service used by K2. It watches for unusual activity and potential threats 24/7, enabling the team to respond quickly to anything suspicious.

### Interest Rate Strategy

The model that determines how borrow and supply rates change based on utilization. K2 uses a two-slope model: rates rise gradually up to the optimal utilization point, then rise steeply above it to incentivize repayment and protect liquidity.

### kToken

When you supply an asset to K2, you receive a corresponding kToken at a 1:1 ratio. Your kToken balance increases automatically over time as interest accrues. When you withdraw, your kTokens are burned and you receive the underlying asset plus all earned interest.

### Liquidation

The process by which a third party (a liquidator) repays part of your debt in exchange for a portion of your collateral at a discount, when your health factor drops below 1.0. Liquidation exists to keep the protocol solvent.

### Liquidation Bonus

The premium a liquidator receives on your collateral as an incentive for performing a liquidation. The bonus varies by asset. Stablecoins carry a 5% bonus, while more volatile assets carry higher bonuses of 10 to 15%.

### Liquidation Threshold

The collateral-to-debt ratio at which your position becomes eligible for liquidation. Always higher than the LTV, creating a buffer between when you can borrow and when you can be liquidated.

### Loan-to-Value (LTV)

The maximum percentage of your collateral's value that you can borrow. For example, an 80% LTV means you can borrow up to $800 against $1,000 of collateral. LTV varies by asset.

### Oracle

A service that provides real-time asset prices to the protocol. K2 uses price oracles to calculate health factors, determine liquidation amounts, and value collateral. K2 supports Reflector and RedStone oracles, with staleness checks and a circuit breaker to protect against bad data.

### Pause

An emergency state where all operations on the protocol or a specific asset are halted. The emergency admin can pause; only the pool admin can unpause. Used in response to potential security incidents.

### Reserve

The pool of liquidity for a single asset. Each asset supported by K2 has its own reserve, which tracks available liquidity, total debt, interest rates, and configuration parameters.

### Reserve Factor

The percentage of interest earnings that go to the protocol treasury rather than to suppliers. K2 uses a 10% reserve factor for stablecoins and 20% for other assets.

### Supply Cap

The maximum total amount of an asset that can be supplied to the protocol. Once reached, no further deposits are accepted until existing suppliers withdraw.

### Utilization Rate

The percentage of a reserve's liquidity that is currently borrowed. Higher utilization means less liquidity available for withdrawals, and results in higher interest rates to encourage repayment and attract new supply.

### Variable Rate

An interest rate that changes over time based on utilization. Both supply and borrow rates in K2 are variable. They go up when a reserve is heavily borrowed and come down when utilization falls. K2 does not offer fixed rates.
