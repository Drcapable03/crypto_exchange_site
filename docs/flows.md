# Operational Flows

## User Registration & Login
1. User signs up/logs in (email/password, no KYC).
2. Gets access to dashboard with internal balances (per coin).

## Deposit Flow
1. User goes to Deposit section in dashboard.
2. Selects coin (e.g., USDT).
3. Platform displays the **static control wallet address** for that coin (hardcoded in config).
4. User sends crypto from their external wallet to this address.
5. User handles proof externally: Takes screenshot/txn hash and sends to admin (email or other channel).
6. Admin verifies on blockchain explorer (confirms amount, confirmations).
7. Admin manually credits user's internal balance (via admin dashboard).
   - No in-app proof upload or auto-detection required initially.

## Withdrawal Flow
1. User clicks Withdraw in dashboard.
2. Selects coin, enters amount (≥ $50 equiv.), destination external address.
3. Submits request → balance reserved/locked temporarily.
4. User sees status: "In progress, ~30 minutes."
5. Request enters admin queue (DB table).
6. Admin reviews (checks for issues), approves or denies.
7. On approval:
   - Admin manually signs & sends txn from the control hot wallet (same coin).
   - Deduct 0.1% fee + network fee (if applicable).
   - Update status: Processing → Completed.
8. On deny: Status → Rejected, balance unlocked.

## Trading Flow
1. User views market (real external prices, updated 5-10 min via polling/WebSockets).
2. Places limit order (buy/sell, price, amount) on USDT pair.
3. Order added to internal order book (visible bids/asks).
4. Matching engine checks for matches (price-time priority).
5. On match: Execute trade → update both users' balances, deduct 0.1% fee each side.
6. No on-chain txn; all internal DB.

## Admin Dashboard Flows
- View & credit deposits (manual entry after external proof).
- Manage withdrawal queue (approve/deny, trigger manual send).
- Adjust user balances (display corrections only).
- Monitor orders, balances, activity.

Notes:
- Control wallets: One per coin (hot for sends, cold for storage/security).
- Cross-coin: User must trade internally to "convert" (e.g., USDT → BTC via trades).