# Steam game data API — examples

Steam store data — search games or pull full detail: price, genres, Metacritic, reviews.

**Live page, full schema & pricing → [quanticdata.io/collectors/steam-store-api/](https://quanticdata.io/collectors/steam-store-api/)**

Two modes from Steam's public endpoints. Pass a query to search games (appid, name, icon). Pass app_ids for the full store record per game: type, price with discount, developers/publishers, genres and categories, release date, Metacritic score, recommendation count, platforms and description. Keyless — no Steam Web API key required.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/steam/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "portal", "max_results": 10}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string) — Search term (search mode). Use this OR app_ids.
- `app_ids` (array) — Steam appids or store URLs for full detail. Use this OR query.
- `country` (string) — Storefront country for pricing (default us).
- `max_results` (integer) — How many apps to deliver at most (1–50). You pay only for delivered apps.

## Output — one row per app

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `app_id` | string | Steam appid. |
| `name` | string | Game/app title. |
| `type` | string | game, dlc, demo… (detail mode). |
| `is_free` | boolean | Free-to-play (detail mode). |
| `price` | number | Final price (detail mode). |
| `price_formatted` | string | Price as shown (detail mode). |
| `discount_pct` | integer | Discount % (detail mode). |
| `currency` | string | Price currency (detail mode). |
| `developers` | string[] | Developers (detail mode). |
| `publishers` | string[] | Publishers (detail mode). |
| `genres` | string[] | Genres (detail mode). |
…and 9 more fields — full schema on the [live page](https://quanticdata.io/collectors/steam-store-api/).

## Pricing

**$0.0008 per delivered app** ($0.8 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 2,500 apps — no card required.

## Links

- This collector: https://quanticdata.io/collectors/steam-store-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
