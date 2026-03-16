# Liquidation

Liquidation is the protocol's safety mechanism. It protects suppliers by ensuring that borrowed positions always remain adequately collateralized. If your health factor drops below 1.0, part of your collateral can be seized to repay your debt.

## When Does Liquidation Happen?

Liquidation becomes possible the moment your health factor falls below 1.0. This typically happens when:

- The value of your collateral drops significantly
- The value of your borrowed asset rises
- Enough interest accrues on your debt to tip the balance

There is no grace period. Once the health factor falls below 1.0, a liquidator can act immediately.

## What Happens During Liquidation?

A liquidator repays up to 50% of your outstanding debt. In return, they receive an equivalent value of your collateral plus a liquidation bonus. The bonus depends on which asset is used as collateral and is set per-reserve:

| Asset | Liquidation Bonus |
|---|---|
| USDC | 5% |
| PYUSD | 5% |
| XLM | 10% |
| SolvBTC / wBTC | 10% |
| AQUA | 15% |

Your debt is reduced and your health factor improves.

## When Can 100% Be Liquidated?

The full outstanding debt can be liquidated in a single call if any of the following are true:

- Your health factor falls below 0.5
- Your individual debt position is worth less than $2,000
- Your individual collateral position is worth less than $2,000

These conditions allow full liquidation to keep the protocol solvent and avoid dust positions.

> **Example:** You owe 1,000 USDC and have $1,500 worth of XLM as collateral. XLM carries a 10% liquidation bonus. A liquidator repays 500 USDC of your debt and receives approximately 550 USDC worth of your XLM (500 plus 10% bonus). Your remaining debt is 500 USDC and your collateral is now approximately $950 worth of XLM. Your health factor has improved.

## How Much Do You Lose?

The liquidation bonus is the effective cost of being liquidated. It is taken from your collateral and given to the liquidator as incentive. A small portion of that bonus may also be retained by the protocol as a fee (0.3% by default). In the example above, you effectively lost approximately $50 worth of XLM collateral compared to repaying the debt yourself.

The best strategy is to avoid liquidation entirely by monitoring your health factor and acting before it reaches 1.0.

## Can You Be Fully Liquidated?

Usually not. The close factor limits liquidation to 50% of your debt per transaction. This gives you a chance to recover your position. The exception is if your health factor drops below 0.5, or your position value falls below $2,000, in which case liquidators can close 100% of your debt in one call.

## How to Avoid Liquidation

- Keep your health factor well above 1.0. Aim for 1.5 or higher.
- Do not borrow the maximum allowed by your LTV.
- Monitor your position during volatile market conditions.
- Repay debt or add collateral when your health factor starts declining.
- Diversify collateral across assets to reduce single-asset risk.
- Use stablecoins as collateral for more predictable health factor behavior.

## Who Can Liquidate?

Liquidation is designed to be permissionless. Anyone can act as a liquidator, which ensures there is always economic incentive for someone to close out risky positions and keep the protocol healthy.

In practice, K2 typically operates with a whitelisted set of trusted liquidators during its early period after launch. This gives the team time to verify that liquidation mechanics are working correctly in production before opening it up fully. As the protocol matures and stability is established, the whitelist is removed and liquidation becomes open to all.

The protocol also supports a blacklist to permanently block specific addresses from acting as liquidators regardless of other settings.
