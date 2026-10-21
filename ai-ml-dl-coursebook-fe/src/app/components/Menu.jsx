"use client";
import { motion } from "framer-motion";
import { menu } from "@/lib/menu";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";

export default function Menu() {
  const pathname = usePathname();
  const [activePage, setActivePage] = useState("/");

  useEffect(() => {
    const currentPage = pathname.startsWith("/courses")
      ? "/courses"
      : pathname.startsWith("/setup")
      ? "/setup"
      : "/";
    setActivePage(currentPage);
  }, [pathname]);

  return (
    <motion.div
      whileHover={{
        width: "250px",
      }}
      className={`fixed left-0 top-0 bottom-0 right-auto z-100 
      bg-white border-r-2 py-3
      h-screen w-[60px] flex flex-col justify-start gap-4 overflow-hidden`}
    >
      <motion.div
        initial={{ opacity: 0, y: -100 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, ease: "easeOut" }}
      >
        <button className="flex gap-3 text-black items-center px-3 py-1">
          <img
            src="/assets/logo.jpg"
            alt=""
            className="w-9 rounded-full border-2"
          />
          <h4 className="text-[35px] font-semibold">
            ixxmmivsdrdn
          </h4>
        </button>

        {menu.map((item, index) => (
          <button
            key={index}
            className={`flex gap-3 px-3 py-1 items-center justify-start 
            text-[30px] w-full ${
              activePage === item.href
                ? "text-black font-semibold"
                : "text-gray-400 hover:text-black"
            } transition-all duration-300 ease-in-out`}
            onClick={() =>
              (window.location.href = item.href)
            }
          >
            {item.icon}
            <h4 className="">{item.label}</h4>
          </button>
        ))}
      </motion.div>
    </motion.div>
  );
}
