"use client"

import { CoinPrice } from "@/types"
import { Card } from "@/components/ui/card"

const COIN_LABELS: Record<string, string> = {
  bitcoin: "BTC",
  ethereum: "ETH",
  solana: "SOL",
}

interface PriceCardProps {
  coin: string
  data: CoinPrice
}

export function PriceCard({ coin, data }: PriceCardProps) {
  const symbol = COIN_LABELS[coin] ?? coin.toUpperCase()
  const isPositive = data.usd_24h_change >= 0

  const formattedPrice = data.usd.toLocaleString("en-US", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  })

  const formattedChange = `${isPositive ? "+" : ""}${data.usd_24h_change.toFixed(2)}%`

  return (
    <Card className="bg-card border-border p-5 space-y-3 hover:border-primary/30 transition-colors">
      <div className="flex items-center justify-between">
        <span className="text-xs uppercase tracking-widest text-muted-foreground">
          {coin}
        </span>
        <span className="text-xs font-bold tracking-widest text-muted-foreground">
          {symbol}
        </span>
      </div>

      <div className="flex items-end justify-between gap-2">
        <span className="text-2xl font-bold tracking-tight tabular-nums text-foreground">
          ${formattedPrice}
        </span>
        <span className={`text-sm font-medium tabular-nums ${isPositive ? "price-up" : "price-down"}`}>
          {formattedChange}
        </span>
      </div>

      <div className="pt-1 border-t border-border">
        <span className="text-xs text-muted-foreground uppercase tracking-widest">
          24h change
        </span>
      </div>
    </Card>
  )
}
