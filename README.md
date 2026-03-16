# K2 Protocol

K2 is a decentralized borrowing and lending protocol deployed on Stellar's Soroban smart contract platform. It allows anyone to supply assets to earn interest, borrow against collateral, swap collateral positions, and execute flash loans — all in a transparent, non-custodial environment.

## What K2 Does

| For Suppliers | For Borrowers | For the Ecosystem |
|---|---|---|
| Supply assets to earn variable interest (receive kTokens) | Borrow against collateral at market-driven rates | First institutional-grade lending protocol on Stellar |
| Withdraw your supplied assets plus all accrued interest | Flexible repayment with no lock-up periods | Composable with Stellar DEXes (Soroswap, Aquarius) |
| Swap collateral from one asset to another without withdrawing | Flash loans for capital-efficient operations | Audited smart contracts with multi-layer security |

## Why Stellar and Soroban?

**Fast, deterministic finality.** Stellar's consensus protocol closes a ledger every 3 to 5 seconds with immediate, irreversible finality. No re-orgs, no confirmation waiting. Without a public mempool, the window for transaction-ordering exploitation is dramatically smaller than on EVM chains, making classic front-running and sandwich attacks impractical in practice.

**Low and predictable fees.** Stellar's base fee is 0.00001 XLM, a fraction of a cent. Fees can rise slightly during congestion via surge pricing but remain negligible regardless, making it practical to interact with K2 as often as needed without cost becoming a barrier.

**Purpose-built asset infrastructure.** Soroban uses the SEP-41 token standard for fungible assets, analogous to ERC-20. K2 works directly with Stellar-native tokens including XLM and Circle-issued USDC without requiring bridges for core assets. Other supported assets may be bridged from other chains and carry the associated bridge risks.

**Soroban: a safer smart contract environment.** Soroban processes contract calls sequentially, preventing classic re-entrancy attacks by design — a vulnerability responsible for hundreds of millions in losses across EVM lending protocols. This is a structural guarantee, not a coding convention. Smart contract risk is never zero, but a significant attack surface present on other platforms is absent here.

**Oracle integration.** K2 uses RedStone as its primary on-chain price oracle for collateral valuation, with Reflector serving as a secondary source. Both are ecosystem-native oracle solutions on Stellar and Soroban, providing redundancy in price feeds rather than relying on a single source.

## Protocol at a Glance

| Metric | Detail |
|---|---|
| Architecture | Modular router pattern (Aave V3-inspired) |
| Supported Assets | USDC, XLM, PYUSD, SolvBTC, wBTC |
| Interest Rates | Variable, algorithmically determined by utilization |
| Oracle System | Multi-source (Primary: Redstone, Secondary: Reflector) with circuit breakers |
| Liquidation | Whitelisted during launch period, opens to permissionless over time |
| Security | Professional audits completed, all critical findings remediated |
| Network | Stellar |
