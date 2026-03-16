# Oracle and Pricing

K2 uses a layered oracle system to resolve asset prices. For each asset, the protocol works through the following priority order until a valid price is found:

1. **RedStone.** Configured as the primary data source for crypto asset pricing. RedStone delivers frequently updated, reliable data feeds including yield-bearing assets such as LSTs, LRTs, Bitcoin LSTs, and yield-accruing stablecoins.
2. **Reflector.** The base oracle used for assets not covered by a RedStone feed.

All price data is subject to staleness thresholds. If a price exceeds its allowed age, the protocol rejects it and automatically moves to the next source in the priority order. This ensures that lending decisions are always based on current, reliable market data.

## Protections Against Bad Data

Price feeds can fail, get stale, or be manipulated. K2 has three layers of protection:

**Staleness Check.** Every price has a timestamp. If the price is older than the configured maximum age (default: 1 hour), the query fails. The staleness threshold can also be configured per-asset, overriding the global default. This prevents the protocol from acting on outdated information.

**Circuit Breaker.** If a new price arrives that differs by more than 20% from the last recorded price, K2 rejects it. The protocol continues using the last known good price rather than accepting a potentially corrupted value. This protects against sudden oracle failures, price feed manipulation, and flash crashes that could otherwise trigger incorrect liquidations. If a legitimate large price movement occurs, such as a major market event, an admin can reset the circuit breaker to allow the new price through.

**Zero Price Rejection.** The protocol never accepts a price of zero. If an oracle returns zero, the query fails immediately. There is also a global oracle pause switch. If the entire oracle contract is paused by an admin, all price queries fail regardless of the data.

## How Prices Affect You

- **Collateral value.** Determines how much you can borrow and your health factor.
- **Debt value.** Changes in the borrowed asset's price affect your health factor.
- **Liquidation.** Prices determine when positions become liquidatable.
