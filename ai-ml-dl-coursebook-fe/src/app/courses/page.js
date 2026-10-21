"use client";

import React from "react";
import { motion } from "framer-motion";
import { courses } from "@/lib/menu";

export default function page() {
  return (
    <div className="flex flex-col w-full lg:w-[80%] mx-auto p-4">
      <motion.h1
        initial={{ y: -100, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.3, ease: "easeOut" }}
        className="text-[50px] font-semibold text-center mb-5"
      >
        Courses
      </motion.h1>

      <motion.div
        initial={{ y: 200, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.3, ease: "easeInOut" }}
        className="grid grid-cols-1 lg:grid-cols-2 w-full gap-3"
      >
        {courses.map((item, index) => (
          <button
            key={index}
            className="col-span-1 border-2 rounded-lg h-[150px] text-[30px]
            hover:bg-black hover:text-white hover:font-semibold transition-all duration-300 ease-in-out truncate overflow-hidden p-3 text-left"
            onClick={() =>
              (window.location.href = item.href)
            }
          >
            {item.label}
          </button>
        ))}
      </motion.div>
    </div>
  );
}
