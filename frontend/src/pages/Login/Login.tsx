"use client"

import "./Login.scss"
import LoginForm from "../../components/Auth/LoginForm"
import { useEffect, useRef } from "react"

function FloatingStars() {
  const canvasRef = useRef<HTMLCanvasElement>(null)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext("2d")
    if (!ctx) return

    canvas.width = window.innerWidth
    canvas.height = window.innerHeight

    const stars: Array<{
      x: number
      y: number
      size: number
      speedX: number
      speedY: number
      opacity: number
      fadeDirection: number
    }> = []

    // Create star particles
    for (let i = 0; i < 50; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 3 + 1,
        speedX: (Math.random() - 0.5) * 0.5,
        speedY: (Math.random() - 0.5) * 0.5,
        opacity: Math.random(),
        fadeDirection: Math.random() > 0.5 ? 1 : -1,
      })
    }

    function animate() {
      if (!ctx || !canvas) return

      ctx.clearRect(0, 0, canvas.width, canvas.height)

      stars.forEach((star) => {
        // Update position
        star.x += star.speedX
        star.y += star.speedY

        // Wrap around screen
        if (star.x < 0) star.x = canvas.width
        if (star.x > canvas.width) star.x = 0
        if (star.y < 0) star.y = canvas.height
        if (star.y > canvas.height) star.y = 0

        // Fade in and out
        star.opacity += star.fadeDirection * 0.01
        if (star.opacity <= 0 || star.opacity >= 1) {
          star.fadeDirection *= -1
        }

        // Draw star with glow
        ctx.save()
        ctx.globalAlpha = star.opacity

        // Outer glow
        const gradient = ctx.createRadialGradient(star.x, star.y, 0, star.x, star.y, star.size * 3)
        gradient.addColorStop(0, "rgba(0, 212, 255, 0.8)")
        gradient.addColorStop(0.5, "rgba(0, 212, 255, 0.3)")
        gradient.addColorStop(1, "rgba(0, 212, 255, 0)")
        ctx.fillStyle = gradient
        ctx.fillRect(star.x - star.size * 3, star.y - star.size * 3, star.size * 6, star.size * 6)

        // Star core
        ctx.fillStyle = "#00d4ff"
        ctx.beginPath()
        ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2)
        ctx.fill()

        ctx.restore()
      })

      requestAnimationFrame(animate)
    }

    animate()

    const handleResize = () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
    }

    window.addEventListener("resize", handleResize)
    return () => window.removeEventListener("resize", handleResize)
  }, [])

  return <canvas ref={canvasRef} className="floating-stars" />
}

export default function Login() {
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!containerRef.current) return

      const { clientX, clientY } = e
      const { innerWidth, innerHeight } = window

      const xPercent = (clientX / innerWidth - 0.5) * 2
      const yPercent = (clientY / innerHeight - 0.5) * 2

      containerRef.current.style.setProperty("--mouse-x", `${xPercent * 20}px`)
      containerRef.current.style.setProperty("--mouse-y", `${yPercent * 20}px`)
    }

    window.addEventListener("mousemove", handleMouseMove)
    return () => window.removeEventListener("mousemove", handleMouseMove)
  }, [])

  return (
    <div className="login-page" ref={containerRef}>
      <FloatingStars />

      <div className="login-container">
        <div className="login-content">
          <div className="login-hero">
            <img className="symbol-bg" src="/images/symbol.png" alt="UEFA symbol background" />
          </div>

          <div className="login-card">
            <div className="card-glow"></div>
            <div className="login-card-content">
              <div className="login-card-header">
                <h2 className="login-form-title">Welcome Back</h2>
                <p className="login-form-subtitle">Sign in to access your account</p>
              </div>
              <LoginForm />
            </div>
          </div>
        </div>
      </div>

      <div className="login-background">
        <div className="background-image"></div>
        <div className="background-overlay"></div>
      </div>
    </div>
  )
}
