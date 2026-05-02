import type { Metadata } from "next"
import { Geist_Mono } from "next/font/google"
import { Toaster } from "@/components/ui/sonner"
import "./globals.css"

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
})

export const metadata: Metadata = {
  title: "CryptoPulse",
  description: "Real-time crypto price monitoring",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={geistMono.variable}>
      <body className="min-h-screen bg-background font-mono antialiased scanline">
        {children}
        <Toaster />
      </body>
    </html>
  )
}
