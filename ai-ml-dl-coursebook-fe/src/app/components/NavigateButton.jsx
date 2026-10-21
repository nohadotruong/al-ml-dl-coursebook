"use client";

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { courses } from "@/lib/menu";

export default function NavigateButton({ lesson }) {
  const [mounted, setMounted] = useState(false);

  useEffect(() => setMounted(true), []);
  if (!mounted) return null;

  const navigateBtn = [
    {
      label: "Previous Lesson",
      href: lesson > 0 ? courses[lesson - 1].href : "",
    },
    {
      label: "Back to Courses",
      href: "/courses",
    },
    {
      label: "Next Lesson",
      href: courses[lesson + 1].href,
    },
  ];
  return (
    <motion.div
      initial={{ y: 200, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.3, ease: "easeOut" }}
      className="grid grid-cols-3 gap-3 my-2"
    >
      {navigateBtn.map((item, index) => (
        <button
          key={index}
          onClick={() => (window.location.href = item.href)}
          disabled={item.href === ""}
          className={`text-[25px] border-2 rounded-lg px-2 py-1 overflow-hidden  text-nowrap 
          transition-all duration-300 ease-in-out 
          ${
            item.href === ""
              ? "disabled:text-gray-400"
              : "hover:bg-black hover:text-white"
          }`}
        >
          {item.label}
        </button>
      ))}
    </motion.div>
  );
}
