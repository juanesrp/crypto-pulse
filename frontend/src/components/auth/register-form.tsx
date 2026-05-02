"use client"

import { useState } from "react"
import Link from "next/link"
import { toast } from "sonner"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useAuth } from "@/hooks/use-auth"

export function RegisterForm() {
  const [form, setForm] = useState({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  })
  const [loading, setLoading] = useState(false)
  const { register } = useAuth()

  const set = (field: keyof typeof form) => (e: React.ChangeEvent<HTMLInputElement>) =>
    setForm((prev) => ({ ...prev, [field]: e.target.value }))

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    try {
      await register(form)
    } catch {
      toast.error("Error al crear la cuenta")
    } finally {
      setLoading(false)
    }
  }

  const fields: { key: keyof typeof form; label: string; type: string; placeholder: string }[] = [
    { key: "username", label: "Username", type: "text", placeholder: "juanr" },
    { key: "first_name", label: "First name", type: "text", placeholder: "Juan" },
    { key: "last_name", label: "Last name", type: "text", placeholder: "Rendón" },
    { key: "email", label: "Email", type: "email", placeholder: "juan@email.com" },
    { key: "password", label: "Password", type: "password", placeholder: "••••••••" },
  ]

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {fields.map(({ key, label, type, placeholder }) => (
        <div key={key} className="space-y-2">
          <Label htmlFor={key} className="text-xs uppercase tracking-widest text-muted-foreground">
            {label}
          </Label>
          <Input
            id={key}
            type={type}
            value={form[key]}
            onChange={set(key)}
            placeholder={placeholder}
            required
            className="bg-secondary border-border font-mono"
          />
        </div>
      ))}

      <Button type="submit" disabled={loading} className="w-full font-mono uppercase tracking-widest mt-2">
        {loading ? "Creating account..." : "Register"}
      </Button>

      <p className="text-center text-xs text-muted-foreground">
        Already have an account?{" "}
        <Link href="/login" className="text-primary hover:underline">
          Login
        </Link>
      </p>
    </form>
  )
}
