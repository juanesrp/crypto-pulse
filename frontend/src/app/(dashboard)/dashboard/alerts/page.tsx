"use client"

import { useAuth } from "@/hooks/use-auth"
import { useAlerts } from "@/hooks/use-alerts"
import { AlertForm } from "@/components/dashboard/alert-form"
import { Card } from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"

export default function AlertsPage() {
  const { user } = useAuth()
  const { alerts, loading, createAlert } = useAlerts(user?.id)

  const alertEntries = Object.entries(alerts)

  return (
    <div className="space-y-8 max-w-lg">
      <div className="space-y-1">
        <h2 className="text-xs uppercase tracking-widest text-muted-foreground">
          Price Alerts
        </h2>
        <p className="text-xs text-muted-foreground">
          Get notified when a coin reaches your target price.
        </p>
      </div>

      <Card className="bg-card border-border p-5 space-y-5">
        <span className="text-xs uppercase tracking-widest text-muted-foreground">
          New alert
        </span>
        <AlertForm onSubmit={createAlert} />
      </Card>

      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <span className="text-xs uppercase tracking-widest text-muted-foreground">
            Active alerts
          </span>
          <span className="text-xs text-primary">{alertEntries.length}</span>
        </div>

        <Separator className="bg-border" />

        {loading ? (
          <div className="space-y-2">
            {[1, 2].map((i) => (
              <div key={i} className="h-12 bg-card border border-border animate-pulse" />
            ))}
          </div>
        ) : alertEntries.length === 0 ? (
          <p className="text-xs text-muted-foreground py-4">
            No alerts set yet.
          </p>
        ) : (
          <div className="space-y-2">
            {alertEntries.map(([coin, threshold]) => (
              <div
                key={coin}
                className="flex items-center justify-between px-4 py-3 border border-border bg-card"
              >
                <span className="text-xs uppercase tracking-widest text-muted-foreground">
                  {coin}
                </span>
                <span className="text-sm font-bold tabular-nums text-primary">
                  ${threshold.toLocaleString("en-US", { minimumFractionDigits: 2 })}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
