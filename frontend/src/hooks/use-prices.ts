"use client"

import { useState, useEffect } from "react"
import { PricesResponse } from "@/types"
import api from "@/lib/api"
import { toast } from "sonner"

const POLL_INTERVAL = 30_000

export function usePrices() {
  const [prices, setPrices] = useState<PricesResponse>({})
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  const fetchAll = async () => {
    try {
      const res = await api.get<PricesResponse>("/prices")
      setPrices(res.data)
      setError(false)
    } catch {
      setError(true)
      toast.error("No se pudieron cargar los precios")
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchAll()
    const id = setInterval(fetchAll, POLL_INTERVAL)
    return () => clearInterval(id)
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  return { prices, loading, error }
}
