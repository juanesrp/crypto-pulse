"use client"

import { usePrices } from "@/hooks/use-prices"
import { PriceCard } from "@/components/dashboard/price-card"

const COINS = ["bitcoin", "ethereum", "solana"]

export default function DashboardPage() {
  const { prices, loading } = usePrices()

  return (
    <div className="space-y-8">
      <div className="flex items-center justify-between">
        <div className="space-y-1">
          <h2 className="text-xs uppercase tracking-widest text-muted-foreground">
            Live Prices
          </h2>
          <div className="flex items-center gap-2">
            <div className="h-1.5 w-1.5 rounded-full bg-primary animate-pulse" />
            <span className="text-xs text-primary">Auto-refreshing every 30s</span>
          </div>
        </div>
      </div>

      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {COINS.map((coin) => (
            <div key={coin} className="h-32 bg-card border border-border animate-pulse" />
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {COINS.map((coin) =>
            prices[coin] ? (
              <PriceCard key={coin} coin={coin} data={prices[coin]} />
            ) : null
          )}
        </div>
      )}
    </div>
  )
}
