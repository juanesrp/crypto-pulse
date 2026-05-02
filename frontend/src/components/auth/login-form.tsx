"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import { toast } from "sonner"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useAuth } from "@/hooks/use-auth"

export function LoginForm() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [loading, setLoading] = useState(false)
  const { login } = useAuth()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    try {
      await login(email, password)
    } catch {
      toast.error("Credenciales inválidas")
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-5">
      <div className="space-y-2">
        <Label htmlFor="email" className="text-xs uppercase tracking-widest text-muted-foreground">
          Email
        </Label>
        <Input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="user@email.com"
          required
          className="bg-secondary border-border font-mono"
        />
      </div>

      <div className="space-y-2">
        <Label htmlFor="password" className="text-xs uppercase tracking-widest text-muted-foreground">
          Password
        </Label>
        <Input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="••••••••"
          required
          className="bg-secondary border-border font-mono"
        />
      </div>

      <Button type="submit" disabled={loading} className="w-full font-mono uppercase tracking-widest">
        {loading ? "Authenticating..." : "Login"}
      </Button>

      <p className="text-center text-xs text-muted-foreground">
        No account?{" "}
        <Link href="/register" className="text-primary hover:underline">
          Register
        </Link>
      </p>
    </form>
  )
}
