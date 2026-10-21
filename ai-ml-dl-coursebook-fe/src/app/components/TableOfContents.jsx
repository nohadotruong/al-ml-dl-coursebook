"use client";

import React, { useState } from "react";
import { motion } from "framer-motion";
import { ChevronUp } from "lucide-react";

export default function TableOfContents({ data }) {
  const [tableOpen, setTableOpen] = useState(false);
  const scrollToSection = (id) => {
    const el = document.querySelector(id);
    if (el) {
      window.scrollTo({
        top: el.offsetTop - 100, // adjust for header height
        behavior: "smooth",
      });
    }
  };

  return (
    <motion.div
      initial={{ x: -300, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      transition={{ duration: 0.3, ease: "easeOut" }}
      className={`flex flex-col w-full border-2 text-black rounded-lg p-3
        ${tableOpen ? "max-h-[300px]" : "max-h-[75px]"}
        overflow-hidden transition-all duration-300 ease-in-out`}
    >
      <div
        className="flex justify-between items-center mb-3 cursor-pointer"
        onClick={() => setTableOpen((prev) => !prev)}
      >
        <h4 className="text-[35px] text-nowrap truncate">
          Table of Contents
        </h4>
        <button
          className={`${
            !tableOpen ? "rotate-180" : "rotate-0"
          } transition-all duration-300 ease-in-out`}
        >
          <ChevronUp className="min-h-10 min-w-10" />
        </button>
      </div>

      <div className="flex flex-col gap-2 w-full p-3 overflow-y-auto">
        {data.map(({ title, href }) => (
          <a
            key={href}
            href={href}
            className="text-[25px] hover:underline w-fit cursor-pointer"
            onClick={(e) => {
              e.preventDefault();
              scrollToSection(href);
              setTableOpen(false);
            }}
          >
            {title}
          </a>
        ))}
      </div>
    </motion.div>
  );
}
