"use client";
import React from "react";
import Menu from "./Menu";
import ScrollToTop from "./ScrollToTop";
import Footer from "./Footer";

export default function ClientLayout({ children }) {
  return (
    <div className="min-h-screen w-full flex flex-col">
      <Menu />

      <main className="flex flex-col flex-1 pl-[60px] w-full">
        {children}
      </main>

      <Footer />

      <ScrollToTop />
    </div>
  );
}
