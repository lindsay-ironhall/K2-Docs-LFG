# Third Party Markets

Some markets on K2 are deployed on K2's contracts but curated and operated by outside groups. Each one is run by a named organisation, identified in the market title, and grouped in the **Third-Party Markets** section of the app, separate from the markets K2 lists and configures itself.

Access is not open. An operator must be approved by K2 before it can deploy a market on the protocol, and must meet defined requirements covering how the market will be run: how parameters are published, how the oracle is sourced, how liquidation is resourced, and what is disclosed to users. Approval covers the operator and its operating commitments. It is not a review of the market's parameters or a view on the asset.

Every third-party market is an isolated market. Isolation is enforced at the contract level: collateral and debt in a third-party market cannot be combined with positions in K2's primary market, and a shortfall in one of these markets cannot reach primary market suppliers. Each market has its own reserve, its own caps, and its own oracle configuration.

### What Makes Them Different

The distinction is not the isolation, K2 lists isolated markets of its own. The distinction is who sets the terms.

**K2 does not set the parameters in a third-party market.** The operator selects the collateral, sets the LTV, liquidation threshold, liquidation bonus, supply and borrow caps, and chooses the oracle. K2 provides the contracts and the interface.

This exists because not every asset fits the framework K2 applies to its own listings. An asset may be priced off a NAV feed rather than a market feed, redeem through an issuer rather than trade on a DEX, carry a term structure that does not map cleanly onto a pooled variable-rate reserve, or simply be too new to have the liquidity history K2 requires. None of that makes an asset unsound, it means the asset sits outside the criteria K2 uses when it sets parameters itself. Rather than decline assets on that basis alone, K2 makes the infrastructure available and lets the party closest to the asset publish its own parameters and its own reasoning.

K2 makes no assessment of these markets in either direction. That an operator has been approved to build on K2, and that its market appears in the app, should not be read as a review, an endorsement, or a judgement that the asset or its parameters are appropriate for you.

|                                  | K2-listed markets   | Third-party markets                 |
| -------------------------------- | ------------------- | ----------------------------------- |
| Operator                         | K2                  | Named outside group, approved by K2 |
| Risk parameters                  | Set by K2           | Set by the operator                 |
| Oracle                           | Selected by K2      | Selected by the operator            |
| Risk analysis                    | Conducted by K2     | Conducted by the operator           |
| Isolation                        | Pooled or isolated  | Always isolated                     |
| Cross-margin with primary market | Pooled markets only | Never                               |

### Liquidation

Liquidation in a third-party market may not follow the mechanics described on the [Liquidation](https://docs.k2lend.com/liquidation.md) page.

The health factor works the same way at the contract level, but the thresholds, the close factor, the bonus, and the set of addresses permitted to liquidate are all configured per market by the operator. Some of these markets hold collateral with no reliable on-chain venue, so settlement may run through an issuer redemption or a committed liquidator facility rather than a DEX. That path, and who is responsible for it, is defined by the operator and disclosed on the market itself.

If you are supplying to or borrowing from a third-party market, read its liquidation terms specifically. Do not assume they match the primary market.

### Where to Find the Details

Full details for each third-party market live in the **Third-Party Markets** section of the app: the operator, the current parameter set, the oracle and its contract address, the liquidation path, the caps, and the operator's published risk analysis.

Those details are maintained by the operator and can change, so they are not duplicated here. The app is the source of truth for anything specific to an individual market.

> Before you supply or borrow in a third-party market, check who operates it, read the operator's risk analysis, and confirm you understand how liquidation and withdrawal work in that market. These are materially different products from K2's pooled markets.
