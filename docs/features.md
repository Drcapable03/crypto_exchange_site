# Features - MVP Scope

## Must-Have (Phase 1-4)
- User auth (register/login, roles: user/admin)
- User dashboard: Balances (per coin), deposit address display, withdrawal form, trading interface (order placement, basic order book view)
- Admin dashboard: User list, balance adjustments, withdrawal queue (approve/deny), manual deposit credit
- Internal order book + matching engine (limit orders only, price-time priority)
- Real-time prices (CoinGecko polling every 5-10 min, WebSockets push)
- Fees: 0.1% on trades & withdrawals
- Withdrawal min $50
- Pending message logic
- Basic security: JWT, password hashing, admin-only routes
- Local dev setup (Docker + Postgres)

## Post-MVP (Nice-to-Have)
- 2FA for users/admins
- Email notifications (withdrawal status)
- Basic charts (Recharts)
- Logging & error monitoring
- Rate limiting
- Reserve monitoring for control wallets

Prioritize: Get auth → balances → manual deposit/withdrawal → trading → polish.