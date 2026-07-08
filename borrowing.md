# Borrowing

K2 enables users to borrow assets by supplying collateral. Borrowed assets are transferred to your wallet immediately. Interest accrues on your outstanding debt at a variable rate. Users benefit by keeping exposure to their collateral asset while accessing a different asset.

## How It Works

1. Supply an asset to K2 and make sure it is enabled as collateral.
2. Choose an asset to borrow from the available pools.
3. Borrow up to a percentage of your collateral value, determined by each asset's LTV ratio.
4. Interest accrues on your loan at a variable rate.
5. Repay whenever you like. There are no fixed terms or lock-up periods.

> **Example:** You supply $10,000 worth of XLM (LTV = 50%). You can borrow up to $5,000 worth of USDC. If you borrow $3,000, you still have $2,000 of remaining borrowing power.

## Loan-to-Value (LTV)

LTV is the maximum percentage of your deposited asset's value that you are allowed to borrow against. LTV varies by asset depending on how volatile and liquid it is.

| Asset          | LTV | You deposit $10,000 and can borrow up to |
| -------------- | --- | ---------------------------------------- |
| USDC           | 80% | $8,000                                   |
| PYUSD          | 80% | $8,000                                   |
| SolvBTC / wBTC | 70% | $7,000                                   |
| XLM            | 65% | $6,500                                   |

## Borrowing Power

If you supply multiple assets as collateral, your total borrowing power is the sum of each collateral's value multiplied by its LTV:

* **Total Borrowing Power** = sum of (Collateral Value x LTV)
* **Available to Borrow** = Total Borrowing Power minus Current Debt

> **Example:** $1,000 USDC at 80% LTV gives $800 borrowing power. $2,000 XLM at 50% LTV gives $1,000. Total borrowing power: $1,800. With $500 existing debt, you can borrow up to a maximum of $1,300 more.

## Health Factor

Once you borrow, your position has a health factor. This value measures how safe your position is. If your health factor drops below 1.0, your position is eligible to be liquidated.

> **Health Factor = (Collateral Value x Liquidation Threshold) / Total Debt Value**

The higher your health factor, the more cushion you have. The closer it gets to 1.0, the closer you are to liquidation.

## What Happens at 1.0?

When your health factor drops below 1.0, liquidators can repay a portion of your debt and seize a corresponding amount of your collateral plus a bonus. This can happen if:

* The price of your collateral assets falls
* The price of your borrowed asset rises
* Interest accrual gradually increases your debt over time

## Tips for Safe Borrowing

* Borrow well below your maximum capacity to leave room for price movements
* Monitor your health factor regularly, especially during volatile market conditions
* Keep additional assets ready to supply as collateral quickly if needed
* Repay debt proactively when the market moves against your position
* Be aware of how borrow interest accumulates over time, adding to your debt
* Aim for a health factor of 1.5 or higher as a comfortable buffer

## Step by Step

### 1. Supply collateral

You need to have assets supplied to K2 before you can borrow.

### 2. Check your borrowing power

The K2 interface shows how much you can borrow based on your collateral.

### 3. Choose an asset and amount

Select the asset you want to borrow and enter an amount within your available borrowing power.

### 4. Confirm the transaction

Once confirmed, the borrowed asset is transferred to your wallet. A debt position is created and interest starts accruing immediately.

## Things to Know

**Interest is variable.** Your borrow rate changes based on pool utilization. When many users are borrowing, rates go up. When borrowing drops, rates come down.

**There are no fixed terms.** You can hold your loan for as long as you want, as long as your health factor stays above 1.0.

**Borrow caps exist.** Each asset has a maximum total amount that can be borrowed from the protocol. If the cap is reached, no new borrows are possible.

**Interest compounds.** Your debt grows over time. The actual amount you owe is always your original borrow plus accumulated interest.
