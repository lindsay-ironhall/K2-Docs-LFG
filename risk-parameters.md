# Risk Parameters

Each asset in K2 has a set of risk parameters that control how it can be used as collateral and borrowed. These are configured per-asset by the protocol admin.

## Core Parameters

**Loan-to-Value (LTV).** The maximum percentage of your collateral value you can borrow. LTV varies by asset depending on how volatile and liquid it is. Stablecoins like USDC carry higher LTVs (up to 80%) while more volatile assets like XLM and AQUA sit lower (50%). The full range across supported assets is 50 to 80%.

**Liquidation Threshold.** The point at which your position becomes liquidatable. Always higher than LTV, creating a safety buffer. The gap between your LTV and the liquidation threshold is your breathing room. Stablecoins have tighter thresholds (85%) while volatile assets are set lower (65%) to account for larger price swings. The full range across supported assets is 65 to 85%.

**Liquidation Bonus.** The premium a liquidator receives, paid from your seized collateral. The bonus is higher for more volatile assets, reflecting the greater risk a liquidator takes on when seizing them:

- Stablecoins (USDC, PYUSD): 5%
- XLM, SolvBTC, wBTC: 10%
- AQUA: 15%

**Reserve Factor.** The percentage of interest earnings that go to the protocol treasury instead of suppliers. K2 uses two tiers: stablecoins are set at 10% and all other assets at 20%.

**Borrow Cap.** The maximum total amount of an asset that can be borrowed across the entire protocol at any one time. Once the cap is reached, no further borrowing of that asset is possible until existing loans are repaid. Borrow caps exist to limit the protocol's exposure to any single asset, particularly important for less liquid or more volatile assets where a large concentrated borrow position could destabilize the reserve. Each asset has its own cap set independently, and caps are always lower than the corresponding supply cap to ensure there is always a buffer of unborrowed liquidity available for withdrawals.
