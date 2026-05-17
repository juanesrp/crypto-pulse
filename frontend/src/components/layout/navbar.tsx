"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { Button } from "@/components/ui/button"
import { useAuth } from "@/hooks/use-auth"

const navLinks = [
  { href: "/dashboard", label: "Prices" },
  { href: "/dashboard/alerts", label: "Alerts" },
]

export function Navbar() {
  const pathname = usePathname()
  const { user, logout } = useAuth()

  return (
    <header className="border-b border-border bg-card px-6 py-3">
      <div className="max-w-6xl mx-auto flex items-center justify-between">
        <div className="flex items-center gap-8">
          <Link href="/dashboard" className="text-sm font-bold tracking-widest">
            <span className="text-primary glow-green">CRYPTO</span>
            <span className="text-foreground">PULSE</span>
          </Link>

          <nav className="flex items-center gap-1">
            {navLinks.map(({ href, label }) => (
              <Link
                key={href}
                href={href}
                className={`px-3 py-1 text-xs uppercase tracking-widest transition-colors ${
                  pathname === href
                    ? "text-primary"
                    : "text-muted-foreground hover:text-foreground"
                }`}
              >
                {label}
              </Link>
            ))}
          </nav>
        </div>

        <div className="flex items-center gap-4">
          {user && (
            <span className="text-xs text-muted-foreground">
              {user.username}
            </span>
          )}
          <Button
            variant="outline"
            size="sm"
            onClick={logout}
            className="text-xs uppercase tracking-widest border-border"
          >
            Logout
          </Button>
        </div>
      </div>
    </header>
  )
}
