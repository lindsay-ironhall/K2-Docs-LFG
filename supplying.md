# Supplying Assets

Supplying is the simplest way to participate in K2. Deposit a supported asset into a reserve, receive aTokens in return, and your balance grows automatically as borrowers pay interest.

## How It Works

1. Deposit a supported asset (for example, USDC or XLM) into K2.
2. Receive aTokens in return. These represent your deposit and will grow to include any interest earned over time.
3. Withdraw your assets at any time.

## What Are aTokens?

When you deposit USDC into K2, you receive aUSDC as your receipt token at a 1:1 ratio. Deposit 100 USDC and 100 aUSDC appears in your wallet. Your balance then grows automatically as interest accrues, with no claiming or manual compounding required.

The protocol tracks a liquidity index internally that records cumulative interest over time. When you check your balance, the contract multiplies your position by the current index and returns the full USDC-equivalent amount. This happens automatically; you will always see your real withdrawable balance, not a scaled internal figure.

**Key things to know:**

* Your aUSDC balance increases over time. If you deposit 100 USDC and the APY is 5%, after one year your balance will show approximately 105 aUSDC, redeemable for 105 USDC.
* You do not need to claim or manually compound interest.
* aTokens can be transferred to other addresses.
* Your supply balance can be used as collateral to borrow other assets.

## Supply Step by Step

### 1. Choose an asset to supply

Pick from the supported assets listed in the K2 interface. Each asset shows its current supply APY, which is the annualized rate that a supplier will earn.

### 2. Approve and deposit

Approve K2 to access the tokens, then confirm the supply transaction. The assets move from your wallet to the protocol.

### 3. Receive aTokens

Your wallet will now show aTokens (for example, aUSDC) representing your position. These grow in value as interest accrues.

### 4. Optionally enable as collateral

If you want to borrow against your supply, make sure collateral is enabled for the asset.

## What Affects Your Supply APY?

Your earnings depend on:

* **Utilization rate.** The percentage of the pool that is being borrowed. Higher utilization means a higher APY.
* **Reserve factor.** The protocol receives a small portion of interest earned. The rest goes to suppliers.
* **Market conditions.** As borrowing demand changes, so does your rate.

## Interest Compounding

K2 compounds interest automatically through its liquidity index. Each time the index updates, it multiplies against your full position including previously accrued interest. You do not need to claim, reinvest, or take any action to benefit from compounding.
