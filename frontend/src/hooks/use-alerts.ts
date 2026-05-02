"use client"

import { useState, useEffect, useCallback } from "react"
import { AlertsResponse } from "@/types"
import api from "@/lib/api"

export function useAlerts(userId: string | undefined) {
  const [alerts, setAlerts] = useState<Record<string, number>>({})
  const [loading, setLoading] = useState(false)

  const fetchAlerts = useCallback(async () => {
    if (!userId) return
    setLoading(true)
    const res = await api.get<AlertsResponse>(`/alerts/${userId}`)
    setAlerts(res.data.alerts)
    setLoading(false)
  }, [userId])

  useEffect(() => {
    fetchAlerts()
  }, [fetchAlerts])

  const createAlert = async (coin: string, threshold: number) => {
    if (!userId) return
    await api.post("/alerts", { user_id: userId, coin, threshold })
    await fetchAlerts()
  }

  return { alerts, loading, createAlert, refetch: fetchAlerts }
}
