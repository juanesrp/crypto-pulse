"use client"

import { useState } from "react"
import { toast } from "sonner"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

const COINS = ["bitcoin", "ethereum", "solana"]

interface AlertFormProps {
  onSubmit: (coin: string, threshold: number) => Promise<void>
}

export function AlertForm({ onSubmit }: AlertFormProps) {
  const [coin, setCoin] = useState("bitcoin")
  const [threshold, setThreshold] = useState("")
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const value = parseFloat(threshold)
    if (isNaN(value) || value <= 0) {
      toast.error("Enter a valid threshold")
      return
    }
    setLoading(true)
    try {
      await onSubmit(coin, value)
      toast.success(`Alert set for ${coin} at $${value.toLocaleString()}`)
      setThreshold("")
    } catch {
      toast.error("Failed to create alert")
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="space-y-2">
        <Label className="text-xs uppercase tracking-widest text-muted-foreground">
          Coin
        </Label>
        <div className="flex gap-2">
          {COINS.map((c) => (
            <button
              key={c}
              type="button"
              onClick={() => setCoin(c)}
              className={`px-3 py-1.5 text-xs uppercase tracking-widest border transition-colors ${
                coin === c
                  ? "border-primary text-primary bg-primary/10"
                  : "border-border text-muted-foreground hover:border-foreground/30"
              }`}
            >
              {c.slice(0, 3)}
            </button>
          ))}
        </div>
      </div>

      <div className="space-y-2">
        <Label htmlFor="threshold" className="text-xs uppercase tracking-widest text-muted-foreground">
          Price threshold (USD)
        </Label>
        <Input
          id="threshold"
          type="number"
          value={threshold}
          onChange={(e) => setThreshold(e.target.value)}
          placeholder="50000"
          min={0}
          step="any"
          required
          className="bg-secondary border-border font-mono tabular-nums"
        />
      </div>

      <Button
        type="submit"
        disabled={loading}
        className="w-full text-xs uppercase tracking-widest"
      >
        {loading ? "Setting alert..." : "Set alert"}
      </Button>
    </form>
  )
}
