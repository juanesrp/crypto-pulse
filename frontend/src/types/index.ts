export interface User {
  id: string
  username: string
  first_name: string
  last_name: string
  email: string
  is_active: boolean
  created_at: string
}

export interface TokenResponse {
  access_token: string
  token_type: string
}

export interface LoginRequest {
  email: string
  password: string
}

export interface RegisterRequest {
  username: string
  first_name: string
  last_name: string
  email: string
  password: string
}

export interface Alert {
  user_id: string
  coin: string
  threshold: number
}

export interface AlertsResponse {
  user_id: string
  alerts: Record<string, number>
}

export interface CoinPrice {
  usd: number
  usd_24h_change: number
}

export type PricesResponse = Record<string, CoinPrice>
