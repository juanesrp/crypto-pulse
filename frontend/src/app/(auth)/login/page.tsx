import { LoginForm } from "@/components/auth/login-form"

export default function LoginPage() {
  return (
    <main className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-sm space-y-8">
        <div className="space-y-1">
          <h1 className="text-2xl font-bold tracking-tight glow-green text-primary">
            CRYPTO<span className="text-foreground">PULSE</span>
          </h1>
          <p className="text-xs text-muted-foreground uppercase tracking-widest">
            Terminal v1.0 — Sign in to continue
          </p>
        </div>

        <div className="border border-border bg-card p-6 space-y-6">
          <div className="flex items-center gap-2">
            <div className="h-1.5 w-1.5 rounded-full bg-primary animate-pulse" />
            <span className="text-xs text-muted-foreground uppercase tracking-widest">
              Authentication required
            </span>
          </div>
          <LoginForm />
        </div>
      </div>
    </main>
  )
}
