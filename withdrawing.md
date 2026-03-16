# Withdrawing

Withdrawing lets you redeem your kTokens for the underlying asset, including any interest you have earned.

## How It Works

1. Request a withdrawal of a supplied asset.
2. K2 burns your kTokens and transfers the underlying tokens back to your wallet.
3. The amount you receive includes your original deposit plus any accrued interest.

> **Example:** You supplied 1,000 USDC six months ago. The pool has earned 3% APY. You withdraw and receive approximately 1,015 USDC.

## Things to Know

**You can withdraw to a different address.** The tokens do not have to go back to the same wallet that supplied them. However, the original supplier must authorize the transaction, and the recipient address must pass the same access controls as the supplier.

**Your health factor must stay above 1.0.** If your supply is being used as collateral, K2 will check that withdrawing does not push your health factor below 1.0. If it would, the withdrawal is rejected.

## Step by Step

### 1. Choose the asset to withdraw

Select the supplied asset in the K2 interface. You will see your current balance, which includes your original deposit plus interest earned.

### 2. Enter an amount

Enter a specific amount, or select Max to withdraw everything.

### 3. Confirm the transaction

Your kTokens are burned and the underlying asset is sent to your wallet.
