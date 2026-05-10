import { TokenResponse, LoginRequest, RegisterRequest, User } from "@/types"
import api from "./api"

export const authApi = {
  login: async (data: LoginRequest): Promise<TokenResponse> => {
    const res = await api.post<TokenResponse>("/auth/login", data)
    return res.data
  },

  register: async (data: RegisterRequest): Promise<User> => {
    const res = await api.post<User>("/auth/register", data)
    return res.data
  },

  me: async (): Promise<User> => {
    const res = await api.get<User>("/auth/me")
    return res.data
  },
}

export const tokenStorage = {
  get: () => localStorage.getItem("access_token"),
  set: (token: string) => {
    localStorage.setItem("access_token", token)
    document.cookie = `access_token=${token}; path=/; SameSite=Strict`
  },
  remove: () => {
    localStorage.removeItem("access_token")
    document.cookie = "access_token=; path=/; max-age=0"
  },
}
