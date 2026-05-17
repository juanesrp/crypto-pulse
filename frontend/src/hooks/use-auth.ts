"use client";

import { useState, useEffect, useCallback } from "react";
import { useRouter } from "next/navigation";
import { User } from "@/types";
import { authApi, tokenStorage } from "@/lib/auth";

export function useAuth() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const token = tokenStorage.get();
    if (!token) {
      setLoading(false);
      return;
    }

    authApi
      .me()
      .then(setUser)
      .catch(() => tokenStorage.remove())
      .finally(() => setLoading(false));
  }, []);

  const login = useCallback(
    async (email: string, password: string) => {
      const { access_token } = await authApi.login({ email, password });
      tokenStorage.set(access_token);
      const me = await authApi.me();
      setUser(me);
      router.push("/dashboard");
    },
    [router],
  );

  const register = useCallback(
    async (data: {
      username: string;
      first_name: string;
      last_name: string;
      email: string;
      password: string;
    }) => {
      await authApi.register(data);
      await login(data.email, data.password);
    },
    [login],
  );

  const logout = useCallback(() => {
    tokenStorage.remove();
    setUser(null);
    router.push("/login");
  }, [router]);

  return { user, loading, login, register, logout };
}
